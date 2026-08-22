# Guía de Oportunidades para Toda la Vida 86 — Administrador de Bases de Datos

**Versión:** 2.0 — maestro de trabajo controlado  
**Idioma:** Español latinoamericano neutral (`es-419`)  
**Referencia principal de EE. UU.:** O*NET-SOC 15-1242.00 — Database Administrators  
**Comparación de Canadá:** NOC 21223 — Database analysts and data administrators  
**Comparación de Colombia:** CUOC 25210 — Diseñadores y administradores de bases de datos  
**Fecha de revisión:** 2026-08-22  
**Fuente inglesa congelada:** blob `ce3f8215c91230c15e1efdd702e6f73571c7ae18`

## Qué es esta carrera

Un Administrador de Bases de Datos (DBA) ayuda a mantener las bases de datos de una organización disponibles, correctas, seguras, recuperables y sostenibles. El trabajo puede incluir instalar o configurar sistemas gestores de bases de datos, crear y mantener bases de datos, controlar accesos, probar cambios, monitorear rendimiento y capacidad, aplicar actualizaciones aprobadas, apoyar respaldos y recuperación, resolver incidentes, documentar configuraciones y ayudar a otros equipos a usar los sistemas de datos de manera segura.

Esta guía usa **O*NET-SOC 15-1242.00 — Database Administrators** como referencia principal de Estados Unidos. Canadá se compara con **NOC 21223 — Database analysts and data administrators**. Colombia tiene una correspondencia directa en **CUOC 25210 — Diseñadores y administradores de bases de datos**, que incluye expresamente la denominación *Administrador de base de datos*.

Un DBA puede tener acceso técnico muy poderoso. Eso **no** significa que tenga autorización irrestricta para leer, copiar, modificar, exportar o borrar cualquier información. Los cambios de producción, el acceso privilegiado, los respaldos, los controles de seguridad y las acciones de recuperación deben permanecer dentro de la autorización del empleador, la gestión de cambios y las obligaciones aplicables de privacidad y seguridad.

## Por qué esta carrera sigue siendo importante

Las organizaciones dependen de bases de datos para transacciones, clientes, finanzas, operaciones, logística, salud, servicios públicos, analítica, identidad, aplicaciones y sistemas internos. Las plataformas en la nube y los servicios administrados automatizan algunas tareas de infraestructura, pero no eliminan la necesidad de personas capaces de:

- comprender estructuras y dependencias de datos;
- controlar accesos;
- detectar problemas de rendimiento o capacidad;
- proteger integridad y disponibilidad;
- comprobar respaldos y capacidad real de recuperación;
- planear y validar cambios;
- investigar incidentes;
- documentar sistemas;
- coordinar con equipos de aplicaciones, nube, seguridad y negocio.

La ocupación está evolucionando, no simplemente desapareciendo. Las proyecciones actuales de EE. UU. muestran una ligera disminución del empleo total de DBA, pero el reemplazo y la rotación siguen generando miles de vacantes al año. Por eso conviene desarrollar habilidades transferibles entre bases tradicionales, servicios administrados en nube, automatización, plataformas de datos y operaciones con enfoque de seguridad.

## Qué hace realmente un Administrador de Bases de Datos

Las tareas actuales de O*NET incluyen:

- modificar bases de datos o plataformas DBMS existentes, o dirigir cambios aprobados;
- planear e implementar medidas de seguridad para bases de datos;
- instalar actualizaciones aprobadas de DBMS;
- especificar usuarios y niveles de acceso;
- probar cambios de bases de datos y aplicaciones;
- corregir errores y realizar modificaciones necesarias;
- capacitar usuarios y apoyar personal técnico junior o clientes;
- planear y supervisar instalación y pruebas de nuevos sistemas de bases de datos cuando corresponda;
- evaluar rendimiento;
- desarrollar parámetros, especificaciones y modelos de datos.

Un puesto puede enfatizar solo una parte de estas funciones. Algunos DBA se concentran en Oracle o SQL Server; otros trabajan con PostgreSQL, MySQL, bases administradas en nube, warehouses, NoSQL, alta disponibilidad, automatización o soporte de aplicaciones.

## Un DBA no es lo mismo que todos los roles de datos cercanos

### Administrador de Bases de Datos

Suele enfatizar:

- bases operativas;
- seguridad y acceso;
- respaldo y recuperación;
- parches y actualizaciones;
- rendimiento;
- capacidad;
- disponibilidad;
- incidentes;
- cambios controlados.

### Desarrollador de bases de datos

Puede enfocarse más en:

- objetos del esquema;
- procedimientos almacenados;
- funciones;
- desarrollo de consultas;
- lógica de base de datos para aplicaciones.

### Arquitecto de bases de datos

Suele trabajar en un nivel de diseño más amplio:

- selección de plataformas;
- arquitectura de datos;
- patrones de integración;
- resiliencia;
- estándares;
- diseño de largo plazo.

### Ingeniero de datos

A menudo se enfoca más en:

- pipelines;
- movimiento y transformación de datos;
- warehouses/lakes;
- orquestación;
- plataformas de analítica.

### Analista de Datos / Analista de BI

Normalmente se concentra más en consultas, análisis, métricas, visualización e interpretación de negocio que en administración operacional de bases de datos.

Los empleadores pueden combinar responsabilidades. Lea la descripción real del puesto, no solo el título.

## Primera regla operativa: conozca su autoridad antes de actuar

Antes de un cambio de producción, confirme:

1. ¿Qué sistema y ambiente están en alcance?
2. ¿La acción está autorizada?
3. ¿Se requiere ticket, aprobación o ventana de mantenimiento?
4. ¿Cuál es el impacto de negocio si falla?
5. ¿Se requiere respaldo, snapshot, punto de restauración o ruta de reversión?
6. ¿El script o cambio fue probado en un ambiente no productivo apropiado?
7. ¿Quién debe ser notificado?
8. ¿Qué validación demuestra éxito?
9. ¿Qué condición obliga a detenerse y escalar?
10. ¿Qué evidencia debe conservarse para auditoría o revisión de incidentes?

La capacidad técnica no equivale a autoridad organizacional.

## Fundamentos de bases de datos

Un DBA sólido debe comprender:

- bases relacionales;
- tablas, filas y columnas;
- claves primarias y foráneas;
- restricciones;
- índices;
- vistas;
- esquemas;
- transacciones;
- aislamiento y concurrencia;
- normalización y desnormalización;
- tipos de datos;
- procedimientos/funciones cuando se utilicen;
- archivos y estructuras de almacenamiento;
- logs o journals;
- replicación;
- tipos de respaldo;
- recuperación;
- patrones de alta disponibilidad.

La implementación cambia por plataforma, pero los principios se transfieren.

## SQL

SQL es la señal tecnológica más frecuente en las ofertas actuales relacionadas con esta ocupación.

Un DBA normalmente debe entender:

- `SELECT` y filtros;
- joins;
- agregación;
- lenguaje de definición de datos (DDL);
- lenguaje de manipulación de datos (DML);
- transacciones;
- permisos;
- índices;
- planes de ejecución;
- bloqueos y contención;
- procedimientos/funciones donde correspondan;
- vistas del catálogo/sistema;
- scripting seguro y validación de cambios.

Una consulta o script no es seguro solo porque se ejecuta sin error.

Antes de una acción SQL de impacto, verifique:

- ambiente destino;
- nombres de objetos;
- alcance de filas;
- comportamiento de transacción;
- permisos;
- conteos esperados;
- preparación de respaldo/reversión;
- impacto de rendimiento;
- validación posterior.

## Señales tecnológicas actuales

Los datos de ofertas de empleo de O*NET para 2025 muestran señales de demanda como:

- SQL — **62%**;
- Python — **42%**;
- AWS — **29%**;
- Microsoft Azure — **25%**;
- Snowflake — **16%**;
- Apache Spark — **13%**;
- Microsoft Power BI — **12%**;
- Java — **12%**;
- PostgreSQL — **11%**;
- Apache Kafka — **10%**;
- Apache Airflow — **9%**;
- Microsoft SQL Server — **9%**;
- Tableau — **9%**;
- NoSQL — **9%**;
- Amazon Redshift — **9%**;
- Git — **8%**;
- Linux — **8%**;
- MySQL — **8%**;
- Oracle PL/SQL — **7%**;
- Oracle Database — **7%**;
- UNIX — **6%**;
- Terraform — **5%**;
- PowerShell — **5%**;
- MongoDB — **5%**.

Son señales de ofertas, no una lista obligatoria para todos los puestos DBA. Profundice según la plataforma y el empleador objetivo.

## Identidad, acceso y administración privilegiada

El acceso a bases de datos debe seguir controles aprobados.

Buenas prácticas incluyen:

- mínimo privilegio;
- acceso basado en roles cuando sea compatible;
- cuentas normales y privilegiadas separadas cuando la política lo requiera;
- MFA en acceso administrativo compatible;
- almacenamiento aprobado de credenciales y secretos;
- no colocar contraseñas o connection strings en chats, tickets, repositorios públicos o notas personales;
- evitar cuentas administradoras compartidas salvo proceso heredado/emergencia expresamente aprobado;
- revisión periódica de accesos;
- retiro oportuno de privilegios innecesarios;
- registro/auditoría de acciones privilegiadas cuando sea posible;
- segregación de funciones para operaciones sensibles cuando corresponda.

Nunca use acceso de base de datos para curiosear información.

## Seguridad e integridad de bases de datos

O*NET incluye expresamente la seguridad de bases de datos como responsabilidad central.

Un DBA puede participar en:

- control de acceso;
- endurecimiento de configuración;
- cifrado cuando sea parte de su responsabilidad;
- parches y actualizaciones;
- remediación de vulnerabilidades;
- auditoría y logs;
- exposición segura de red;
- protección de respaldos;
- gestión de secretos;
- monitoreo de accesos sospechosos o fallidos;
- preservación de evidencia en incidentes;
- recuperación después de incidentes de integridad o disponibilidad.

La arquitectura de seguridad y la interpretación legal pueden corresponder a otros equipos. Sepa cuándo escalar.

## Un respaldo no es lo mismo que la recuperabilidad

Un log que diga “backup completed” sirve como evidencia operativa, pero no demuestra por sí solo que la organización pueda recuperar lo necesario.

Un proceso maduro puede incluir:

- calendarios aprobados de respaldo;
- reglas de retención;
- cifrado/protección de medios o repositorios;
- copias fuera del mismo dominio de falla cuando se requieran;
- pruebas de restauración;
- recuperación a un punto en el tiempo cuando la plataforma lo permita;
- runbooks documentados;
- monitoreo de respaldos fallidos o tardíos;
- verificación del alcance del respaldo;
- ejercicios de recuperación ante desastres;
- pruebas de dependencias entre aplicación y base de datos.

Las organizaciones pueden definir **RPO** (Recovery Point Objective) y **RTO** (Recovery Time Objective). El DBA debe entender los objetivos establecidos por la organización y no inventarlos independientemente.

## Pruebas de restauración

Una prueba de restauración debe responder, entre otras cosas:

- ¿El respaldo se puede leer?
- ¿Contiene la base y versión esperadas?
- ¿Puede restaurarse en el ambiente requerido?
- ¿Las claves o secretos necesarios están disponibles mediante procesos aprobados?
- ¿La base restaurada pasa controles de integridad?
- ¿Las aplicaciones se reconectan correctamente?
- ¿Los pasos de recuperación están documentados y actualizados?
- ¿La prueba cumplió los objetivos de recuperación establecidos?

Nunca realice una restauración destructiva sobre producción sin autorización explícita y plan controlado.

## Alta disponibilidad, replicación y failover

Según la plataforma, un DBA puede apoyar:

- réplicas;
- clústeres;
- availability groups;
- bases standby;
- réplicas administradas en nube;
- configuraciones multizona o multirregión;
- procedimientos de failover;
- monitoreo de retraso de replicación.

Alta disponibilidad no reemplaza el respaldo. La replicación puede copiar corrupción, borrados o cambios maliciosos.

El failover debe probarse bajo procedimientos aprobados, no asumirse correcto solo porque los componentes parecen saludables.

## Rendimiento y capacidad

Un DBA puede investigar:

- consultas lentas;
- planes de ejecución ineficientes;
- índices faltantes o excesivos;
- locks, blocking y deadlocks;
- presión de CPU/memoria;
- presión de almacenamiento;
- latencia de I/O;
- agotamiento de conexiones;
- crecimiento del transaction log;
- retraso de replicación;
- crecimiento de tablas e índices;
- sobrecarga de mantenimiento;
- cambios de carga de trabajo.

Ajuste con evidencia. Un cambio que mejora una consulta puede perjudicar otra carga.

Documente:

- línea base;
- métrica observada;
- hipótesis;
- cambio;
- validación;
- plan de reversión;
- resultado.

## Gestión de cambios

Los cambios de producción pueden afectar muchas aplicaciones y usuarios. Un cambio disciplinado puede requerir:

- propósito documentado;
- solicitud/ticket aprobado;
- revisión de dependencias;
- script o paquete probado;
- revisión por pares;
- respaldo o punto de restauración;
- ventana de mantenimiento;
- plan de comunicación;
- pasos de ejecución;
- controles de validación;
- pasos de rollback;
- monitoreo posterior;
- evidencia de finalización.

No “arregle” producción silenciosamente fuera de controles aprobados solo porque el cambio parezca pequeño.

## Cambios de esquema y migraciones

Antes de una migración de esquema o datos, considere:

- tamaño de tabla;
- duración de bloqueos;
- impacto en transaction log;
- compatibilidad de aplicaciones;
- impacto en índices;
- impacto en replicación;
- factibilidad de rollback;
- conversión de tipos;
- comportamiento de nulos/defaults;
- zona horaria y codificación;
- downtime necesario;
- conteos/checksums de validación;
- impacto de privacidad/seguridad.

Para cambios grandes o de alto riesgo, use el patrón probado de la organización; no improvise en producción.

## Parches y actualizaciones

Las plataformas requieren mantenimiento de seguridad y ciclo de vida.

Un plan controlado puede incluir:

- revisión del ciclo de soporte del proveedor;
- evaluación de compatibilidad;
- compatibilidad de drivers/clientes;
- preparación de respaldo/recuperación;
- pruebas no productivas;
- secuencia de HA/failover;
- aprobación de ventana de mantenimiento;
- plan de rollback/fallback;
- validación posterior de integridad y rendimiento;
- documentación de versión/configuración.

No prometa “cero downtime” si la arquitectura y las pruebas no lo respaldan.

## Monitoreo y alertas

Áreas útiles incluyen:

- disponibilidad;
- conexiones fallidas;
- fallos de autenticación;
- errores de base de datos;
- CPU/memoria/almacenamiento;
- latencia I/O;
- duración de consultas;
- blocking/deadlocks;
- éxito/fallo de respaldos;
- estado de replicación;
- crecimiento del transaction log;
- umbrales de capacidad;
- expiración de certificados/credenciales cuando aplique;
- salud/costos anómalos de servicios cloud.

Las alertas deben tener responsable, severidad y respuesta esperada. Demasiadas alertas de baja calidad generan ruido y pueden ocultar incidentes reales.

## Respuesta a incidentes y escalamiento

Un DBA puede participar ante:

- caída de base de datos;
- corrupción;
- acceso no autorizado sospechado;
- compromiso de credenciales;
- ransomware o actividad destructiva;
- borrado accidental;
- fallo de replicación;
- recuperación fallida;
- degradación severa de rendimiento;
- preocupación de integridad de datos;
- exposición inesperada de información.

Siga el proceso de incidentes. Preserve evidencia y tiempos. No destruya logs ni “limpie” antes de que seguridad/incidentes determine qué debe conservarse.

## Privacidad, retención y gobierno de datos

Los DBA pueden ver información muy sensible. Ese acceso es una responsabilidad, no un beneficio del puesto.

Siga reglas aprobadas sobre:

- propósito autorizado;
- acceso mínimo necesario;
- clasificación de datos;
- retención y eliminación;
- legal holds cuando correspondan;
- masking/tokenización cuando se requieran;
- extractos seguros;
- datos de prueba;
- verificación de destinatarios;
- exportaciones;
- auditoría;
- reporte de incidentes.

No copie datos de producción a ambientes personales o de desarrollo sin control.

## Separación de desarrollo, pruebas y producción

Cuando la organización lo permita:

- desarrolle y pruebe cambios fuera de producción;
- use datos sintéticos, enmascarados o aprobados;
- restrinja credenciales de producción;
- separe aprobación y desarrollo cuando corresponda;
- controle connection strings y secretos por ambiente;
- valide el destino antes de ejecutar scripts.

Un error de alto impacto muy común es ejecutar el script correcto en el ambiente equivocado.

## Bases de datos en nube y servicios administrados

Los servicios administrados pueden automatizar hardware, opciones de parches, snapshots o replicación. No eliminan las responsabilidades del cliente.

Un DBA u operador de datos puede seguir administrando:

- identidad y acceso;
- exposición de red;
- security groups/firewalls;
- usuarios y roles;
- cifrado y claves cuando sean configurables;
- retención de backups;
- logging/auditoría;
- mantenimiento;
- sizing;
- rendimiento de consultas;
- resiliencia;
- credenciales de aplicaciones;
- costos/capacidad;
- gobierno de cambios.

Comprenda el modelo de responsabilidad compartida del proveedor. “Está en la nube” no significa que el proveedor gestione toda la seguridad.

## Automatización, scripting e infraestructura como código

La automatización reduce tareas repetitivas, pero también puede multiplicar errores.

Herramientas comunes pueden incluir:

- Python;
- PowerShell;
- shell scripts;
- SQL scripts;
- Terraform;
- herramientas de configuration management;
- CI/CD;
- automatización cloud.

Controles útiles:

- control de versiones;
- revisión por pares;
- validación de parámetros;
- protecciones por ambiente;
- gestión de secretos;
- modo de prueba/dry-run cuando exista;
- logging;
- rollback;
- permisos limitados para identidades de automatización.

## IA responsable en trabajo DBA

La IA puede apoyar tareas de bajo riesgo cuando la política organizacional lo permita, por ejemplo:

- redactar SQL o scripts administrativos;
- explicar un plan de ejecución;
- redactar runbooks;
- proponer casos de prueba;
- generar datos sintéticos;
- resumir documentación pública;
- sugerir consultas de monitoreo;
- explicar mensajes de error.

La validación humana sigue siendo obligatoria.

No:

- cargue datos de producción, credenciales, esquemas privados, connection strings o logs protegidos en una IA no aprobada;
- ejecute SQL generado por IA en producción sin revisión, prueba y autorización;
- acepte nombres de objetos, sintaxis, métricas o comportamiento de proveedor inventados;
- permita cambios autónomos de producción fuera de la gobernanza aprobada;
- trate salida de IA como evidencia de incidente o documentación oficial del proveedor;
- omita rollback porque una recomendación parezca plausible.

Para cambios importantes, verifique contra documentación autoritativa y controles organizacionales.

NIST AI RMF y su perfil de IA generativa son guías voluntarias de gestión de riesgo; no reemplazan el gobierno de bases de datos o seguridad.

## Accesibilidad y documentación utilizable

La documentación debe funcionar para quienes la necesiten, incluso bajo presión de un incidente.

Prácticas útiles:

- encabezados significativos;
- pasos claros y ordenados;
- fuentes y contraste legibles;
- tablas con encabezados adecuados;
- descripciones textuales de diagramas;
- no depender solo del color;
- herramientas/documentación accesibles por teclado cuando sea compatible;
- ramas claras de decisión/error;
- lenguaje sencillo en pasos de alto impacto;
- comandos/scripts diferenciados del texto explicativo.

Un verificador automático no demuestra cumplimiento legal de accesibilidad.

## Educación y rutas de entrada — Estados Unidos

O*NET ubica Database Administrators en **Job Zone Four — Considerable Preparation Needed**.

Las respuestas actuales de educación indican:

- **89%** licenciatura/bachelor's degree;
- **4%** certificado post-baccalaureate;
- **3%** associate degree.

Son respuestas ocupacionales, no una regla absoluta para cada vacante.

Se puede avanzar hacia DBA desde:

- soporte TI;
- soporte de aplicaciones;
- administración de sistemas;
- desarrollo de bases de datos;
- operaciones de datos;
- desarrollo de software;
- soporte cloud;
- reporting/BI;
- programas formales de informática/sistemas;
- capacitación del empleador;
- aprendizaje o rutas técnicas.

### Localizadores de capacitación y financiamiento en EE. UU.

CareerOneStop y American Job Centers ayudan a investigar formación local, proveedores WIOA y apoyos. Elegibilidad y financiamiento varían; no están garantizados.

O*NET lista títulos aprobados de aprendizaje:

- **Database Administrator (Nof)**;
- **Database Technician**.

Use Apprenticeship.gov para verificar oportunidades activas en su ubicación.

## Canadá

Canada Job Bank asigna Database Administrator (DBA) a **NOC 21223 — Database analysts and data administrators**.

Los requisitos típicos actuales incluyen:

- bachelor's degree o programa de college, usualmente en informática, ingeniería informática o matemáticas;
- programación y experiencia relacionada.

Job Bank indica actualmente que la ocupación **no está regulada en Canadá**. Aun así, los requisitos del empleador pueden ser exigentes.

### Salarios de Canadá

Los salarios nacionales actuales de Job Bank son:

- **C$25.00/hora — bajo**;
- **C$40.87/hora — mediano**;
- **C$61.03/hora — alto**.

Corresponden a NOC 21223 y no son pago garantizado para toda vacante DBA.

Canada.ca ofrece enlaces de ayuda estudiantil, formación, servicios de empleo y programas provinciales/territoriales. La elegibilidad y disponibilidad varían.

## Colombia

La correspondencia directa es **CUOC 25210 — Diseñadores y administradores de bases de datos**, nivel de competencia 4.

Denominaciones oficiales incluyen:

- Administrador de base de datos;
- Administrador de datos;
- Analista de base de datos;
- Arquitecto de bases de datos;
- Data manager;
- Desarrollador de base de datos;
- Diseñador de bases de datos;
- Gerente de base de datos;
- Programador de base de datos.

Las funciones oficiales cubren arquitectura, implementación/prueba de DBMS, políticas de acceso/uso, respaldo/recuperación, seguridad/integridad, gestión de riesgo y coordinación técnica.

OCUPACOL actualmente no muestra una cifra disponible de ocupados para este perfil. Esta guía no fabrica un salario nacional representativo para DBA en Colombia.

### SENA — ruta de formación titulada

**Implementación y gestión de bases de datos**

- Tecnólogo;
- **3,984 horas**;
- formación titulada;
- listado actual en Betowa;
- aplican selección y requisitos de examen de Estado;
- verifique ubicación, modalidad, cohorte, cupos y fechas.

### SENA — rutas complementarias

**Bases de datos: generalidades y sistemas de gestión**

- formación complementaria virtual;
- **40 horas**;
- bases relacionales, normalización, entidad-relación y fundamentos de diseño.

**Construcción de bases de datos con MySQL**

- formación complementaria;
- **48 horas**;
- construcción focalizada con MySQL.

Los cursos cortos complementan; no reemplazan el Tecnólogo de larga duración ni la experiencia que pueda exigir el empleador.

## América Latina y el Caribe

OIT/Cinterfor ayuda a localizar instituciones y sistemas de formación profesional de la región. Es un localizador, no una garantía de curso DBA vigente, beca, admisión o financiamiento.

## Salarios oficiales de Estados Unidos

Los datos BLS 2025 mostrados por O*NET son:

| Percentil | Anual | Por hora |
|---|---:|---:|
| 10 | $60,230 | $28.96 |
| 25 | $79,610 | $38.28 |
| Mediana | $104,620 | $50.30 |
| 75 | $135,460 | $65.13 |
| 90 | $163,320 | $78.52 |

Corresponden a O*NET-SOC 15-1242.00 Database Administrators.

## Perspectiva de empleo de Estados Unidos

Las proyecciones O*NET/BLS muestran:

- empleo 2024: **78,000**;
- empleo proyectado 2034: **77,500**;
- crecimiento proyectado: **-1%**;
- vacantes anuales proyectadas: **3,800**.

Es una ligera disminución del empleo total, no crecimiento. Las vacantes incluyen reemplazo/rotación.

## Estimación actual no gubernamental de EE. UU.

La página actual de Indeed para Database Administrator, revisada en agosto de 2026, informa aproximadamente:

- salario base promedio: **$110,414/año**;
- bajo: **$73,876/año**;
- alto: **$165,024/año**;
- **2.1k** salarios provenientes de ofertas de empleo en los **36 meses** anteriores;
- actualización **10 de agosto de 2026**.

Es una estimación específica del título y no gubernamental, no una serie salarial oficial ni compensación garantizada.

## Secuencia práctica de aprendizaje

### Etapa 1 — fundamentos

Aprenda:

- modelos relacionales;
- claves/restricciones;
- normalización;
- SQL;
- transacciones;
- seguridad básica;
- conceptos de backup.

### Etapa 2 — una plataforma en profundidad

Elija, por ejemplo:

- PostgreSQL;
- Microsoft SQL Server;
- MySQL;
- Oracle Database.

Practique instalación/configuración, usuarios/roles, respaldo/restauración, monitoreo y cambios seguros.

### Etapa 3 — operaciones

Agregue:

- análisis de rendimiento;
- índices;
- monitoreo;
- mantenimiento;
- parches;
- pruebas de recuperación;
- resolución de incidentes;
- automatización.

### Etapa 4 — nube y resiliencia

Aprenda:

- una plataforma cloud;
- bases administradas;
- controles de identidad/red;
- replicación/alta disponibilidad;
- retención de backups;
- automatización de infraestructura;
- responsabilidad compartida.

### Etapa 5 — especialización

Posibles rutas:

- cloud DBA/data platform engineer;
- database reliability;
- seguridad de bases de datos;
- performance engineering;
- data engineering;
- arquitectura;
- automatización de plataforma.

## Proyectos de portafolio seguros

Use datos sintéticos, públicos o con licencia explícita.

Proyectos posibles:

1. crear un esquema relacional con restricciones;
2. documentar un modelo entidad-relación;
3. crear roles de mínimo privilegio;
4. respaldar y restaurar una base de práctica;
5. demostrar point-in-time recovery en laboratorio cuando sea compatible;
6. crear línea base y ejercicio de tuning de índices;
7. simular replicación/failover en laboratorio;
8. escribir una migración con validación y rollback;
9. crear dashboard de monitoreo con carga sintética;
10. redactar y probar un runbook de recuperación.

Nunca publique:

- datos de empleador o clientes;
- credenciales o connection strings;
- esquemas o capturas de producción;
- IPs/hostnames privados;
- configuración propietaria;
- backups reales;
- tokens o claves;
- detalles de vulnerabilidades de sistemas sin autorización.

## Plan inicial de cuatro semanas

### Semana 1 — SQL y esquema

- instale una base local de práctica;
- cree tablas, claves y restricciones;
- practique SQL de forma segura;
- documente el esquema;
- cree usuarios no privilegiados.

### Semana 2 — respaldo y recuperación

- cree un respaldo de laboratorio;
- restáurelo en una instancia separada;
- registre tiempo y pasos;
- verifique objetos/conteos;
- documente fallos y correcciones.

### Semana 3 — monitoreo y rendimiento

- cree carga sintética;
- capture línea base;
- identifique una consulta lenta;
- revise su plan de ejecución;
- pruebe una mejora;
- compare evidencia antes/después.

### Semana 4 — cambio y portafolio

- cree una pequeña migración de esquema;
- escriba prechecks, ejecución, validación y rollback;
- elimine secretos/datos privados;
- redacte un README;
- busque vacantes actuales DBA/Database Technician/Cloud Database;
- compare requisitos con su siguiente objetivo de aprendizaje.

## Títulos de puesto para buscar

- Database Administrator;
- DBA;
- Junior Database Administrator;
- Database Technician;
- SQL Server DBA;
- Oracle DBA;
- PostgreSQL DBA;
- MySQL DBA;
- Cloud Database Administrator;
- Database Support Engineer;
- Database Operations Engineer;
- Database Reliability Engineer;
- Data Platform Administrator;
- Database Analyst.

## Preguntas para un empleador

Considere preguntar:

- ¿Qué plataformas y versiones están en alcance?
- ¿Qué porcentaje es on-premises versus cloud administrado?
- ¿Cuáles son las expectativas de on-call?
- ¿Cómo se gestionan las cuentas privilegiadas?
- ¿Se exige MFA para administración?
- ¿Con qué frecuencia se prueban restauraciones?
- ¿Están documentados RPO/RTO?
- ¿Quién es responsable de configuración de seguridad de bases de datos?
- ¿Cómo se aprueban parches y cambios de esquema?
- ¿Existe ventana de mantenimiento definida?
- ¿Qué plataforma de monitoreo/alertas se usa?
- ¿Cómo se almacenan secretos?
- ¿La automatización está versionada y revisada?
- ¿Qué distingue responsabilidad junior de senior?
- ¿Qué apoyo de formación/certificación existe?

## Enlaces de verificación

Verifique valores y disponibilidad de programas antes de una decisión importante.

### Estados Unidos

- O*NET Database Administrators: https://www.onetonline.org/link/details/15-1242.00
- O*NET salarios nacionales: https://www.onetonline.org/link/localwages/15-1242.00
- O*NET tendencias nacionales: https://www.onetonline.org/link/localtrends/15-1242.00
- O*NET tecnologías actuales: https://www.onetonline.org/link/hot_tech/15-1242.00
- CareerOneStop WIOA: https://www.careeronestop.org/LocalHelp/EmploymentAndTraining/find-WIOA-training-programs.aspx
- Apprenticeship.gov: https://www.apprenticeship.gov/
- Indeed contexto salarial DBA: https://www.indeed.com/career/database-administrator/salaries

### Canadá

- Job Bank resumen DBA: https://www.jobbank.gc.ca/marketreport/summary-occupation/17875/ca
- Job Bank requisitos DBA: https://www.jobbank.gc.ca/marketreport/requirements/17875/ca
- Job Bank salarios DBA: https://www.jobbank.gc.ca/marketreport/wages-occupation/17875/ca
- Canada training gateway: https://www.canada.ca/en/services/jobs/training.html

### Colombia

- OCUPACOL CUOC 25210: https://ocupacol.mintrabajo.gov.co/Profile/OccupationalProfile/25210
- SENA Implementación y gestión de bases de datos: https://betowa.sena.edu.co/oferta/implementacion-y-gestion-de-bases-de-datos?modality=P&offertype=open&programId=178214
- SENA Bases de datos generalidades: https://betowa.sena.edu.co/oferta/bases-de-datos-generalidades-y-sistemas-de-gestion?modality=V&offertype=open&programId=73885

### Regional, seguridad, IA y accesibilidad

- OIT/Cinterfor: https://www.oitcinterfor.org/statsfp/paises
- CISA Secure Our World: https://www.cisa.gov/secure-our-world
- NIST Cybersecurity Framework: https://www.nist.gov/cyberframework
- NIST Privacy Framework: https://www.nist.gov/privacy-framework
- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework
- Section 508: https://www.section508.gov/create/
- WCAG 2.2: https://www.w3.org/TR/WCAG22/

## Aviso importante

Esta guía ofrece información general de educación y planificación profesional. No garantiza empleo, ingresos, admisión, financiamiento, colocación en aprendizaje, certificación, ascenso ni ningún otro resultado. Las correspondencias ocupacionales son comparaciones y los requisitos varían por empleador y jurisdicción. Salarios, tecnologías, programas y condiciones cambian con el tiempo.

Esta guía no proporciona asesoría jurídica, de privacidad, ciberseguridad, contabilidad ni asesoría profesional específica de un proveedor, y no certifica independientemente que un sistema sea seguro, recuperable, conforme o accesible.

## Autor y asistencia de IA

Creada y dirigida por **Alberto “Al” Leiva**. ChatGPT apoyó investigación, organización, edición, apoyo de traducción y preparación documental bajo la dirección del autor. El autor conserva la responsabilidad de las decisiones editoriales y de publicación.

## Licencia

Salvo que un archivo indique lo contrario, este material se distribuye bajo **CC BY-NC-SA 4.0**.
