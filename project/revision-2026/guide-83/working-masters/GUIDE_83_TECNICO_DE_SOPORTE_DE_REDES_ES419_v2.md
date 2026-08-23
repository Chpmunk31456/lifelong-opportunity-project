# Guía de Oportunidades para Toda la Vida 83 — Técnico de soporte de redes

**Versión:** 2.0 — maestro de trabajo controlado  
**Idioma:** español neutro de América Latina (`es-419`)  
**Referencia principal de EE. UU.:** O*NET-SOC 15-1231.00 — Computer Network Support Specialists  
**Comparación con Canadá:** NOC 22220 — Computer network and web technicians  
**Comparación con Colombia:** CUOC 35130 — Técnicos en redes y tecnologías de la información  
**Fecha de revisión:** 2026-08-21

## Qué es esta carrera

Un técnico de soporte de redes ayuda a mantener las redes de datos disponibles, utilizables, seguras y con capacidad de soporte. El trabajo puede incluir solucionar problemas de conectividad LAN, WAN, inalámbrica, VPN, nube e híbrida; revisar switches, routers, puntos de acceso, firewalls y servicios relacionados; analizar registros y datos de monitoreo; documentar incidentes y cambios; brindar soporte a usuarios; respaldar configuraciones; y escalar fallas o señales de seguridad que excedan la autoridad asignada.

Esta guía utiliza **O*NET-SOC 15-1231.00 — Computer Network Support Specialists** como referencia principal de Estados Unidos. Canadá se compara estrechamente con **NOC 22220 — Computer network and web technicians**. Colombia tiene una correspondencia directa en **CUOC 35130 — Técnicos en redes y tecnologías de la información**.

El soporte de redes no es lo mismo que arquitectura de redes, pruebas de penetración, ingeniería de seguridad ni autoridad administrativa irrestricta. Un técnico puede diagnosticar y corregir muchas fallas, pero el acceso a producción, los cambios de configuración y las acciones de seguridad deben mantenerse dentro de la autorización del empleador y de los procesos de control de cambios.

## Por qué puede ser una buena oportunidad

Las organizaciones siguen dependiendo de conectividad confiable entre oficinas, centros de datos, servicios en la nube, usuarios remotos, redes inalámbricas y sistemas expuestos a internet. Aunque el monitoreo y ciertas configuraciones rutinarias se automaticen, siguen siendo necesarias personas que puedan interpretar síntomas, aislar fallas, comunicar impacto, validar cambios, preservar evidencia y saber cuándo escalar.

La estrategia más sólida a largo plazo no es quedarse únicamente en tareas repetitivas y guionizadas. Conviene avanzar hacia redes más profundas, sistemas, nube, automatización, observabilidad y ciberseguridad.

Una progresión práctica puede ser:

**mesa de ayuda o soporte de campo → técnico de soporte de redes → administrador de redes / administrador de sistemas / soporte de nube → ingeniero de redes, ingeniero de nube, operaciones de seguridad o especialista en infraestructura.**

La progresión real depende de la experiencia, educación, estructura del empleador y jurisdicción.

## Técnico de soporte de redes, administrador de redes e ingeniero de redes no son lo mismo

### Técnico de soporte de redes

Suele enfocarse en:

- incidentes de conectividad de usuarios y sedes;
- estado de dispositivos de red y diagnóstico inicial;
- problemas de cableado, puertos, VLAN, IP, DNS, DHCP y Wi-Fi;
- alertas de monitoreo;
- tareas de configuración autorizadas;
- escalamiento y documentación;
- soporte remoto y coordinación con carriers/proveedores.

### Administrador de redes

Puede tener responsabilidad más amplia sobre:

- administración continua de la red;
- controles de cuentas y acceso;
- respaldo y recuperación;
- servicios de red y servidores;
- parches y ciclo de vida;
- mayor autoridad para cambios.

### Ingeniero o arquitecto de redes

Puede diseñar e implementar arquitecturas más amplias de routing, switching, wireless, nube, WAN, segmentación, resiliencia y seguridad. Estos puestos normalmente requieren mayor profundidad técnica y autoridad de cambio.

### Roles de seguridad

Analistas e ingenieros de seguridad pueden investigar amenazas, ajustar controles, ejecutar pruebas autorizadas o diseñar arquitectura de seguridad. El personal de soporte de redes debe reconocer y escalar indicadores de seguridad, pero no debe realizar escaneos, explotación ni destrucción de evidencia sin autorización.

## Límites de autoridad profesional

El título de soporte de redes **no** autoriza automáticamente a una persona para:

- eludir controles de acceso para solucionar un problema;
- usar la cuenta privilegiada de otra persona;
- desactivar un firewall, control de endpoint, MFA o monitoreo porque parezca inconveniente;
- escanear o sondear sistemas fuera del alcance autorizado;
- realizar pruebas de penetración sin un alcance explícito y aprobado;
- hacer cambios de routing, switching, Wi-Fi, DNS o firewall en producción fuera del proceso aprobado;
- copiar contraseñas, llaves, tokens o configuraciones protegidas en notas públicas o servicios de IA no aprobados;
- borrar registros o evidencia después de una posible intrusión;
- afirmar que un servicio fue restaurado antes de validarlo;
- tomar decisiones de arquitectura, regulatorias o legales fuera de la autoridad asignada;
- afirmar certificaciones o credenciales que realmente no posee.

Cuando un problema requiera privilegios más amplios, investigación de seguridad, autoridad de cambio de emergencia o rediseño de arquitectura, debe escalarse por el proceso aprobado.

## Un modelo disciplinado de solución de problemas

Una buena solución de problemas de red se basa en evidencia. Una secuencia práctica es:

1. definir el usuario, servicio, sede e impacto al negocio;
2. establecer qué cambió y cuándo;
3. verificar si el problema es aislado o generalizado;
4. identificar la ruta esperada y las dependencias;
5. recopilar evidencia antes de cambiar algo;
6. probar primero las hipótesis de menor riesgo;
7. hacer solamente cambios aprobados y reversibles;
8. validar el servicio desde la perspectiva del usuario;
9. registrar lo observado, modificado y confirmado;
10. escalar hallazgos no resueltos o sensibles a seguridad.

Evite ejecutar comandos al azar. Un comando es útil cuando se sabe qué pregunta debe responder.

## Los modelos OSI y TCP/IP como herramientas de diagnóstico

Los modelos son útiles cuando ayudan a aislar una falla.

Una progresión simplificada:

- **física/enlace:** energía, cable, óptica, radio, estado de interfaz, errores;
- **enlace de datos:** aprendizaje MAC, pertenencia a VLAN, trunks, spanning tree;
- **red:** direccionamiento IPv4/IPv6, subred, gateway, routing;
- **transporte:** alcance TCP/UDP y puertos;
- **aplicación/servicio:** DNS, autenticación, web, mensajería, archivos o aplicación de negocio.

No suponga que el problema es “la red” únicamente porque una aplicación no está disponible.

## Direccionamiento IP y subnetting

Un técnico de redes debe comprender:

- direcciones IPv4 y máscaras/prefijos;
- espacio privado versus público;
- gateways predeterminados;
- conceptos de red/broadcast en IPv4;
- notación CIDR;
- conceptos básicos de direcciones y prefijos IPv6;
- direccionamiento estático versus dinámico;
- direcciones duplicadas;
- pools y agotamiento de direcciones;
- cómo un subnetting incorrecto crea problemas de alcance.

El subnetting es especialmente útil al leer tablas de routing, scopes DHCP, ACL y diagramas de red.

## DHCP, DNS y resolución de nombres

### DHCP

DHCP suele proporcionar a los clientes:

- dirección IP;
- información de subred/prefijo;
- gateway predeterminado;
- servidores DNS;
- tiempo de concesión y otras opciones.

El diagnóstico puede incluir estado de concesión, disponibilidad del pool, relay/helper, ubicación en VLAN y opciones recibidas por el cliente.

### DNS

Los problemas de DNS pueden parecer fallas de red. Verifique:

- si el host alcanza al servidor DNS;
- si existe el registro esperado;
- si el cliente usa el resolver correcto;
- si hay información cacheada u obsoleta;
- si el problema afecta a un nombre, una zona o toda la resolución.

No haga cambios de DNS sin confirmar autoridad e impacto aguas abajo.

## Switching, VLAN y trunks

Conceptos útiles incluyen:

- puertos de acceso;
- pertenencia a VLAN;
- enlaces trunk;
- tráfico etiquetado/no etiquetado;
- tablas MAC;
- prevención de bucles y spanning tree;
- errores de puerto y negociación;
- agregación de enlaces;
- administración y respaldo de configuraciones de switches.

Un error común es cambiar un puerto o VLAN antes de confirmar el diseño previsto. Primero verifique documentación, dispositivo, interfaz e identidad del endpoint.

## Routing y gateways

Conceptos útiles incluyen:

- redes directamente conectadas;
- rutas estáticas;
- ruta predeterminada;
- tablas de routing;
- siguiente salto;
- conceptos de preferencia administrativa/métricas;
- conocimiento general de routing dinámico;
- asimetría de rutas;
- conceptos de NAT.

Los datos de ofertas de empleo de O*NET identifican específicamente **Border Gateway Protocol (BGP)** entre las señales tecnológicas actuales. Un técnico inicial no necesita diseñar BGP a escala de internet, pero debe comprender que los cambios de routing dinámico requieren autorización y validación cuidadosas.

## Redes inalámbricas

El soporte Wi-Fi puede involucrar:

- SSID y autenticación;
- conectividad del punto de acceso;
- intensidad de señal e interferencia;
- compatibilidad del cliente;
- canales y congestión;
- roaming;
- segmentación de invitados versus red interna;
- portales cautivos;
- autenticación empresarial;
- configuraciones de seguridad aprobadas.

No debilite cifrado o autenticación inalámbrica solamente para lograr que un dispositivo se conecte.

## VPN y conectividad remota

Los problemas de acceso remoto pueden relacionarse con:

- conectividad a internet;
- DNS;
- identidad/MFA;
- configuración del cliente;
- certificados o credenciales;
- política de split tunnel/full tunnel;
- rutas;
- postura del endpoint;
- política de firewall;
- licenciamiento/capacidad;
- caída del servicio.

Respete la privacidad durante sesiones remotas. Explique qué hará, use herramientas aprobadas, limite el acceso a la tarea y cierre la sesión al terminar.

## Rendimiento y disponibilidad

Métricas útiles incluyen:

- latencia;
- pérdida de paquetes;
- jitter;
- throughput;
- utilización de ancho de banda;
- errores/discards de interfaz;
- retransmisiones;
- disponibilidad y duración de interrupciones.

Una aplicación lenta puede deberse a red, servidor, cliente, almacenamiento, autenticación, DNS, código de aplicación o una dependencia externa. Correlacione evidencia antes de asignar causa.

## Monitoreo, registros y observabilidad

El soporte puede utilizar:

- monitoreo de interfaces/dispositivos;
- syslog y registros de eventos;
- SNMP u otra telemetría;
- datos de flujo;
- capturas de paquetes cuando estén autorizadas;
- dashboards de rendimiento;
- alertas;
- sistemas de historial/configuración;
- correlación de tickets/eventos.

Preserve el contexto temporal y la identidad de la fuente. Si se sospecha un incidente de seguridad, siga los procedimientos de preservación y escalamiento en vez de borrar o “limpiar” registros.

## Redes de nube e híbridas

El soporte moderno toca cada vez más:

- conceptos de redes virtuales/VPC/VNet;
- subredes y tablas de rutas;
- grupos de seguridad/reglas de firewall;
- VPN y conectividad dedicada;
- balanceadores;
- DNS;
- identidad y acceso;
- monitoreo de nube;
- conectividad híbrida entre nube y redes locales.

Las ofertas actuales en O*NET incluyen Microsoft Azure como señal tecnológica. Aprenda conceptos transferibles de redes en nube en lugar de asumir que un solo proveedor es universal.

## Control de configuración, respaldo y recuperación

Antes de un cambio autorizado en producción, conozca:

- qué se cambiará;
- por qué;
- quién lo aprobó;
- dependencias;
- pasos de validación;
- método de rollback;
- ventana de mantenimiento si aplica;
- cómo se registrará la configuración/evidencia.

Mantenga los respaldos requeridos y siga reglas de retención/seguridad. Un respaldo con credenciales o topología sensible debe protegerse adecuadamente.

## Gestión de cambios

Un buen registro de cambio incluye:

- cambio solicitado;
- dispositivos/servicios afectados;
- riesgo e impacto;
- aprobación;
- plan de implementación;
- plan de prueba/validación;
- plan de rollback;
- resultado real;
- vínculo al incidente/problema si aplica.

Los cambios de emergencia pueden usar un proceso más rápido, pero “emergencia” no significa sin documentación o autoridad ilimitada.

## Calidad de tickets y documentación

Un buen ticket debe permitir reproducir el trabajo. Registre:

- quién/qué está afectado;
- ubicación/sede;
- identificadores de dispositivos/servicios;
- síntomas y horas;
- impacto al negocio;
- diagnósticos ejecutados;
- evidencia/resultados;
- cambios realizados;
- validación;
- escalamiento/próxima acción.

Evite cierres vagos como “red arreglada”. Explique qué estaba mal y qué confirmó la restauración.

## Ciberseguridad en soporte de redes

O*NET incluye explícitamente configurar ajustes/permisos de seguridad y analizar brechas o intentos de brecha entre las tareas de la ocupación.

Buenos hábitos de seguridad incluyen:

- mínimo privilegio;
- cuentas nominativas;
- MFA cuando corresponda;
- manejo seguro de credenciales;
- cambios autorizados;
- procesos de parcheo/actualización;
- conciencia sobre phishing e ingeniería social;
- soporte remoto seguro;
- protección de diagramas/configuraciones;
- escalamiento de tráfico o acceso sospechoso;
- preservación de registros/evidencia.

Un técnico no debe declarar de forma independiente que un incidente está contenido ni realizar pruebas ofensivas salvo que ese rol y alcance estén formalmente asignados.

El material Secure Our World de CISA es útil para conciencia básica. Las políticas del empleador y los procedimientos autorizados de incidentes siguen siendo determinantes.

## IA y automatización responsables

La IA y automatización pueden ayudar con:

- resumir registros;
- redactar tickets/runbooks;
- explicar protocolos;
- generar ejemplos de laboratorio;
- proponer hipótesis de diagnóstico;
- formatear datos repetitivos;
- crear ejemplos de configuración no productivos.

Controles:

- use únicamente sistemas y clases de datos aprobados;
- nunca coloque credenciales, tokens, llaves o configuraciones protegidas en servicios públicos de IA no aprobados;
- verifique cada comando/configuración antes de usarlo;
- conserve trazabilidad de fuentes/registros;
- pruebe apropiadamente antes de producción;
- no permita cambios autónomos de producción sin autoridad aprobada;
- compare conclusiones de IA con evidencia observada;
- escale recomendaciones inseguras o inexplicables.

El AI Risk Management Framework de NIST y su Generative AI Profile son orientación voluntaria para gestión de riesgos. No sustituyen la gobernanza del empleador sobre redes, seguridad o cambios.

## Accesibilidad y soporte inclusivo

Los procesos de soporte deben ser utilizables por personas con discapacidad. Buenas prácticas incluyen:

- herramientas accesibles por teclado cuando sea posible;
- encabezados legibles y runbooks estructurados;
- etiquetas significativas;
- contraste suficiente;
- indicadores que no dependan solamente del color;
- alternativas de texto para diagramas/capturas cuando corresponda;
- alternativas de comunicación si el soporte solo por voz no es adecuado;
- documentos electrónicos accesibles.

Las verificaciones automáticas de accesibilidad no constituyen certificación legal completa.

## Perfil actual de preparación en Estados Unidos

O*NET ubica **15-1231.00** en **Job Zone Four — Considerable Preparation Needed**. Indica que muchas ocupaciones de esta zona requieren un título universitario de cuatro años, aunque algunas no, y que puede ser necesaria experiencia considerable y formación vocacional o en el trabajo.

Esto no significa que cada puesto de técnico de soporte de redes requiera licenciatura. Los empleadores varían. Las vías relevantes pueden incluir:

- experiencia en soporte de TI más práctica en redes;
- community college o educación técnica;
- programas de administración de redes;
- certificaciones cuando los empleadores las valoren;
- evidencia de laboratorio/portafolio;
- aprendizajes relacionados;
- formación técnica militar o del empleador.

O*NET enumera como títulos de aprendizaje aprobados **Cloud Support Specialist** y **Junior Cloud Engineer (Nof)**. Un título aprobado no garantiza una vacante local.

## Salarios y perspectiva en Estados Unidos

Datos nacionales BLS 2025 mostrados por O*NET para 15-1231.00:

| Percentil | Anual | Por hora |
|---|---:|---:|
| 10 | $47,120 | $22.65 |
| 25 | $58,240 | $28.00 |
| Mediana | $76,220 | $36.64 |
| 75 | $98,750 | $47.48 |
| 90 | $127,780 | $61.43 |

Proyecciones 2024–2034:

- empleo 2024: **152,700**;
- empleo proyectado 2034: **155,500**;
- crecimiento proyectado: **2%**, más lento que el promedio;
- **9,600 vacantes proyectadas por año**.

Las vacantes anuales incluyen crecimiento y reemplazos y no garantizan oportunidades para una persona específica.

### Contexto actual no gubernamental de título relacionado

Indeed informó un salario base promedio de **$26.30 por hora** para **Network Technician** en Estados Unidos, con rango mostrado de **$17.46–$39.60 por hora**, basado en aproximadamente **2.1k salarios** de publicaciones de los 36 meses anteriores, actualizado el **3 de agosto de 2026**.

Es una estimación no gubernamental para un título relacionado que puede representar una población más amplia o junior que O*NET-SOC 15-1231.00. No la sustituya por la serie oficial BLS/O*NET.

## Señales actuales de tecnologías en ofertas de EE. UU.

O*NET Hot Technologies, basado en publicaciones estadounidenses de 2025, incluye:

- Microsoft Office **13%**;
- Microsoft Active Directory **13%**;
- ServiceNow **9%**;
- Linux **7%**;
- Apple macOS **6%**;
- Microsoft Windows Server **6%**;
- Microsoft Outlook **6%**;
- Microsoft Excel **6%**;
- Microsoft Windows **5%**;
- BGP **3%**;
- Microsoft Azure **3%**;
- PowerShell **2%**;
- SQL **1%**;
- Python **1%**;
- Splunk Enterprise **1%**.

Estas son señales de mercado, no una lista obligatoria para todos los empleos.

## Ruta en Canadá

Canada Job Bank identifica **NOC 22220 — Computer network and web technicians**. Los técnicos de redes establecen, operan, mantienen y coordinan LAN/WAN y hardware/software relacionado, y monitorean conectividad y rendimiento.

Los requisitos actuales indican normalmente:

- completar un programa de college u otro programa en informática, administración de redes, tecnología web o campo relacionado;
- algunos empleadores pueden requerir formación/certificación del proveedor de software;
- **se requiere registro ante un organismo regulador en Saskatchewan**.

No describa la ocupación como uniformemente no regulada en todo Canadá.

Salarios nacionales actuales, actualizados el 19 de noviembre de 2025:

- bajo: **C$21.00/hora**;
- mediana: **C$36.00/hora**;
- alto: **C$55.00/hora**.

Las perspectivas cambian por provincia/territorio. Use la vista regional actual de Job Bank para la ubicación considerada.

## Ruta en Colombia

### CUOC 35130 — Técnicos en redes y tecnologías de la información

Es una correspondencia ocupacional directa. Entre los títulos relevantes se incluyen:

- Técnico de apoyo de red;
- Técnico de redes y sistemas informáticos;
- Técnico de sistemas en red;
- Técnico de soporte de red informática;
- Técnico en mantenimiento de red informática;
- Técnico en redes de computadores;
- Técnico especialista en infraestructura tecnológica.

Las funciones oficiales incluyen implementar/operar/solucionar problemas de redes de datos, instalar software de red y sistemas operativos, respaldar/recuperar, configurar dispositivos de interconexión, ejecutar diagnósticos de seguridad, monitorear centros de datos, mantener infraestructura, atender usuarios y documentar.

OCUPACOL muestra información salarial histórica/derivada, pero advierte expresamente que los datos carecen de representatividad estadística. Por ello esta guía **no** usa ese rango como referencia nacional actual representativa para Colombia.

### SENA — Instalación de redes de computadores

SENA Betowa actualmente muestra **Instalación de redes de computadores** como:

- **Técnico**;
- **2,208 horas**;
- formación titulada;
- competencias que incluyen implementación de redes físicas de datos y redes inalámbricas locales.

Las cohortes, sedes y fechas de inscripción cambian. Verifique disponibilidad actual antes de planificar una admisión específica.

### SENA — Gestión de redes de datos

SENA Betowa también muestra **Gestión de redes de datos** como:

- **Tecnólogo**;
- **3,984 horas**;
- formación titulada;
- cableado estructurado, centros de datos, redes alámbricas/inalámbricas y seguridad de redes entre sus temas.

Esta ruta más profunda puede apoyar el crecimiento profesional, pero no es obligatoria para todos los puestos iniciales de soporte de redes.

## Ruta más amplia en América Latina

Los sistemas de formación varían por país. Los recursos por país de OIT/Cinterfor pueden ayudar a localizar instituciones nacionales de formación profesional. Verifique directamente con el proveedor el estado actual, admisión, modalidad, costo y reconocimiento de credenciales.

## Estrategia de aprendizaje gratuita o de bajo costo primero

Antes de pagar una formación costosa:

1. aprenda fundamentos de redes con materiales confiables gratuitos o económicos;
2. construya un laboratorio aislado o use ambientes de nube/lab autorizados;
3. practique direccionamiento, VLAN, routing, DNS, DHCP, Wi-Fi y troubleshooting;
4. documente incidentes y cambios como si trabajara en producción;
5. aprenda conceptualmente un flujo de ticketing/monitoreo;
6. luego decida si una certificación de proveedor o programa formal coincide con los empleadores objetivo.

Para lectores en EE. UU., los localizadores WIOA y de formación de CareerOneStop pueden ayudar a encontrar opciones elegibles. La elegibilidad y financiación se determinan localmente y no están garantizadas.

## Proyectos éticos de portafolio

Use solamente dispositivos, redes, tenants y datos propios o para los que tenga autorización explícita.

Ideas:

- laboratorio pequeño de routing/VLAN con diagrama y plan de direccionamiento;
- caso de troubleshooting DNS/DHCP;
- escenario de aislamiento de una falla inalámbrica;
- diseño simulado de conectividad sucursal-nube;
- dashboard de monitoreo con datos sintéticos;
- ejercicio de backup y rollback de configuración;
- ticket de incidente con evidencia, hipótesis, cambio y validación;
- runbook de red accesible;
- script de automatización que procese logs sintéticos sin cambiar producción.

Nunca escanee sistemas públicos o redes de terceros para crear evidencia de portafolio.

## Evidencia para el currículum

Los buenos bullets describen resultados y alcance, por ejemplo:

- redujo incidentes repetidos mejorando documentación de causa raíz;
- restauró conectividad de una sede tras aislar una falla de VLAN, DHCP o routing;
- mantuvo respaldos de configuración y validó procedimientos de rollback;
- soportó routers, switches, Wi-Fi y VPN bajo control de cambios;
- mejoró la calidad de alertas/tickets mediante mejor evidencia de monitoreo.

Use solo hechos que pueda respaldar. No invente experiencia con productos, métricas de disponibilidad, certificaciones o autoridad de seguridad.

## Preparación para entrevistas

Prepárese para explicar:

- cómo diagnosticaría cuando un usuario no puede conectarse;
- cómo cambia el enfoque si una sede completa está caída;
- diferencia entre DNS y DHCP;
- función de un gateway predeterminado;
- qué es una VLAN;
- cómo investigaría latencia alta o pérdida de paquetes;
- por qué importan control de cambios y rollback;
- qué haría ante evidencia de compromiso;
- cómo protege credenciales en soporte remoto;
- cómo documenta un incidente resuelto.

Una buena respuesta explica razonamiento, límites de seguridad y validación, no solamente comandos.

## Preguntas para un empleador

Pregunte sobre:

- tamaño de la red y tecnologías principales;
- turnos/on-call;
- trabajo de campo versus remoto;
- autoridad y aprobación de cambios;
- herramientas de monitoreo/ticketing;
- escalamiento de incidentes;
- estándares de documentación;
- apoyo para formación/certificaciones;
- progresión hacia administración/ingeniería/nube/seguridad;
- requisitos físicos y viajes;
- proceso de accesibilidad/adaptaciones.

## Primeros 30 días en un puesto nuevo

Prioridades:

1. aprender topología, sedes y servicios críticos;
2. aprender severidad de tickets y reglas de escalamiento;
3. conocer límites de acceso autorizado;
4. comprender procedimientos de backup/cambio/rollback;
5. aprender fuentes de monitoreo y logs;
6. revisar incidentes comunes y errores conocidos;
7. comprender contactos de carrier/proveedor;
8. verificar procedimientos de seguridad e incidentes;
9. mejorar documentación mientras aprende;
10. no hacer cambios productivos indocumentados para “demostrar” capacidad.

## Plan de progreso de 90 días

Busque poder:

- solucionar sistemáticamente problemas comunes de conectividad;
- explicar dependencias principales de la red;
- ejecutar cambios asignados con seguridad;
- distinguir si una falla es de red, aplicación, endpoint o servicio;
- usar evidencia de monitoreo/logs eficazmente;
- mantener runbooks útiles;
- escalar correctamente problemas de seguridad;
- identificar el siguiente camino: administración de redes, nube, sistemas, automatización o seguridad.

## Lista previa a postularse

Antes de postularse ampliamente, confirme que puede conversar sobre:

- IPv4/subred/gateway;
- DNS y DHCP;
- VLAN/switching;
- routing;
- troubleshooting cableado e inalámbrico;
- VPN/conectividad remota;
- monitoreo/logs;
- cambio/rollback;
- documentación de tickets;
- mínimo privilegio y escalamiento de seguridad;
- límites de IA responsable.

## Preguntas antes de comprar formación

Pregunte al proveedor:

- ¿Para qué ocupaciones/títulos está diseñado el programa?
- ¿Qué laboratorios prácticos de redes incluye?
- ¿Cubre routing, switching, Wi-Fi y redes de nube actuales?
- ¿Qué equipos/software están incluidos?
- ¿El examen de certificación está incluido o cuesta aparte?
- ¿Cuál es el costo total con tarifas/materiales?
- ¿Los resultados son verificables de forma independiente?
- ¿Existe financiación y cuáles son las reglas de elegibilidad?
- ¿Qué adaptaciones de accesibilidad ofrece?
- ¿La credencial es reconocida por los empleadores objetivo?

No dependa de promesas de empleo o ingresos garantizados.

## Fuentes controladas

1. https://www.onetonline.org/link/details/15-1231.00
2. https://www.onetonline.org/link/summary/15-1231.00
3. https://www.onetonline.org/link/localwages/15-1231.00
4. https://www.onetonline.org/link/localtrends/15-1231.00
5. https://www.onetonline.org/link/hot_tech/15-1231.00
6. https://www.onetonline.org/link/demand/15-1231.00
7. https://www.careeronestop.org/LocalHelp/EmploymentAndTraining/find-WIOA-training-programs.aspx
8. https://www.careeronestop.org/FindTraining/find-training.aspx
9. https://www.indeed.com/career/network-technician/salaries
10. https://www.jobbank.gc.ca/marketreport/summary-occupation/24514/ca
11. https://www.jobbank.gc.ca/marketreport/requirements/24514/ca
12. https://www.jobbank.gc.ca/wagereport/occupation/24514
13. https://www.canada.ca/en/services/jobs/training.html
14. https://ocupacol.mintrabajo.gov.co/Profile/OccupationalProfile/35130
15. https://betowa.sena.edu.co/oferta/instalacion-de-redes-de-computadores?level=2&location=57008001&modality=P&programId=132975
16. https://betowa.sena.edu.co/oferta/gestion-de-redes-de-datos?level=6&modality=V&programId=107412
17. https://www.oitcinterfor.org/statsfp/paises
18. https://www.cisa.gov/secure-our-world
19. https://www.nist.gov/cyberframework
20. https://www.nist.gov/itl/ai-risk-management-framework
21. https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
22. https://www.section508.gov/create/

## Aviso de alcance y no garantía

Esta guía ofrece información educativa y de planificación profesional. No garantiza empleo, ingresos, admisión, financiación, certificación, licencia, promoción ni ningún otro resultado. Los requisitos, remuneración y oportunidades cambian según jurisdicción, empleador y tiempo.

No proporciona asesoría legal, autorización de ciberseguridad, autorización para pruebas de penetración, aprobación de arquitectura ni certificación de accesibilidad. Siga la ley aplicable, las políticas del empleador, los procesos de cambio y la autoridad asignada.

Creada y dirigida por **Alberto “Al” Leiva**. ChatGPT apoyó la investigación, organización, edición, apoyo de traducción y preparación de documentos bajo la dirección del autor. El autor conserva la responsabilidad por las decisiones editoriales y de publicación.

Salvo que un archivo indique lo contrario, estos materiales se ofrecen bajo licencia **CC BY-NC-SA 4.0**.
