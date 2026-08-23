# Guide 01 — es-419 Revision Control Ledger

## Controlled status

- Target edition: neutral Latin American Spanish (`es-419`), version 1.1.
- Approved source of truth: `Lifelong_Opportunity_Community_Health_Worker_Guide_English_v1.1_INTEGRATED_MASTER.md`.
- English source QA status: PASS.
- English source SHA-256: `fe62c4189b1557554453d4f707b553bd768a342e62b531bad84d7fc00dab2202`.
- Legacy Spanish source: `Lifelong_Opportunity_Community_Health_Worker_Guide_es-419_v1.0_EXTRACTED_BASELINE.md`.
- The legacy Spanish file is a translation baseline only. It is not approved as the v1.1 publication master.
- No independent human certification, professional translation certification, accreditation review, accessibility certification, legal review, or medical review has been obtained or claimed.

## Revision objective

Create a complete, natural, region-neutral Spanish edition that preserves the English v1.1 meaning, warnings, evidence boundaries, section order, links, versioning, and distinction between official statistics and commercial market estimates.

## Blocking structural differences to correct

The legacy Spanish baseline uses an obsolete 15-section structure and a DOCX-derived table of contents. The approved English v1.1 master uses the following controlled structure, which the Spanish v1.1 edition must mirror:

1. Cómo usar esta guía
2. En qué consiste el trabajo
3. Funciones, herramientas y ciclos de trabajo
4. Ajuste profesional, condiciones y seguridad
5. Ética, límites y escalamiento
6. Salario, beneficios y perspectivas
7. Educación y credenciales
8. Aprendizaje respaldado por el empleador
9. Accesibilidad e inclusión
10. Privacidad, ciberseguridad e IA ética
11. Construir evidencia de capacidad
12. Preparación para entrevistas
13. Primeros 30, 60 y 90 días
14. Avance, portabilidad y planificación de salida
15. Antes de inscribirse o firmar
16. Plan de acción de doce semanas
17. Hojas de trabajo
18. Fuentes, fechas y mantenimiento

Required structural actions:

- Remove the static page-number table of contents inherited from the DOCX extraction.
- Add the missing sections on how to use the guide, first 30/60/90 days, explicit source dates, and maintenance.
- Preserve genuine ordered sequences as numbered lists and use bullets for non-sequential comparisons.
- Preserve all tables semantically, including header rows and readable column labels.
- Use UTF-8 without a byte-order mark and LF line endings.

## Required factual integrations

### United States

The Spanish v1.1 edition must accurately preserve:

- BLS median pay of USD 51,030 per year and USD 24.54 per hour for May 2024.
- BLS projection of 11% growth from 2024 through 2034.
- Approximately 7,800 openings per year on average.
- The statement that these are national occupational statistics, not a promise of local pay, hours, benefits, hiring, or job availability.
- The distinction between common entry practice and state-specific certification requirements.

### Commercial U.S. estimates

The Spanish v1.1 edition must label Indeed and Glassdoor figures as supplementary commercial market signals, not official statistics. It must preserve the displayed observation dates, sample or methodology limitations, title-matching risk, geography limits, and warning to verify current local postings and written offers.

### Canada

The Spanish v1.1 edition must preserve:

- The mapping to the broader Social and community service workers, NOC 42201 classification.
- The warning that the Canadian classification is not identical to the U.S. BLS occupation.
- Job Bank national wages of CAD 19.00 low, CAD 26.00 median, and CAD 36.06 high per hour, updated November 19, 2025.
- The reported 83.6% non-wage-benefit figure.
- The separate, clearly labelled Glassdoor Canada estimate and its methodology limitations.

### Colombia

The Spanish v1.1 edition must preserve:

- SENA Betowa as a current catalogue search path for `Promotor de salud` training.
- The warning that availability is location- and cohort-specific.
- The April 24, 2026 Antioquia and July 15, 2026 Casanare examples as evidence of active public initiatives, not permanent nationwide availability, automatic hiring, professional licensure, or fixed pay.
- Agencia Pública de Empleo SENA, territorial health secretariats, authorized training providers, and Ministry of Education programme-status verification.

### Latin America

The Spanish v1.1 edition must state that `trabajador comunitario de salud`, `promotora o promotor de salud`, `agente comunitario de salud`, `auxiliar promotor de salud`, `navegador de pacientes`, and broader social-service classifications are not automatically equivalent. It must require country-specific verification of legal scope, training, compensation model, employment status, and employer requirements.

## Funding and learning pathways

The translation must preserve the free-first order of preference:

- employer-paid onboarding and supervised training;
- public libraries and adult education;
- public community or technical colleges;
- official workforce services;
- recognized nonprofit or public-health programmes;
- registered apprenticeship or other paid work-based learning where available; and
- SENA or other authorized public training in Colombia.

It must not imply that a scholarship, apprenticeship, public programme, tuition benefit, or employer reimbursement is guaranteed or universally available.

## Controlled terminology

Use the following preferred terms consistently unless local legal context requires a more specific title:

| English source term | Preferred es-419 term | Control note |
|---|---|---|
| Community Health Worker | trabajador/a comunitario/a de salud | Use as the generic occupation; retain local official titles where cited. |
| promotora/promotor de salud | promotora o promotor de salud | Avoid slash-heavy prose in running text. |
| patient navigator | navegador/a de pacientes | Explain that title and scope vary. |
| outreach | alcance comunitario | Use `actividades de alcance comunitario` where natural. |
| referral | remisión / derivación | Prefer `remisión` for Colombia-facing text; avoid false equivalence across countries. |
| scope of practice | alcance autorizado de la función | Do not imply a licensed clinical scope unless applicable. |
| escalation | escalamiento | Use consistently for reporting matters beyond authority. |
| registered apprenticeship | programa de aprendizaje registrado | Retain U.S.-specific context. |
| work-based learning | aprendizaje basado en el trabajo | Do not translate as ordinary unpaid practice by default. |
| employer-supported learning | aprendizaje respaldado por el empleador | Distinguish reimbursement, direct payment, scholarship, and forgivable loan. |
| non-wage benefits | beneficios no salariales | Preserve percentage context and source. |
| commercial estimate | estimación comercial | Always label separately from official data. |
| accessibility accommodation | adaptación de accesibilidad | Use `ajuste razonable` only when the legal context specifically supports it. |
| background check | verificación de antecedentes | Do not imply universal legal requirements. |
| credential | credencial | Distinguish certificate, certification, licence, diploma, and degree. |

## Language and readability controls

- Use neutral Latin American Spanish, not Spain-specific administrative or educational terminology unless a cited source requires it.
- Prefer direct sentences, active voice, plain language, and respectful gender-inclusive wording that remains readable.
- Avoid literal English calques where a natural Spanish expression exists.
- Do not translate `college` automatically as `universidad`; use the institution type supported by context.
- Do not translate `license` and `certification` as interchangeable concepts.
- Preserve cautious verbs such as `puede`, `suele`, `varía`, `verifique`, and `no garantiza`.
- Keep monetary currencies explicit as USD or CAD and preserve dates attached to statistics.
- Do not localize or modify URLs.

## Required QA gates before approval

The Spanish v1.1 master cannot advance to publication generation until all of the following pass:

- full section and heading parity with the English v1.1 master;
- factual-claim and date parity;
- official-versus-commercial income-label parity;
- Colombia and Latin America scope-warning parity;
- funding, scholarship, apprenticeship, and employer-support caveat parity;
- controlled-terminology review;
- link destination and link-count review;
- UTF-8, line-ending, whitespace, and replacement-character checks;
- spelling, grammar, punctuation, natural-readability, and non-literal-translation review;
- version, author, AI-assistance, limitation, and maintenance metadata review;
- explicit confirmation that no independent certification or accreditation is claimed.

## Next controlled action

Produce `Lifelong_Opportunity_Community_Health_Worker_Guide_es-419_v1.1_INTEGRATED_MASTER.md` from the approved English master, using the legacy Spanish baseline only as reusable language where it remains accurate, complete, natural, and structurally aligned.