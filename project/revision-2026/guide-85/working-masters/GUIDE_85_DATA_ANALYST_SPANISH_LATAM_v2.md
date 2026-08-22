# Guía de Oportunidades para Toda la Vida 85 — Analista de Datos

**Versión:** 2.0 maestra de trabajo controlada  
**Idioma:** Español neutro de América Latina (`es-419`)  
**Referencia cuantitativa principal de EE. UU.:** O*NET-SOC 15-2041.00 — Statisticians  
**Referencia adyacente de EE. UU.:** O*NET-SOC 15-2051.01 — Business Intelligence Analysts  
**Comparación de Canadá:** NOC 21223 — Database analysts and data administrators  
**Comparaciones de Colombia:** CUOC 25210, CUOC 25110 y CUOC 21200, seleccionadas según las funciones del puesto  
**Fecha de revisión:** 2026-08-21  
**Fuente inglesa congelada:** blob `6139ca58f49692ef57556c3fd593e6d8b6d33f8b`

## Qué es esta carrera

Un analista de datos convierte preguntas en evidencia. El trabajo suele incluir localizar datos relevantes, comprender qué significa cada campo y cada fila, limpiar y validar la información, analizar patrones, poner a prueba supuestos, crear tablas o visualizaciones comprensibles y explicar qué respaldan —y qué no respaldan— los datos.

El título **Analista de Datos** es muy amplio. Algunos puestos se acercan a inteligencia de negocios y elaboración de informes. Otros se relacionan más con bases de datos, investigación de operaciones, estadística, finanzas, analítica de marketing, calidad, fraude, políticas públicas, salud, ciberseguridad, cadena de suministro, investigación o analítica de producto. Por eso, esta guía no supone que un solo código ocupacional oficial represente perfectamente todos los empleos llamados Data Analyst.

Para comparaciones controladas del mercado laboral, esta guía usa **O*NET-SOC 15-2041.00 — Statisticians** como referencia cuantitativa principal de Estados Unidos porque sus funciones oficiales incluyen directamente preparación de datos, análisis estadístico, identificación de tendencias, preparación de informes y evaluación de la calidad de datos, y porque O*NET enumera títulos de aprendizaje aprobados como Data Analyst y Junior Data Analyst. Sin embargo, la referencia de Statisticians es matemáticamente más avanzada y suele exigir más educación de posgrado que muchos puestos comerciales de Analista de Datos de nivel inicial. Esa limitación debe mantenerse visible cuando se presenten salarios, educación o perspectivas oficiales.

La Guía 84 analiza con más detalle la carrera de Business Intelligence Analyst. Ambas ocupaciones se superponen, pero no son intercambiables.

## Por qué el análisis de datos puede ser una buena oportunidad

Las organizaciones recopilan datos en casi todas las funciones, entre ellas:

- ventas;
- servicio al cliente;
- marketing;
- finanzas;
- contabilidad;
- operaciones;
- logística;
- cadena de suministro;
- calidad;
- salud;
- educación;
- gobierno;
- ciberseguridad;
- recursos humanos;
- manufactura;
- transporte;
- programas sin fines de lucro;
- investigación científica y social.

Los datos solo crean valor cuando alguien puede convertirlos en información confiable. Por eso, un buen analista combina habilidades técnicas con criterio, documentación y comunicación.

Es posible ingresar al análisis de datos desde:

- trabajos administrativos con muchos informes u hojas de cálculo;
- operaciones de negocio;
- apoyo financiero o contable;
- operaciones de atención al cliente;
- soporte de TI;
- bases de datos o gestión de registros;
- aseguramiento de calidad;
- marketing;
- logística;
- asistencia de investigación;
- soporte técnico o de ingeniería;
- estadística o matemáticas;
- programación o soporte de software.

Una progresión posible es:

**asistente de datos/reportes → analista de datos junior → analista de datos → analista senior → líder de analítica, analista BI, ingeniero de analítica, ingeniero de datos, científico de datos, analista de producto, analista de operaciones, analista de riesgo o puesto de gestión.**

La trayectoria exacta depende de la profundidad técnica, el conocimiento del sector, la educación, las expectativas del empleador y la capacidad demostrada para producir análisis confiables.

## Analista de Datos no es un solo tipo de trabajo

### Analista orientado a reportes

Puede concentrarse en:

- informes recurrentes;
- hojas de cálculo;
- seguimiento de KPI;
- tableros;
- SQL básico;
- conciliación;
- resúmenes operativos.

### Analista de negocio u operaciones con énfasis en datos

Puede concentrarse en:

- métricas de procesos;
- investigación de causa raíz;
- análisis de costos o productividad;
- niveles de servicio;
- apoyo a pronósticos;
- recomendaciones para partes interesadas.

### Analista estadístico o de investigación

Puede utilizar:

- muestreo;
- probabilidad;
- inferencia estadística;
- regresión;
- métodos experimentales o de encuestas;
- R, Python, SAS o SPSS;
- documentación formal de investigación.

### Analista orientado a bases de datos o gestión de datos

Puede trabajar más profundamente con:

- modelos de datos;
- estructuras de bases de datos;
- SQL;
- almacenes de datos;
- calidad de datos;
- gobierno de datos;
- diccionarios de datos;
- controles de acceso.

### Analista de producto, marketing, finanzas, riesgo o ciberseguridad

Aplica los mismos principios analíticos dentro de un dominio especializado. El conocimiento del sector puede ser tan importante como las herramientas.

Lea siempre la descripción real del puesto; no suponga que el título revela el nivel técnico completo.

## Primera regla: defina la pregunta antes de tocar los datos

Un análisis débil suele comenzar con un conjunto de datos y preguntar: “¿Qué puedo encontrar?”. Un análisis sólido comienza con una decisión o una pregunta.

Antes de crear una consulta, fórmula o gráfico, aclare:

1. ¿Qué pregunta intentamos responder?
2. ¿Qué decisión apoyará este análisis?
3. ¿Quién es la audiencia?
4. ¿Qué población o proceso está dentro del alcance?
5. ¿Qué periodo importa?
6. ¿Qué representa una fila?
7. ¿Qué fuente de datos es autoritativa?
8. ¿Qué reglas de negocio, filtros y exclusiones aplican?
9. ¿Qué nivel de precisión se necesita?
10. ¿Qué incertidumbre o limitación debe declararse?
11. ¿Quién puede acceder a los datos y al resultado?
12. ¿Cómo se validará la salida?

Si la pregunta es ambigua, escriba una versión comprobable antes de continuar.

## Fuente, linaje y granularidad de los datos

Todo resultado importante debe poder rastrearse hasta su fuente.

Documente, cuando corresponda:

- sistema fuente;
- tabla, archivo, API o informe;
- fecha/hora de extracción;
- propietario o custodio;
- frecuencia de actualización;
- definiciones de campos;
- granularidad de fila;
- transformaciones;
- uniones;
- filtros;
- exclusiones;
- campos derivados;
- reglas de cálculo;
- versión de salida;
- correcciones o historial de cambios.

### Granularidad

La granularidad indica qué representa una fila.

Una fila puede representar:

- un cliente;
- un pedido;
- una línea de pedido;
- un caso de soporte;
- un empleado-mes;
- una lectura de máquina;
- un pago;
- una respuesta de encuesta.

Unir tablas con granularidades incompatibles puede multiplicar filas e inflar totales. Antes de cada unión importante, pregunte:

- ¿La clave es única?
- ¿La relación es uno a uno, uno a muchos o muchos a muchos?
- ¿Qué ocurre con las filas sin coincidencia?
- ¿La unión puede duplicar medidas?
- ¿Debo agregar antes de unir?

## Habilidades de hojas de cálculo

Las hojas de cálculo siguen siendo comunes en trabajos de análisis. Entre las habilidades útiles están:

- ordenar y filtrar;
- tablas;
- referencias relativas y absolutas;
- `SUM`, `AVERAGE`, `COUNT`, `COUNTIF(S)`, `SUMIF(S)`;
- funciones de búsqueda;
- funciones de texto y fecha;
- funciones lógicas;
- tablas dinámicas;
- gráficos;
- formato condicional;
- validación de datos;
- importación/exportación;
- comprobación de errores;
- rangos protegidos y disciplina de acceso;
- Power Query o herramientas equivalentes de transformación cuando estén disponibles.

Una hoja de cálculo no es automáticamente un sistema analítico confiable. El trabajo importante debe evitar cambios manuales no documentados, fórmulas ocultas, totales codificados, valores copiados sin explicación y versiones sin control.

## SQL

SQL es una de las habilidades más transferibles para un analista.

Conceptos principales:

- `SELECT`;
- filtros con `WHERE`;
- ordenamiento;
- agregación;
- `GROUP BY`;
- joins;
- lógica `CASE`;
- expresiones de tabla comunes;
- subconsultas;
- funciones de ventana;
- lógica de fecha/hora;
- manejo de nulos;
- deduplicación;
- validación del número de filas.

Una consulta no es correcta solo porque se ejecuta.

Valide consultas importantes revisando:

- número esperado de filas;
- claves duplicadas;
- registros de muestra conocidos;
- totales frente a un informe autoritativo;
- límites de fecha;
- nulos y categorías faltantes;
- efecto de las uniones;
- filtros y exclusiones;
- conversiones de unidades;
- valores inesperados.

## Python, R y herramientas estadísticas

Algunos puestos usan programación para análisis reproducible. Las señales actuales de ofertas de O*NET para la referencia de Statisticians muestran fuerte demanda de R, SAS, Python y SQL, aunque esa referencia es más estadística que muchos puestos generales de Analista de Datos.

Capacidades útiles:

- importar datos;
- limpiar y remodelar;
- agrupar y agregar;
- unir conjuntos de datos;
- estadística descriptiva;
- visualización;
- notebooks o scripts reproducibles;
- pruebas estadísticas sencillas;
- validación;
- exportación de resultados controlados.

No intente aprender todos los lenguajes a la vez. Para muchas personas, una secuencia práctica es:

1. fundamentos de hojas de cálculo;
2. SQL;
3. visualización;
4. un lenguaje de scripting como Python o R;
5. estadística más profunda a medida que aumenten las exigencias del puesto.

## Limpieza de datos

Tareas frecuentes:

- estandarizar categorías;
- corregir mapeos aprobados;
- interpretar fechas;
- convertir tipos de datos;
- manejar valores faltantes;
- identificar registros duplicados;
- resolver identificadores inconsistentes;
- eliminar espacios innecesarios;
- validar rangos;
- conciliar totales con la fuente;
- documentar transformaciones.

Limpiar nunca debe significar modificar registros legítimos hasta que el resultado cuente una historia preferida.

Si los datos fuente parecen erróneos, siga el proceso autorizado de corrección. Mantenga la diferencia entre la fuente original, la fuente corregida y las transformaciones analíticas.

## Datos faltantes

Los valores faltantes pueden significar cosas distintas:

- realmente desconocido;
- no aplica;
- no recopilado;
- aún no disponible;
- suprimido por privacidad;
- falla en la transferencia;
- campo omitido por el usuario;
- valor predeterminado del sistema.

Nunca suponga que faltante significa cero.

Antes de completar, excluir o imputar datos faltantes, documente la razón y evalúe si el tratamiento puede sesgar el resultado.

## Duplicados

Un duplicado no es simplemente “dos filas que se parecen”. Dos transacciones pueden tener legítimamente el mismo cliente, monto y fecha.

Una regla defendible para duplicados debe identificar:

- la clave única esperada;
- el evento de negocio representado;
- qué campos determinan la unicidad;
- si varios registros pueden ser válidos;
- el proceso de corrección si se confirman duplicados.

## Estadística descriptiva

Fundamentos útiles:

- conteo;
- suma;
- media;
- mediana;
- mínimo;
- máximo;
- percentiles;
- proporciones;
- tasas;
- varianza;
- desviación estándar;
- distribuciones;
- tablas de frecuencia.

### Media frente a mediana

La media puede verse fuertemente influida por valores extremos. La mediana suele representar mejor distribuciones sesgadas como salarios, valores de propiedades o tiempos de respuesta.

Use la medida que corresponda a la pregunta y explíquela claramente.

## Valores atípicos

Los outliers pueden indicar:

- eventos realmente inusuales;
- errores de captura;
- fraude;
- problemas de equipo;
- clientes raros pero importantes;
- fallas de proceso;
- resultados extremos válidos.

No los elimine solo porque dificultan un gráfico o modelo.

Flujo defendible:

1. definir la regla de outlier;
2. inspeccionar los registros fuente;
3. determinar si el valor es válido;
4. documentar cualquier exclusión o corrección;
5. comparar resultados con y sin la observación cuando sea útil;
6. revelar sensibilidad material.

## Muestreo y sesgo de selección

Un conjunto de datos puede ser enorme y aun así inducir a error.

Pregunte:

- ¿Quién tuvo oportunidad de ser incluido?
- ¿Quién falta?
- ¿La participación fue voluntaria?
- ¿La muestra sobrerrepresenta ciertos lugares, clientes, dispositivos o periodos?
- ¿Un cambio de política o sistema alteró quién aparece en los datos?
- ¿Solo se registran casos exitosos?
- ¿Existe sesgo de supervivencia?

Más filas no eliminan automáticamente el sesgo.

## Correlación no significa causalidad

Que dos variables se muevan juntas no demuestra que una causó la otra.

Una relación puede deberse a:

- coincidencia;
- una tercera variable;
- causalidad inversa;
- sesgo de selección;
- tendencias temporales;
- diferencias de medición.

Use lenguaje causal solo cuando el diseño y la evidencia lo respalden. En otros casos use expresiones como **asociado con**, **correlacionado con**, **más alto entre** u **observado junto con**.

## Confianza e incertidumbre

Un analista inicial no necesita convertirse de inmediato en estadístico, pero sí debe comprender que las estimaciones tienen incertidumbre.

Conceptos importantes:

- tamaño de muestra;
- variabilidad;
- intervalos de confianza;
- margen de error;
- significancia estadística frente a significancia práctica;
- incertidumbre del modelo;
- error de pronóstico;
- sensibilidad a supuestos.

No convierta una estimación puntual en falsa certeza.

## Visualización de datos

Un buen gráfico facilita la comparación prevista; no manipula al lector.

Prácticas útiles:

- títulos claros;
- unidades etiquetadas;
- periodos relevantes visibles;
- texto legible;
- evitar decoración innecesaria;
- usar línea base cero en barras cuando la longitud representa magnitud;
- revelar ejes truncados cuando se justifique;
- evitar efectos 3D que distorsionan el tamaño;
- ordenar categorías de manera significativa;
- mostrar etiquetas o tablas cuando se necesitan valores exactos;
- usar contraste y patrones accesibles;
- incluir texto alternativo o resumen textual accesible cuando el contexto de publicación lo requiera.

### Evite gráficos engañosos

No:

- trunque ejes para exagerar diferencias sin explicación;
- compare totales de poblaciones muy distintas cuando deberían usarse tasas;
- seleccione periodos para favorecer una conclusión;
- oculte categorías que debilitan la historia preferida;
- use escalas inconsistentes entre gráficos similares;
- implique causalidad a partir de una asociación visual.

## Calidad de datos

Dimensiones comunes:

- exactitud;
- integridad/completitud;
- consistencia;
- oportunidad;
- validez;
- unicidad;
- integridad referencial o estructural.

La calidad debe evaluarse según el uso previsto. Un campo suficiente para un conteo operativo interno puede ser inadecuado para una afirmación regulatoria, financiera, clínica o pública.

## Validación y conciliación

Antes de publicar un resultado importante:

- compare totales con una fuente autoritativa;
- verifique registros de muestra;
- inspeccione patrones de faltantes y duplicados;
- confirme límites de fecha;
- revise denominadores;
- pruebe casos límite;
- revise unidades y moneda;
- verifique filtros;
- inspeccione cardinalidad de joins;
- compare tendencias con eventos conocidos;
- solicite revisión de otra persona calificada para lógica de alto impacto cuando la organización lo exija.

Si el resultado no concilia, investigue antes de presentarlo como final.

## Documentación y reproducibilidad

Un buen analista deja un rastro que otra persona competente puede seguir.

Documente:

- propósito;
- propietario;
- fuente;
- fecha de actualización;
- definiciones;
- lógica;
- consultas o fórmulas;
- exclusiones;
- supuestos;
- limitaciones;
- versión;
- validación realizada;
- historial de correcciones.

Cuando corresponda, use:

- control de versiones;
- SQL guardado;
- scripts reutilizables;
- notebooks;
- diccionarios de datos;
- definiciones de métricas;
- repositorios controlados de informes;
- registros de cambios.

## Comunicación de resultados

Un resumen analítico útil debe responder:

1. ¿Qué analizamos?
2. ¿Qué encontramos?
3. ¿Qué tan grande es el efecto o la diferencia?
4. ¿Qué evidencia lo respalda?
5. ¿Cuáles son las limitaciones?
6. ¿Qué decisión o siguiente paso está respaldado?

Evite jerga cuando una explicación sencilla funcione.

Separe:

- hechos observados;
- cálculos;
- supuestos;
- interpretaciones;
- pronósticos;
- recomendaciones.

## Privacidad, seguridad y control de acceso

Los analistas pueden trabajar con datos de clientes, empleados, finanzas, operaciones, salud, ubicación, autenticación, dispositivos o información confidencial del negocio.

Controles prácticos:

- usar sistemas aprobados por el empleador;
- aplicar acceso de mínimo privilegio;
- no copiar conjuntos protegidos a almacenamiento personal;
- no enviar extractos al correo personal;
- no eludir controles de acceso “para terminar el trabajo”;
- usar almacenamiento y transferencia cifrados aprobados;
- minimizar la recopilación;
- eliminar campos innecesarios;
- respetar reglas de retención y eliminación;
- verificar destinatarios antes de compartir extractos;
- reportar exposición o acceso no autorizado sospechado;
- usar MFA y prácticas de contraseñas aprobadas;
- seguir la política organizacional para exportaciones, capturas y archivos locales.

Un analista no debe inventar políticas legales o de seguridad. Siga el gobierno aprobado y escale la incertidumbre.

## IA responsable y automatización

La IA puede apoyar trabajo analítico de bajo riesgo cuando la política organizacional lo permita.

Usos posibles:

- explicar una fórmula;
- proponer SQL, Python o R;
- sugerir preguntas exploratorias;
- generar datos sintéticos de prueba;
- redactar documentación;
- resumir información pública no sensible;
- proponer alternativas de gráficos;
- revisar estilo de código.

La validación humana sigue siendo obligatoria.

No:

- cargue datos confidenciales, credenciales, contratos privados, registros regulados o extractos protegidos a una herramienta de IA no aprobada;
- suponga que SQL o código generado por IA es correcto;
- publique una interpretación redactada por IA sin verificar los cálculos subyacentes;
- acepte campos, definiciones o citas inventadas;
- permita que la IA elija exclusiones que alteren materialmente el resultado sin revisión humana documentada;
- trate la salida de IA como evidencia;
- presente predicciones de IA como hechos observados;
- permita publicación autónoma de analítica crítica fuera del gobierno aprobado.

Regla práctica: **la IA puede ayudar a redactar, explicar o probar; los datos autoritativos, la lógica aprobada y la revisión humana responsable determinan el resultado final.**

El AI Risk Management Framework de NIST y su Generative AI Profile ofrecen orientación voluntaria de gestión de riesgos. No reemplazan el gobierno organizacional ni las responsabilidades profesionales.

## Límites éticos

Un Analista de Datos no debe:

- alterar datos fuente para producir una conclusión preferida;
- ocultar filtros o exclusiones;
- eliminar outliers válidos porque debilitan la narrativa;
- elegir un denominador después de ver qué resultado luce mejor;
- presentar correlación como causalidad;
- fabricar datos, registros, citas, hallazgos o muestras;
- ocultar limitaciones materiales;
- eludir controles de acceso;
- publicar información protegida o confidencial sin autorización;
- afirmar certeza estadística no sustentada por el método;
- emitir conclusiones contables, legales, clínicas, regulatorias o de ingeniería fuera de la experiencia asignada;
- manipular visualizaciones para engañar;
- presentar un pronóstico o modelo como garantía.

Un buen análisis es rastreable, reproducible, transparente sobre la incertidumbre y abierto a correcciones.

## Accesibilidad y comunicación inclusiva de datos

Prácticas útiles:

- títulos descriptivos de gráficos;
- ejes con etiquetas significativas;
- contraste suficiente;
- no depender solo del color;
- patrones o etiquetas directas cuando convenga;
- tamaños de letra legibles;
- tablas accesibles;
- texto alternativo o resúmenes textuales para gráficos importantes;
- orden lógico de lectura;
- explicación en lenguaje sencillo;
- tableros accesibles por teclado cuando la plataforma lo permita;
- pruebas con herramientas de accesibilidad integradas cuando estén disponibles.

Las normas y obligaciones legales de accesibilidad varían según jurisdicción y contexto. Esta guía no certifica que un tablero, informe o sistema sea legalmente accesible.

## Educación y rutas de entrada — Estados Unidos

La referencia oficial de Statisticians tiene un fuerte componente de posgrado: O*NET informa que muchas nuevas contrataciones en esa ocupación tienen maestría. Eso **no** debe interpretarse como requisito universal para todos los puestos de Analista de Datos.

Los puestos comerciales y operativos pueden aceptar combinaciones de:

- licenciatura o grado universitario;
- associate degree;
- certificado técnico;
- capacitación del empleador;
- aprendizaje;
- experiencia laboral relevante;
- evidencia de portafolio;
- buenas habilidades en hojas de cálculo/SQL/reportes;
- conocimiento del sector.

Áreas de estudio comunes:

- estadística;
- matemáticas;
- analítica de datos;
- ciencias de la computación;
- sistemas de información;
- negocios;
- economía;
- finanzas;
- ingeniería;
- ciencias sociales;
- salud u otros campos específicos.

### Localizadores de capacitación gratuita/de bajo costo y financiamiento en EE. UU.

CareerOneStop ayuda a localizar:

- American Job Centers;
- programas de capacitación elegibles para WIOA;
- servicios locales de capacitación;
- información de carreras.

La elegibilidad y el financiamiento WIOA no son automáticos. Un American Job Center puede explicar elegibilidad local, proveedores aprobados y servicios de apoyo.

Busque más allá de “Data Analyst”. Los programas pueden aparecer bajo:

- data analytics;
- statistics;
- business analytics;
- computer information systems;
- database technology;
- business intelligence;
- programming;
- Excel/SQL;
- digital skills.

### Aprendizaje y formación basada en el trabajo

El perfil de Statisticians de O*NET enlaza títulos de aprendizaje aprobados, incluidos **Data Analyst**, **Data Analyst (Nof)** y **Junior Data Analyst**.

La disponibilidad depende del lugar y del empleador. Verifique oportunidades actuales mediante Apprenticeship.gov y los sistemas locales de fuerza laboral.

Otras rutas de aprendizaje laboral pueden incluir:

- pasantías pagadas;
- puestos trainee;
- trabajos de asistente de reportes;
- capacitación financiada por el empleador;
- proyectos con datos internos autorizados;
- investigación u operaciones supervisadas.

## Canadá

Job Bank de Canadá vincula **Data Analyst - Informatics and Systems** con **NOC 21223 — Database analysts and data administrators**. Es una comparación útil, pero está más orientada a gestión de datos que muchos puestos generales de análisis.

Los requisitos actuales de Job Bank indican que normalmente se requiere un programa universitario o de college, por lo general en ciencias de la computación, ingeniería informática o matemáticas, junto con programación o experiencia relacionada. Job Bank identifica actualmente esta ocupación como no regulada a nivel nacional, aunque los requisitos del empleador varían.

### Referencia salarial de Canadá

Los salarios nacionales actuales de Job Bank, actualizados el 19 de noviembre de 2025, muestran aproximadamente:

- **C$25.00/hora bajo**;
- **C$40.87/hora mediano**;
- **C$61.03/hora alto**.

Estos valores corresponden a NOC 21223, no a todos los títulos posibles de Analista de Datos.

### Capacitación y apoyos de financiamiento en Canadá

Canada.ca ofrece enlaces nacionales a:

- ayuda estudiantil;
- formación de habilidades;
- servicios de empleo;
- programas provinciales/territoriales;
- capacitación corta reconocida;
- información sobre Employment Insurance y capacitación cuando corresponda.

La elegibilidad, el financiamiento y el diseño del programa varían según provincia, territorio y circunstancias individuales.

## Colombia

El título genérico **Analista de datos** abarca varios grupos CUOC. Esta guía usa comparaciones por función y no afirma un único código colombiano exclusivo.

### CUOC 25210 — Diseñadores y administradores de bases de datos

Relevante cuando el trabajo enfatiza:

- estructuras de bases de datos;
- arquitectura de datos;
- warehouses;
- administración de datos;
- calidad de datos;
- limpieza/extracción/transformación;
- visualización y comunicación;
- seguridad e integridad de bases de datos.

El grupo oficial incluye el título **Analista de datos comerciales**.

### CUOC 25110 — Analistas de sistemas

Relevante para roles de analítica y BI. Las denominaciones oficiales incluyen:

- Analista de analytics;
- Analista de inteligencia de negocios;
- Analista de Power BI;
- Analista de información comercial;
- Analista de procesamiento de información.

### CUOC 21200 — Matemáticos, actuarios y estadísticos

Relevante cuando el trabajo es fuertemente estadístico o de investigación. Incluye **Analista estadístico**.

OCUPACOL advierte que los indicadores ocupacionales mostrados en sus perfiles no tienen representatividad estadística bajo la metodología aplicada. Por ello, esta guía no presenta esos rangos como salario nacional representativo de Analista de Datos.

### Rutas SENA

SENA Betowa lista actualmente rutas relevantes, entre ellas:

**Programación para analítica de datos**  
- Técnico;
- 2.208 horas;
- formación titulada;
- competencias de procesamiento, integración, visualización y análisis de datos.

**Visualización de datos usando Power BI**  
- curso complementario/especial;
- 48 horas;
- útil como formación focalizada y no como calificación profesional completa.

**Analítica de datos para procesos logísticos**  
- formación complementaria virtual;
- 48 horas;
- contenido de analítica aplicado a logística.

La disponibilidad, ciudad, modalidad, cohortes, cupos, requisitos y fechas pueden cambiar. Verifique Betowa en vivo antes de postular.

## América Latina y el Caribe

OIT/Cinterfor ofrece una red regional y un localizador de instituciones nacionales de formación profesional. Puede ayudar a identificar entidades de capacitación y comparar sistemas de desarrollo de habilidades en América Latina y el Caribe.

Es un localizador y una red de conocimiento; no garantiza que exista un curso, beca o financiamiento de Analista de Datos en cada país.

Verifique catálogo, elegibilidad, costo, modalidad y reconocimiento del empleador con la institución nacional correspondiente.

## Investigación de ingresos — úsela con cuidado

### Referencia cuantitativa oficial de Estados Unidos

Para **Statisticians (O*NET-SOC 15-2041.00)**, los datos salariales BLS 2025 mostrados por O*NET indican:

| Percentil | Anual | Por hora |
|---|---:|---:|
| 10 | $54,680 | $26.29 |
| 25 | $70,710 | $33.99 |
| Mediana | $105,650 | $50.79 |
| 75 | $143,140 | $68.82 |
| 90 | $170,700 | $82.07 |

Son salarios de **Statisticians**, no una tabla salarial universal para Data Analyst.

### Perspectiva de EE. UU. para la referencia Statisticians

Los datos O*NET/BLS muestran:

- empleo 2024: aproximadamente **32,200**;
- empleo proyectado 2034: aproximadamente **34,900**;
- crecimiento proyectado: **9%**;
- vacantes proyectadas por año: aproximadamente **2,000**.

Estas cifras pertenecen a la referencia de Statisticians.

### Estimación no gubernamental actual de EE. UU.

La página salarial actual de Indeed para **Data Analyst** en Estados Unidos reporta un salario base promedio de aproximadamente **$85,108/año**, con un rango mostrado de aproximadamente **$52,084–$139,074/año** y cerca de **8.1 mil observaciones salariales provenientes de ofertas de empleo de los 36 meses anteriores** en la página revisada de 2026.

Es una **estimación de mercado no gubernamental y específica del título**, no una estadística salarial oficial ni una compensación garantizada. Las páginas de mercado cambian; verifique el valor actual antes de tomar decisiones salariales.

### Canadá

Los salarios nacionales de Job Bank para NOC 21223 son aproximadamente:

- C$25.00/hora bajo;
- C$40.87/hora mediano;
- C$61.03/hora alto.

Corresponden a la comparación con database analysts/data administrators, no a una tarifa universal de Analista de Datos.

### Colombia

Como las correspondencias CUOC/OCUPACOL dependen de la función y OCUPACOL advierte que sus indicadores ocupacionales no tienen representatividad estadística, esta guía no inventa un único salario nacional oficial representativo para Analista de Datos.

Para decisiones de compensación en Colombia, compare varias ofertas vigentes de empleadores y fuentes de mercado reputadas para el alcance exacto, ciudad, seniority, idiomas, stack tecnológico y modalidad contractual.

## Secuencia práctica de aprendizaje

### Etapa 1 — fundamentos

Aprenda:

- hojas de cálculo;
- porcentajes y tasas;
- estadística descriptiva;
- tablas limpias;
- gráficos básicos;
- privacidad de datos;
- documentación.

### Etapa 2 — consultas

Aprenda:

- conceptos relacionales;
- claves;
- joins;
- filtrado y agregación SQL;
- controles de calidad;
- validación.

### Etapa 3 — análisis

Aprenda:

- distribuciones;
- datos faltantes;
- outliers;
- muestreo;
- sesgo;
- correlación frente a causalidad;
- visualización accesible;
- comunicación con partes interesadas.

### Etapa 4 — automatización

Agregue un lenguaje como Python o R para:

- limpieza reproducible;
- conjuntos de datos grandes;
- análisis repetible;
- flujos estadísticos;
- validación automatizada.

### Etapa 5 — profundidad de dominio

Elija un área de negocio o técnica, por ejemplo:

- finanzas;
- marketing;
- salud;
- ciberseguridad;
- logística;
- calidad;
- políticas públicas;
- operaciones;
- analítica de producto.

Comprender el dominio ayuda a formular mejores preguntas y detectar resultados improbables.

## Proyectos de portafolio sin exponer datos privados

Fuentes seguras:

- conjuntos de datos públicos del gobierno;
- portales de datos abiertos;
- datos con licencia explícita;
- datos sintéticos creados por usted;
- datasets de formación cuyos términos permitan uso en portafolio.

Un buen proyecto inicial puede incluir:

1. pregunta;
2. fuente y licencia;
3. diccionario de datos;
4. pasos de limpieza;
5. SQL o código;
6. controles de validación;
7. gráficos o dashboard;
8. hallazgos;
9. limitaciones;
10. resumen accesible;
11. README con pasos para reproducir.

No cargue:

- datos de empleadores;
- registros de clientes;
- información de empleados;
- capturas de sistemas confidenciales;
- SQL interno con identificadores sensibles;
- definiciones propietarias de reportes;
- credenciales o tokens.

## Plan inicial de cuatro semanas

### Semana 1 — hojas de cálculo y calidad de datos

- elija un conjunto de datos público o sintético;
- identifique qué representa una fila;
- cree un diccionario sencillo;
- revise faltantes y duplicados;
- calcule conteos, tasas, media y mediana;
- cree un gráfico honesto.

### Semana 2 — SQL

- cree o use una base pequeña de práctica;
- escriba consultas de filtrado y agregación;
- practique joins;
- valide el número de filas antes y después de unir;
- documente una consulta en lenguaje sencillo.

### Semana 3 — análisis y comunicación

- escriba una pregunta clara de negocio o investigación;
- analícela con su dataset;
- identifique al menos dos limitaciones;
- cree un gráfico accesible y un resumen breve;
- distinga observación de interpretación.

### Semana 4 — portafolio y preparación laboral

- limpie el README;
- documente fuente y licencia;
- incluya pasos reproducibles;
- elimine información sensible;
- redacte dos bullets de currículum que describan el proyecto con precisión;
- busque puestos actuales con varios títulos relacionados;
- compare requisitos reales antes de decidir qué aprender después.

## Títulos de búsqueda laboral

Según sus habilidades, considere:

- Data Analyst;
- Junior Data Analyst;
- Reporting Analyst;
- Business Data Analyst;
- Operations Analyst;
- Marketing Analyst;
- Sales Analyst;
- Quality Analyst;
- Research Analyst;
- Data Quality Analyst;
- BI Analyst;
- Power BI Analyst;
- SQL Analyst;
- Analytics Specialist;
- Data Coordinator;
- Reporting Specialist.

Lea las funciones con cuidado. Dos puestos con el mismo título pueden tener requisitos técnicos y educativos muy distintos.

## Preguntas antes de aceptar un puesto

Considere preguntar:

- ¿Cuáles son las principales fuentes de datos?
- ¿Se usa SQL a diario?
- ¿Qué herramientas se utilizan para tableros y análisis?
- ¿Cómo se gobiernan las definiciones de métricas?
- ¿Quién es responsable de la calidad de datos?
- ¿Cómo se espera que los analistas validen resultados?
- ¿Existe revisión de código o revisión entre pares?
- ¿Qué datos pueden consultarse de manera remota?
- ¿Qué capacitación de privacidad/seguridad se exige?
- ¿Son comunes horas extra, guardias o picos por fechas límite?
- ¿El puesto es principalmente reportes, análisis estadístico, análisis de negocio o bases de datos?
- ¿Qué habilidades distinguen a un junior de un senior?
- ¿El empleador ofrece capacitación o apoyo para certificaciones?

## Fuentes y enlaces de verificación

Verifique valores y disponibilidad de programas antes de tomar una decisión importante.

### Estados Unidos

- O*NET — Statisticians: https://www.onetonline.org/link/details/15-2041.00
- O*NET — Business Intelligence Analysts: https://www.onetonline.org/link/details/15-2051.01
- CareerOneStop WIOA training locator: https://www.careeronestop.org/LocalHelp/EmploymentAndTraining/find-WIOA-training-programs.aspx
- Apprenticeship.gov: https://www.apprenticeship.gov/
- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework

### Canadá

- Job Bank — NOC 21223 occupational information: https://www.jobbank.gc.ca/
- Canada training gateway: https://www.canada.ca/en/services/jobs/training.html

### Colombia

- OCUPACOL: https://ocupacol.mintrabajo.gov.co/
- SENA Betowa: https://betowa.sena.edu.co/

### América Latina y el Caribe

- OIT/Cinterfor: https://www.oitcinterfor.org/

### Contexto actual de mercado no gubernamental

- Indeed U.S. Data Analyst salary page: https://www.indeed.com/career/data-analyst/salaries

## Aviso importante

Esta guía ofrece información general de educación y planificación profesional. No garantiza empleo, ingresos, admisión, financiamiento, colocación en aprendizaje, certificación, ascenso ni ningún otro resultado. Las correspondencias ocupacionales son comparaciones y pueden no ser equivalencias exactas entre jurisdicciones. Los requisitos, salarios, expectativas tecnológicas, disponibilidad de formación y condiciones laborales cambian con el tiempo.

No se afirma certificación humana independiente, acreditación profesional, revisión legal, certificación estadística, certificación de accesibilidad ni certificación de traducción, salvo que exista documentación separada que lo demuestre.

## Autor y asistencia de IA

Creada y dirigida por **Alberto “Al” Leiva**. ChatGPT apoyó la investigación, organización, edición, apoyo de traducción y preparación documental bajo la dirección del autor. El autor conserva la responsabilidad de las decisiones editoriales y de publicación.

## Licencia

Salvo que un archivo indique lo contrario, este material se distribuye bajo **CC BY-NC-SA 4.0**.