# Guide 33 — Spanish Localization QA 06

**Guide:** 33 — Machinist and CNC Machine Operator  
**Target:** `project/revision-2026/guide-33/publication-candidate/GUIDE_33_SPANISH_es-419_v2.md`  
**Target blob:** `8f97db301f6fbf999c7555ed98a31bb0a50a15f0`  
**Source:** frozen English Version 2.0, blob `62054bb81fcd0e76629623e285ec2d2a9eab84f9`  
**Locale:** neutral Latin American Spanish (`es-419`)  
**Date:** 2026-08-11  
**Result:** **PASS**

## Structural parity

**PASS.** The Spanish candidate preserves the frozen English source's complete numbered structure **1 through 22** in the same semantic order. It retains occupation scope and title distinctions, duties, safety boundaries, entry routes, U.S. labor-market evidence, free-first U.S. training/funding pathways, NIMS credential boundaries, Canada, Colombia, wider Latin America, skills, beginner sequence, 90-day plan, training-program evaluation, truthful portfolio guidance, responsible AI/privacy/cybersecurity, accessibility, career progression, offer comparison, pause/decline criteria, source notes, and final checklist.

The opening educational disclaimer is preserved without adding any guarantee of employment, wages, admission, funding, reimbursement, apprenticeship placement, certification, licensing, promotion, or legal authority.

## Numerical parity

**PASS.** Controlled numerical values and dates were checked against the frozen English source:

- BLS May 2024 machinist median: **USD 56,150/year**;
- BLS lowest 10 percent: below **USD 38,100**;
- BLS highest 10 percent: above **USD 78,760**;
- machinist projected employment change, 2024–2034: approximately **0%**;
- combined machinists/tool-and-die-makers openings: about **34,200/year** on average;
- Indeed U.S. CNC Machinist estimate updated **July 20, 2026**: approximately **USD 28.06/hour**, displayed range approximately **USD 20.44–38.53/hour**;
- Red Seal Machinist: **NOC 72100**;
- Red Seal harmonization recommendation: **4 technical-training levels** and **7,200 total apprenticeship training hours**;
- Canada Job Bank national wage references: **C$21.00 / C$30.00 / C$41.50 per hour**;
- Job Bank update date: **November 19, 2025**, reference period 2023–2024;
- Canada Apprentice Loan: up to **C$4,000** per eligible technical-training period;
- NIMS policy boundary: credentials earned on or after **June 30, 2026** have a five-year validity period unless renewed under the current policy;
- former Canadian Apprenticeship Incentive Grant and Apprenticeship Completion Grant cutoff: progression/completion dates after **March 31, 2025** are not treated as current open grant eligibility.

BLS and Government of Canada figures remain identified as official-source evidence. Indeed remains explicitly labeled a **non-government market estimate**, not definition-equivalent to BLS data and not a guaranteed wage.

## Safety and task-boundary parity

**PASS.** The Spanish edition preserves machine guarding, interlocks, enclosures, emergency systems, lockout/tagout, rotating-equipment entanglement, hot/sharp chip, workholding, ejection, metalworking-fluid, ventilation, hygiene, SDS, PPE/EPP, setup, jam-clearing, alarm-recovery, maintenance, troubleshooting, and stop/escalate controls.

It retains the source's warning against bypassing guards or safety systems, falsifying measurements or inspection, concealing scrap, working outside verified competence, or entering danger zones based only on an assumption that motion has stopped.

Special handling boundaries for export-controlled/defense data, medical-device traceability, aerospace requirements, hazardous materials, and regulated quality systems are preserved. OSHA remains clearly presented as a U.S. authority rather than universal Latin American law.

## Credential and jurisdiction parity

**PASS.** NIMS remains an **industry credential**, not a government license. The candidate does not imply that one credential establishes competence across all machines, controls, materials, tolerances, inspection methods, or programming environments, and it preserves the boundary between a school certificate and a NIMS credential.

Red Seal Machinist remains associated with **NOC 72100**, while apprenticeship registration, certification, exams, compulsory/voluntary trade status, and implementation remain provincial or territorial matters.

SENA machining/CNC pathways are treated as training locators whose current cohort, city, regional center, level, and entry requirements must be verified. SENA Agencia Pública de Empleo remains a free public employment service whose individual vacancies are not national wage standards.

For Latin America outside Colombia, the edition requires country-specific verification rather than importing U.S., Canadian, or Colombian rules.

## Training, funding, apprenticeship, and opportunity parity

**PASS.** The Spanish edition preserves the free-first sequence: employer-paid training, public technical/community-college routes, Registered Apprenticeship where applicable, WIOA/American Job Center support, scholarships, tuition/credential reimbursement, tool/PPE support, paid study time, Canadian apprentice support, SENA, and public vocational routes elsewhere in Latin America.

The Apprenticeship.gov caveat is preserved: Advanced Manufacturing resources identify CNC Machine Operator and Precision Machinist among apprenticeship occupations, while the current O*NET Machinists 51-4041.00 occupation entry is described as not currently approved for Registered Apprenticeship use. Readers are directed to verify the exact sponsor, registered occupation, wage progression, related instruction, hours, credentials, cancellation terms, and completion status.

No funding, reimbursement, scholarship, apprenticeship placement, credential, or employer support is guaranteed.

## AI, privacy, cybersecurity, accessibility, and claims controls

**PASS.** AI is limited to study support, public-concept explanation, truthful résumé drafting, checklists, non-proprietary examples, and language support. The edition explicitly rejects relying on AI alone for production-ready G-code, toolpaths, feeds/speeds, workholding, offsets, dimensional interpretation, safety procedures, controller recovery, inspection acceptance, or regulated-process documentation.

The Spanish text protects proprietary drawings, CAD/CAM files, machine programs, customer information, export-controlled data, medical-device records, aerospace/defense information, passwords, credentials, network diagrams, and confidential process data from unauthorized upload to public AI services.

Accessibility language is preserved without weakening essential safety, measurement, physical, technical, or job-scope requirements. No independent human linguistic certification, professional translation certification, accreditation, legal review, safety approval, accessibility certification, or professional credential recognition is claimed.

## Language, terminology, and encoding

**PASS.** Language was reviewed for neutral Latin American usage and natural human readability. Institutional and credential names whose identity matters remain recognizable, including `OSHA`, `BLS`, `Apprenticeship.gov`, `WIOA`, `American Job Centers`, `CareerOneStop`, `NIMS`, `Red Seal`, `NOC 72100`, `SENA`, and `Agencia Pública de Empleo (APE)`.

Technical terms and abbreviations including `CNC`, `CAD/CAM`, `G-code`, `M-code`, `EDM`, `SDS`, and `EPP` remain understandable without converting them into claims of licensure or authority. Accented Spanish characters render normally in UTF-8; no mojibake was observed in the live repository fetch.

## Source and link parity

**PASS.** Section 21 preserves the direct source identities and URLs for BLS, O*NET, Apprenticeship.gov, U.S. DOL WIOA, OSHA, NIMS, Red Seal, Canada Job Bank, Canada Apprentice Loan, SENA, SENA APE, and the Indeed salary estimate. Indeed remains labeled non-government evidence.

External-link reachability is reserved for the later Technical QA/publication gate; this localization gate confirms source identity and URL parity rather than permanent availability.

## Final gate decision

All Spanish-localization completion criteria in `GUIDE_33_SPANISH_LOCALIZATION_PREP_06A.md` are satisfied against frozen English blob `62054bb81fcd0e76629623e285ec2d2a9eab84f9`.

**Spanish Localization Helper: PASS.**
