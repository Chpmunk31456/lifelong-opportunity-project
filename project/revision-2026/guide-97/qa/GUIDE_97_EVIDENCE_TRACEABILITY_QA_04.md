# Guide 97 — Evidence / Traceability QA 04

## Guide
Mechanical Engineering Technician

## Review date
2026-08-22

## Controlled inputs
- Research evidence: `project/revision-2026/guide-97/research/GUIDE_97_CURRENT_SOURCE_EVIDENCE_02.md`
- English master: `project/revision-2026/guide-97/working-masters/GUIDE_97_MECHANICAL_ENGINEERING_TECHNICIAN_ENGLISH_v2.md`
- English master blob reviewed: `f923ec4bbe08cd81d881091f204a4aa3d0c6c7cb`

## Gate purpose
Verify that consequential claims in the controlled English master are traceable to the current research pack, that official and non-government sources are not conflated, that jurisdictional comparisons are properly bounded, and that no unsupported certification, licensure, accreditation, wage, funding, safety, or AI claim is promoted into the frozen source.

## Traceability matrix

| Claim area | Controlled source(s) | English-master treatment | Result |
|---|---|---|---|
| U.S. occupation identity and task scope | O*NET 17-3027.00 | Correctly identifies Mechanical Engineering Technologists and Technicians and support-under-engineering-staff scope | PASS |
| U.S. current official median wage | O*NET 2026 profile using BLS 2025 wage data | $35.82/hour and $74,510/year, explicitly identified as 2025 median | PASS |
| U.S. OOH wage and education | BLS OOH | May 2024 median $68,730; associate degree or other postsecondary training; value is separately dated | PASS |
| U.S. employment/outlook | O*NET/BLS | About 38,300 workers in 2024, little/no change 2024–2034, about 3,200 openings/year | PASS |
| U.S. training funding | CareerOneStop WIOA finder | Presented as an eligibility-dependent locator; American Job Center verification required | PASS |
| Canada occupation identity | Job Bank NOC 22301 | Correctly identified as Mechanical engineering technologists and technicians | PASS |
| Canada wages | Job Bank | C$23.08 low / C$35.00 median / C$51.28 high per hour; updated Nov. 19, 2025 | PASS |
| Canada prospects | Job Bank | National moderate risk of shortage 2024–2033 with near-term provincial variation | PASS |
| Canada education/certification | Job Bank requirements | Distinguishes 1–2 year technician and 2–3 year technologist college pathways; certification may be required; Quebec title rule bounded | PASS |
| Canada training supports | Canada.ca training / LMDA / WDA | Presented as eligibility-dependent supports, not automatic funding | PASS |
| Colombia occupation identity | OCUPACOL CUOC 31150 | Correctly identifies Técnicos en ingeniería mecánica, competence-level context | PASS |
| Colombia training | SENA Betowa | Mantenimiento Mecánico Industrial and Mantenimiento Electromecánico Industrial, 3,984-hour Tecnólogo pathways; live availability caveat retained | PASS |
| Latin America regional locator | OIT/Cinterfor | Presented only as a vocational-training network/locator, not a guaranteed course or scholarship | PASS |
| U.S. private compensation | ZipRecruiter / Salary.com | Clearly labelled non-government estimates with dates and methodology/title-scope limitations | PASS |
| Colombia private compensation | Computrabajo | Clearly labelled broader-title context, not an official CUOC 31150 wage equivalent | PASS |
| Rejected anomalous salary scrape | Research QA decision | Implausible Indeed Colombia scrape explicitly excluded and not carried into master | PASS |
| Engineering-authority boundaries | O*NET/BLS scope plus jurisdictional professional-practice caution | Technician support is separated from licensed/regulated engineering authority | PASS |
| Hazardous energy / LOTO | OSHA | Conservative isolation/authorization language; no unsafe shortcuts | PASS |
| Machine guarding / mechanical hazards | OSHA-related controls | Guard/interlock bypass prohibited; stored energy, pressure, lifting and hot-work boundaries included | PASS |
| Cybersecurity | CISA Secure Our World | MFA/password/phishing/update principles adapted to engineering/test/industrial context without inventing policy | PASS |
| Responsible AI | NIST AI RMF + Generative AI Profile | Low-risk drafting/learning only; consequential technical facts require approved sources and human verification | PASS |
| Accessibility | Controlled editorial standard | Physical-demand variability and accommodation-process language included without certification or legal guarantee | PASS |
| Legacy six-step action-plan defect | Baseline inventory + English master | Six numbered steps with checkable milestones now present | PASS |

## Official-source hierarchy
**PASS**

The master uses official government or intergovernmental sources as the primary authority for occupation classification, official wages, public funding/training locators, safety controls, and national labour-market context.

Private compensation sources are never substituted for official wage statistics.

## Wage-control review
**PASS**

### United States
- Current principal official value: **2025 median $35.82/hour / $74,510 annually** from O*NET using BLS 2025 wage data.
- BLS OOH comparison value: **May 2024 median $68,730 annually**.
- BLS May 2025 OEWS mean: retained in research as a secondary control and not confused with the median in the reader-facing master.

### Canada
- Current Job Bank national values: **C$23.08 low / C$35.00 median / C$51.28 high hourly**.

### Colombia
- OCUPACOL salary display is not promoted as the principal current benchmark because of reference-period/methodology limitations.
- Computrabajo is presented only as a current broader-title private-market reference.

## Funding and training controls
**PASS**

The master does not promise:
- WIOA eligibility;
- American Job Center funding;
- Canadian LMDA/WDA eligibility;
- student aid;
- an apprenticeship;
- employer tuition assistance;
- SENA admission or seat availability;
- any specific OIT/Cinterfor-connected course or scholarship.

All such pathways are framed as locators or possibilities requiring live verification.

## Credential, licensure, and accreditation controls
**PASS**

The master does not claim that:
- a technician is a licensed professional engineer;
- a particular credential is universally required;
- this guide confers a credential;
- SENA, a college, or another provider is accredited by this project;
- any edition has independent human certification;
- any future translation will be professionally certified unless separately documented.

Canada's provincial certification/title context is explicitly jurisdiction-dependent.

## Safety traceability
**PASS**

Safety claims are conservative and consistent with the research pack:
- hazardous energy can remain after normal shutdown;
- employer energy-control procedures govern lockout/tagout;
- guarding and interlocks must not be casually bypassed;
- pressure, stored force, lifting, rigging, electrical work, welding/hot work, and other specialized hazards can require trained/authorized personnel and additional controls;
- the guide does not provide a procedure that could substitute for an employer's site-specific safe-work procedure.

## Cybersecurity traceability
**PASS**

The master carries role-appropriate cybersecurity guidance tied to CISA principles and engineering-system context. It does not authorize the learner to alter production networks, controller logic, safety systems, firmware, or configurations without explicit approval and change control.

## Responsible-AI traceability
**PASS**

The master maps the NIST risk-management approach into a conservative practical rule: AI may assist with low-risk drafting, learning, and organization; approved engineering sources and authorized humans control consequential technical decisions.

The prohibited/verification-required list covers dimensions, tolerances, loads, stresses, materials, pressure and temperature limits, torque, safety factors, lifting limits, maintenance intervals, acceptance criteria, guarding, LOTO, engineering changes, regulations, failure conclusions, and production release.

## Accessibility and human-readability traceability
**PASS**

Accessibility content stays within educational and workplace-planning scope and does not claim legal certification. The document uses short sections, lists, explicit milestones, and a final checklist to support readers who benefit from structured information.

## Link/evidence presence review
**PASS for traceability stage**

The English master contains verification destinations covering:
- O*NET;
- BLS OOH and OEWS;
- CareerOneStop;
- OSHA;
- CISA;
- NIST;
- Canada Job Bank;
- Canada.ca training and labour-market agreements;
- OCUPACOL;
- SENA Betowa;
- OIT/Cinterfor;
- ZipRecruiter;
- Salary.com;
- Computrabajo.

Research-stage web verification confirmed the key current occupation, wage, training, safety, and compensation facts used in the reconstruction. Full URL/live-link automation, parity checks, document generation, metadata, rendering, and publication-candidate checks remain downstream and are not claimed by this gate.

## Known legacy defects
**PASS — controlled repair confirmed**

The legacy English QC recorded `Action Plan 1 To 6: False`. The controlled English master now contains six sequential action-plan steps, each with a measurable milestone. This repair is source-level and must be preserved in localization and publication.

## Unsupported-claim scan
**PASS**

No unsupported claim found for:
- guaranteed employment;
- guaranteed income;
- automatic funding;
- guaranteed admission;
- guaranteed apprenticeship;
- independent human certification;
- professional translation certification;
- engineering licensure;
- legal review;
- accessibility certification;
- safety certification;
- employer endorsement.

## Gate result
**PASS — Evidence / Traceability**

The English master is eligible for English Source Freeze. No blocker identified.

## Post-freeze source-link correction revalidation — 2026-08-22

NIST moved the reader-verification page for *Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile*. The obsolete URL ending in `-profile` returned HTTP 404 during Publication QA. The official NIST publication page was reverified on 2026-08-22 and the URL-only correction was applied in English, `es-419`, and `pt-BR` with no change to occupational claims, wage/training values, safety/professional-scope controls, cybersecurity/AI guidance, action-plan milestones, or assurance boundaries.

- Revalidated English blob: `f923ec4bbe08cd81d881091f204a4aa3d0c6c7cb`
- Revalidated Spanish blob: `f851c168d366ee8ab551a63c842a7df830bcba91`
- Revalidated Portuguese blob: `183a888d50148d4059c041b850548bef87e2cb09`
- Correct official NIST destination: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
- Result: **PASS — affected gate revalidated after URL-only source correction.**
