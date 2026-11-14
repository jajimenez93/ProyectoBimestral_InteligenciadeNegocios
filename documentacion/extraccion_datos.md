=====Actividad 3: Proceso ETL — Extracción de los datos=====

# 1. Objetivo

Extraer los datos de matrícula estudiantil del Ecuador registrados al inicio y al final del año lectivo, utilizando dos archivos CSV del Ministerio de Educación, para comprobar que puedan leerse correctamente y estén disponibles para las siguientes etapas del proceso ETL.

# 2. Fuentes de datos utilizadas

*Fuente 1: Registro de Matrícula — Inicio

- Archivo: `registro-administrativo-historico_2009-2024-inicio.csv`
- Formato: CSV
- Separador: punto y coma (`;`)
- Registros: 442.716
- Columnas: 27

*Fuente 2: Descomposición de la Matrícula — Fin

- Archivo: `registro-administrativo-historico_2009-2024-fin.csv`
- Formato: CSV
- Separador: punto y coma (`;`)
- Registros: 286.111
- Columnas: 23

# 3. Proceso de extracción

Se utiliza Python y la biblioteca de `pandas` para leer los dos archivos CSV mediante la función `read_csv()`.

El proceso se realizó en el archivo `etl_matriculas.py`, utilizando el parámetro `sep=";"` para reconocer correctamente las columnas.

Luego se utilizaron `shape` y `columns` para comprobar la cantidad de registros, el número de columnas y los nombres de los atributos disponibles.

# 4. Resultados de la extracción

La lectura de ambos archivos se realizó correctamente.

Se identificaron tambien campos comunes como `Año_lectivo`, `Provincia`, `Canton`, `AMIE` y `Nombre_Institucion`, que podrán utilizarse despues para analizar la relación entre los conjuntos de los datos.

Durante la lectura se presentó una advertencia relacionada con tipos de datos mixtos en algunas columnas, esta observación deberá considerarse en la etapa de diagnóstico y transformación.

# 5. Conservación de los datos originales

Los dos archivos CSV se mantienen en la carpeta `datos` sin modificaciones.

La extracción realizada permite disponer de la información original para las siguientes etapas del proyecto, sin efectuar todavía procesos de limpieza, transformación o integración de los datos.

# 6. Conclusión

Se completó la extracción inicial de las dos fuentes de datos del Ministerio de Educación. Se comprobó que ambos archivos pueden leerse mediante Python y que sus columnas están disponibles para continuar con el proceso ETL.