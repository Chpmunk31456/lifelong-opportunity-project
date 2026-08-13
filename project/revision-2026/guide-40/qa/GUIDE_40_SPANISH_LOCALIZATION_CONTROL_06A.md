# Guide 40 — Spanish Localization Control Sheet

**Locale:** es-419  
**Date:** 2026-08-13  
**Purpose:** Pre-localization control record; this file does **not** mark the Spanish Localization gate PASS.

## Authoritative source

- Frozen English master: `project/revision-2026/guide-40/working-masters/GUIDE_40_CONSTRUCTION_LABORER_AND_TRADE_HELPER_ENGLISH_v2.md`
- Research evidence: `project/revision-2026/guide-40/research/GUIDE_40_CURRENT_SOURCE_EVIDENCE_02.md`
- Helper manifest: `project/revision-2026/guide-40/GUIDE_40_HELPER_STATUS.json`

## Required occupation and safety boundaries

The es-419 edition must preserve the general construction laborer/trade-helper scope and must not imply that helper experience independently qualifies a learner for a regulated skilled trade, heavy-equipment operation, hazardous-material removal, blasting, specialized scaffolding/rigging, electrical/plumbing practice, or another separately controlled occupation.

OSHA 10-hour and 30-hour Construction Outreach must remain described as voluntary awareness training, not a certification or license and not a substitute for standard-specific, task-specific, site-specific, employer-required, or qualified-person training.

Work-at-height training in Colombia must remain a separate high-risk training area; no general construction course may be represented as automatically satisfying current employer, site, or Colombian requirements.

## Numeric and classification parity — do not drift

### United States

- BLS combined Construction Laborers and Helpers May 2024 median: **$46,050/year; $22.14/hour**.
- Construction Laborers May 2024 median: **$46,730/year**.
- Helpers, Construction Trades May 2024 median: **$40,430/year**.
- Combined employment: **1,649,100 jobs in 2024**.
- Projected growth: **7% from 2024–2034**.
- Projected openings: about **149,400 per year**.
- O*NET occupation anchor: **47-2061.00 — Construction Laborers**.
- O*NET current wage view using BLS 2025 data: about **$47,120/year; $22.66/hour**.
- Private Salary.com estimate, clearly separated: about **$43,578/year; $21/hour**, July 1, 2026; stated 25th–75th percentile range **$40,504–$49,004**.

### Canada

- NOC **75110 — Construction trades helpers and labourers**.
- National wage values: **CAD $18.25/hour low; CAD $25.00/hour median; CAD $40.00/hour high**.
- Wage page update date: **November 19, 2025**; reference period **2023–2024**.
- Construction Craft Worker / Red Seal is a possible progression route, not a universal requirement for every NOC 75110 helper job.
- Canada Apprentice Loan: up to **CAD $4,000** in interest-free loans for eligible apprentices; eligibility and designated-trade conditions remain conditional.

### Colombia

- SENA is a free-first public training source; cohort, location, and admissions vary.
- Occupation-adjacent example: **Mampostería**, operator level, in-person, approximately **1,296 hours**.
- Program existence does not guarantee a live seat.
- SENA Agencia Pública de Empleo is a free public employment locator and does not guarantee selection.

## Funding and work-based-learning terminology

Use neutral Latin American Spanish. Distinguish clearly among capacitación gratuita, apoyo condicionado, préstamo, reembolso de matrícula, aprendizaje remunerado, formación en el trabajo, empleo, and employer/union support. Do not translate conditional funding or directory presence into guaranteed financing, placement, or admission.

Suggested terminology:

- construction laborer: `obrero de construcción` / `trabajador de construcción`, according to sentence context;
- trade helper: `ayudante de oficio` or `ayudante de oficio de construcción`;
- skilled trade: `oficio especializado`;
- worksite/jobsite: `sitio de trabajo` / `obra`;
- PPE: `equipo de protección personal (EPP)`;
- apprenticeship: retain official program names such as `Registered Apprenticeship`, otherwise use `aprendizaje` with context;
- on-the-job training: `capacitación en el trabajo`;
- work-based learning: `formación basada en el trabajo`;
- Red Seal and Construction Craft Worker: retain official English names where needed for source fidelity.

## Required source-URL parity

The completed Spanish master must carry the same controlled source inventory as the frozen English master, including the BLS/O*NET/OSHA, Apprenticeship.gov, CareerOneStop, Statistics Canada/Job Bank/Red Seal/Canada funding, SENA/Betowa/APE, OIT/Cinterfor, and Salary.com URLs. URLs must remain byte-for-byte unchanged during localization; exact URL parity is rechecked later in Trilingual Technical QA.

## Accessibility, AI, privacy, and anti-scam controls

The Spanish edition must preserve the English boundaries that:

- physical demands differ by actual job and do not justify blanket disability exclusion;
- the guide does not make medical or legal determinations;
- AI may assist low-risk learning and administration but must not replace site procedures, manufacturer instructions, drawings/specifications, safety controls, required professional decisions, or qualified supervision;
- protected project, credential, access-control, incident, customer, contractor, drawing, or security information must not be uploaded to unapproved public AI systems; and
- training/job guarantees, generic certificates presented as universal authorization, payment for job offers, hidden tool/PPE costs, and unclear refund/financing terms are warning signs.

## Release condition for Spanish Localization gate

Do not mark `spanish_localization` PASS until all of the following exist and are reviewed:

1. complete neutral es-419 Version 2 master derived only from the frozen English master;
2. occupation/safety/funding/income boundaries preserved;
3. numeric values, dates, classifications, and official program names reconciled;
4. source URLs preserved;
5. UTF-8 accents/punctuation checked;
6. no unsupported claim of independent human certification, accreditation, certified translation, legal review, financial advice, or guaranteed employment introduced; and
7. dedicated Spanish Localization QA evidence records the PASS.

**Current disposition:** Spanish Localization remains **PENDING**. This control sheet is an auditable preparation artifact only.
