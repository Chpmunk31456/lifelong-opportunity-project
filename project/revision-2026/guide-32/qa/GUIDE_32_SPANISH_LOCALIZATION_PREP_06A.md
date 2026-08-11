# Guide 32 — Spanish Localization Preparation 06A

**Guide:** 32 — Welder and Fabrication Technician  
**Target language:** neutral Latin American Spanish (`es-419`)  
**Date:** 2026-08-11  
**Authoritative branch:** `revision/guide-00-100-2026`  
**Authoritative PR:** #17  
**Frozen English source:** `project/revision-2026/guide-32/publication-candidate/GUIDE_32_ENGLISH_v2.md`  
**Frozen English blob:** `9705e9f509590ad2f9260cc36815e3010863538a`  
**Gate status after this preparation step:** **PENDING** — no Spanish PASS is claimed until the complete `es-419` candidate and localization QA are committed.

## Correction recorded during live-source reconciliation

The first version of this preparation record incorrectly described the frozen English source as containing 18 numbered sections. Live reconciliation against the frozen blob confirmed **22 numbered sections**. This record corrects that coordination defect before localization work proceeds. No manifest stage is advanced by this correction.

## Authoritative source controls

Translate only from the frozen English Version 2.0 source, not from legacy Spanish README, DOCX, or PDF artifacts. Preserve all **22 numbered sections** and their occupation-specific controls covering welding/fabrication scope, safety, training, funding, credentials, United States/Canada/Colombia/Latin America pathways, responsible AI, accessibility, job-search preparation, career progression, the 90-day plan, spending checklist, current-source list, and final reminder.

No localization write may silently change numerical evidence, jurisdiction, credential scope, safety authority, source identity, or the distinction between official and non-government labor-market evidence.

## Required terminology controls

Use neutral Latin American Spanish while preserving source identity for legal, regulatory, credential, and program names where translation could create ambiguity. In particular:

- keep `OSHA`, `29 CFR 1910 Subpart Q`, `1910.252`, `1910.253`, and `1910.254` as U.S.-specific references;
- retain `AWS Certified Welder`, `AWS Accredited Testing Facilities`, `Red Seal`, `NOC 72106`, `Registered Apprenticeship`, `WIOA`, `American Job Centers`, `SENA`, `Betowa`, and `Agencia Pública de Empleo (APE)` as identifiable program or credential names;
- use natural occupational terms such as `soldador`, `técnico de fabricación`, `ayudante de soldadura` and `soldador-armador` without implying a regulated title not present in the English source;
- preserve process abbreviations such as `SMAW`, `GMAW/MIG`, `FCAW`, and `GTAW/TIG`, with plain-language explanations where useful;
- never translate an industry credential into language implying a government license, professional licensure, accreditation, or universal authorization.

## Safety and scope parity requirements

The Spanish candidate must preserve, without dilution:

- fire and explosion prevention, hot-work permits, fire watch, isolation, gas testing, housekeeping, and fire protection;
- welding fumes, gases, coatings, hazardous base metals, ventilation, local exhaust, respiratory protection, medical evaluation, fit testing, and exposure monitoring where applicable;
- compressed-gas cylinder handling and oxygen/fuel-gas hazards;
- electric shock and optical-radiation hazards;
- confined-space work, atmospheric testing, ventilation, attendants, permits, communication, rescue planning, and site-specific controls;
- stop-and-escalate conditions for unclear procedures, missing qualifications, unknown coatings/residues, damaged equipment, pressure/critical structures, energized systems, elevated work, specialized code work, or requests to bypass inspection or safety controls.

U.S. OSHA rules must remain explicitly U.S.-specific. Outside the United States, readers must be directed to verify competent local authorities, employer rules, project requirements, contracts, codes, and worksite controls.

## Numerical and labor-market parity controls

Preserve the semantic values and labels from the frozen source, including:

- U.S. BLS May 2024 median: **USD 51,000/year** and **USD 24.52/hour**;
- BLS projected 2024–2034 employment growth: **2%**;
- approximately **45,600 projected openings per year**;
- Salary.com snapshot dated **July 1, 2026**: approximately **USD 59,272/year**, about **USD 28/hour**, with displayed 25th–75th percentile values of approximately **USD 52,614–67,828/year**;
- Canada Job Bank national wage references for NOC 72106: approximately **C$22.00/hour low**, **C$30.00/hour median**, and **C$47.00/hour high**, with the source page identified as updated **November 19, 2025**;
- Canada Apprentice Loan support of up to **C$4,000** in interest-free loans per eligible technical-training period, subject to current eligibility rules.

BLS and Government of Canada figures must remain official-source evidence. Salary.com must remain explicitly labeled a non-government market estimate and not be presented as definition-equivalent to BLS data or as a guaranteed wage.

## Training, funding, apprenticeship, and jurisdiction controls

Preserve the free-first decision sequence and cautions around Registered Apprenticeship, WIOA/American Job Centers, public/community technical programs, scholarships, employer-paid trainee routes, tuition or test reimbursement, paid study time, and tool/PPE support. Eligibility, approval timing, covered expenses, wage progression, training hours, testing, cancellation terms, and recognized outcomes must be verified before spending money. No funding source may be described as guaranteed.

Preserve that Red Seal Welder is associated with **NOC 72106**, while apprenticeship registration, compulsory/voluntary trade status, certification, exams, and legal work requirements remain provincial or territorial. Preserve the closed status of the former Canadian Apprenticeship Incentive Grant and Apprenticeship Completion Grant.

For Colombia, SENA Betowa remains a current-cohort training locator, not a promise that a specific course is open. SENA APE remains a free public-employment locator; individual vacancies are not national wage benchmarks. Short complementary training must not be represented as authorization for structural, pressure, pipeline, industrial, construction, or other specialized welding work.

For the rest of Latin America, direct readers to verify each country’s labor, occupational-safety, technical-education, qualification, public-employment, code/project, and credential-recognition rules rather than importing U.S., Canadian, or Colombian requirements.

## Claims, AI, accessibility, and publication boundaries

The Spanish candidate must remain educational and must not claim guaranteed employment, income, admission, funding, reimbursement, apprenticeship placement, certification, licensing, promotion, or legal authority. It must not claim independent human linguistic certification, professional translation certification, accreditation, legal review, accessibility certification, or code approval.

AI may support study, organization, terminology explanation, and drafting, but must not replace qualified supervision, approved welding procedures, code requirements, competent safety authority, inspections, qualification tests, engineering decisions, or site-specific hazard assessment. Accessibility language may support accommodations and alternative learning formats without removing essential safety or legal-scope requirements.

## Completion criteria for Spanish Localization PASS

Before `spanish_localization` may change from `PENDING` to `PASS`, all of the following must exist and be checked:

1. a complete `GUIDE_32_SPANISH_es-419_v2.md` candidate translated from the frozen English source;
2. structural parity across all **22 numbered sections**;
3. controlled numerical parity for wage, outlook, funding, and date values;
4. safety, credential, jurisdiction, and claims-boundary parity;
5. preserved source identities and direct URLs;
6. neutral Latin American Spanish terminology and natural readability;
7. UTF-8/encoding review with no mojibake;
8. a dedicated Spanish localization QA record concluding PASS only if every control passes;
9. helper-manifest evidence updated only after those artifacts are committed.

## Result

**Preparation checkpoint: COMPLETE after correction.**  
**Spanish Localization Helper: remains PENDING.**
