# Guía de Oportunidades para Toda la Vida 92 — Técnico en Sistemas de Información Geográfica

**Versión:** 2.0 maestra de trabajo controlada  
**Idioma:** Español neutro de América Latina (`es-419`)  
**Referencia principal de EE. UU.:** O*NET-SOC 15-1299.02 — Geographic Information Systems Technologists and Technicians  
**Comparación de Canadá:** NOC 22214 — Technical occupations in geomatics and meteorology  
**Comparación de Colombia:** CUOC 31123 — Técnicos en cartografía  
**Fecha de revisión:** 2026-08-22  
**Fuente inglesa congelada:** blob `5fc776670bc33d9e2b01a5dda8084a9099627165`

## Qué es esta carrera

Un Técnico en Sistemas de Información Geográfica (SIG/GIS) ayuda a recolectar, organizar, validar, analizar, mapear y mantener información relacionada con ubicación. El trabajo puede incluir edición de capas, mantenimiento de bases espaciales, digitalización, georreferenciación, control de geometría y atributos, elaboración de mapas/reportes, soporte a usuarios, análisis espacial, automatización y publicación autorizada de mapas o servicios web.

El título se cruza con tecnólogo GIS, técnico geomático, técnico cartográfico, técnico de mapeo y funciones geoespaciales junior. Algunas vacantes son principalmente de producción; otras requieren más análisis, programación, bases de datos o soporte. Lea las funciones reales y no suponga que todos los puestos utilizan las mismas herramientas o tienen el mismo nivel analítico.

Estados Unidos tiene una ocupación directa en **O*NET-SOC 15-1299.02**. Canadá corresponde directamente a **NOC 22214**, que incluye GIS Technician. Colombia tiene una comparación directa en **CUOC 31123 — Técnicos en cartografía**, que incluye explícitamente **Técnico sistemas de información geográfica**.

## Divulgación crítica sobre estadísticas de EE. UU.

O*NET indica expresamente que los salarios y datos de empleo de 15-1299.02 se recopilan desde **Computer Occupations, All Other**. Son cifras oficiales, pero no representan una población salarial pura del título GIS Technician.

Esto importa porque una estimación actual no gubernamental específica del título GIS Technician es mucho menor que la mediana cruzada de O*NET. No se deben promediar ambos conjuntos. Describen poblaciones, definiciones y metodologías diferentes.

## Qué hace un técnico GIS

Las tareas actuales de O*NET respaldan trabajo como:
- crear y actualizar capas, mapas, tablas y reportes;
- mantener bases de datos GIS;
- digitalizar o convertir entidades;
- revisar vigencia, utilidad, calidad y documentación de datos;
- apoyar usuarios y clientes;
- analizar relaciones espaciales;
- integrar información espacial y no espacial;
- interpretar imágenes aéreas u ortofotos;
- apoyar remote sensing/cartografía;
- desarrollar scripts o aplicaciones GIS cuando corresponda;
- publicar o soportar productos web GIS;
- documentar métodos y limitaciones.

Un mapa visualmente atractivo puede ser incorrecto si CRS, linaje, atributos, geometría o clasificación son incorrectos.

## Modelos de datos espaciales

### Datos vectoriales
Los vectores representan entidades discretas mediante:
- **puntos** — árboles, sensores, direcciones o activos;
- **líneas** — vías, ríos, tuberías o rutas;
- **polígonos** — parcelas, zonas, lagos o áreas de servicio.

Cada entidad puede tener atributos en una tabla.

### Datos raster
Raster usa celdas/píxeles y puede representar imágenes, elevación, temperatura, cobertura del suelo u otras superficies continuas. Resolución y tamaño de celda importan. Ampliar un raster de baja resolución no crea detalle espacial real.

### Atributos
Comprenda tipos de campo, dominios/valores codificados, nulos, validación, joins/relates, identificadores y diccionarios de datos.

### Bases espaciales
GIS puede usar geodatabases de archivo, enterprise geodatabases o bases relacionales con capacidades espaciales. Comprenda tablas, claves, índices, permisos, transacciones y version/edit workflows según el puesto.

## Sistemas de referencia de coordenadas

Errores de CRS pueden invalidar un trabajo aparentemente correcto.

Distinga:
- sistemas geográficos con coordenadas angulares como latitud/longitud;
- sistemas proyectados con unidades lineales;
- datum y marco de referencia;
- proyección;
- unidades;
- identificadores como códigos EPSG a nivel conceptual;
- transformación/reproyección.

Que una capa aparezca en el lugar esperado no prueba que su metadata de CRS sea correcta. El software puede reproyectar dinámicamente para visualización y ocultar errores.

## Distorsión de proyección y adecuación

Toda proyección implica compromisos. Puede distorsionar área, forma, dirección o distancia.

Antes de medir o analizar pregunte:
- ¿Cuál es el uso previsto?
- ¿Cuál es la extensión geográfica?
- ¿Qué unidades se necesitan?
- ¿La proyección preserva la propiedad relevante para esta tarea?

No reporte áreas o distancias precisas desde un CRS inadecuado solo porque el software entrega un número.

## Linaje y metadata

Un dataset GIS defendible debe conservar lo conocido sobre:
- fuente/procedencia;
- fecha o período de captura;
- organización responsable;
- exactitud posicional;
- exactitud de atributos;
- completitud;
- consistencia lógica;
- escala/resolución;
- CRS y datum;
- transformaciones;
- pasos de procesamiento;
- historial de edición;
- estado autoritativo versus derivado;
- limitaciones conocidas.

Si se transforma, generaliza, recorta, une, clasifica o deriva información, documente lo necesario para reproducir o comprender el resultado.

## Calidad de datos

Calidad significa adecuación al propósito. Revise:
- atributos faltantes/ inválidos;
- duplicados;
- valores imposibles;
- información obsoleta;
- unidades inconsistentes;
- CRS incompatibles;
- defectos geométricos;
- cobertura incompleta;
- códigos/nombres inconsistentes;
- conflictos entre fuentes;
- outliers inesperados.

No “corrija” silenciosamente datos autoritativos cuando corresponde documentar y escalar al propietario de la fuente.

## Geometría y topología

Problemas frecuentes:
- self-intersections;
- entidades duplicadas;
- anillos inválidos;
- overlaps;
- gaps;
- líneas colgantes;
- undershoots/overshoots;
- polígonos sliver;
- segmentos desconectados;
- snapping/tolerance incorrectos.

Las reglas de topología dependen del dominio. Un detector automático identifica condiciones, pero no decide todas las reglas del negocio sin requisitos.

## Georreferenciación

Flujo defendible:
1. identificar imagen/mapa fuente y CRS objetivo;
2. seleccionar puntos de control confiables y distribuidos;
3. elegir transformación adecuada;
4. revisar residual/error;
5. inspeccionar el resultado;
6. validar contra referencias independientes conocidas cuando sea posible;
7. documentar fuente, método, puntos y limitaciones.

Un residual bajo no prueba por sí solo exactitud posicional real. Puntos de control pobres pueden producir un resultado matemáticamente limpio pero incorrecto.

## Digitalización y captura

Al digitalizar:
- use escala/zoom apropiados;
- siga reglas de snapping/tolerance;
- capture atributos consistentemente;
- respete exactitud/resolución de la fuente;
- evite falsa precisión;
- valide geometría y atributos;
- documente fuente y método.

Trazar una fuente borrosa con mucho zoom no genera exactitud topográfica o catastral.

## Cartografía y comunicación

Un mapa profesional debe tener propósito y audiencia claros. Considere extensión, escala, simbología, método de clasificación, jerarquía de etiquetas, leyenda, título, fuente/fecha, unidades, incertidumbre, contraste, accesibilidad y texto/tablas de apoyo.

Evite decisiones visuales engañosas. Símbolos excesivos, rampas dramáticas o cortes de clasificación inadecuados pueden exagerar diferencias.

## Métodos de clasificación

Mapas coropléticos pueden cambiar de significado según el método: intervalos iguales, cuantiles, natural breaks o rangos de dominio.

Antes de clasificar:
- revise distribución;
- distinga conteos, tasas o medidas normalizadas;
- identifique outliers;
- considere audiencia;
- documente método cuando afecte interpretación.

Mapear conteos crudos puede engañar cuando las regiones difieren mucho en población o tamaño.

## Análisis espacial

Puede incluir buffers, overlays/intersections, clipping, dissolve, proximity, spatial joins, network analysis, raster analysis, terrain/surface y otras técnicas.

Antes de interpretar resultados verifique CRS, unidades, calidad de fuentes, supuestos y parámetros. Un geoproceso que termina correctamente puede responder la pregunta equivocada.

## SQL y bases espaciales

SQL puede apoyar queries, joins, validación y operaciones en bases espaciales. Dependiendo de la plataforma puede usar geometry/geography y relaciones espaciales.

Practique en ambientes de lectura o no productivos. No ejecute updates destructivos sobre datos empresariales autoritativos sin permiso, backup/change control y plan de validación.

## Python y automatización

Python, ArcPy y otros scripts pueden automatizar geoprocesos repetitivos.

Conserve:
- inputs;
- parámetros;
- versión del script;
- versión del ambiente/software cuando aplique;
- output/version;
- warnings/errors;
- resultados de validación.

La automatización escala errores igual que procesos correctos. Pruebe con un subconjunto controlado antes de una operación grande o destructiva.

## Señales tecnológicas actuales

O*NET/Lightcast 2025 muestra:
- ESRI ArcGIS **75%**;
- GIS systems **67%**;
- Python **34%**;
- SQL **22%**;
- GIS software **21%**;
- Microsoft Office **14%**;
- Excel **14%**;
- JavaScript **13%**;
- AutoCAD **10%**;
- ArcMap **7%**;
- QGIS **7%**;
- ArcGIS Survey123 **6%**;
- Access **6%**;
- PowerPoint **6%**;
- Azure **5%**;
- ArcPy **5%**;
- Outlook **5%**;
- AWS **5%**.

Son señales de ofertas, no requisitos universales. CRS, calidad, razonamiento espacial, linaje y reproducibilidad son más transferibles que una interfaz específica.

## Web GIS y publicación

Web GIS puede incluir hosted feature layers, servicios de mapas/tiles, dashboards, web maps y permisos públicos/privados.

Antes de publicar o cambiar sharing:
- confirme audiencia;
- verifique permisos;
- revise campos sensibles;
- confirme que la precisión de ubicación sea apropiada;
- revise dependencias;
- documente owner/fuente;
- confirme que la vista pública no exponga datos protegidos.

Una capa pública puede revelar ubicaciones sensibles aunque la base original siga privada.

## Privacidad y ubicaciones sensibles

Los datos geoespaciales pueden revelar domicilios/personas, clientes/activos, infraestructura crítica, rutas operativas, recursos ambientales/culturales sensibles o poblaciones vulnerables.

Controles posibles:
- need-to-know;
- publicación aprobada;
- agregación/generalización/redacción;
- eliminación de identificadores innecesarios;
- protección de credenciales;
- escalamiento de incidentes.

No publique coordenadas protegidas, capas privadas o detalles de infraestructura crítica en mapas públicos, almacenamiento personal, repositorios públicos o IA no aprobada.

## Datos de campo y móviles

Considere seguridad del dispositivo/cuenta, copias offline, conflictos de sync, timestamps, exactitud GPS, validación de formularios, fotos, información personal, pérdida del dispositivo, retención y autorización de upload.

Una coordenada GPS no es automáticamente survey-grade. Conozca la exigencia de exactitud del trabajo.

## Versionamiento y change control

Para datos autoritativos, conozca quién puede editar, aprobar o publicar. Puede haber versioning, branch workflows, edit tracking o tickets formales.

Tener permiso técnico de escritura no significa autoridad para modificar límites oficiales, parcelas legales, redes de servicios u otros datasets controlados.

## Límite con topografía y registros legales

Un técnico GIS puede usar información de survey, parcelas, ingeniería o límites legales, pero editar/visualizar en GIS no otorga autoridad profesional de topografía.

No afirme survey-grade accuracy, altere límites legales ni certifique registros catastrales sin autoridad profesional y evidencia correspondiente. Escale interpretación legal/topográfica al profesional autorizado.

## Remote sensing e imágenes

Revise fecha de adquisición, resolución, nubes/obstrucciones, corrección geométrica, CRS, método de clasificación, ground truth/referencia y nivel de incertidumbre.

La clasificación automatizada debe validarse contra referencias apropiadas antes de decisiones operativas.

## IA responsable

La IA aprobada puede ayudar con explicación de código, borradores de metadata, ideas de geoprocesamiento, revisión de geocoding, extracción de features, clasificación, documentación y datos sintéticos.

Controles:
- no enviar coordenadas protegidas, locations de clientes/activos, capas propietarias, credenciales o imágenes restringidas a herramientas no aprobadas;
- validar código y lógica geoespacial;
- verificar CRS, unidades y supuestos;
- detectar funciones/paquetes inventados;
- evaluar sesgo/error de extracción/clasificación;
- preservar linaje;
- no permitir que IA invente coordenadas autoritativas, límites legales o exactitud survey-grade;
- mantener validación humana/de dominio.

El output de IA no es evidencia de ejecución correcta.

## Accesibilidad

Use texto legible, contraste suficiente, codificación que no dependa solo de color, leyendas/labels claros, patrones/formas cuando ayuden, contexto/alt text para mapas estáticos, alternativas de texto/tabla para información clave y controles web navegables por teclado cuando corresponda.

Un scanner automatizado no demuestra cumplimiento legal.

## Estados Unidos — educación y workforce

O*NET 15-1299.02 es una ocupación GIS directa, pero los requisitos varían. Las rutas pueden incluir GIS/geospatial technology, geografía, ciencias ambientales, planning, informática, surveying/mapping u otras áreas según funciones.

CareerOneStop/American Job Centers permite investigar WIOA y recursos locales. Elegibilidad y financiamiento varían; el locator no garantiza pago de un programa.

## Estados Unidos — salarios y perspectiva oficiales cruzados

O*NET usa **Computer Occupations, All Other** para los valores oficiales 2025:

| Percentil | Anual | Por hora |
|---|---:|---:|
| 10 | $55,940 | $26.89 |
| 25 | $79,370 | $38.16 |
| Mediana | $116,580 | $56.05 |
| 75 | $157,500 | $75.72 |
| 90 | $188,470 | $90.61 |

Perspectiva 2024–2034, también cruzada:
- empleo 2024: **472,000**;
- proyectado 2034: **510,500**;
- crecimiento: **8%**;
- vacantes anuales: **31,300**.

Son cifras oficiales, pero no una población salarial/ocupacional pura del título GIS Technician.

### Contexto no gubernamental específico del título

Indeed, actualizado **2 de agosto de 2026**, muestra para **GIS Technician** aproximadamente:
- **$25.88/hora promedio**;
- **$17.60/hora bajo**;
- **$38.06/hora alto**;
- **749** observaciones;
- **36 meses**.

La diferencia con O*NET se debe a poblaciones y metodologías diferentes. No promedie ambos conjuntos ni presente uno como corrección exacta del otro.

## Canadá

Job Bank mapea GIS Technician directamente a **NOC 22214**.

Salarios nacionales:
- **C$23.08/hora** bajo;
- **C$38.10/hora** mediano;
- **C$53.85/hora** alto.

La preparación puede incluir college en geomatics, cartography, photogrammetry, aerial survey, remote sensing, GIS o disciplinas relacionadas. El perfil actual requiere secundaria.

En Quebec, Job Bank señala membership en el organismo regulatorio para usar el título **Professional Technologist**. Trátelo como requisito de título/estatus profesional y no como afirmación de que todo trabajo GIS en Canadá está regulado de la misma manera.

### Perspectiva de Canadá

La proyección nacional 2024–2033 para NOC 22214 indica **strong risk of labour surplus**. Las perspectivas a tres años varían y son Limited o Moderate en muchas provincias/territorios. Verifique la región específica.

## Colombia

**CUOC 31123 — Técnicos en cartografía**, nivel de competencia 3, incluye explícitamente **Técnico sistemas de información geográfica**.

Las funciones incluyen apoyo a diseño/contenido de mapas, recolección desde fotografías aéreas/registros/mapas, producción digital de mapas/gráficos, control de completitud/exactitud, interpretación aérea, equipos cartográficos digitales y remote sensing.

No fabrique un salario nacional representativo cuando los indicadores históricos disponibles no tengan metodología adecuada para ese uso.

## Colombia — rutas SENA

### Introducción a los Sistemas de Información Geográfica
- formación complementaria/curso especial;
- **80 horas**;
- modalidad presencial en ofertas actuales;
- competencia de operar SIG según necesidades del usuario.

### Sistemas de Información Geográfica
- curso especial complementario;
- **48 horas**;
- ofertas presenciales 2026;
- algunos cohorts piden conocimientos básicos.

### Aplicación de SIG en Sistemas Forestales y Agroecológicos
- formación complementaria virtual;
- **48 horas**;
- estructura/captura/gestión/evaluación/calidad de datos espaciales para proyectos forestales/agroecológicos.

Son rutas útiles pero suplementarias, no una credencial profesional universal. Verifique centro, modalidad, prerequisitos, fechas y cupos vivos.

## América Latina y Caribe

OIT/Cinterfor ayuda a localizar instituciones nacionales de formación profesional. No garantiza programa GIS, cupos, financiamiento o admisión.

## Portafolio seguro

Use datos públicos/abiertos, datos personales obtenidos legalmente o sintéticos. Ejemplos:
- mapa temático con fuente/CRS documentados;
- georreferenciación con imagen no sensible;
- QA/topología vectorial;
- SQL/Python espacial con open data;
- mapa accesible con alternativa texto/tabla;
- metadata/linaje;
- mapa sintético de inspección de activos;
- ejercicio de permisos de web map con datos no sensibles.

Nunca publique capas protegidas de empleadores/clientes, direcciones privadas, localizaciones exactas de infraestructura crítica, sitios culturales/ambientales restringidos o schemas propietarios.

## Plan inicial de cuatro semanas

### Semana 1 — fundamentos espaciales
Vector/raster/atributos, CRS, datums, proyecciones y metadata. Cargue open data y revise CRS/fuente.

### Semana 2 — edición y calidad
Digitalización, atributos, geometry/topology, joins, georreferenciación y cartografía. Documente cambios.

### Semana 3 — análisis y automatización
Buffers, overlays, spatial joins y un workflow SQL/Python reproducible. Verifique unidades, CRS y parámetros.

### Semana 4 — comunicación y portafolio
Cree mapa/reporte seguro, documente fuentes/limitaciones, agregue alternativa accesible, revise sharing y prepare ejemplos de juicio de calidad.

## Preparación para entrevistas

Prepárese para explicar vector vs raster; CRS geográfico vs proyectado; datum/reproyección; por qué una capa visible no prueba CRS correcto; errores topológicos; validación de georreferenciación; linaje/metadata; clasificación engañosa; protección de ubicaciones; validación de scripts/IA; y por qué GIS no equivale a exactitud topográfica/legal.

## Preguntas al empleador

- ¿Qué plataformas y bases GIS usan?
- ¿El rol es producción, análisis, gestión de datos, soporte o desarrollo?
- ¿Qué capas son autoritativas?
- ¿Quién aprueba cambios oficiales?
- ¿Qué CRS/datums son estándar?
- ¿Qué QA/topology rules aplican?
- ¿Se recoge field data?
- ¿Cómo se protegen ubicaciones sensibles?
- ¿Hay capas web públicas?
- ¿Se espera SQL/scripting?
- ¿Qué training ofrecen?
- ¿Qué responsabilidades survey/legal quedan fuera del cargo?

## Enlaces de verificación para lectores

1. https://www.onetonline.org/link/details/15-1299.02
2. https://www.onetonline.org/link/summary/15-1299.02
3. https://www.onetonline.org/link/localwages/15-1299.02
4. https://www.onetonline.org/link/localtrends/15-1299.02
5. https://www.onetonline.org/link/demand/15-1299.02
6. https://www.indeed.com/career/gis-technician/salaries
7. https://www.careeronestop.org/LocalHelp/EmploymentAndTraining/find-WIOA-training-programs.aspx
8. https://www.jobbank.gc.ca/marketreport/summary-occupation/3493/ca
9. https://www.jobbank.gc.ca/marketreport/wages-occupation/3493/ca
10. https://www.jobbank.gc.ca/marketreport/requirements/3493/AB
11. https://www.jobbank.gc.ca/marketreport/outlook-occupation/3493/ca
12. https://www.canada.ca/en/services/jobs/training.html
13. https://ocupacol.mintrabajo.gov.co/Profile/OccupationalProfile/31123
14. https://betowa.sena.edu.co/oferta/introduccion-a-los-sistemas-de-informacion-geografica?modality=P&offertype=company&programId=85021
15. https://betowa.sena.edu.co/oferta/sistemas-de-informacion-geografica?modality=P&offertype=company&programId=164857
16. https://betowa.sena.edu.co/oferta/aplicacion-de-sig-en-sistemas-forestales-y-agroecologicos?modality=V&programId=173415
17. https://www.oitcinterfor.org/statsfp/paises
18. https://www.nist.gov/privacy-framework
19. https://www.nist.gov/itl/ai-risk-management-framework
20. https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
21. https://www.cisa.gov/secure-our-world
22. https://www.section508.gov/create/
23. https://www.w3.org/TR/WCAG22/

## Límites importantes

Esta guía ofrece información educativa y de planificación profesional. No garantiza empleo, compensación, admisión, financiamiento, disponibilidad de formación, estatus profesional o promoción. No constituye certificación legal, topográfica, catastral, de privacidad, ciberseguridad, exactitud geoespacial o accesibilidad. Los datos salariales/de empleo de O*NET están cruzados desde **Computer Occupations, All Other** y no se representan como una población pura de GIS Technician. Las ediciones lingüísticas son localizaciones controladas, no traducciones certificadas.
