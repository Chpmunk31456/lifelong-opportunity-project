# Guía de Oportunidades para Toda la Vida 84 — Analista de inteligencia de negocios

**Versión:** 2.0 — maestro de trabajo controlado  
**Idioma:** español neutro de América Latina (`es-419`)  
**Referencia principal de EE. UU.:** O*NET-SOC 15-2051.01 — Business Intelligence Analysts  
**Comparación con Canadá:** NOC 21221 — Business systems specialists  
**Comparación con Colombia:** CUOC 25110 — Analistas de sistemas  
**Fecha de revisión:** 2026-08-21

## Qué es esta carrera

Un analista de inteligencia de negocios (BI) convierte preguntas del negocio en métricas, informes, tableros e información confiable para apoyar decisiones. El trabajo normalmente exige comprender qué decisión intenta tomar una persona o equipo, encontrar los datos pertinentes, validar definiciones, consultar y transformar información, crear resultados comprensibles, comprobar que los resultados concilien con fuentes autorizadas y explicar qué muestran —y qué no muestran— los datos.

Esta guía utiliza **O*NET-SOC 15-2051.01 — Business Intelligence Analysts** como referencia principal de Estados Unidos. Canada Job Bank asigna el título orientado a TI **Business Intelligence Analyst - Information Technology (IT)** a **NOC 21221 — Business systems specialists**. Colombia tiene una correspondencia directa dentro de **CUOC 25110 — Analistas de sistemas**, cuyas denominaciones oficiales incluyen **Analista de inteligencia de negocios**, **Analista de inteligencia de negocio TI**, **Analista de Power BI** y **Analista de analytics**.

El trabajo de BI está entre operaciones de negocio, datos, tecnología y comunicación. Un buen analista no es simplemente alguien que construye tableros. Debe entender de dónde provino cada cifra, qué reglas la produjeron, si los datos están completos y actualizados y cómo una persona razonable podría interpretar mal el resultado.

## Por qué puede ser una buena oportunidad

Las organizaciones recopilan cada vez más datos de finanzas, ventas, marketing, operaciones, cadena de suministro, servicio al cliente, RR. HH., tecnología y riesgo. Necesitan personas capaces de convertir esos datos en información confiable, no solamente en más gráficos.

BI puede ser una ruta desde:

- operaciones empresariales;
- apoyo financiero o contable;
- reporting;
- ingreso de datos o gestión de registros;
- operaciones de clientes;
- soporte de TI;
- desarrollo de bases de datos/reportes;
- calidad y mejora de procesos;
- analítica o investigación.

Una progresión práctica puede ser:

**soporte de reporting/datos → analista BI → analista BI senior / analytics engineer / desarrollador BI → líder de analítica, data product, ingeniería de datos, ciencia de datos, sistemas empresariales o gestión.**

La ruta depende de la profundidad técnica, conocimiento del negocio, educación, expectativas del empleador y capacidad para entregar información confiable para decisiones.

## Analista BI, analista de datos, desarrollador BI, analytics engineer y científico de datos no son lo mismo

### Analista de inteligencia de negocios

Suele enfocarse en:

- requerimientos del negocio;
- definiciones de KPI y métricas;
- SQL/consultas;
- reportes recurrentes;
- tableros y visualización;
- análisis de tendencias;
- comunicación con stakeholders;
- validación y conciliación de datos;
- apoyo a decisiones.

### Analista de datos

Puede solaparse mucho con BI, pero según el empleador puede incluir más análisis ad hoc, experimentación, estadística, análisis operativo o investigación.

### Desarrollador BI

Suele profundizar en:

- modelos semánticos;
- arquitectura de reportes;
- DAX/capas de cálculo;
- integración ETL/ELT;
- despliegue y rendimiento;
- administración de plataformas BI.

### Analytics engineer

Suele enfocarse en transformar datos crudos de un warehouse en modelos analíticos documentados, probados y reutilizables para analistas y herramientas de reporting.

### Científico de datos

Puede usar estadística avanzada, machine learning, experimentación y modelos predictivos. Los datos oficiales de salarios y empleo que O*NET muestra para Business Intelligence Analysts se recopilan de **Data Scientists**, pero esa correspondencia estadística no convierte ambas ocupaciones en la misma función.

## Regla principal: primero defina la pregunta de negocio

Un tablero no debe comenzar con “¿qué gráfico puedo hacer?”.

Comience con:

1. ¿Qué decisión o acción se quiere apoyar?
2. ¿Qué pregunta del negocio debe responderse?
3. ¿Qué métrica o evidencia respondería esa pregunta?
4. ¿Qué población, período y granularidad son pertinentes?
5. ¿Cuál es la fuente autorizada?
6. ¿Qué exclusiones o reglas de negocio aplican?
7. ¿Qué tan recientes deben ser los datos?
8. ¿Quién está autorizado para ver el resultado?
9. ¿Cómo se validará la cifra?
10. ¿Qué limitaciones deben revelarse?

Un buen BI reduce la ambigüedad antes de producir visualizaciones.

## Fuente de verdad y linaje de datos

Toda métrica importante debe poder rastrearse.

Documente:

- sistema fuente;
- tabla/archivo/API fuente;
- responsable del negocio;
- fecha/hora de extracción o frecuencia de actualización;
- transformaciones;
- joins y claves;
- filtros/exclusiones;
- reglas de cálculo;
- reporte/tablero de salida;
- versión o historial de cambios cuando corresponda.

Una cifra sin linaje es difícil de defender cuando finanzas, operaciones, auditoría o liderazgo preguntan por qué cambió.

No sustituya silenciosamente una fuente autorizada por una hoja de cálculo conveniente porque el resultado “se ve mejor”.

## Fundamentos de datos relacionales

Un analista BI debe entender:

- tablas y filas;
- columnas/campos;
- claves primarias;
- claves foráneas;
- relaciones uno a uno, uno a muchos y muchos a muchos;
- normalización;
- duplicados;
- nulos/faltantes;
- tipos de datos;
- fechas/horas;
- granularidad o nivel de detalle.

Un error común es unir tablas de granularidad incompatible y multiplicar registros sin darse cuenta.

Antes de hacer un join, pregunte:

- ¿Qué representa una fila en cada tabla?
- ¿La clave es única?
- ¿Qué pasa con registros sin coincidencia?
- ¿La unión puede duplicar medidas?

## SQL

SQL es la señal tecnológica más fuerte en las publicaciones asociadas a la ocupación de O*NET: **35%** de las ofertas de EE. UU. vinculadas en 2025.

Conceptos útiles:

- `SELECT`;
- filtros;
- ordenamiento;
- agregación;
- `GROUP BY`;
- joins;
- lógica `CASE`;
- CTE;
- subconsultas;
- funciones de ventana;
- lógica de fechas;
- manejo de nulos;
- deduplicación;
- validación de consultas.

El objetivo no es solamente lograr que una consulta ejecute. El objetivo es devolver la población y medida correctas.

Valide consultas importantes con:

- conteos de filas;
- claves duplicadas;
- registros conocidos;
- totales contra una fuente autorizada;
- límites de fechas esperados;
- valores faltantes;
- categorías inesperadas;
- efecto de cada join y filtro.

## Limpieza y transformación

El trabajo común incluye:

- estandarizar categorías;
- convertir fechas;
- manejar faltantes;
- usar tablas de mapeo aprobadas;
- reestructurar datos;
- unir datos de referencia;
- derivar campos;
- eliminar duplicados verdaderos;
- validar rangos;
- documentar la lógica.

No “limpie” datos eliminando observaciones legítimas y poco comunes solo porque hacen incómodo un gráfico.

Si un registro fuente está incorrecto, siga el proceso autorizado de corrección. No reescriba silenciosamente datos productivos desde la capa de reporting.

## Reproducibilidad

Un resultado analítico confiable debe poder reproducirse.

Prefiera:

- SQL guardado o consultas gobernadas;
- transformaciones documentadas;
- scripts con control de versiones cuando corresponda;
- fuentes nombradas;
- timestamps de actualización;
- parámetros controlados;
- cálculos reutilizables;
- casos de prueba;
- historial de cambios.

Evite reportes críticos que dependan de ediciones manuales de Excel que solo una persona conoce.

## Modelado dimensional y esquema estrella

Los sistemas BI suelen organizar datos en:

- **tablas de hechos:** eventos medibles como ventas, órdenes, llamadas o transacciones;
- **tablas de dimensiones:** contexto descriptivo como cliente, producto, lugar o fecha.

Conceptos útiles:

- granularidad;
- claves sustitutas;
- dimensión fecha;
- dimensiones lentamente cambiantes;
- dimensiones conformadas;
- medidas aditivas y no aditivas;
- esquema estrella frente a diseño operacional muy normalizado.

No es necesario ser arquitecto de datos para comprender por qué un modelo semántico limpio hace más confiables los tableros.

## Modelos semánticos y capas de cálculo

Un modelo semántico da significado de negocio a los datos subyacentes.

Puede definir:

- relaciones;
- medidas;
- jerarquías;
- columnas calculadas;
- etiquetas de negocio;
- roles de seguridad;
- inteligencia de tiempo;
- lógica reutilizable de KPI.

Centralizar una definición reduce el riesgo de que cinco tableros calculen “cliente activo” de cinco maneras diferentes.

## Gobierno de KPI y métricas

Un KPI no es solamente una fórmula.

Para métricas importantes, defina:

- nombre;
- propósito;
- fórmula;
- numerador/denominador;
- población;
- exclusiones;
- base temporal;
- fuente;
- frecuencia de actualización;
- responsable;
- meta/umbral, si aplica;
- limitaciones conocidas.

No cambie una definición porque a alguien no le guste el resultado. Si cambia la definición empresarial, documente quién lo aprobó, fecha de vigencia e impacto en la comparabilidad histórica.

## Filtros y lógica de fechas

Los filtros pueden cambiar materialmente una conclusión.

Sea explícito sobre:

- rango de fechas;
- período fiscal versus calendario;
- zona horaria;
- estado activo/inactivo;
- geografía;
- producto/unidad de negocio;
- registros de prueba/internos;
- cancelaciones/devoluciones;
- datos tardíos;
- lógica snapshot versus transacción.

Un tablero no debe ocultar un filtro que cambie la historia aparente.

## Calidad de datos

Dimensiones comunes:

- completitud;
- exactitud;
- consistencia;
- validez;
- oportunidad;
- unicidad;
- integridad;
- trazabilidad.

Un campo lleno no necesariamente es correcto.

Rutina útil:

1. compare conteos con rangos esperados;
2. revise claves duplicadas;
3. revise tasas de nulos;
4. valide categorías;
5. concilie totales con la fuente autorizada;
6. pruebe fechas límite;
7. muestree registros individuales;
8. compare timestamps de actualización;
9. documente excepciones;
10. detenga la publicación si queda una discrepancia material sin resolver.

## Conciliación

Antes de publicar un tablero crítico para decisiones, concílielo.

Ejemplos:

- ingresos BI contra fuente aprobada por finanzas;
- conteos de órdenes contra sistema operacional;
- headcount contra fuente designada por RR. HH.;
- clientes contra maestro gobernado;
- inventario contra registro autorizado.

Diferencias pequeñas pueden tener causas válidas. La tarea es explicarlas, no ocultarlas.

## Estadística descriptiva e interpretación de tendencias

Conceptos útiles:

- media;
- mediana;
- percentiles;
- tasas/ratios;
- distribución;
- varianza;
- desviación estándar;
- crecimiento;
- promedio móvil;
- estacionalidad;
- cohortes;
- efecto del denominador.

Evite sobreafirmar. Que dos variables se muevan juntas no prueba causalidad.

## Tableros y visualización

Un tablero útil responde preguntas con rapidez.

Buenas prácticas:

- título y propósito claros;
- período visible;
- unidades claras;
- escalas coherentes;
- variedad limitada de gráficos;
- etiquetas legibles;
- ordenamiento útil;
- filtros claros;
- definiciones para métricas ambiguas;
- acceso al detalle cuando corresponda.

### Selección de gráficos

- barras: comparar categorías;
- línea: tendencia temporal;
- dispersión: relación entre variables numéricas;
- tabla: detalle exacto;
- tarjeta KPI: una medida principal bien definida;
- histograma: distribución;
- mapa: solo cuando la geografía realmente importa y la interpretación geográfica es válida.

Evite gráficos decorativos que dificulten comparar.

## Evitar visualizaciones engañosas

No:

- recorte ejes para exagerar diferencias sin explicarlo;
- use escalas inconsistentes para crear una impresión deseada;
- compare períodos incompatibles sin explicación;
- oculte datos faltantes;
- use efectos de área/volumen que distorsionen magnitudes;
- use color como único medio para significado crítico;
- muestre precisión excesiva no soportada por la fuente;
- presente valores acumulados y de período como si fueran iguales.

La visualización forma parte de la integridad analítica.

## Power BI, Tableau y habilidades transferibles

Las señales actuales incluyen **Power BI 20%** y **Tableau 19%**.

Conceptos transferibles:

- conexión a fuentes;
- relaciones/modelado;
- medidas/cálculos;
- filtros/contexto;
- drill-down/drill-through;
- seguridad a nivel de fila;
- actualización;
- rendimiento;
- workspaces/despliegue;
- diseño visual;
- compartir de forma gobernada.

Comprender estos conceptos facilita aprender otras plataformas.

## Señales tecnológicas actuales en EE. UU.

O*NET/Lightcast para publicaciones de 2025 muestra:

- SQL **35%**;
- Microsoft Power BI **20%**;
- Python **20%**;
- Tableau **19%**;
- SAP **19%**;
- Microsoft Excel **17%**;
- R **10%**;
- AWS **9%**;
- Microsoft PowerPoint **8%**;
- Microsoft Office **8%**;
- Microsoft Azure **8%**;
- Snowflake **5%**;
- SAS **5%**;
- Salesforce **5%**.

Son señales de mercado, no requisitos universales.

## Excel y hojas de cálculo

Excel aparece en **17%** de publicaciones vinculadas actuales.

Capacidades útiles:

- tablas estructuradas;
- fórmulas;
- búsquedas;
- tablas dinámicas;
- validación;
- gráficos;
- conceptos de Power Query;
- conciliación;
- importaciones/exportaciones controladas.

Las hojas se vuelven riesgosas cuando funcionan como bases de datos no documentadas o contienen lógica crítica manual oculta.

## Python y R

Las señales incluyen **Python 20%** y **R 10%**.

Pueden ayudar con:

- limpieza;
- análisis repetible;
- APIs/archivos;
- estadística;
- automatización;
- validación;
- visualización.

No todos los empleos BI requieren programación avanzada. Aprenda según el rol objetivo.

## Nube y plataformas modernas de datos

Señales actuales incluyen AWS **9%**, Azure **8%** y Snowflake **5%**.

Conceptos útiles:

- almacenamiento/warehouse en nube;
- identidad y acceso;
- separación de cómputo/consulta;
- pipelines programados;
- actualización;
- conciencia de costos;
- compartir gobernado;
- logs/monitoreo;
- gestión de secretos.

Un analista debe entender suficiente arquitectura para usar datos con seguridad sin atribuirse autoridad de arquitecto de nube o seguridad.

## Requerimientos y comunicación con stakeholders

BI falla con frecuencia porque el resultado técnico responde otra pregunta.

Aclare:

- decisión deseada;
- audiencia;
- definiciones;
- frecuencia;
- tolerancia a latencia;
- nivel de detalle;
- alcance de seguridad;
- necesidad de exportación;
- criterios de éxito;
- pruebas de aceptación.

Use ejemplos y mockups si hay ambigüedad.

## Storytelling analítico sin distorsión

Separe:

- hechos observados;
- métricas calculadas;
- supuestos;
- interpretación;
- recomendación.

Frases útiles:

- “Los datos muestran...”
- “Este cálculo supone...”
- “Una posible explicación es...”
- “Los datos no establecen causalidad...”
- “Este resultado excluye...”

La claridad genera confianza.

## Privacidad y datos confidenciales

BI puede exponer información sensible incluso cuando un tablero parece inofensivo.

Siga reglas aprobadas para:

- datos de clientes;
- empleados;
- finanzas;
- salud u otros datos regulados;
- datos comerciales sensibles;
- contratos/precios confidenciales;
- identificadores;
- acceso a nivel de fila.

Buenas prácticas:

- mínimo privilegio;
- fuentes aprobadas;
- exportaciones controladas;
- almacenamiento seguro;
- compartir aprobado;
- enmascaramiento/agregación cuando se requiera;
- retención/eliminación;
- reporte de incidentes.

Poder consultar una tabla no demuestra autorización para usar cada campo.

## Ciberseguridad en BI

Controles prácticos:

- proteger credenciales/tokens;
- usar MFA cuando se requiera;
- no incrustar secretos en reportes compartidos o repositorios públicos;
- limitar cuentas de servicio;
- usar conectores aprobados;
- reportar accesos o exposiciones inesperadas;
- validar solicitudes inusuales de exportación masiva;
- no eludir seguridad a nivel de fila;
- no copiar datos productivos a herramientas personales no administradas.

NIST Cybersecurity Framework y Privacy Framework aportan contexto de gobernanza. Las políticas y leyes aplicables siguen siendo determinantes.

## IA y automatización responsables

La IA puede ayudar con:

- redactar SQL;
- explicar lógica;
- sugerir DAX/fórmulas;
- crear casos de prueba;
- resumir hallazgos no sensibles;
- redactar documentación;
- generar ejemplos sintéticos.

Controles:

- use solo sistemas y clases de datos aprobados;
- no coloque datos confidenciales, credenciales o extractos protegidos en IA pública no aprobada;
- valide SQL generado antes de ejecutarlo;
- valide cálculos y fórmulas;
- concilie contra fuentes autorizadas;
- distinga narrativa generada de evidencia observada;
- revise afirmaciones causales no soportadas;
- revise error sistemático y sesgo;
- exija aprobación humana antes de publicar resultados críticos cuando corresponda.

El AI Risk Management Framework de NIST y su Generative AI Profile son guías voluntarias; no sustituyen el gobierno de datos organizacional.

## Accesibilidad e inclusión

Buenas prácticas:

- contraste legible;
- tamaño de texto adecuado;
- títulos significativos;
- etiquetas descriptivas;
- acceso por teclado cuando la plataforma lo soporte;
- navegación/orden lógico;
- no depender solamente de color;
- alternativas de tabla/texto para información crítica cuando sea práctico;
- alt text significativo en gráficos exportados cuando aplique;
- lenguaje conciso y unidades comprensibles.

Las verificaciones automáticas no demuestran cumplimiento legal completo. WCAG 2.2 y recursos de Section 508 pueden aportar contexto de diseño/prueba.

## Portafolio ético

Use datos públicos, sintéticos o autorizados.

Ideas:

- tablero de ventas con transacciones sintéticas;
- tablero de servicio con tickets inventados;
- modelo KPI de inventario;
- conciliación financiera con cuentas sintéticas;
- análisis SQL con pruebas documentadas;
- esquema estrella;
- tablero Power BI/Tableau con checklist de accesibilidad;
- caso que muestre cómo un join incorrecto duplicó ingresos;
- reporte de calidad con nulos/duplicados;
- diccionario de métricas y linaje.

No publique datos de empleadores/clientes ni capturas confidenciales sin autorización.

## Ruta en Estados Unidos

O*NET ubica BI en **Job Zone Four — Considerable Preparation Needed**.

Respuestas actuales sobre educación de nuevas contrataciones:

- **68% licenciatura/bachelor's**;
- **23% maestría**;
- **5% associate degree**.

Son patrones, no requisitos legales universales.

O*NET lista **Business Intelligence Engineer** como título aprobado de Registered Apprenticeship. No garantiza una vacante local.

CareerOneStop puede ayudar a localizar formación WIOA y otras opciones. Elegibilidad y financiación deben confirmarse.

## Salarios y perspectiva en Estados Unidos — divulgación obligatoria de correspondencia

O*NET declara expresamente que los datos salariales y de empleo para **Business Intelligence Analysts** se recopilan de **Data Scientists**.

Por eso, las siguientes cifras son referencias oficiales BLS/O*NET de la serie asignada, **no una muestra exclusiva de personas con título BI Analyst**.

### Serie salarial BLS 2025 utilizada por O*NET

| Percentil | Anual | Por hora |
|---|---:|---:|
| 10 | $67,240 | $32.33 |
| 25 | $85,660 | $41.18 |
| Mediana | $120,230 | $57.80 |
| 75 | $158,880 | $76.39 |
| 90 | $199,130 | $95.74 |

### Proyecciones 2024–2034 utilizadas por O*NET

- empleo 2024: **245,900**;
- empleo proyectado 2034: **328,300**;
- crecimiento proyectado: **34%**, mucho más rápido que el promedio;
- **23,400 vacantes proyectadas por año**.

No convierta las vacantes anuales en un total garantizado ni asuma que cada vacante lleva el título Business Intelligence Analyst.

### Contexto actual específico del título BI, no gubernamental

Indeed informó un salario base promedio de **$94,707/año** para **Business Intelligence Analyst** en Estados Unidos, con rango mostrado de **$61,569–$145,682/año**, basado en aproximadamente **1.6k salarios** de publicaciones de los **36 meses** anteriores, actualizado el **3 de agosto de 2026**.

Es una estimación actual no gubernamental y más específica del título BI. No es sustituto de estadísticas oficiales ni debe mezclarse con la serie de Data Scientists como si midieran la misma población.

## Ruta en Canadá

Canada Job Bank asigna el título de TI **Business Intelligence Analyst - Information Technology (IT)** a **NOC 21221 — Business systems specialists**.

Requisitos típicos actuales:

- bachelor's en computer science, business administration, information systems o disciplina relacionada **o** programa de college en computer science generalmente requerido;
- algunos empleadores pueden exigir certificación/formación de proveedor;
- según Job Bank, la ocupación **no está regulada en Canadá**.

Salarios nacionales actuales, actualizados el 19 de noviembre de 2025:

- bajo: **C$30.67/hora**;
- mediana: **C$45.13/hora**;
- alto: **C$62.50/hora**.

NOC 21221 es más amplio que BI exclusivamente; se trata de una comparación ocupacional. Las perspectivas cambian por provincia/territorio.

## Ruta en Colombia

### CUOC 25110 — Analistas de sistemas

OCUPACOL incluye explícitamente:

- Analista de analytics;
- Analista de inteligencia de negocio TI;
- **Analista de inteligencia de negocios**;
- Analista de Power BI;
- Analista de información comercial;
- Analista de procesamiento de información;
- Analista informático para análisis de negocio;
- Especialista en inteligencia comercial.

Las funciones oficiales incluyen análisis de requerimientos/procesos, especificaciones funcionales, pruebas, integración de datos con técnicas de visualización/análisis, sistematización de datos masivos y gestión de representaciones de datos.

OCUPACOL muestra un rango histórico/derivado de **COP 800,000–7,113,801**, pero declara que los datos **no cuentan con representatividad estadística**. Esta guía no lo usa como salario nacional actual representativo para BI en Colombia.

### SENA — Programación para analítica de datos

SENA Betowa muestra:

- **Técnico**;
- **2,208 horas**;
- formación titulada;
- procesamiento de datos, metodología estadística e integración/visualización de datos.

La página puede no tener cohortes abiertas en un momento dado. Verifique la oferta actual.

### SENA — Visualización de datos usando Power BI

SENA Betowa muestra:

- formación complementaria/curso especial;
- **48 horas**;
- ofertas 2026 en algunas modalidades/sedes;
- conocimiento básico de ofimática y fundamentos de bases/estadística recomendados.

Es un curso de habilidad puntual, no una cualificación profesional completa de BI.

### SENA — Analítica de datos para procesos logísticos

SENA Betowa muestra:

- complementaria virtual;
- **48 horas**;
- almacenamiento/tratamiento, consultas, homogenización y presentación analítica.

Es un complemento específico de dominio, no una credencial universal de BI.

## Ruta más amplia en América Latina

Los sistemas de formación varían. OIT/Cinterfor puede ayudar a localizar instituciones nacionales. Verifique directamente programa, costo, modalidad, admisión y reconocimiento.

## Evidencia para el currículum

Bullets fuertes muestran impacto y evidencia, por ejemplo:

- concilió métricas ejecutivas con la fuente gobernada de finanzas;
- redujo reporting manual automatizando un pipeline validado;
- definió KPI con responsables y documentó linaje;
- identificó un error de join que sobrestimaba transacciones;
- creó tableros con acceso restringido por roles;
- mejoró monitoreo de calidad de nulos y duplicados.

Use solo hechos demostrables. No invente impacto financiero, usuarios, certificaciones o experiencia con herramientas.

## Preparación para entrevistas

Prepárese para explicar:

- cómo convierte una solicitud vaga en una métrica;
- cómo valida SQL;
- riesgo de joins muchos-a-muchos;
- diferencia entre hecho y dimensión;
- cómo concilia un tablero;
- cómo maneja definiciones de KPI conflictivas;
- cómo elige un gráfico;
- cómo evita interpretación engañosa;
- cómo protege datos sensibles;
- cómo valida SQL/narrativa de IA;
- qué hace si el resultado contradice expectativas.

Un buen analista explica método y limitaciones, no solo herramientas.

## Preguntas para un empleador

Pregunte sobre:

- plataformas de datos autorizadas;
- herramientas BI;
- arquitectura warehouse/lakehouse;
- propiedad/gobierno de métricas;
- calidad de datos;
- revisión/despliegue;
- acceso/seguridad;
- división analista-ingeniería;
- profundidad esperada de SQL;
- estadística/experimentación;
- política de IA;
- documentación/control de versiones;
- apoyo a formación;
- estándares de accesibilidad.

## Primeros 30 días

Prioridades:

1. aprender el modelo de negocio y decisiones clave;
2. identificar fuentes autorizadas y responsables;
3. aprender definiciones de métricas;
4. comprender frecuencia/latencia;
5. aprender reglas de acceso/seguridad;
6. revisar tableros recurrentes y problemas conocidos;
7. conocer revisión/despliegue;
8. comprender expectativas de stakeholders;
9. documentar linaje y supuestos;
10. no cambiar lógica KPI productiva sin aprobación.

## Plan de progreso de 90 días

Busque poder:

- aclarar requerimientos comunes;
- escribir/validar SQL confiable;
- explicar linaje;
- mantener métricas gobernadas;
- conciliar tableros;
- detectar problemas de calidad;
- comunicar limitaciones;
- crear visuales accesibles y orientados a decisiones;
- manejar datos sensibles correctamente;
- usar IA/automatización bajo controles;
- elegir la siguiente ruta: BI senior, analytics engineering, data engineering, data science, sistemas o liderazgo.

## Lista antes de postularse

Confirme que puede hablar de:

- pregunta de negocio/KPI;
- joins/agregación SQL;
- granularidad/duplicación;
- limpieza/transformación;
- esquema estrella;
- conciliación;
- diseño de tableros;
- estadística descriptiva;
- riesgos de visualización engañosa;
- privacidad/acceso;
- IA responsable;
- un proyecto de portafolio con fuente/validación documentada.

## Preguntas antes de comprar formación

- ¿Enseña SQL con práctica?
- ¿Cubre modelado, no solo clics de dashboard?
- ¿Incluye calidad y conciliación?
- ¿Qué plataformas usa?
- ¿Hay portafolio con datos públicos/sintéticos?
- ¿Los instructores/resultados son verificables?
- ¿Cuál es el costo total, incluidos exámenes/software?
- ¿Hay financiación y cuáles son las reglas?
- ¿Qué adaptaciones de accesibilidad ofrece?
- ¿La credencial coincide con empleadores objetivo?

No dependa de promesas de trabajo o ingresos garantizados.

## Fuentes controladas

1. https://www.onetonline.org/link/details/15-2051.01
2. https://www.onetonline.org/link/summary/15-2051.01
3. https://www.onetonline.org/link/localwages/15-2051.01
4. https://www.onetonline.org/link/localtrends/15-2051.01
5. https://www.onetonline.org/link/hot_tech/15-2051.01
6. https://www.onetonline.org/link/demand/15-2051.01
7. https://www.careeronestop.org/LocalHelp/EmploymentAndTraining/find-WIOA-training-programs.aspx
8. https://www.careeronestop.org/FindTraining/find-training.aspx
9. https://www.indeed.com/career/business-intelligence-analyst/salaries
10. https://www.jobbank.gc.ca/marketreport/summary-occupation/296881/ca
11. https://www.jobbank.gc.ca/marketreport/requirements/296881/ca
12. https://www.jobbank.gc.ca/marketreport/wages-occupation/296881/ca
13. https://www.canada.ca/en/services/jobs/training.html
14. https://ocupacol.mintrabajo.gov.co/Profile/OccupationalProfile/25110
15. https://betowa.sena.edu.co/oferta/programacion-para-analitica-de-datos?location=57054001&modality=P&programId=133094
16. https://betowa.sena.edu.co/oferta/visualizacion-de-datos-usando-power-bi?modality=V&offertype=company&programId=160058
17. https://betowa.sena.edu.co/oferta/analitica-de-datos-para-procesos-logisticos?modality=V&offertype=company
18. https://www.oitcinterfor.org/statsfp/paises
19. https://www.cisa.gov/secure-our-world
20. https://www.nist.gov/cyberframework
21. https://www.nist.gov/privacy-framework
22. https://www.nist.gov/itl/ai-risk-management-framework
23. https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
24. https://www.section508.gov/create/
25. https://www.w3.org/TR/WCAG22/

## Aviso de alcance y no garantía

Esta guía ofrece información educativa y de planificación profesional. No garantiza empleo, ingresos, admisión, financiación, certificación, licencia, promoción ni otro resultado. Requisitos, compensación y oportunidades cambian según jurisdicción, empleador y tiempo.

No proporciona certificación legal, contable, de privacidad, ciberseguridad, regulación o accesibilidad. Siga la ley aplicable, políticas del empleador, gobierno aprobado de datos/métricas y autoridad asignada.

Creada y dirigida por **Alberto “Al” Leiva**. ChatGPT apoyó investigación, organización, edición, apoyo de traducción y preparación de documentos bajo la dirección del autor. El autor mantiene la responsabilidad por las decisiones editoriales y de publicación.

Salvo que un archivo indique lo contrario, estos materiales están bajo licencia **CC BY-NC-SA 4.0**.
