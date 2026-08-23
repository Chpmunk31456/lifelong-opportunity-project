# Guide 85 — Trilingual Technical QA 08

**Guide:** 85 — Data Analyst  
**Controlled branch:** `revision/guide-00-100-2026`  
**Frozen English source:** `GUIDE_85_DATA_ANALYST_ENGLISH_v2.md` — blob `6139ca58f49692ef57556c3fd593e6d8b6d33f8b`  
**Spanish master:** `GUIDE_85_DATA_ANALYST_SPANISH_LATAM_v2.md` (`es-419`)  
**Portuguese master:** `GUIDE_85_DATA_ANALYST_PORTUGUESE_PTBR_v2.md` (`pt-BR`)  
**Review date:** 2026-08-22

## Gate purpose
This gate checks technical, numeric, source, scope, safety and opportunity-pathway parity across the three controlled language masters. It is an internal controlled QA gate, not independent human linguistic certification or professional statistical/legal/accessibility certification.

## Occupation-scope parity — PASS
All three editions preserve the central rule that **Data Analyst is a broad cross-cutting market title, not one universal occupation code**.

All three retain:
- O*NET-SOC **15-2041.00 — Statisticians** as the primary U.S. quantitative benchmark;
- the explicit warning that the Statisticians benchmark is more mathematically advanced and graduate-heavy than many commercial entry-level Data Analyst jobs;
- O*NET-SOC **15-2051.01 — Business Intelligence Analysts** as an adjacent, not interchangeable, benchmark;
- Canada **NOC 21223** as a database/data-management-oriented comparison rather than a perfect crosswalk;
- Colombia **CUOC 25210 / 25110 / 21200** as function-dependent comparisons rather than one exclusive national code.

No edition silently converts the benchmark into a universal title-only wage, education or outlook series.

## Numeric parity — PASS
The controlled values are preserved across English, es-419 and pt-BR:

### U.S. Statisticians 2025 wages
- 10th: **$54,680 / $26.29**
- 25th: **$70,710 / $33.99**
- median: **$105,650 / $50.79**
- 75th: **$143,140 / $68.82**
- 90th: **$170,700 / $82.07**

### U.S. Statisticians outlook
- 2024 employment: **32,200**
- 2034 projected employment: **34,900**
- growth: **9%**
- projected annual openings: about **2,000**

### Current non-government U.S. Data Analyst context
- Indeed average base salary: approximately **$85,108/year**
- displayed range: approximately **$52,084–$139,074/year**
- about **8.1k** observations over the prior 36 months on the reviewed 2026 page
- explicitly labelled non-government, title-specific and changeable

### Canada NOC 21223 wages
- low: **C$25.00/hour**
- median: **C$40.87/hour**
- high: **C$61.03/hour**

### SENA pathways
- Programación para analítica de datos — Técnico — **2,208 hours/horas**
- Visualización de datos usando Power BI — **48 hours/horas**
- Analítica de datos para procesos logísticos — **48 hours/horas**

## Source and link parity — PASS
The controlled research evidence pack retains **27 evidence URLs** for claim traceability across O*NET, CareerOneStop, Indeed, Canada Job Bank/Canada.ca, OCUPACOL, SENA, OIT/Cinterfor, CISA, NIST, Section 508 and WCAG 2.2.

The three **reader-facing masters intentionally share the same curated 11 verification URLs** for usability:
- O*NET Statisticians detail;
- O*NET Business Intelligence Analysts detail;
- CareerOneStop WIOA locator;
- Apprenticeship.gov;
- NIST AI RMF;
- Canada Job Bank landing point for NOC 21223 verification;
- Canada training gateway;
- OCUPACOL;
- SENA Betowa;
- OIT/Cinterfor;
- Indeed U.S. Data Analyst salary context.

The shorter reader list does not replace the 27-source evidence pack. No fabricated source or AI-generated authority is introduced.

## Analytical-method parity — PASS
All editions preserve the core professional workflow:
- define the decision/question before analysis;
- identify authoritative sources;
- document lineage and row grain;
- understand tables, keys and joins;
- validate row counts and join effects;
- use spreadsheets, SQL and appropriate Python/R/statistical tools;
- document cleaning transformations;
- distinguish missing data from zero;
- use defensible duplicate rules;
- understand descriptive statistics, outliers, sampling and selection bias;
- distinguish correlation from causation;
- communicate uncertainty and limitations;
- avoid misleading visualizations;
- evaluate data quality;
- reconcile important outputs to authoritative sources;
- retain reproducible logic, definitions and correction history.

## Integrity and ethical-boundary parity — PASS
All editions prohibit or clearly warn against:
- changing source data to obtain a preferred conclusion;
- hiding material filters or exclusions;
- removing valid outliers only because they weaken the story;
- denominator shopping;
- presenting correlation as causation;
- fabricating data, samples, findings or citations;
- presenting model/forecast/AI narrative as observed fact;
- unsupported statistical certainty;
- unauthorized access/disclosure;
- misleading visualization;
- presenting accounting, legal, clinical, regulatory or engineering conclusions outside assigned competence.

## Privacy and cybersecurity parity — PASS
All editions retain:
- employer-approved systems;
- least privilege;
- MFA and approved credential practices;
- no protected extracts in personal storage/email;
- no bypass of access controls;
- approved encrypted storage/transfer;
- recipient verification;
- retention/deletion requirements;
- incident reporting and escalation;
- explicit statement that query access does not mean every field may be used or redistributed.

## Responsible-AI parity — PASS
All editions permit only controlled assistance such as drafting code/formulas, explaining logic, synthetic test-data generation or low-risk documentation where policy permits, and require:
- approved tools/data classes;
- no protected/confidential data in unapproved public AI;
- accountable human validation of code, calculations and narrative;
- reconciliation to authoritative sources;
- review for fabricated fields/citations, data leakage, bias and unsupported causal claims;
- no autonomous publication of decision-critical analytics outside approved governance.

NIST AI RMF and Generative AI Profile remain described as voluntary risk-management guidance rather than law.

## Accessibility parity — PASS
All editions preserve accessible chart/report guidance including meaningful titles and labels, readable text/contrast, non-color-only encoding, accessible tables/text alternatives, logical reading order and keyboard-accessible dashboard considerations where supported. No edition claims automated checking proves legal accessibility compliance.

## Expanded-opportunity parity — PASS
All editions preserve:
- U.S. CareerOneStop/American Job Center/WIOA discovery with eligibility caveats;
- O*NET/Apprenticeship.gov Data Analyst / Data Analyst (Nof) / Junior Data Analyst apprenticeship discovery without promising availability;
- employer training, internship and supervised work-based-learning routes;
- Canada training and student-aid gateway guidance without promising funding;
- SENA Betowa pathways with live cohort/seat/modality verification requirements;
- OIT/Cinterfor as a regional locator;
- ethical portfolio work using public, licensed or synthetic data;
- job-search title variants;
- employer due-diligence questions;
- the four-week starter action plan.

## Claims/certification boundary — PASS
No edition guarantees employment, income, funding, admission, apprenticeship placement, certification or promotion. No edition claims independent human certification, professional accreditation, legal review, statistical certification, accessibility certification or certified translation.

## Technical QA gate result
**PASS — Trilingual Technical QA**

**Blockers:** none.

Guide 85 is cleared to enter controlled Publication QA and Release Audit.
