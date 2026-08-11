# Guide 32 — Spanish Localization Preparation 06A

**Guide:** 32 — Welder and Fabrication Technician  
**Target language:** neutral Latin American Spanish (`es-419`)  
**Date:** 2026-08-11  
**Authoritative branch:** `revision/guide-00-100-2026`  
**Authoritative PR:** #17  
**Frozen English source:** `project/revision-2026/guide-32/publication-candidate/GUIDE_32_ENGLISH_v2.md`  
**Frozen English blob:** `9705e9f509590ad2f9260cc36815e3010863538a`  
**Gate status after this preparation step:** **PENDING** — no Spanish PASS is claimed until the complete `es-419` candidate and localization QA are committed.

## Purpose

This checkpoint records the controlled source-to-target localization requirements before the Guide 32 Spanish candidate is written. It is intentionally fail-closed: the existing legacy Spanish publication material is not treated as equivalent to the frozen English Version 2.0 source, and the helper manifest remains unchanged until complete parity evidence exists.

## Authoritative source controls

The Spanish edition must be translated from the frozen English Version 2.0 source rather than from the older Spanish README or legacy DOCX/PDF artifacts. The frozen source contains 18 numbered sections and occupation-specific controls covering welding/fabrication scope, safety, training, funding, credentials, United States/Canada/Colombia/Latin America pathways, responsible AI, accessibility, job-search preparation, and career progression.

No localization write may silently change numerical evidence, jurisdiction, credential scope, safety authority, source identity, or the distinction between official and non-government labor-market evidence.

## Required terminology controls

Use neutral Latin American Spanish while preserving source identity for legal, regulatory, credential, and program names where translation could create ambiguity. In particular:

- keep `OSHA`, `29 CFR 1910 Subpart Q`, `1910.252`, `1910.253`, and `1910.254` as U.S.-specific references;
- retain `AWS Certified Welder`, `AWS Accredited Testing Facilities`, `Red Seal`, `NOC 72106`, `Registered Apprenticeship`, `WIOA`, `American Job Centers`, `SENA`, `Betowa`, and `Agencia Pública de Empleo (APE)` as identifiable program or credential names;
- translate occupational terminology naturally, using forms such as `soldador`, `técnico de fabricación`, `ayudante de soldadura`, `soldador-armador` or context-appropriate equivalents without implying a regulated title that the English source does not claim;
- preserve welding-process abbreviations such as `SMAW`, `GMAW/MIG`, `FCAW`, and `GTAW/TIG` alongside plain-language Spanish descriptions when useful;
- do not translate an industry credential into wording that implies a government license, professional licensure, accreditation, or universal authorization.

## Safety and scope parity requirements

The Spanish candidate must preserve, without dilution, the frozen source controls for:

- fire and explosion prevention, hot-work permits, fire watch, isolation, gas testing, housekeeping, and fire protection;
- welding fumes, gases, coatings, hazardous base metals, ventilation, local exhaust, respiratory protection, medical evaluation, fit testing, and exposure monitoring where applicable;
- compressed-gas cylinder handling and oxygen/fuel-gas hazards;
- electric shock and optical-radiation hazards;
- confined-space work, atmospheric testing, ventilation, attendants, permits, communication, rescue planning, and site-specific controls;
- stop-and-escalate conditions for unclear procedures, missing qualifications, unknown coatings/residues, damaged equipment, pressure/critical structures, energized systems, elevated work, specialized code work, or requests to bypass inspection or safety controls.

The localization must not turn U.S. OSHA rules into universal Latin American legal requirements. Outside the United States, readers must be directed to verify the competent local authority, employer, project, contract, code, and worksite requirements.

## Numerical and labor-market parity controls

The Spanish candidate must preserve the semantic values and labels from the frozen source, including:

- U.S. BLS May 2024 median: **USD 51,000/year** and **USD 24.52/hour**;
- BLS projected 2024–2034 employment growth: **2%**;
- approximately **45,600 projected openings per year**;
- Salary.com snapshot dated **July 1, 2026**: approximately **USD 59,272/year**, about **USD 28/hour**, with displayed 25th–75th percentile values of approximately **USD 52,614–67,828/year**;
- Canada Job Bank national wage references for NOC 72106: approximately **C$22.00/hour low**, **C$30.00/hour median**, and **C$47.00/hour high**, with the source page identified as updated **November 19, 2025**;
- Canada Apprentice Loan support of up to **C$4,000** in interest-free loans per eligible technical-training period, subject to current eligibility rules.

BLS and Government of Canada figures must remain official-source evidence. Salary.com must remain explicitly labeled a non-government market estimate and not be presented as definition-equivalent to BLS data or as a guaranteed wage.

## Training, funding, and apprenticeship parity controls

The Spanish edition must preserve the free-first decision sequence and cautions around:

- Registered Apprenticeship and structured employer training;
- WIOA/American Job Center eligibility and Eligible Training Provider List verification where applicable;
- community and technical colleges, public vocational routes, scholarships, employer-paid trainee pathways, tuition reimbursement, certification-test reimbursement, paid study time, and tool/PPE support;
- written verification of eligibility, approval timing, covered expenses, wage progression, training hours, testing, cancellation terms, and recognized outcomes before committing money;
- the closed status of former Canadian Apprenticeship Incentive Grant and Apprenticeship Completion Grant programs so outdated grant claims are not revived.

No funding source may be described as guaranteed.

## Canada, Colombia, and Latin America controls

The candidate must preserve that Red Seal Welder is associated with **NOC 72106**, while apprenticeship registration, compulsory/voluntary trade status, certification, exams, and legal work requirements remain provincial or territorial.

For Colombia, SENA Betowa must remain a current-cohort training locator rather than a promise that a specific course is open. SENA APE must remain a free public-employment locator whose individual vacancies are not national wage benchmarks. The localization must preserve the distinction between short complementary training and authorization or qualification for structural, pressure, pipeline, industrial, construction, or other specialized welding work.

For the rest of Latin America, the candidate must direct readers to verify each country's labor, occupational-safety, technical-education, qualification, public-employment, code/project, and credential-recognition rules rather than importing U.S., Canadian, or Colombian requirements.

## Claims, AI, accessibility, and publication boundaries

The Spanish candidate must retain the frozen source's educational-only character and must not claim:

- guaranteed employment, income, admission, funding, reimbursement, apprenticeship placement, certification, licensing, promotion, or legal authority;
- independent human linguistic certification, professional translation certification, accreditation, legal review, accessibility certification, or code approval;
- that AI can replace a qualified supervisor, welding procedure, code requirement, competent safety authority, inspection, qualification test, or site-specific hazard assessment.

Accessibility language should support accommodations and alternative learning formats without implying removal of essential safety or legal-scope requirements.

## Completion criteria for Spanish Localization PASS

Before `spanish_localization` may be changed from `PENDING` to `PASS`, all of the following must exist and be checked:

1. a complete `GUIDE_32_SPANISH_es-419_v2.md` candidate translated from the frozen English source;
2. structural parity across all 18 numbered sections;
3. controlled numerical parity for wage, outlook, funding, and date values;
4. safety, credential, jurisdiction, and claims-boundary parity;
5. preserved source identities and direct URLs;
6. neutral Latin American Spanish terminology and natural readability;
7. UTF-8/encoding review with no mojibake;
8. a dedicated Spanish localization QA record concluding PASS only if every control passes;
9. helper-manifest evidence updated only after those artifacts are committed.

## Result

**Preparation checkpoint: COMPLETE.**  
**Spanish Localization Helper: remains PENDING.**

This checkpoint does not weaken or bypass the manifest. It establishes the exact parity controls for the next write against the live frozen Guide 32 English source.
