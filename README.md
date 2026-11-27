# Proyecto Bimestral del Primer Bimestre - Introducccion a la Inteligencia de Negocios

===============================Información general=========================================

Universidad: Universidad Técnica Particular de Loja (UTPL)

Integrantes: Jose Antonio Jimenez, Luis Bermeo, David Apolo

Docente: Ing. Angel Eduardo Encalada Encalada

Asignatura: Introduccion a la Inteligencia de Negocios

==========================================================================================

## 1\. Tema del proyecto

Integración y analisis de la matricula estudiantil al inicio y final del año lectivo en Ecuador mediante un proceso ETL.

## 2\. Objetivo

Integrar y preparar datos educativos oficiales del Ecuador mediante un proceso de extracción, transformación y carga (ETL), para asi obtener información organizada y confiable que nos permita analizar la matrícula estudiantil al inicio y final del año lectivo.

## 3\. Fuentes de datos

Se utilizarán dos conjuntos de datos públicos del Ministerio de Educación del Ecuador:

*Fuente 1: Registro de Matrícula – MINEDUC*\*

Información recopilada al inicio del año lectivo.

https://www.datosabiertos.gob.ec/dataset/registro-de-matricula-mineduc

\*Fuente 2: Descomposición de la Matrícula – MINEDUC

Información recopilada al finalizar el año lectivo.

https://www.datosabiertos.gob.ec/dataset/descomposicion-de-la-matricula-mineduc

## 4\. Herramientas de trabajo a utilizar

* Python
* Google Colab
* Pandas
* GitHub

## 5\. Proceso de Extraccion, Transformacion y Carga (ETL)

El proyecto contempla tres etapas:

1. Extracción: Lectura y exploración de los archivos CSV originales.
2. Transformación: Limpieza, estandarización e integración de los datos.
3. Carga: Generación del conjunto de datos integrado y validación de los resultados.

## 6\. Organización del repositorio

El repositorio contiene los archivos y documentos utilizados para el desarrollo del proyecto.

===Archivos CSV utilizados===

En la carpeta datos\_fuente se encuentran los dos conjuntos de datos originales del Ministerio de Educación del Ecuador:

* registro-administrativo-historico\_2009-2024-inicio.csv: Datos registrados al inicio del año lectivo.
* registro-administrativo-historico\_2009-2024-fin.csv: Datos registrados al finalizar el año lectivo.

===Documentación de las actividades===

En la carpeta documentacion/ se encuentran:

* actividad1\_fuentesdedatos.md: Selección de la temática, necesidad de información y fuentes de datos.
* actividad3\_extracciondedatos.md: Proceso de extracción de los archivos CSV.
* actividad4\_almacenamientodedatos.md: Propuesta de almacenamiento de los datos.

===Código del proyecto===

En la carpeta scripts\_etl se encuentra el archivo etl\_matriculas.py desarrollado en Python con la biblioteca pandas. Este programa Python esta utilizado para leer y verificar los archivos CSV originales.

===Datos Resultantes===
En la carpeta datos\_resultantes se almacenará el conjunto de datos integrado que se obtendrá después de realizar las etapas de transformación, integración y carga del proceso ETL.

===Evidencias del Proyecto===
En la carpeta evidencias se guardarán las capturas de pantalla y demás evidencias que permitan comprobar el desarrollo y funcionamiento del proceso Extraccion,Transformacion y Carga de datos(ETL).



## 7\. Resultados

Como resultado del proceso ETL se obtuvo el archivo matriculas\_integradas.csv, con 283,734 registros y 35 columnas. Cada registro representa la información integrada de una institución educativa (identificada mediante el código AMIE) para un año lectivo. El conjunto cubre 15 periodos, desde 2009-2010 hasta 2023-2024, e identifica 29,241 códigos AMIE distintos y 25 valores distintos en el campo Provincia. .

La estructura reúne datos de identificación y ubicación institucional (AMIE, año lectivo, provincia, cantón y parroquia), características de las instituciones (tipo de educación, sostenimiento, área, régimen, jurisdicción, modalidad y jornada), información de docentes y estudiantes al inicio y resultados al cierre del año lectivo. Entre las variables principales se encuentran Total\_Estudiantes\_Inicio, Total\_Estudiantes\_Fin, Promovidos, No\_Promovidos y Abandono. En la suma de los registros institución-año, el total de estudiantes al inicio alcanza 64,509,455 y al final 63,286,743. La diferencia agregada es de 1,222,712 registros (1.90% respecto del total inicial). Estos valores son sumas de observaciones por institución y periodo, no un conteo de personas únicas a lo largo de los quince años.

## 8\. Propuesta de almacenamiento

Se propone utilizar un Data Warehouse para almacenar y organizar los datos educativos integrados para que se mas facil el analisis y la comparacion.

## 9\. Conclusiones

El desarrollo del proyecto permitió integrar dos conjuntos de datos oficiales del Ministerio de Educación del Ecuador, correspondientes al registro de matrícula al inicio y al final de los años lectivos. Mediante el proceso ETL se consiguió organizar la información en un único conjunto de datos, facilitando su consulta y análisis.



La utilización de Python y la biblioteca Pandas permitió realizar las actividades de extracción, transformación e integración de manera automatizada. Esto facilitó la limpieza, estandarización y estructuración de los datos, reduciendo las inconsistencias y mejorando su utilidad para futuros análisis.



El conjunto de datos resultante contiene 283.734 registros y 35 columnas, correspondientes a 15 periodos lectivos comprendidos entre 2009-2010 y 2023-2024. Esta información permite comparar los datos de matrícula inicial y final, así como analizar variables relacionadas con la promoción, no promoción y abandono estudiantil.



La integración de estos datos constituye una base importante para la Inteligencia de Negocios, debido a que permite transformar registros educativos en información útil para identificar tendencias y diferencias entre los periodos lectivos. Además, el almacenamiento mediante un Data Warehouse facilitaría la elaboración de consultas, reportes y paneles de visualización para apoyar la toma de decisiones.



Finalmente, el proyecto demuestra la importancia de los procesos ETL en el tratamiento de grandes volúmenes de información. La preparación adecuada de los datos es fundamental para garantizar que los análisis posteriores sean confiables y permitan comprender mejor el comportamiento de la matrícula estudiantil en Ecuador.

