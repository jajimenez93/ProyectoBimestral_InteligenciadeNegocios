# Proyecto Bimestral del Primer Bimestre - Introducccion a la Inteligencia de Negocios

===============================Información general=========================================

Universidad: Universidad Técnica Particular de Loja (UTPL)

Integrantes: Jose Antonio Jimenez, Luis Bermeo, David Apolo

Docente: Ing. Angel Eduardo Encalada Encalada

Asignatura: Introduccion a la Inteligencia de Negocios

==========================================================================================

## 1. Tema del proyecto

Integración y analisis de la matricula estudiantil al inicio y final del año lectivo en Ecuador mediante un proceso ETL.

## 2. Objetivo

Integrar y preparar datos educativos oficiales del Ecuador mediante un proceso de extracción, transformación y carga (ETL), para asi obtener información organizada y confiable que nos permita analizar la matrícula estudiantil al inicio y final del año lectivo.

## 3. Fuentes de datos

Se utilizarán dos conjuntos de datos públicos del Ministerio de Educación del Ecuador:

*Fuente 1: Registro de Matrícula – MINEDUC**

Información recopilada al inicio del año lectivo.

https://www.datosabiertos.gob.ec/dataset/registro-de-matricula-mineduc

*Fuente 2: Descomposición de la Matrícula – MINEDUC

Información recopilada al finalizar el año lectivo.

https://www.datosabiertos.gob.ec/dataset/descomposicion-de-la-matricula-mineduc

## 4. Herramientas de trabajo a utilizar

- Python
- Google Colab
- Pandas
- GitHub

## 5. Proceso de Extraccion, Transformacion y Carga (ETL)

El proyecto contempla tres etapas:

1. Extracción: Lectura y exploración de los archivos CSV originales.
2. Transformación: Limpieza, estandarización e integración de los datos.
3. Carga: Generación del conjunto de datos integrado y validación de los resultados.

## 6. Organización del repositorio

El repositorio contiene los archivos y documentos utilizados para el desarrollo del proyecto.

===Archivos CSV utilizados===

En la carpeta datos_fuente se encuentran los dos conjuntos de datos originales del Ministerio de Educación del Ecuador:

- registro-administrativo-historico_2009-2024-inicio.csv: Datos registrados al inicio del año lectivo.

- registro-administrativo-historico_2009-2024-fin.csv: Datos registrados al finalizar el año lectivo.

===Documentación de las actividades===

En la carpeta documentacion/ se encuentran:

- actividad1_fuentesdedatos.md: Selección de la temática, necesidad de información y fuentes de datos.

- actividad3_extracciondedatos.md: Proceso de extracción de los archivos CSV.

- actividad4_almacenamientodedatos.md: Propuesta de almacenamiento de los datos.

===Código del proyecto===

En la carpeta scripts_etl se encuentra el archivo etl_matriculas.py desarrollado en Python con la biblioteca pandas. Este programa Python esta utilizado para leer y verificar los archivos CSV originales.

===Datos Resultantes===
En la carpeta datos_resultantes se almacenará el conjunto de datos integrado que se obtendrá después de realizar las etapas de transformación, integración y carga del proceso ETL.

===Evidencias del Proyecto===
En la carpeta evidencias se guardarán las capturas de pantalla y demás evidencias que permitan comprobar el desarrollo y funcionamiento del proceso Extraccion,Transformacion y Carga de datos(ETL).


## 7. Resultados



## 8. Propuesta de almacenamiento

Se propone utilizar un Data Warehouse para almacenar y organizar los datos educativos integrados para que se mas facil el analisis y la comparacion.

## 9. Conclusiones

