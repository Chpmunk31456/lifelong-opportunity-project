# Guía de Oportunidades para Toda la Vida 88 — Desarrollador Web

**Versión:** 2.0 maestra de trabajo controlada  
**Idioma:** Español neutro de América Latina (`es-419`)  
**Referencia principal de EE. UU.:** O*NET-SOC 15-1254.00 — Web Developers  
**Comparación de Canadá:** NOC 21234 — Web developers and programmers  
**Comparación de Colombia:** CUOC 25130 — Desarrolladores Web y multimedia  
**Fecha de revisión:** 2026-08-22  
**Fuente inglesa congelada:** blob `a25d99dc19dcc0ed795ea9e55be20d95101ef1e2`

## Qué es esta carrera

Un desarrollador web crea, modifica y mantiene sitios y aplicaciones web. Dependiendo del puesto, puede trabajar con interfaces de navegador, layouts responsivos, lógica del lado del cliente, servicios de servidor, APIs, bases de datos, autenticación, rendimiento, pruebas, despliegue, accesibilidad y soporte de producción.

El título es amplio. Un desarrollador front-end suele concentrarse en la experiencia del navegador. Un desarrollador back-end puede enfocarse en lógica de servidor, APIs y datos. Un desarrollador full-stack puede trabajar en varias capas. Otros puestos se orientan a CMS, comercio electrónico o integración de plataformas.

Estados Unidos tiene una referencia directa en **O*NET-SOC 15-1254.00 — Web Developers**, Bright Outlook y actualizada en 2026. Canadá corresponde a **NOC 21234 — Web developers and programmers**. Colombia tiene una correspondencia directa en **CUOC 25130 — Desarrolladores Web y multimedia**.

## Por qué sigue siendo útil

Los sistemas web soportan comercio, banca, salud, educación, gobierno, medios, portales internos, software como servicio e identidad. Las herramientas cambian, pero siguen siendo valiosas habilidades como comprender requisitos, escribir código mantenible, integrar APIs y datos, probar comportamientos, proteger credenciales, construir interfaces accesibles y usar control de versiones.

## Familias de puestos

### Front-end
Puede trabajar con HTML, CSS, JavaScript/TypeScript, diseño responsivo, browser APIs, accesibilidad, rendimiento y frameworks como React, Angular o Vue.

### Back-end
Puede trabajar con código de servidor, APIs, autenticación/autorización, bases de datos, colas, caché, logging, integraciones y despliegue.

### Full-stack
Combina varias capas. No significa ser experto en toda tecnología existente.

### CMS y comercio electrónico
Puede trabajar con WordPress, Shopify u otras plataformas, plantillas, plugins, contenido, integraciones y mantenimiento.

## Fundamentos web

Aprenda:

- HTML semántico;
- CSS y diseño responsivo;
- JavaScript;
- DOM y eventos;
- formularios;
- URLs;
- HTTP;
- cookies/sesiones;
- JSON;
- APIs;
- accesibilidad;
- Git;
- seguridad y privacidad básicas.

## HTML semántico

Use elementos por su significado, no solo por apariencia. Una buena estructura mejora mantenimiento, navegación por teclado, interpretación por lectores de pantalla, formularios y pruebas. Prefiera controles nativos cuando sean adecuados; los componentes personalizados pueden requerir trabajo adicional de teclado, foco y accesibilidad.

## CSS y diseño responsivo

Comprenda cascada, especificidad, box model, Flexbox, Grid, unidades, media/container queries cuando correspondan, imágenes responsivas, tipografía, contraste, foco visible, reduced motion y reflow.

No asuma que una página es responsiva porque se ve bien en un teléfono y un monitor. Pruebe rangos de viewport y estados reales del contenido.

## JavaScript y TypeScript

Las señales actuales de O*NET muestran **JavaScript 47%** y **TypeScript 22%**. Fundamentos útiles incluyen variables, funciones, objetos, arrays, módulos, promises, async/await, manejo de errores, eventos, DOM, network requests, estado, debugging y pruebas.

TypeScript puede mejorar mantenibilidad, pero no sustituye validación en runtime ni controles de seguridad.

## Tecnologías actuales

Las ofertas vinculadas a O*NET durante 2025 muestran:

- JavaScript **47%**;
- React **35%**;
- CSS **33%**;
- AWS **27%**;
- HTML **26%**;
- RESTful API **24%**;
- Java **23%**;
- TypeScript y Git **22%**;
- Python y SQL **21%**;
- Node.js y Angular **18%**;
- Docker y Azure **16%**;
- Kubernetes **15%**;
- PostgreSQL **12%**;
- MySQL, PHP y GitHub **10%**;
- Vue.js **9%**;
- GraphQL **8%**;
- Jenkins CI **7%**;
- WordPress y MongoDB **6%**;
- JIRA, JSON y Linux **5%**.

Son señales del mercado, no una lista obligatoria para cada empleo.

## HTTP y APIs

Comprenda métodos GET/POST/PUT/PATCH/DELETE, códigos de estado, headers, content types, tokens, caché, paginación, rate limits, timeouts, retries, idempotencia cuando aplique y CORS a nivel conceptual.

Nunca exponga secretos en código del navegador. El usuario puede inspeccionar el código y las solicitudes de red.

## Autenticación frente a autorización

- **Autenticación:** ¿quién es la persona?
- **Autorización:** ¿qué puede hacer?

Ocultar un botón en la interfaz no sustituye la autorización del servidor. Un usuario autenticado no debe recibir acceso automático a todos los objetos o acciones.

## Sesiones, cookies y tokens

Siga la arquitectura aprobada para cookies, tokens, expiración, revocación, CSRF cuando corresponda y scopes mínimos. Evite secretos en URLs y logs. No invente una arquitectura de seguridad si el equipo ya tiene estándares definidos.

## Desarrollo del lado del servidor

Puede incluir routing, validación, reglas de negocio, acceso a datos, background jobs, caché, integraciones, archivos, autenticación/autorización, logging y errores. Valide input no confiable en el servidor; la validación del cliente mejora UX pero no es un límite de seguridad.

## Bases de datos y SQL

Conceptos útiles:

- tablas/documentos;
- claves y relaciones;
- índices;
- transacciones;
- restricciones;
- consultas parametrizadas;
- migraciones;
- conexiones;
- responsabilidad de backup/recovery.

### SQL injection

No concatene input no confiable directamente en consultas. Use consultas parametrizadas/prepared statements u ORM aprobado. La validación de input no sustituye la construcción segura de consultas.

## Git y colaboración

Use ramas, commits, diffs, pull/merge requests, reviews y resolución de conflictos según la práctica del equipo. Nunca confirme passwords, API keys, certificados privados u otros secretos. Si un secreto llega al historial, siga el proceso de rotación/incidente.

## Pruebas

Pueden incluir pruebas unitarias, componentes, integración, API, end-to-end, accesibilidad, compatibilidad y rendimiento. Las pruebas de seguridad requieren autorización.

Que una suite pase es evidencia; no demuestra por sí sola que la aplicación sea segura, accesible legalmente o libre de defectos.

## Accesibilidad

Considere:

- HTML semántico;
- teclado;
- foco visible;
- labels;
- mensajes de error;
- contraste;
- zoom/reflow;
- comunicación no basada solo en color;
- alt text;
- media alternatives;
- compatibilidad con lectores de pantalla.

Los escáneres automáticos detectan solo parte de los problemas. Un PASS automático no establece cumplimiento legal.

## Rendimiento

Factores relevantes incluyen tamaño de payload, imágenes, fonts, ejecución JavaScript, rendering, latencia, caché, queries, APIs, capacidad de servidor, CDN y lazy loading.

Core Web Vitals pueden ser señales útiles, pero ninguna métrica garantiza ranking, conversiones o ingresos.

## Logging y monitoreo

Maneje errores sin revelar información interna. Use logs estructurados, IDs de correlación cuando corresponda, monitoreo y alertas, protegiendo información sensible. No registre passwords, tokens, datos completos de pago o información personal innecesaria.

## Secretos y configuración

No coloque en el código fuente passwords de bases de datos, private API keys, signing keys, OAuth client secrets, cloud credentials o certificados privados. Use sistemas aprobados de secretos/configuración.

Un archivo `.env` no es automáticamente seguro; respete reglas de exclusión y gestión de secretos.

## Dependencias

Las dependencias de terceros agregan riesgo de supply chain. Reduzca paquetes innecesarios, revise advisories, actualice versiones soportadas, verifique licencias cuando corresponda, evite paquetes abandonados y pruebe actualizaciones antes de producción.

## Despliegue y rollback

Defina versión, ambiente, pruebas, migraciones, monitoreo, rollback/forward-fix y autoridad de release. No despliegue directamente a producción solo porque tiene acceso técnico.

## Cloud y responsabilidad compartida

AWS y Azure aparecen con fuerza en ofertas actuales. Los servicios administrados no trasladan automáticamente todas las responsabilidades de aplicación, identidad, datos, configuración y código al proveedor. Siga el modelo de responsabilidad compartida y la arquitectura organizacional.

## Privacidad y minimización de datos

Recoja y conserve solo datos necesarios para propósitos aprobados. Siga reglas sobre información personal, consentimiento/preferencias cuando aplique, analytics, cookies/tracking, retención, borrado, exports y datos de prueba. Escale preguntas legales/de privacidad a la función responsable.

## Desarrollo seguro

Prácticas relevantes pueden incluir validación de servidor, output encoding, consultas parametrizadas, autenticación/autorización, session protections, secrets management, dependency management, configuración segura, logging y security review.

NIST SSDF y OWASP son referencias útiles. No otorgan autorización para penetration testing. Scanning intrusivo, explotación o pruebas destructivas requieren alcance y permiso explícitos.

## IA responsable

La IA puede ayudar, cuando la política lo permita, con explicación de código, drafting, refactoring, pruebas, datos sintéticos, documentación y debugging.

No cargue código propietario, datos de clientes, secretos, credenciales o información no publicada a herramientas no aprobadas. Revise y pruebe código generado. Verifique paquetes/APIs, licencias y patrones de seguridad. No permita despliegue autónomo a producción fuera de gobernanza.

## Límites éticos y profesionales

Un desarrollador web no debe:

- desplegar sin autoridad;
- ocultar defectos críticos conocidos;
- poner secretos en repositorios públicos;
- saltar autenticación/autorización para cumplir un plazo;
- usar datos de producción en demos personales;
- realizar pruebas de seguridad no autorizadas;
- afirmar seguridad, accesibilidad o ausencia de bugs solo porque las pruebas pasaron;
- garantizar ranking SEO, ingresos o conversiones;
- publicar código o arquitectura privada del empleador.

## Educación y entrada — Estados Unidos

O*NET ubica Web Developers en **Job Zone Three — Medium Preparation Needed**. Es común encontrar formación vocacional/técnica, experiencia relacionada o associate degree, aunque los empleadores varían.

CareerOneStop/American Job Centers ayudan a localizar capacitación y WIOA. Elegibilidad y financiamiento no son automáticos. Apprenticeship.gov puede usarse para buscar oportunidades actuales; no se garantiza una vacante.

## Canadá

Job Bank usa **NOC 21234**. Los requisitos típicos incluyen bachelor’s degree en informática/programación/web/software engineering **o** college program relacionado; experiencia en programación suele ser requerida.

Job Bank identifica actualmente la ocupación como **no regulada en Canadá**.

### Salarios Canadá

- **C$21.48/hora** bajo;
- **C$38.46/hora** mediano;
- **C$57.16/hora** alto.

### Perspectiva Canadá

El panorama nacional 2024–2033 indica demanda y oferta ampliamente en equilibrio. Las perspectivas de tres años varían por provincia/territorio, así que verifique la región específica.

## Colombia

**CUOC 25130 — Desarrolladores Web y multimedia** es una correspondencia directa de nivel de competencia 4.

No se fabrica un salario nacional representativo porque los indicadores disponibles no permiten una afirmación estadísticamente sólida.

### Rutas SENA

**Análisis y desarrollo de software**  
- Tecnólogo;
- **3.984 horas**;
- formación amplia en requisitos, diseño, desarrollo, implementación y calidad;
- disponibilidad/cupos/modalidad varían.

**Desarrollo web con PHP**  
- complementaria virtual;
- **40 horas**;
- requiere conocimientos previos de programación/HTML;
- formación suplementaria.

El curso de 40 horas no equivale al Tecnólogo de 3.984 horas.

## América Latina y Caribe

OIT/Cinterfor sirve como localizador regional de instituciones de formación profesional. No garantiza cursos, becas, financiamiento o cupos.

## Ingresos y perspectiva actual

### Estados Unidos oficial

| Percentil | Anual | Por hora |
|---|---:|---:|
| 10 | $48,100 | $23.12 |
| 25 | $64,230 | $30.88 |
| Mediana | $92,650 | $44.54 |
| 75 | $126,230 | $60.69 |
| 90 | $162,290 | $78.03 |

Perspectiva 2024–2034:

- empleo 2024: **86,000**;
- proyectado 2034: **92,500**;
- crecimiento: **8%**;
- vacantes anuales: **5,400**.

### Contexto de mercado no gubernamental

Indeed, actualizado **2 de agosto de 2026**, reporta aproximadamente:

- promedio **$86,333/año**;
- bajo **$50,037/año**;
- alto **$148,958/año**;
- **1.4 mil** observaciones;
- **36 meses** de ofertas;
- contexto de bonus en efectivo **$2,500/año**.

Es una estimación de mercado específica del título, no una estadística oficial.

## Secuencia práctica de aprendizaje

1. Browser foundations: HTML, CSS, JavaScript, accesibilidad y Git.
2. Aplicación: framework, forms, estado, APIs, validación y pruebas.
3. Servidor/datos: un stack de servidor, SQL, autenticación/autorización y queries seguras.
4. Delivery: CI/CD, configuración, logging, monitoreo, deploy y rollback.
5. Especialización: front end, back end, full stack, CMS/e-commerce, accesibilidad, performance, cloud o secure development.

## Portafolio seguro

Use sistemas propios, open source o demo y datos sintéticos/públicos. Puede mostrar UI responsiva/semántica, APIs, autenticación demo, CRUD con queries parametrizadas, pruebas, Git, README, CI y un despliegue demo controlado.

No publique código de empleadores, datos reales de clientes, credenciales, internal URLs, arquitectura privada o vulnerabilidades no autorizadas.

## Plan de cuatro semanas

### Semana 1
Construya un sitio responsivo multipágina con HTML/CSS y pruebe teclado y viewports.

### Semana 2
Agregue JavaScript, validación, una API pública/demo y estados loading/error.

### Semana 3
Agregue un servidor/API y una base de datos pequeña con queries parametrizadas y configuración segura.

### Semana 4
Agregue pruebas, README, notas de accesibilidad/performance, historial Git y deployment demo controlado.

## Títulos de búsqueda

- Web Developer;
- Junior Web Developer;
- Front-End Developer;
- Back-End Web Developer;
- Full-Stack Developer;
- Web Application Developer;
- JavaScript Developer;
- React Developer;
- WordPress Developer;
- PHP Developer;
- UI Developer;
- E-commerce Developer.

## Preguntas antes de aceptar un puesto

- ¿Es front end, back end, full stack o CMS/e-commerce?
- ¿Qué frameworks/lenguajes se usan realmente?
- ¿Quién decide arquitectura y seguridad?
- ¿Cómo funcionan code review y CI/CD?
- ¿Cómo se liberan cambios a producción?
- ¿Cómo gestionan secretos y configuración?
- ¿Cómo verifican accesibilidad?
- ¿Qué pruebas se esperan del desarrollador?
- ¿Hay on-call o despliegues fuera de horario?
- ¿Qué distingue junior de senior?

## Fuentes y enlaces de verificación

### Estados Unidos
- O*NET details: https://www.onetonline.org/link/details/15-1254.00
- O*NET summary: https://www.onetonline.org/link/summary/15-1254.00
- O*NET Job Zone: https://www.onetonline.org/skills/zone/15-1254.00
- O*NET wages: https://www.onetonline.org/link/localwages/15-1254.00
- O*NET outlook: https://www.onetonline.org/link/localtrends/15-1254.00
- O*NET technologies: https://www.onetonline.org/link/demand/15-1254.00
- CareerOneStop WIOA: https://www.careeronestop.org/LocalHelp/EmploymentAndTraining/find-WIOA-training-programs.aspx
- Apprenticeship.gov: https://www.apprenticeship.gov/
- Indeed: https://www.indeed.com/career/web-developer/salaries

### Canadá
- Job Bank summary: https://www.jobbank.gc.ca/marketreport/summary-occupation/17892/ca
- Job Bank requirements: https://www.jobbank.gc.ca/marketreport/requirements/17892/ca
- Job Bank wages: https://www.jobbank.gc.ca/marketreport/wages-occupation/17892/ca
- Job Bank outlook: https://www.jobbank.gc.ca/marketreport/outlook-occupation/17892/ca
- Canada training: https://www.canada.ca/en/services/jobs/training.html

### Colombia y América Latina
- CUOC 25130: https://ocupacol.mintrabajo.gov.co/Profile/OccupationalProfile/25130
- SENA Análisis y desarrollo de software: https://betowa.sena.edu.co/oferta/analisis-y-desarrollo-de-software
- SENA Desarrollo web con PHP: https://betowa.sena.edu.co/oferta/desarrollo-web-con-php?modality=V&offertype=company
- OIT/Cinterfor: https://www.oitcinterfor.org/statsfp/paises

### Seguridad, IA y accesibilidad
- NIST SSDF: https://csrc.nist.gov/pubs/sp/800/218/final
- OWASP WSTG: https://owasp.org/www-project-web-security-testing-guide/
- NIST AI RMF: https://www.nist.gov/itl/ai-risk-management-framework
- Section 508: https://www.section508.gov/create/
- WCAG 2.2: https://www.w3.org/TR/WCAG22/

## Aviso importante

Esta guía ofrece información general de educación y planificación profesional. No garantiza empleo, ingresos, admisión, financiamiento, apprenticeship, certificación, ascenso, ranking, ingresos comerciales, conversiones, seguridad o cumplimiento de accesibilidad.

No se afirma certificación humana independiente, acreditación profesional, revisión legal, evaluación de seguridad, certificación de accesibilidad, certificación cloud/vendor ni traducción certificada salvo documentación separada.

## Autor y asistencia de IA

Creada y dirigida por **Alberto “Al” Leiva**. ChatGPT apoyó investigación, organización, edición, apoyo de traducción y preparación de documentos bajo la dirección del autor. El autor conserva la responsabilidad editorial y de publicación.

## Licencia

Salvo indicación contraria, este material está licenciado bajo **CC BY-NC-SA 4.0**.
