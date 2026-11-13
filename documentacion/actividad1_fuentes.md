======= ACTIVIDAD 1. SELECCIÓN DE LA TEMÁTICA, NECESIDAD DE INFORMACIÓN Y FUENTES DE DATOS======

----1. Tema del proyecto----

Este proyecto se enfoca en la integración y preparación de datos educativos del Ecuador, especificamente en la matrícula estudiantil registrada al inicio y al final del año lectivo.
Para desarrollar el proyecto se utilizarán 2 conjuntos de datos abiertos del Ministerio de Educación del Ecuador para asi aplicar despues un proceso ETL (extraccion, transformacion y carga).

----2. Necesidad de información----

Se busca disponer de información organizada que permita comparar los registros de matrícula estudiantil al inicio y al final del año lectivo.

*Pregunta de análisis para Inteligencia de Negocios:

¿Como varia la matruicula estudiantil entre el inicio y el final del año lectivo en las instituciones educativas del Ecuador?

----3. Selección de fuentes de datos----

Se selecciono 2 conjuntos de datos públicos disponibles en el Portal de Datos Abiertos del Ecuador

Fuente 1. Registro de Matrícula – MINEDUC

- Institución: Ministerio de Educación del Ecuador.
- Procedencia: Portal de Datos Abiertos del Ecuador.
- Formato: CSV
- Archivo: MINEDUC_RegistroAdministrativoHistorico_2009-2024Inicio.
- Contenido: Información administrativa recopilada al inicio del año lectivo sobre instituciones educativas y matrícula estudiantil.
- Atributos relevantes: Identificador AMIE, año lectivo, provincia, cantón y datos de la matrícula.

**Enlaces oficiales:**

https://www.datosabiertos.gob.ec/dataset/registro-de-matricula-mineduc

Fuente 2. Descomposición de la Matrícula – MINEDUC

- Institución: Ministerio de Educación del Ecuador.
- Procedencia: Portal de Datos Abiertos del Ecuador.
- Formato: CSV.
- Archivo: MINEDUC_RegistroAdministrativoHistorico_2009-2024Fin.
- Contenido:Información administrativa recopilada al finalizar el año lectivo, relacionada con la matrícula y los resultados educativos.
- Atributos relevantes: Identificador AMIE, año lectivo, provincia, cantón y datos de matrícula al finalizar el período.

*Enlace oficial:

https://www.datosabiertos.gob.ec/dataset/descomposicion-de-la-matricula-mineduc

----4. Importancia de integrar las fuentes----

La integración de los dos conjuntos de datos permitira relacionar la información registrada al inicio y al final del año lectivo mediante campos comunes, como el código AMIE de las instituciones educativas y el año lectivo, se buscara obtener un conjunto de datos que facilite la comparación de la matrícula estudiantil.

Antes de realizar la integración, será necesario revisar la calidad de los datos, identificar registros compatibles y estandarizar los campos correspondientes.

----5. Información que se espera obtener----

Una vez este  completado el proceso ETL, se espera disponer de datos integrados que permitan:

- Comparar la matrícula al inicio y al final del año lectivo.
- Analizar las diferencias de matrícula por provincia.
- Consultar información por institución educativa y período.
- Apoyar el análisis de información educativa mediante herramientas de Inteligencia de Negocios.

----6. Referencias de las fuentes----

Ministerio de Educación del Ecuador. (s. f.). *Registro de Matrícula – MINEDUC*. Portal de Datos Abiertos del Ecuador. https://www.datosabiertos.gob.ec/dataset/registro-de-matricula-mineduc

Ministerio de Educación del Ecuador. (s. f.). *Descomposición de la Matrícula – MINEDUC*. Portal de Datos Abiertos del Ecuador. https://www.datosabiertos.gob.ec/dataset/descomposicion-de-la-matricula-mineduc
