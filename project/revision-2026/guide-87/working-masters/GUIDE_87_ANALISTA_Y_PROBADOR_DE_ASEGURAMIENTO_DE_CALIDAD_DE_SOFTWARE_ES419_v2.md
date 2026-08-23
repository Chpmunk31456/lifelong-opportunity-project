# Guía de Oportunidades para Toda la Vida 87 — Analista y Probador de Aseguramiento de Calidad de Software

**Versión:** 2.0 maestra de trabajo controlada  
**Idioma:** Español neutro de América Latina (`es-419`)  
**Referencia principal de EE. UU.:** O*NET-SOC 15-1253.00 — Software Quality Assurance Analysts and Testers  
**Comparaciones de Canadá:** NOC 21222 — Information systems specialists; NOC 22222 — Information systems testing technicians  
**Comparación de Colombia:** CUOC 25190 — Desarrolladores y analistas de software y multimedia no clasificados en otras ocupaciones  
**Fecha de revisión:** 2026-08-22  
**Fuente inglesa congelada:** blob `446a05a75eaed4739a007d9327faba8234210d19`

## Qué es esta carrera

Los analistas y probadores de aseguramiento de calidad de software ayudan a determinar si una aplicación se comporta como se espera, cumple requisitos definidos, maneja errores de forma segura y puede liberarse con un nivel de riesgo entendido. El trabajo puede incluir revisar requisitos, diseñar casos de prueba, preparar datos, ejecutar verificaciones manuales o automatizadas, documentar defectos, volver a probar correcciones, apoyar regresión y evaluar usabilidad y accesibilidad.

QA no es simplemente “buscar errores”. Es trabajo de evidencia. Un buen probador sabe qué se verifica, qué ambiente y versión se usaron, qué precondiciones y datos aplicaron, qué resultado se esperaba, qué ocurrió realmente y cómo otra persona puede reproducir la observación.

Estados Unidos tiene una correspondencia directa en **O*NET-SOC 15-1253.00**. Canadá separa mejor el alcance: el trabajo de analista de QA se compara con **NOC 21222**, mientras que la ejecución técnica de pruebas se compara con **NOC 22222**. Colombia tiene una correspondencia sólida en **CUOC 25190**.

## Por qué sigue siendo importante

El software afecta banca, salud, gobierno, transporte, educación, comercio, comunicaciones, manufactura y servicios digitales. Un defecto puede causar cálculos incorrectos, transacciones fallidas, indisponibilidad, pérdida de datos, exposición de privacidad, problemas de seguridad, interfaces inaccesibles, retrabajo y pérdida de confianza.

La automatización y la IA amplían la capacidad de pruebas, pero no eliminan la necesidad de personas que definan verificaciones confiables, interpreten fallas, detecten evidencia débil, exploren casos límite y comuniquen riesgo.

## Títulos de trabajo relacionados

Busque, según experiencia y especialización:

- Software QA Analyst;
- Software Quality Assurance Analyst;
- QA Tester;
- Software Tester;
- Manual Tester;
- QA Engineer;
- Test Engineer;
- Automation Tester;
- Test Automation Engineer;
- Quality Engineer;
- SDET;
- API Tester;
- Accessibility Tester;
- Performance Tester;
- UAT Analyst.

Lea siempre las funciones reales, la profundidad de programación, el alcance de pruebas y la autoridad de liberación.

## Base de prueba y trazabilidad

Toda prueba importante debe partir de una base definida, por ejemplo:

- requisito aprobado;
- criterio de aceptación;
- historia de usuario;
- contrato de interfaz o API;
- diseño o especificación;
- corrección de defecto;
- riesgo;
- flujo de usuario documentado;
- requisito regulatorio o de política cuando corresponda.

La trazabilidad puede conectar:

**requisito o riesgo → caso de prueba → ejecución → evidencia → defecto o resultado → retest / decisión de liberación.**

QA no debe inventar silenciosamente requisitos para hacer que una prueba pase o falle.

## Diseño de casos de prueba

Un caso defendible puede incluir:

- objetivo;
- requisito o riesgo;
- precondiciones;
- ambiente;
- build/versión;
- datos de prueba;
- pasos;
- resultado esperado;
- resultado real;
- estado aprobado/fallido/bloqueado;
- evidencia;
- limpieza o restablecimiento;
- defecto o requisito relacionado.

Cuando el requisito es ambiguo o contradictorio, se debe escalar la ambigüedad en lugar de decidir el resultado esperado después de observar el producto.

## Reportes de defectos reproducibles

Un reporte útil debe permitir que otra persona reproduzca e investigue el problema. Incluya, cuando corresponda:

- título conciso;
- ambiente, navegador, dispositivo o plataforma;
- build/versión;
- precondiciones;
- pasos reproducibles;
- resultado esperado;
- resultado real;
- frecuencia;
- capturas, logs o video seguros;
- severidad/impacto;
- requisito o prueba relacionada;
- identificador de datos sin exponer información protegida.

Describa lo observado. No culpe a un desarrollador ni afirme una causa raíz no demostrada.

## Severidad frente a prioridad

- **Severidad**: impacto del defecto en usuarios, sistema, datos, seguridad o negocio.
- **Prioridad**: urgencia u orden en que la organización decide atenderlo.

Los equipos usan escalas distintas. Siga las definiciones y reglas de escalamiento del empleador.

## Niveles y tipos de prueba

Pueden incluir:

- unitarias;
- integración;
- sistema;
- end-to-end;
- aceptación;
- funcionales;
- regresión;
- negativas/error;
- valores límite;
- compatibilidad;
- API;
- validación de datos;
- usabilidad;
- accesibilidad;
- rendimiento/carga/estrés;
- recuperación/resiliencia;
- seguridad únicamente con autorización explícita.

Una sola persona no necesariamente realiza todos estos tipos. QA tampoco posee automáticamente la decisión final de liberación.

## Pruebas exploratorias y guionadas

Las pruebas guionadas aportan repetibilidad y trazabilidad. Las exploratorias utilizan juicio para investigar comportamientos y combinaciones inesperadas. Son complementarias.

Las pruebas exploratorias también deben respetar alcance, ambiente, datos, autorización y documentación básica de lo realizado.

## Datos de prueba

Prefiera:

- datos sintéticos;
- datos enmascarados aprobados;
- cuentas de prueba diseñadas para ese fin;
- conjuntos controlados con resultados conocidos.

No copie casualmente datos de producción a ambientes de prueba. Proteja credenciales, tokens y llaves. No adjunte datos protegidos a tickets si no es necesario y autorizado. Sanitice logs, capturas y videos cuando corresponda.

## Ambientes y configuración

Registre información importante como:

- versión/build;
- sistema operativo;
- navegador/dispositivo;
- versión de API o servicio;
- feature flags;
- estado de base de datos;
- rol de la cuenta;
- dependencias;
- configuración específica del ambiente.

No declare una corrección final hasta probar la versión y ambiente relevantes.

## Regresión

La regresión verifica si un cambio dañó funciones previamente operativas. Priorice según:

- componentes modificados;
- dependencias;
- flujos críticos;
- historial de defectos;
- impacto de negocio;
- privacidad/seguridad;
- integraciones;
- tiempo disponible;
- confiabilidad de automatización.

Una suite enorme que nadie confía no es automáticamente mejor que una suite más pequeña y basada en riesgo.

## Automatización de pruebas

Las señales de ofertas de empleo de O*NET incluyen **Python, Selenium, Atlassian JIRA, SQL, Java, Jenkins CI, JavaScript, Postman, AWS, Git, Linux, Microsoft Azure, Apache JMeter, C#, GitHub, C++, Microsoft Playwright, Azure DevOps Services, TestNG, RESTful API, Appium y REST Assured**.

La automatización requiere:

- código mantenible;
- selectores o interfaces estables;
- aserciones significativas;
- control de versiones;
- revisión donde aplique;
- datos controlados;
- diagnóstico de fallas;
- manejo de pruebas flaky;
- mantenimiento cuando cambia el producto.

Que una suite automatizada pase no demuestra que el producto esté libre de defectos.

## Pruebas flaky

Una prueba flaky produce resultados inconsistentes sin un cambio significativo del producto. Causas comunes:

- tiempos rígidos;
- estado compartido;
- datos inestables;
- dependencias no confiables;
- race conditions;
- selectores frágiles;
- capacidad del ambiente;
- red inestable.

No normalice la inestabilidad sin explicación. Regístrela, investigue y repare, ponga en cuarentena o sustituya la prueba según la política del equipo.

## Pruebas de API

Pueden verificar:

- códigos de estado;
- esquemas;
- campos obligatorios;
- autorización;
- validaciones;
- reglas de negocio;
- paginación;
- casos límite;
- manejo de errores;
- rendimiento bajo condiciones aprobadas.

La herramienta no define por sí sola el comportamiento correcto.

## Base de datos y validación de datos

QA puede verificar que:

- las transacciones creen los registros esperados;
- los cambios afecten las filas correctas;
- tipos y restricciones funcionen;
- cálculos concilien;
- migraciones preserven datos requeridos;
- duplicados se manejen según la regla;
- se creen registros de auditoría cuando corresponda.

Use acceso de lectura/escritura únicamente dentro de su autorización.

## CI/CD y liberación

Un buen gate de calidad debe aclarar:

- build probado;
- suites ejecutadas;
- fallas y omisiones;
- confiabilidad de resultados;
- evidencia retenida;
- criterio de liberación;
- quién puede aprobar excepciones.

Pasar pruebas automatizadas es evidencia, no autorización automática para liberar.

## Límite de pruebas de seguridad

QA funcional no equivale automáticamente a penetration testing.

Se pueden hacer verificaciones seguras y autorizadas de roles, autorización, sesiones, validación de entrada, defaults seguros y privacidad. Escaneo intrusivo, explotación, ataques de credenciales, payloads destructivos o pruebas de penetración requieren autorización explícita y reglas de alcance.

NIST SSDF y OWASP WSTG son referencias útiles, pero no otorgan permiso para atacar sistemas.

## Accesibilidad

QA puede revisar teclado, foco visible, etiquetas, mensajes de error, encabezados, contraste, zoom/reflow, lectores de pantalla, subtítulos y alternativas.

Los escáneres automáticos detectan solo parte de los problemas. Pasar un escaneo no establece cumplimiento legal de accesibilidad.

## Rendimiento

Las pruebas pueden medir tiempo de respuesta, throughput, concurrencia, uso de recursos, estabilidad y recuperación. Las pruebas de carga/estrés pueden afectar sistemas; use ambientes, límites, datos y horarios aprobados.

## Privacidad y seguridad de la evidencia

Tickets, capturas, videos, logs y exportaciones pueden contener datos sensibles. Use mínimo privilegio, repositorios aprobados, MFA, enmascaramiento, verificación de destinatarios y reglas de retención. No use correo o almacenamiento personal para artefactos protegidos ni exponga credenciales o secretos.

## IA responsable en QA

La IA puede ayudar, cuando la política lo permita, a:

- proponer ideas de prueba;
- redactar casos;
- generar datos sintéticos;
- explicar un stack trace;
- redactar automatización;
- sugerir edge cases;
- preparar documentación.

La validación humana sigue siendo obligatoria. No cargue código fuente protegido, credenciales, datos de clientes, logs privados o información no publicada en herramientas no aprobadas. No acepte requisitos inventados por IA. No permita que la IA cierre defectos o autorice liberaciones fuera de la gobernanza. No trate una explicación generada como causa raíz demostrada.

NIST AI RMF y su perfil de IA generativa son guías voluntarias de gestión de riesgo.

## Límites éticos

No se debe:

- fabricar resultados;
- marcar PASS sin evidencia;
- ocultar fallas conocidas;
- cambiar el resultado esperado después de ejecutar solo para crear un PASS;
- eliminar defectos sin disposición autorizada;
- usar datos productivos sin autorización;
- explotar sistemas fuera de alcance;
- divulgar defectos o vulnerabilidades confidenciales;
- afirmar que un producto está “sin bugs” porque una suite pasó.

## Educación y rutas de entrada — Estados Unidos

O*NET ubica la ocupación en **Job Zone Four — Considerable Preparation Needed**. Las respuestas actuales sobre educación de nuevas contrataciones incluyen aproximadamente:

- **50%** licenciatura/bachelor’s degree;
- **26%** associate degree;
- **9%** certificado postsecundario.

No son requisitos universales. Los empleadores pueden aceptar diferentes combinaciones de educación, experiencia, portafolio, prácticas, aprendizaje, soporte técnico, desarrollo y automatización.

CareerOneStop/American Job Centers pueden ayudar a localizar capacitación y programas WIOA. La elegibilidad y el financiamiento no son automáticos.

O*NET lista el título de Registered Apprenticeship **Software Quality Assurance Tester (Nof)**. Verifique vacantes reales en Apprenticeship.gov.

## Canadá

### QA a nivel de analista — NOC 21222

El título **Software QA (Quality Assurance) Analyst** se compara con **NOC 21222**. Salarios nacionales actuales:

- **C$28.85/hora** bajo;
- **C$46.15/hora** mediano;
- **C$68.68/hora** alto.

### Software Tester — NOC 22222

El título **Software Tester** se compara con **NOC 22222**. Salarios nacionales actuales:

- **C$17.50/hora** bajo;
- **C$35.00/hora** mediano;
- **C$51.28/hora** alto.

La regulación no es uniforme. Job Bank identifica actualmente esta ocupación como regulada en Manitoba mediante la Certified Technicians and Technologists Association of Manitoba. Verifique la provincia/territorio correspondiente.

## Colombia

**CUOC 25190** incluye títulos como Analista de prueba de software, Analista de pruebas - tester, Analista de aseguramiento de la calidad informática, Probador de sistemas, Probador de software, Coordinador de prueba de software y Líder de pruebas testing.

No se fabrica un salario nacional representativo de Colombia porque el perfil oficial actual no aporta evidencia estadísticamente representativa adecuada para esa afirmación.

### Rutas SENA

**Procesamiento de pruebas de software**  
- Técnico;
- **2.208 horas**;
- formación titulada.

**Manejo de pruebas de software**  
- formación complementaria virtual;
- **40 horas**.

**Modelos de calidad de software**  
- formación complementaria virtual;
- **40 horas**.

**Procesos para software de calidad**  
- formación complementaria virtual;
- **40 horas**.

Los cursos de 40 horas son complementarios y no equivalen al Técnico de 2.208 horas. Verifique disponibilidad, cupos, modalidad y requisitos en Betowa.

## América Latina y el Caribe

OIT/Cinterfor puede ayudar a localizar instituciones nacionales de formación profesional. No garantiza cursos, becas, cupos ni financiamiento de pruebas de software.

## Salarios y perspectiva — use la población correcta

### Estados Unidos

BLS 2025/O*NET para 15-1253.00:

| Percentil | Anual | Por hora |
|---|---:|---:|
| 10 | $61,440 | $29.54 |
| 25 | $80,310 | $38.61 |
| Mediana | $104,300 | $50.14 |
| 75 | $133,180 | $64.03 |
| 90 | $167,010 | $80.29 |

Proyección 2024–2034:

- empleo 2024: **201,700**;
- empleo 2034: **221,900**;
- crecimiento: **10%**;
- vacantes anuales proyectadas: **14,000**.

### Estimación no gubernamental actual

Indeed, revisado en agosto de 2026, reportó para **Software Quality Assurance Analyst** aproximadamente:

- promedio **$87,641/año**;
- bajo **$56,161/año**;
- alto **$136,766/año**;
- **208** observaciones;
- **36 meses** de ofertas;
- actualizado **2 de agosto de 2026**.

Es una estimación de mercado específica del título, no una estadística oficial.

## Secuencia práctica de aprendizaje

1. Fundamentos: requisitos, casos, defectos, severidad/prioridad, regresión, accesibilidad y privacidad.
2. Fundamentos técnicos: HTML/CSS/JavaScript, SQL, HTTP/API, DevTools, Git, logs y línea de comandos.
3. Automatización: un framework, selectores estables, aserciones, datos, setup/teardown, debugging y CI.
4. Especialización: API, móvil, rendimiento, accesibilidad, datos, o QA con enfoque de seguridad autorizado.

## Portafolio seguro

Use software público, con licencia, open source o propio y datos sintéticos. Puede incluir plan de prueba, matriz de trazabilidad, defectos bien escritos, colección API, suite automatizada, revisión de accesibilidad, prueba controlada de rendimiento y workflow CI.

No publique código de empleadores, requisitos propietarios, datos reales de clientes, credenciales, logs privados o vulnerabilidades fuera de autorización.

## Plan inicial de cuatro semanas

### Semana 1
Escriba diez casos de prueba para una app demo, defina resultados esperados antes de ejecutar y documente dos defectos reproducibles.

### Semana 2
Practique HTTP/API y SQL básico con sistemas locales o demo y documente datos y limpieza.

### Semana 3
Automatice un flujo estable con Playwright, Selenium u otro framework apropiado; agregue aserciones y revise una falla intencional.

### Semana 4
Prepare README, evidencia, limitaciones, un flujo CI sencillo si aplica y bullets de currículum precisos.

## Preguntas antes de aceptar una posición

- ¿Es principalmente manual, automatización, análisis QA o ejecución técnica?
- ¿Quién define severidad y prioridad?
- ¿Quién tiene autoridad final de liberación?
- ¿Qué frameworks se usan?
- ¿Cómo manejan pruebas flaky?
- ¿Cómo se crean y protegen datos de prueba?
- ¿Qué pruebas de seguridad pertenecen al alcance QA?
- ¿Cómo se verifica accesibilidad?
- ¿Hay trabajo fuera de horario o fines de semana por liberaciones?
- ¿Qué distingue junior de senior?

## Fuentes y enlaces de verificación

### Estados Unidos
- O*NET: https://www.onetonline.org/link/details/15-1253.00
- O*NET resumen: https://www.onetonline.org/link/summary/15-1253.00
- O*NET salarios: https://www.onetonline.org/link/localwages/15-1253.00
- O*NET perspectiva: https://www.onetonline.org/link/localtrends/15-1253.00
- CareerOneStop WIOA: https://www.careeronestop.org/LocalHelp/EmploymentAndTraining/find-WIOA-training-programs.aspx
- Apprenticeship.gov: https://www.apprenticeship.gov/
- Indeed: https://www.indeed.com/career/software-quality-assurance-analyst/salaries

### Canadá
- QA Analyst: https://www.jobbank.gc.ca/marketreport/summary-occupation/22511/ca
- QA Analyst requisitos: https://www.jobbank.gc.ca/marketreport/requirements/22511/ca
- QA Analyst salarios: https://www.jobbank.gc.ca/marketreport/wages-occupation/22511/ca
- Software Tester: https://www.jobbank.gc.ca/marketreport/summary-occupation/3950/ca
- Software Tester requisitos: https://www.jobbank.gc.ca/marketreport/requirements/3950/ca
- Software Tester salarios: https://www.jobbank.gc.ca/wagereport/occupation/3950
- Capacitación Canadá: https://www.canada.ca/en/services/jobs/training.html

### Colombia
- CUOC 25190: https://ocupacol.mintrabajo.gov.co/Profile/OccupationalProfile/25190
- SENA Procesamiento de pruebas: https://betowa.sena.edu.co/oferta/procesamiento-de-pruebas-de-software?level=2&modality=V&programId=171614
- SENA Manejo de pruebas: https://betowa.sena.edu.co/oferta/manejo-de-pruebas-de-software?programId=103412
- SENA Modelos de calidad: https://betowa.sena.edu.co/oferta/modelos-de-calidad-de-software?modality=V&offertype=open&programId=73282&technology=1
- SENA Procesos para software de calidad: https://betowa.sena.edu.co/oferta/procesos-para-software-de-calidad?programId=68240

### Desarrollo seguro, IA y accesibilidad
- NIST SSDF: https://csrc.nist.gov/pubs/sp/800/218/final
- OWASP WSTG: https://owasp.org/www-project-web-security-testing-guide/
- NIST AI RMF: https://www.nist.gov/itl/ai-risk-management-framework
- Section 508: https://www.section508.gov/create/
- WCAG 2.2: https://www.w3.org/TR/WCAG22/
- OIT/Cinterfor: https://www.oitcinterfor.org/statsfp/paises

## Aviso importante

Esta guía ofrece información general de educación y planificación profesional. No garantiza empleo, ingresos, admisión, financiamiento, aprendizaje, certificación, ascenso ni ningún otro resultado. Las correspondencias ocupacionales pueden no ser equivalencias exactas entre jurisdicciones.

No se afirma certificación humana independiente, acreditación profesional, revisión legal, evaluación de seguridad, certificación de accesibilidad, certificación de liberación de software ni certificación de traducción salvo documentación separada.

## Autor y asistencia de IA

Creada y dirigida por **Alberto “Al” Leiva**. ChatGPT apoyó investigación, organización, edición, apoyo de traducción y preparación de documentos bajo la dirección del autor. El autor conserva la responsabilidad de las decisiones editoriales y de publicación.

## Licencia

Salvo indicación contraria, este material está licenciado bajo **CC BY-NC-SA 4.0**.
