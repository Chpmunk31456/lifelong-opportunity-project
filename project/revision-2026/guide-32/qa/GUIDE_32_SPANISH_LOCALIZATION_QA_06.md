# Guide 32 — Spanish Localization QA 06

**Guide:** 32 — Welder and Fabrication Technician  
**Target:** `project/revision-2026/guide-32/publication-candidate/GUIDE_32_SPANISH_es-419_v2.md`  
**Source:** frozen English Version 2.0, blob `9705e9f509590ad2f9260cc36815e3010863538a`  
**Locale:** neutral Latin American Spanish (`es-419`)  
**Date:** 2026-08-11  
**Result:** **PASS**

## Reconciliation control

Before this QA, the localization-preparation record was corrected because its initial text described the frozen source as having 18 sections. Live-source reconciliation confirmed **22 numbered sections**. The correction was committed before the Spanish candidate and did not advance the manifest.

## Structural parity

**PASS.** The Spanish candidate preserves the complete numbered structure **1 through 22**, including occupation scope, duties, safety, entry routes, U.S. labor-market evidence, U.S. funding/training, AWS credential boundaries, Canada, Colombia, wider Latin America, skills, beginner sequence, portfolio, AI/privacy/cybersecurity, training-provider evaluation, job search, interview/test preparation, progression, 90-day plan, spending checklist, current-source list, and final reminder.

The candidate retains the educational disclaimer, author/AI-assistance disclosure, and CC BY-NC-SA 4.0 license statement without adding certification or accreditation claims.

## Numerical parity

**PASS.** Controlled values were checked against the frozen English source:

- BLS May 2024 median: **USD 51,000/year / USD 24.52/hour**;
- BLS 2024–2034 growth: **2%**;
- projected openings: approximately **45,600/year**;
- Salary.com snapshot date: **July 1, 2026**;
- Salary.com average: approximately **USD 59,272/year / USD 28/hour**;
- Salary.com displayed 25th–75th percentile: approximately **USD 52,614–67,828/year**;
- Job Bank NOC: **72106**;
- Canada national wage references: **C$22.00 / C$30.00 / C$47.00 per hour**;
- Job Bank update date: **November 19, 2025**;
- Canada Apprentice Loan: up to **C$4,000** per eligible technical-training period.

No official value was silently converted into another currency or represented as a guaranteed offer. Salary.com remains explicitly labeled non-government market evidence.

## Safety and scope parity

**PASS.** The Spanish edition preserves hot-work, fire/explosion, fumes, coatings, ventilation, respiratory-protection, compressed-gas, electrical, optical-radiation, confined-space, damaged-equipment, pressure/critical-structure, energized-system, elevated-work, specialized-code, stop-work, and escalation controls.

OSHA 29 CFR 1910 Subpart Q and sections 1910.252, 1910.253, and 1910.254 remain explicitly U.S.-specific. The Spanish text does not universalize U.S. legal requirements and directs readers elsewhere to the competent local authority, employer, project, contract, code, and worksite controls.

## Credential and jurisdiction parity

**PASS.** AWS Certified Welder remains an industry credential rather than a universal government license. AWS Accredited Testing Facilities, process/material/position/code specificity, continuity, employer testing, and school-certificate boundaries are preserved.

Red Seal Welder remains associated with **NOC 72106**, while provincial/territorial authority over apprenticeship registration, compulsory or voluntary trade status, certification, exams, and work requirements is preserved.

SENA Betowa remains a current-cohort training locator; SENA Agencia Pública de Empleo remains a free vacancy locator; neither is represented as a guarantee. Individual APE vacancies are not treated as national wage benchmarks. Specialized Colombian welding remains subject to applicable technical, client, employer, safety, contractual, and regulatory requirements.

For Latin America outside Colombia, the candidate requires country-specific verification instead of importing U.S., Canadian, or Colombian rules.

## Funding and opportunity parity

**PASS.** The Spanish edition retains the free-first pathway: Registered Apprenticeship, employer training, WIOA/American Job Centers, public/community technical programs, scholarships, employer reimbursement/support, Canadian apprentice support, SENA, and public vocational routes elsewhere in Latin America.

The text requires written verification of eligibility, covered costs, timing, terms, testing, wage progression, and recognized outcomes where relevant. It does not guarantee funding. Former Canadian Apprenticeship Incentive Grant and Apprenticeship Completion Grant programs remain identified as closed rather than current cash-grant options.

## AI, privacy, accessibility, and claims controls

**PASS.** AI is limited to study, organization, public-reference summarization, pathway comparison, drafting, and other non-authoritative support. The edition prohibits relying on AI to create/alter WPS, PQR, WPQ, engineering drawings, code requirements, critical-weld parameters, inspection criteria, hazard determinations, or credential/employment records. Confidential, proprietary, restricted, export-controlled, customer, and safety-sensitive information is protected.

No independent human linguistic certification, professional translation certification, accreditation, legal review, accessibility certification, or code approval is claimed.

## Language, terminology, and encoding

**PASS.** Language was reviewed for neutral Latin American usage and natural human readability. Regulatory/program names whose identity matters are preserved. Welding-process abbreviations (`SMAW`, `GMAW/MIG`, `FCAW`, `GTAW/TIG`) remain recognizable. Accented Spanish characters render normally in UTF-8; no mojibake was observed in the live repository fetch.

## Source and link parity

**PASS.** Section 21 preserves the direct source list for BLS, OSHA, Apprenticeship.gov, U.S. DOL WIOA, AWS, Salary.com, Red Seal, Canada Job Bank, Canada apprentice-support pages, SENA Betowa, and SENA APE. Link reachability remains part of later Technical QA/publication controls; this localization gate confirms source identity and URL parity rather than claiming permanent external availability.

## Final gate decision

All required Spanish-localization controls are satisfied against the frozen English source.

**Spanish Localization Helper: PASS.**
