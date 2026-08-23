# Guide 27 - Portuguese localization QA 07

**Guide:** 27 - Diesel Service Technician and Mechanic

**Locale:** Brazilian Portuguese (`pt-BR`)

**Date:** 2026-08-11

**Stage:** Portuguese Localization Helper

**Status:** **PASS**

## Controlled inputs

Frozen English source:

`project/revision-2026/guide-27/publication-candidate/GUIDE_27_ENGLISH_v2.md`

Frozen English Git blob SHA:

`24d4a54a291313c0dac9197b806b7cf56ce77995`

Brazilian Portuguese controlled master:

`project/revision-2026/guide-27/publication-candidate/GUIDE_27_PORTUGUESE_BR_v2.md`

Portuguese Git blob SHA:

`a8e1b08a349d91fd726e14615d2b6e4e1446eab0`

Portuguese master commit:

`f10d5f5a4c2b9e88a6aa76df582e7d874a5b2663`

## Preconditions

- Baseline inventory: **PASS**
- Research Helper: **PASS**
- English Editorial Helper: **PASS**
- Evidence / Traceability Helper: **PASS**
- English Source Freeze: **PASS**
- Spanish Localization Helper: **PASS**
- Active blockers: none

## Structural parity

The Brazilian Portuguese master preserves the frozen English guide's complete 18-section structure, including safety subsections, U.S. evidence/funding sections, Canada pathways, Colombia pathways, Latin America locator framework, 30/60/90-day plan, ethical portfolio guidance, advancement, ethical AI/privacy/cybersecurity, accessibility, decision questions, source links, and final decision rule.

No English source section was intentionally omitted or converted into a claim of guaranteed funding, licensing, employment, earnings, accreditation, or certification.

## Numeric and jurisdiction parity

Material figures and jurisdiction boundaries were checked against the frozen English master and preserved without invented conversion or normalization:

- U.S. 2024 employment: approximately **319,900**.
- BLS May 2024 median: **US$60,640/year / US$29.15/hour**.
- BLS lower 10%: below **US$41,670**.
- BLS upper 10%: above **US$85,980**.
- 2024-2034 projected change: **2%**, approximately **7,800** jobs.
- Projected annual openings: approximately **26,500**.
- Indeed supplemental estimate: approximately **US$30.32/hour**, about **37,900** observations, updated **July 20, 2026**.
- ZipRecruiter supplemental cross-check: approximately **US$58,798/year / US$28.27/hour**, dated **July 29, 2026**.
- IRS Section 127 limit: up to **US$5,250 per employee per year** for qualifying employer educational assistance in 2025 and 2026.
- Canada Truck and Transport Mechanic: **NOC 72410**, approximately **C$29.89/hour**.
- Canada Heavy-duty equipment mechanic: **NOC 72401**, approximately **C$37.12/hour**.
- SENA Técnico, Mantenimiento de los motores diesel: **2,208 hours**.
- U.S. Apprenticeship.gov warning retained: O*NET **49-3031.00** is stated in the checked listing as not currently approved for use in a Registered Apprenticeship Program.
- EPA Section **609** task boundary retained for compensated motor-vehicle air-conditioning service in the United States.

Currency labels remain jurisdiction-specific; U.S. and Canadian amounts were not converted into Brazilian reais or other Latin American currencies.

## Safety and regulated-task parity

The localization retains the fail-closed safety intent for:

- high-pressure common-rail fuel systems;
- compressed air, hydraulics, spring energy and other stored energy;
- high-voltage and hybrid-electric systems;
- lifting/support equipment;
- refrigerants and U.S. EPA Section 609 boundaries;
- emissions-system integrity and anti-tampering language;
- road-test licensing, authorization and insurance;
- employer procedures, qualified supervision and task-specific authorization;
- stop-and-escalate conditions when competence, tools, PPE, service information or legal authority are missing.

The Portuguese wording does not broaden authority to perform regulated or safety-critical work.

## Funding and opportunity parity

The localization preserves the project's free-first and evidence-based opportunity standard:

- American Job Centers and WIOA eligibility are conditional and locally administered.
- Federal Student Aid, Pell Grant and scholarship references are framed as possible assistance, not guarantees.
- Employer-supported learning, trainee roles, tool programs and educational assistance are presented as items to verify.
- The Section 127 amount is explicitly conditional on a qualifying employer plan.
- Canada trade-certification and apprenticeship requirements remain province/territory dependent.
- Colombia SENA and APE pathways are presented as current examples that require live verification.
- Latin America remains explicitly jurisdiction-first; Colombia examples are not represented as regional rules.

## Language and terminology review

The text was localized into natural Brazilian Portuguese rather than literal machine-style phrasing. Key terminology is understandable in Brazil while official proper names, program titles, occupation codes and source labels are retained where translation could impair verification.

Examples include:

- `equipamentos de proteção individual (EPI)` for PPE;
- `manutenção preventiva`;
- `sistemas de pós-tratamento e emissões`;
- `serviço em campo`;
- `alta tensão`, `alta pressão`, `energia armazenada`;
- `Agencia Pública de Empleo do SENA` retained as the Colombian proper name;
- official Canadian trade titles retained in English alongside Portuguese explanation where useful for lookup.

Brazilian spelling, accents, punctuation, heading hierarchy and Markdown list structure were reviewed for readability and accessibility.

## Privacy, AI and cybersecurity parity

The Portuguese edition preserves the prohibition on using general-purpose AI as final authority for safety-critical specifications or regulated decisions and retains the data-protection list covering names, VINs, license plates, telematics, GPS/location history, diagnostic logs, proprietary fleet information, credentials, access tokens, maintenance history and employer-confidential records.

Connected-equipment guidance remains authorization- and competence-bound.

## Source-link parity

The source section preserves the frozen English master's verification links for BLS, U.S. Department of Labor/WIOA, CareerOneStop, Apprenticeship.gov, Federal Student Aid, IRS, EPA, OSHA, NIOSH, Government of Canada Job Bank, Red Seal, SENA Betowa, SENA APE and Indeed.

The private compensation source remains clearly labeled supplemental and non-governmental.

## Claims boundary

This QA is an internal controlled localization review. It does **not** claim independent human certification, professional translation certification, accessibility certification, legal review, accreditation, trade licensing approval, guaranteed funding, employment, or earnings.

## Disposition

**PASS.** The Guide 27 `pt-BR` Version 2.0 controlled master preserves the material meaning, structure, numerical evidence, jurisdiction boundaries, safety controls, opportunity/funding caveats, privacy/AI controls, accessibility guidance and source intent of the frozen English source. Guide 27 may advance to trilingual technical QA after the helper manifest records this PASS.