# -*- coding: utf-8 -*-
"""Script ETL para datos de matrículas.

* **Extracción** – lee dos CSV (inicio y fin) de ``datos_fuente``.
* **Transformación** – normaliza nombres, quita espacios, pone mayúsculas y convierte columnas numéricas a ``Int64``.
* **Evidencia** – genera ``evidencia_integracion.csv`` con filas de muestra y banderas que indican coincidencias.
* **Carga** – no se ejecuta aquí; el resultado se guarda en ``matriculas_integradas.csv`` para que otro proceso lo cargue.
"""

from pathlib import Path
import pandas as pd

# ---------------------------------------------------------------------------
# Configuración
# ---------------------------------------------------------------------------
RAIZ_PROYECTO = Path(__file__).resolve().parents[1]
DIR_ORIGEN = RAIZ_PROYECTO / "datos_fuente"
DIR_SALIDA = RAIZ_PROYECTO / "datos_resultantes"
RUTA_EVIDENCIA = DIR_SALIDA / "evidencia_integracion.csv"
RUTA_INTEGRADO = DIR_SALIDA / "matriculas_integradas.csv"

# Columnas numéricas en cada archivo fuente
COLUMNAS_NUMERICAS_INICIO = [
    "Docentes_Femenino",
    "Docentes_Masculino",
    "Total_Docentes",
    "Estudiantes_Femenino",
    "Estudiantes_Masculino",
    "Total_Estudiantes",
    "Ecuatoriana",
    "Colombiana",
    "Venezolana",
    "Peruana",
    "Otros_Paises_de_America",
    "Otros_Continentes",
]
COLUMNAS_NUMERICAS_FIN = [
    "Total_Estudiantes",
    "Promovidos",
    "No_Promovidos",
    "Abandono",
]

# Clave natural que identifica cada registro
CLAVE = ["AMIE", "Anio_lectivo"]

# ---------------------------------------------------------------------------
# Funciones auxiliares (corto y en español)
# ---------------------------------------------------------------------------
def _limpiar_columnas(df: pd.DataFrame) -> pd.DataFrame:
    """Normaliza nombres de columnas.
    - ``area`` → ``Area``
    - ``no promovidos`` → ``No_Promovidos``
    - resto: quita espacios.
    """
    mapa = {
        col.strip(): (
            "Area"
            if col.strip().casefold() == "area"
            else "No_Promovidos"
            if col.strip().casefold() == "no promovidos"
            else col.strip()
        )
        for col in df.columns
    }
    return df.rename(columns=mapa)


def _normalizar_cadenas(df: pd.DataFrame) -> pd.DataFrame:
    """Recorta, une espacios y pone mayúsculas (excepto la clave)."""
    for col in df.columns:
        df[col] = (
            df[col]
            .astype(str)
            .str.strip()
            .replace(r"^\s*$", pd.NA, regex=True)
            .replace(r"\s+", " ", regex=True)
        )
        if col not in ("Anio_lectivo",) and not col.startswith("Cod_"):
            df[col] = df[col].str.upper()
    return df


def _convertir_numericos(df: pd.DataFrame, columnas: list[str]) -> pd.DataFrame:
    """Convierte a entero manejando puntos como separador de miles."""
    for col in columnas:
        serie = df[col].replace({"": pd.NA, "-": pd.NA})
        # elimina puntos de miles, ej. 1.234 -> 1234
        serie = serie.str.replace(r"(?<=\d)\.(?=\d{3}(?:$|\.))", "", regex=True)
        df[col] = pd.to_numeric(serie, errors="coerce").astype("Int64")
    return df


def transformar_datos(df: pd.DataFrame, columnas_numericas: list[str]) -> pd.DataFrame:
    """Pipeline completo de transformación para un DataFrame bruto."""
    df = df.copy()
    df = _limpiar_columnas(df)
    df = df.replace(r"^\s*$", pd.NA, regex=True).dropna(how="all")
    df = _normalizar_cadenas(df)
    df["Anio_lectivo"] = df["Anio_lectivo"].str.replace(r"\s+(Inicio|Fin)$", "", case=False, regex=True)
    df = df.dropna(subset=CLAVE)
    df = _convertir_numericos(df, columnas_numericas)
    return df


def agrupar_por_institucion_y_anio(df: pd.DataFrame, columnas_numericas: list[str]) -> pd.DataFrame:
    """Agrupa por la clave y suma columnas numéricas; las demás quedan con el primer valor."""
    agg = {
        col: "sum" if col in columnas_numericas else "first"
        for col in df.columns
        if col not in CLAVE
    }
    return df.groupby(CLAVE, as_index=False).agg(agg)


def _preparar_evidencia(df_cruce: pd.DataFrame) -> pd.DataFrame:
    """Construye una tabla corta con banderas que indican si los datos coinciden."""
    columnas = [
        "AMIE_Inicio",
        "AMIE_Fin",
        "Anio_lectivo_Inicio",
        "Anio_lectivo_Fin",
        "Cod_Provincia_Inicio",
        "Cod_Provincia_Fin",
        "Cod_Canton_Inicio",
        "Cod_Canton_Fin",
        "Cod_Parroquia_Inicio",
        "Cod_Parroquia_Fin",
        "Nombre_Institucion_Inicio",
        "Nombre_Institucion_Fin",
        "Total_Estudiantes_Inicio",
        "Total_Estudiantes_Fin",
    ]
    ev = df_cruce[columnas].head(5).copy()
    ev["Coincide_AMIE"] = ev["AMIE_Inicio"] == ev["AMIE_Fin"]
    ev["Coincide_Anio"] = ev["Anio_lectivo_Inicio"] == ev["Anio_lectivo_Fin"]
    ev["Coincide_Ubicacion"] = (
        ev["Cod_Provincia_Inicio"].fillna("") == ev["Cod_Provincia_Fin"].fillna("")
    ) & (
        ev["Cod_Canton_Inicio"].fillna("") == ev["Cod_Canton_Fin"].fillna("")
    ) & (
        ev["Cod_Parroquia_Inicio"].fillna("") == ev["Cod_Parroquia_Fin"].fillna("")
    )
    ev["Coincide_Nombre"] = (
        ev["Nombre_Institucion_Inicio"].fillna("") == ev["Nombre_Institucion_Fin"].fillna("")
    )
    ev["Coincide_Total_Estudiantes"] = (
        ev["Total_Estudiantes_Inicio"] == ev["Total_Estudiantes_Fin"]
    ).fillna(False)
    return ev


def ejecutar_etl() -> pd.DataFrame:
    """Ejecuta todo el proceso ETL y guarda los artefactos.
    Devuelve el DataFrame integrado listo para cargar.
    """
    # ------------------- Extracción -------------------
    df_inicio = pd.read_csv(
        DIR_ORIGEN / "registro-administrativo-historico_2009-2024-inicio.csv",
        sep=";",
        dtype=str,
        keep_default_na=False,
    )
    df_fin = pd.read_csv(
        DIR_ORIGEN / "registro-administrativo-historico_2009-2024-fin.csv",
        sep=";",
        dtype=str,
        keep_default_na=False,
    )

    # ------------------- Transformación -------------------
    df_inicio = transformar_datos(df_inicio, COLUMNAS_NUMERICAS_INICIO)
    df_fin = transformar_datos(df_fin, COLUMNAS_NUMERICAS_FIN)
    df_inicio = agrupar_por_institucion_y_anio(df_inicio, COLUMNAS_NUMERICAS_INICIO)
    df_fin = agrupar_por_institucion_y_anio(df_fin, COLUMNAS_NUMERICAS_FIN)

    # Renombramos claves para que el merge sea explícito
    df_inicio = df_inicio.rename(columns={"AMIE": "AMIE_Inicio", "Anio_lectivo": "Anio_lectivo_Inicio", "Total_Estudiantes": "Total_Estudiantes_Inicio"})
    df_fin = df_fin.rename(columns={"AMIE": "AMIE_Fin", "Anio_lectivo": "Anio_lectivo_Fin", "Total_Estudiantes": "Total_Estudiantes_Fin"})

    # ------------------- Integración (join) -------------------
    df_cruce = df_inicio.merge(
        df_fin,
        left_on=["AMIE_Inicio", "Anio_lectivo_Inicio"],
        right_on=["AMIE_Fin", "Anio_lectivo_Fin"],
        how="inner",
        suffixes=("_Inicio", "_Fin"),
    )
    # Eliminar posibles filas duplicadas que aparecen por coincidencias múltiples
    df_cruce = df_cruce.drop_duplicates(subset=["AMIE_Inicio", "Anio_lectivo_Inicio"])

    # ------------------- Evidencia -------------------
    # Usar el cruce sin duplicados para que la evidencia muestre filas distintas
    evidencia = _preparar_evidencia(df_cruce)

    # ------------------- DataFrame final -------------------
    cols_compartidas = [c for c in df_inicio.columns if c in df_fin.columns]
    cols_a_quitar = [f"{c}_Fin" for c in cols_compartidas] + ["AMIE_Fin", "Anio_lectivo_Fin"]
    df_integrado = df_cruce.drop(columns=cols_a_quitar)
    rename_map = {"AMIE_Inicio": "AMIE", "Anio_lectivo_Inicio": "Anio_lectivo"}
    rename_map.update({f"{c}_Inicio": c for c in cols_compartidas})
    df_integrado = df_integrado.rename(columns=rename_map)

    # ------------------- Verificación de número de columnas -------------------
    # Se calcula cuántas columnas debería contener el dataframe integrado.
    #   * `len(df_inicio.columns)`   → total de columnas del dataset de inicio.
    #   * `len(df_fin.columns)`      → total de columnas del dataset de fin.
    #   * `len(cols_compartidas)`    → columnas presentes en ambos datasets; una de sus versiones se elimina en el merge.
    #   * `- 2`                      → las columnas clave `AMIE` y `Anio_lectivo` aparecen en ambos lados con los sufijos `_Inicio` y `_Fin` y, tras el rename, solo deben contarse una vez.
    columnas_esperadas = (
        len(df_inicio.columns)
        + len(df_fin.columns)
        - len(cols_compartidas)
        - 2
    )
    if len(df_integrado.columns) != columnas_esperadas:
        print(
            f"[ADVERTENCIA] Número de columnas inesperado: {len(df_integrado.columns)} (se esperaban {columnas_esperadas})"
        )
    else:
        print(f"Número de columnas verificado: {len(df_integrado.columns)}")

    # ------------------- Guardado -------------------
    DIR_SALIDA.mkdir(parents=True, exist_ok=True)
    # Si el archivo de evidencia ya existe y está abierto, lo eliminamos antes de crear uno nuevo
    if RUTA_EVIDENCIA.exists():
        RUTA_EVIDENCIA.unlink()
    evidencia.to_csv(RUTA_EVIDENCIA, sep=";", index=False, encoding="utf-8-sig")
    df_integrado.to_csv(RUTA_INTEGRADO, sep=";", index=False, encoding="utf-8-sig")

    # ------------------- Resumen -------------------
    print(f"Claves coincidentes: {len(df_cruce)}")
    print(f"Claves solo en inicio: {len(df_inicio) - len(df_cruce)}")
    print(f"Claves solo en fin: {len(df_fin) - len(df_cruce)}")
    print(f"Dataframe integrado: {len(df_integrado)} filas, {len(df_integrado.columns)} columnas")
    print(f"Evidencia guardada en: {RUTA_EVIDENCIA}")
    print(f"Resultado listo para carga: {RUTA_INTEGRADO}")
    return df_integrado


if __name__ == "__main__":
    ejecutar_etl()
