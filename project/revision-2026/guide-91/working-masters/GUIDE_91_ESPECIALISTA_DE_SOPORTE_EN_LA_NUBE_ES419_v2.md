# Guía de Oportunidades para Toda la Vida 91 — Especialista de Soporte en la Nube

**Versión:** 2.0 maestra de trabajo controlada  
**Idioma:** Español neutro de América Latina (`es-419`)  
**Referencia principal de EE. UU.:** O*NET-SOC 15-1231.00 — Computer Network Support Specialists  
**Comparaciones de Canadá:** NOC 22220 — Computer network and web technicians; NOC 22221 — User support technicians  
**Comparaciones de Colombia:** CUOC 35130 — Técnicos en redes y tecnologías de la información; CUOC 35121 — Técnicos en asistencia y soporte de tecnologías de la información  
**Fecha de revisión:** 2026-08-22  
**Fuente inglesa congelada:** blob `499172975884310af740796bd38f304b07ae0b62`

## Qué es esta carrera

Un Especialista de Soporte en la Nube ayuda a mantener sistemas y servicios cloud disponibles, utilizables, seguros y soportables. Según el empleador, puede trabajar con identidad y acceso, redes virtuales, DNS, cómputo, almacenamiento, monitoreo, logs, incidentes, backups, aplicaciones SaaS, escalamiento con proveedores y cambios controlados en producción.

El título es amplio. Algunos puestos son muy orientados a infraestructura y se parecen a soporte de redes o sistemas; otros se concentran en usuarios y aplicaciones cloud. Algunos quedan cerca de funciones de administrador o ingeniero cloud. Las tareas, permisos y límites de escalamiento importan más que el nombre del cargo.

En Estados Unidos, la mejor referencia actual es **O*NET-SOC 15-1231.00 — Computer Network Support Specialists** porque O*NET incluye explícitamente **cloud networks** y lista **Cloud Support Specialist** y **Junior Cloud Engineer (Nof)** como títulos aprobados de Registered Apprenticeship. Canadá y Colombia requieren un modelo de dos alcances, no una equivalencia forzada.

## Alcance por función

### Soporte de infraestructura/red cloud
Puede incluir redes virtuales, routing, DNS, reglas de firewall/security groups, conectividad, salud de cómputo/almacenamiento, monitoreo, backups y soporte privilegiado de plataforma. Se alinea mejor con **NOC 22220** en Canadá y **CUOC 35130** en Colombia.

### Soporte de usuario/aplicación cloud
Puede incluir acceso SaaS, incidentes de aplicaciones, problemas de cliente/despliegue, configuración de usuario, software de comunicaciones y soporte de primera línea. Se alinea mejor con **NOC 22221** en Canadá y **CUOC 35121** en Colombia.

### Funciones adyacentes
- **Help Desk/User Support:** soporte general de endpoints, usuarios y aplicaciones.
- **Network Support:** conectividad, routing, DNS, dispositivos y redes cloud.
- **Cloud Administrator:** suele tener más autoridad de configuración y administración.
- **Cloud Engineer:** suele asumir más diseño, construcción, automatización e IaC.
- **SRE/DevOps:** suele abarcar ingeniería de confiabilidad, automatización y entrega de software.

No asuma que un Especialista de Soporte en la Nube controla arquitectura, excepciones de seguridad, presupuesto, diseño de políticas IAM o autoridad de liberación a producción salvo que el empleador lo asigne explícitamente.

## Empiece por impacto y alcance

Antes de diagnosticar, identifique:
1. quién o qué está afectado;
2. impacto al negocio/servicio;
3. cuenta, tenant, suscripción o proyecto;
4. región/zona y ambiente;
5. recurso o servicio involucrado;
6. timestamps;
7. cambios recientes;
8. nivel de autorización;
9. logs/métricas disponibles;
10. ruta de escalamiento.

Esto ayuda a evitar cambios amplios y riesgosos solo para “ver si funciona”.

## Jerarquía de cuentas y recursos

Comprenda las variantes del proveedor para organización/cuenta/tenant, suscripción/proyecto, resource groups/folders/projects, regiones y zonas de disponibilidad, IDs de recursos, tags/labels, cuotas/límites y propiedad de costos.

La terminología cambia entre AWS, Azure, Google Cloud y otros proveedores. Verifique siempre el objetivo activo antes de ejecutar un comando o cambio.

## Responsabilidad compartida

Los proveedores operan y protegen partes de la plataforma; el cliente conserva responsabilidades que dependen del modelo de servicio y la configuración. Un servicio administrado **no** significa que:
- el proveedor configure correctamente el IAM del cliente;
- desaparezca la clasificación de datos;
- las vulnerabilidades de la aplicación pasen al proveedor;
- backups y recuperación estén automáticamente correctos;
- no puedan configurarse mal redes/firewalls;
- desaparezcan requisitos de logging y monitoreo.

Use documentación específica del servicio/proveedor en vez de memorizar un único diagrama genérico.

## Identidad, MFA y mínimo privilegio

Prácticas obligatorias:
- identidades nominativas;
- métodos aprobados de autenticación;
- MFA cuando corresponda;
- mínimo privilegio;
- acceso temporal/elevado cuando exista;
- cuidado de service accounts/workload identities;
- verificación de alcance antes de cambiar roles o políticas;
- escalamiento de accesos sospechosos.

Nunca pegue contraseñas, API keys, tokens, signing keys, certificados u otros secretos en tickets, chat, repositorios públicos o herramientas de IA no aprobadas. Tener acceso de soporte no da autoridad ilimitada para inspeccionar datos del cliente o modificar cualquier recurso.

## Fundamentos de cómputo

Conceptos útiles incluyen máquinas virtuales/instances, imágenes/templates, tamaños/tipos, restart/start/stop, discos/volúmenes, autoscaling, containers/managed compute a nivel conceptual, health checks, cuotas y límites de acceso al sistema operativo.

Un restart puede ocultar temporalmente un síntoma sin demostrar causa raíz. Capture evidencia antes de acciones destructivas o que cambien estado cuando la política lo requiera.

## Fundamentos de almacenamiento

Comprenda almacenamiento object/block/file, lifecycle/retention, cifrado/acceso, redundancia, snapshots/backups y versioning cuando exista.

No cambie retención, cifrado, acceso público o replicación sin autoridad y revisión de impacto.

## Redes cloud

Comprenda VPC/VNet/redes virtuales, subnets, route tables, security groups/firewalls, IP públicas/privadas, NAT, load balancers, DNS, VPN/private connectivity, puertos/protocolos, latencia, packet path y certificados/TLS a nivel de soporte.

Diagnostique por capas. Un timeout puede provenir de DNS, routing, firewall, service health, aplicación, certificado o una dependencia.

## Diagnóstico de DNS

Revise hostname esperado, resolver path, tipo/valor del registro, TTL/cache, zonas privadas/públicas, cambios recientes, alineación certificado-hostname y salud real del servicio destino.

No realice cambios amplios de DNS si la evidencia apunta a otra capa.

## Logs, métricas, traces y alertas

La evidencia puede incluir activity/audit logs, authentication logs, network-flow logs, logs de sistema/aplicación, métricas, traces, dashboards, alertas y avisos de service health.

Los logs pueden contener información sensible. Siga controles de acceso, retención, exportación y compartición. No adjunte paquetes completos de logs protegidos cuando sea suficiente un extracto mínimo y sanitizado.

## Flujo repetible de troubleshooting

1. Identifique impacto y urgencia.
2. Confirme cuenta/recurso/región/ambiente.
3. Confirme timestamps y cambios recientes.
4. Revise service health del proveedor.
5. Revise logs, métricas y alertas relevantes.
6. Aísle identidad, red, cómputo, almacenamiento, aplicación o dependencia.
7. Pruebe una hipótesis a la vez.
8. Use solo remediación autorizada.
9. Verifique recuperación desde la perspectiva del usuario/servicio.
10. Documente evidencia, acciones, resultado y escalamiento.

“It works now” no reemplaza evidencia del síntoma, cambio y validación.

## Incidentes y escalamiento

Use definiciones organizacionales de impacto/urgencia. Escale cuando:
- un cambio privilegiado exceda su autoridad;
- haya posible impacto de seguridad/privacidad;
- pueda existir pérdida o corrupción de datos;
- se sospeche un incidente del proveedor o multi-región;
- RPO/RTO u obligaciones contractuales estén en riesgo;
- la causa esté fuera del alcance de soporte;
- se requiera rediseño arquitectónico.

No prometa causa raíz ni tiempo de resolución sin evidencia y autoridad.

## Backup, snapshot y recuperabilidad

Un backup exitoso o snapshot **no** demuestra recuperabilidad. Comprenda alcance, retención, cifrado/acceso, separación de cuenta/región donde aplique, restore testing, conceptos RPO/RTO, consistencia de aplicación, orden de dependencias y ownership de disaster recovery.

**La replicación no es automáticamente un backup.** Eliminación o corrupción pueden replicarse. Las afirmaciones de recuperación deben basarse en pruebas de restore, no solo en indicadores verdes del job.

## Regiones, zonas y resiliencia

Regiones y availability zones pueden reducir ciertos riesgos, pero la resiliencia depende de arquitectura y configuración. Diseños multi-zone o multi-region agregan costo, consistencia, latencia y complejidad operativa.

Un especialista puede reunir evidencia y ejecutar runbooks aprobados, pero no debe rediseñar resiliencia sin autoridad asignada.

## Gestión de cambios y autoridad de producción

Los cambios cloud pueden afectar IAM, firewall/security groups, compute, storage, DNS, rutas, certificados, parámetros del servicio, monitoreo, backups o deployments.

Antes de cambiar, confirme autorización, target exacto, impacto, maintenance window si aplica, rollback o forward-fix, implicaciones de backup/recovery, plan de validación y requisitos de comunicación/escalamiento.

Tener acceso técnico no equivale a tener autoridad de producción.

## CLI, scripting e infraestructura como código

CLI cloud, PowerShell, Bash, Python e IaC pueden modificar recursos rápidamente. Use dispositivos/repositorios aprobados, evite secretos hard-coded, peer review cuando corresponda, pruebe en ambientes de menor riesgo cuando sea posible, confirme cuenta/región y capture evidencia de versión/plan/output.

No pegue comandos destructivos de foros o IA en producción sin comprenderlos y revisarlos.

## Conciencia de costos

El soporte puede afectar costos mediante tamaño/cantidad de instancias, almacenamiento, transferencia de datos, snapshots, retención de logs, managed services y recursos abandonados. La optimización debe respetar autoridad asignada; no elimine recursos solo porque parezcan inactivos.

## Privacidad y residencia de datos

El soporte cloud puede exponer datos personales, de clientes, regulados o confidenciales. Siga controles de acceso, retención, exportación, región/ubicación, datos de prueba e incidentes. No invente requisitos legales; escale la interpretación a la función responsable.

## Límite de seguridad

Un especialista puede investigar logins sospechosos, exposición, misconfiguration o conectividad, pero security testing e incident response deben quedar dentro de autorización explícita. No ejecute scanning intrusivo, exploitation o pruebas destructivas sin permiso.

NIST Cybersecurity Framework y CISA Secure Our World son referencias útiles. La documentación de responsabilidad compartida del proveedor sigue siendo necesaria para los límites específicos del servicio.

## Accesibilidad

El soporte también incluye portales, documentación, dashboards y tickets. Use headings claros, instrucciones legibles, workflows navegables por teclado, labels descriptivos y alternativas accesibles cuando sea práctico. Un scanner automatizado no prueba cumplimiento legal.

## IA responsable

La IA aprobada por política puede ayudar a explicar errores, redactar runbooks, resumir logs sanitizados, proponer hipótesis, crear escenarios sintéticos o revisar scripts.

Controles:
- no enviar secretos, credenciales, datos de clientes, arquitectura propietaria ni logs protegidos a herramientas no aprobadas;
- verificar comandos contra documentación oficial;
- revisar cuenta/región/recurso antes de ejecutar;
- validar código/scripts generados;
- tratar explicaciones de IA como hipótesis, no evidencia;
- nunca permitir que IA apruebe o ejecute cambios privilegiados autónomos fuera de gobernanza.

## Señales tecnológicas actuales

O*NET/Lightcast 2025 para la ocupación más amplia muestra Microsoft Office **13%**, Active Directory **13%**, ServiceNow **9%**, Linux **7%**, macOS **6%**, Windows Server **6%**, Outlook **6%**, Excel **6%**, Windows **5%**, BGP **3%**, Azure **3%**, PowerShell **2%** y SQL/Python/Splunk/Bash alrededor de **1%**. La página de demanda también identifica firewall software en **10%**.

Son señales de ofertas, no requisitos universales. Las habilidades de proveedor deben apoyarse en fundamentos de identidad, redes, sistemas operativos, monitoreo y troubleshooting.

## Estados Unidos — educación y rutas

O*NET ubica 15-1231.00 en **Job Zone Four — Considerable Preparation Needed**. Respuestas actuales de educación: aproximadamente **47%** bachelor's degree, **22%** associate degree y **14%** some college, no degree. No son reglas universales.

O*NET lista **Cloud Support Specialist** y **Junior Cloud Engineer (Nof)** como títulos aprobados de Registered Apprenticeship. Verifique aperturas reales en Apprenticeship.gov. CareerOneStop permite investigar WIOA y otras rutas; elegibilidad y financiamiento varían.

## Estados Unidos — salarios y perspectiva

Salarios oficiales 2025 de **Computer Network Support Specialists**:

| Percentil | Anual | Por hora |
|---|---:|---:|
| 10 | $47,120 | $22.65 |
| 25 | $58,240 | $28.00 |
| Mediana | $76,220 | $36.64 |
| 75 | $98,750 | $47.48 |
| 90 | $127,780 | $61.43 |

2024–2034:
- empleo 2024: **152,700**;
- proyectado 2034: **155,500**;
- crecimiento: **2%**;
- vacantes anuales: **9,600**.

Son estadísticas del benchmark de soporte, no una serie salarial exacta del título Cloud Support Specialist.

### Contexto de mercado adyacente no gubernamental

La página actual de Indeed para **Cloud Engineer** muestra aproximadamente **$135,392/año promedio**, **$88,667 bajo**, **$206,741 alto**, alrededor de **4.5k observaciones**, durante **36 meses**, actualizada el **2 de agosto de 2026**.

Es un título adyacente más orientado a ingeniería y puede pagar materialmente más que soporte. No es dato oficial ni salario exacto de Cloud Support Specialist.

## Canadá — alcance infraestructura/red cloud

Para soporte cloud orientado a infraestructura use **NOC 22220**.

Salarios nacionales:
- **C$21.00/hora** bajo;
- **C$36.00/hora** mediano;
- **C$55.00/hora** alto.

Job Bank indica que normalmente se requiere formación relacionada y algunos empleadores pueden pedir training/certificación de proveedor. Actualmente Job Bank señala registro con un organismo regulatorio en **Saskatchewan** para este NOC; verifique la ocupación exacta y las reglas provinciales vigentes.

## Canadá — alcance usuario/aplicación

Para soporte SaaS/aplicación orientado a usuarios use **NOC 22221**.

Salarios nacionales:
- **C$20.50/hora** bajo;
- **C$31.47/hora** mediano;
- **C$49.00/hora** alto.

Los requisitos típicos incluyen educación/cursos relacionados con computación, programación o administración de redes; algunos empleadores pueden pedir capacitación/certificación de proveedor. El alcance real debe determinar qué NOC es más apropiado.

## Colombia

Para infraestructura/red cloud, **CUOC 35130** es la comparación más fuerte. Cubre operación/troubleshooting de infraestructura y redes, configuración, backups/recovery y documentación.

Para soporte de aplicaciones/usuarios, **CUOC 35121** cubre software, hardware, redes, bases de datos, internet, deployment y soporte.

OCUPACOL advierte que sus indicadores históricos de mercado laboral no son estadísticamente representativos bajo la metodología utilizada. Por eso esta guía no inventa un salario nacional de Cloud Support Specialist a partir de esos rangos.

## Colombia — rutas SENA

### Programación de Aplicaciones y Servicios para la Nube
SENA Betowa identifica actualmente:
- **Técnico**;
- **2,256 horas**;
- formación titulada;
- ofertas virtuales actuales;
- fundamentos de aplicaciones/servicios cloud, bases de datos y tecnología.

Es una ruta sustancial, pero combina orientación de desarrollo y cloud; no es una calificación puramente de soporte.

### Implementación de Servicios de Computación en la Nube
SENA Betowa identifica actualmente:
- formación complementaria virtual;
- **48 horas**;
- conceptos de servicios cloud y competencia de administración de infraestructura tecnológica de red.

Es formación suplementaria y no equivale al Técnico de 2,256 horas. Cohortes, cupos, modalidad y admisión cambian; verifique la oferta viva.

## Aprendizaje con proveedores

Puede investigar Microsoft Learn Azure, AWS Skill Builder y Google Cloud Skills Boost. Parte del contenido puede ser gratuito; exámenes, labs o credenciales pueden tener costo. Verifique precio, disponibilidad regional y relevancia para el empleador antes de pagar.

## Portafolio seguro

Use solo ambientes propios, sandbox, training, open-source o expresamente autorizados. Ejemplos:
- ticket sintético de incidente cloud y escalamiento;
- diagrama de arquitectura de sandbox público;
- revisión IAM de mínimo privilegio de un lab propio;
- diagnóstico DNS/conectividad;
- dashboard con telemetría sintética;
- plan de backup/restore para un lab;
- ejercicio de correlación con provider status;
- IaC simple sin credenciales reales.

Nunca publique cuentas, arquitectura, keys, tokens, logs, vulnerabilidades o runbooks propietarios de empleadores/clientes.

## Plan inicial de cuatro semanas

### Semana 1 — fundamentos
Cuenta/tenant, regiones/zonas, compute, storage, networking, DNS e IAM. Use un lab personal de bajo costo o sandbox y configure alertas de costo si existen.

### Semana 2 — troubleshooting
Practique tickets, service health, logs/métricas, análisis de packet path y pruebas de una hipótesis a la vez.

### Semana 3 — seguridad y recuperación
Practique MFA, mínimo privilegio, secretos, backup/restore, RPO/RTO, audit logs y change/rollback controlado.

### Semana 4 — evidencia y empleo
Construya portafolio seguro, clasifique vacantes por infraestructura vs. soporte de usuario, verifique rutas de formación, practique entrevistas y documente qué puede hacer versus qué debe escalar.

## Preparación para entrevistas

Explique cómo aislaría conectividad cloud; autenticación vs. autorización; mínimo privilegio/MFA; por qué snapshot no prueba recuperabilidad; por qué replicación no es backup automático; provider health vs. configuración del cliente; DNS troubleshooting; verificación de cuenta/región; cuándo escalar un cambio privilegiado; exposición de secretos; y cómo valida consejo generado por IA.

## Preguntas al empleador

- ¿Qué proveedores/servicios se soportan?
- ¿El rol es infraestructura, SaaS/usuario o ambos?
- ¿Qué privilegios de producción tiene?
- ¿Existe on-call?
- ¿Cómo se manejan severidades/incidentes?
- ¿Quién aprueba excepciones IAM/seguridad?
- ¿Quién diseña arquitectura y recovery?
- ¿Qué change/release controls aplican?
- ¿Scripts/IaC requieren revisión?
- ¿Hay apoyo para training/certificaciones?
- ¿Cómo se manejan privacidad, residencia de datos y acceso a clientes?

## Enlaces de verificación para lectores

1. https://www.onetonline.org/link/details/15-1231.00
2. https://www.onetonline.org/link/localwages/15-1231.00
3. https://www.onetonline.org/link/localtrends/15-1231.00
4. https://www.onetonline.org/link/hot_tech/15-1231.00
5. https://www.onetonline.org/link/demand/15-1231.00
6. https://www.careeronestop.org/LocalHelp/EmploymentAndTraining/find-WIOA-training-programs.aspx
7. https://www.apprenticeship.gov/
8. https://www.indeed.com/career/cloud-engineer/salaries
9. https://learn.microsoft.com/en-us/training/azure/
10. https://skillbuilder.aws/
11. https://www.cloudskillsboost.google/
12. https://www.jobbank.gc.ca/marketreport/summary-occupation/24514/ca
13. https://www.jobbank.gc.ca/wagereport/occupation/3757
14. https://www.jobbank.gc.ca/marketreport/summary-occupation/3772/ca
15. https://www.jobbank.gc.ca/marketreport/wages-occupation/3772/ca
16. https://www.canada.ca/en/services/jobs/training.html
17. https://ocupacol.mintrabajo.gov.co/Profile/OccupationalProfile/35130
18. https://ocupacol.mintrabajo.gov.co/Profile/OccupationalProfile/35121
19. https://betowa.sena.edu.co/oferta/programacion-de-aplicaciones-y-servicios-para-la-nube?modality=V&programId=165934
20. https://betowa.sena.edu.co/oferta/implementacion-de-servicios-de-computacion-en-la-nube?modality=V&programId=229523
21. https://www.oitcinterfor.org/statsfp/paises
22. https://aws.amazon.com/compliance/shared-responsibility-model/
23. https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility
24. https://cloud.google.com/architecture/framework/security/shared-responsibility-shared-fate
25. https://www.nist.gov/cyberframework
26. https://www.nist.gov/privacy-framework
27. https://www.nist.gov/itl/ai-risk-management-framework
28. https://www.cisa.gov/secure-our-world
29. https://www.section508.gov/create/
30. https://www.w3.org/TR/WCAG22/

## Límites importantes

Esta guía ofrece información educativa y de planificación profesional. No garantiza empleo, compensación, admisión, financiamiento, apprenticeship, certificación, disponibilidad de servicios cloud o promoción. No constituye certificación legal, de privacidad, ciberseguridad, arquitectura, recovery, proveedor o accesibilidad. Las ediciones lingüísticas son localizaciones controladas del proyecto, no traducciones certificadas.
