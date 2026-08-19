# Guide 49 — English Source Freeze 05

**Guide:** 49 — Dental Assistant  
**Branch:** `revision/guide-00-100-2026`  
**Freeze date:** August 19, 2026  
**Gate:** English Source Freeze  
**Status:** **PASS**

## Frozen source

The controlled localization source is:

`project/revision-2026/guide-49/working-masters/GUIDE_49_DENTAL_ASSISTANT_ENGLISH_v2.md`

Git blob SHA at freeze review: `76e49f3ebe095e06d87be33d9f0e307968c54fc9`.

Predecessor gates are complete:

- Baseline Inventory: PASS
- Current-source Research: PASS
- English Editorial: PASS
- Evidence / Traceability: PASS

No Guide 49 blocker is recorded.

## Frozen controlled facts

Localization must preserve the factual meaning and attribution of these controlled values and identifiers:

### United States

- O*NET **31-9091.00 — Dental Assistants**
- 2025 BLS/O*NET median: **USD $23.11/hour / $48,070/year**
- BLS OOH May 2024 median: **USD $22.74/hour / $47,300/year**
- BLS OOH low/high: **$36,190 / $61,780**
- 2024 employment: **381,900**
- 2034 projected employment: **406,300**
- projected growth: **6%**
- projected numeric increase: **24,400**
- average annual openings: approximately **52,900**
- Salary.com August 1, 2026 private estimate: **$41,739/year / $20/hour**, 25th–75th percentile **$37,596–$46,260**, 10th **$33,824**, 90th **$50,376**; always labeled non-government

### Canada

- NOC **33100**
- OaSIS dental-assistant profile **33100.01**
- Job Bank wage values **CAD $21.00 / $27.00 / $35.00 per hour**
- non-wage-benefit prevalence **72.3%**
- Canada Student Grant maximum for 2026–27: **CAD $4,200/year / $525 per month of study**, subject to eligibility
- preserve province-specific registration/intra-oral limitations and do not imply U.S. credential transfer

### Colombia

- **CUOC 53292 — Auxiliares de salud oral**
- **ReTHUS**
- Decreto 1409 de 2024
- Resolución SENA 2057 de 2025 / **Técnico Laboral en Salud Oral**
- Resolución Minsalud 914 de 2025 reprocessing context
- preserve the explicit exclusion of higher-scope `Higienistas y asistentes odontológicos` functions
- preserve the fail-closed duration control: **do not introduce one definitive national SENA/Salud Oral program duration** unless new competent-authority evidence is separately researched and the English source is reopened through controlled gates

## Frozen safety and scope meaning

Both localizations must preserve that:

- dental-assisting scope is jurisdiction-dependent;
- radiography and expanded functions require exact current legal/training/credential/supervision verification;
- a Dental Assistant title or certificate does not independently authorize diagnosis, treatment planning, prescribing, radiographic diagnosis, irreversible procedures, anesthesia, or another profession's scope;
- infection prevention includes PPE, sharps/exposure controls, instrument cleaning, packaging, sterilization/reprocessing, monitoring, environmental controls, manufacturer instructions, and escalation;
- patient information, images, radiographs, histories, insurance data, identifiers, and payment information must not be placed into public or unauthorized AI systems;
- AI does not replace dentist judgment, diagnosis, radiographic interpretation, treatment planning, emergency decisions, infection-control procedures, manufacturer instructions, or approved records; and
- no national credential automatically transfers legal scope across borders.

## Translation and parity controls

The neutral Latin American Spanish (`es-419`) and Brazilian Portuguese (`pt-BR`) masters must:

1. derive from this frozen English Version 2 rather than from the legacy v1 files;
2. preserve the complete H2 section order and substantive content;
3. preserve every direct source URL exactly so trilingual URL-set parity can be tested mechanically;
4. preserve all controlled numeric values, dates, codes, currencies, percentages, and jurisdictional qualifiers;
5. use natural professional target-language wording while retaining legally important distinctions among dentist, dental assistant, hygienist, therapist, laboratory roles, regulation, registration, credential, authorization, delegation, and supervision;
6. preserve `ReTHUS`, `CUOC 53292`, NOC/OaSIS codes, program/regulation names, and official-source identities without inventing equivalence;
7. preserve privacy, cybersecurity, radiography, infection-control, AI, no-guarantee, accessibility, scam, funding, and assurance boundaries; and
8. make no claim of independent human review, certified/professional translation, accessibility certification, accreditation, dental/legal review, or clinical authorization.

No factual expansion is permitted during localization. If a translator finds a factual defect or needs new evidence, localization must stop and the English source must be reopened through the controlled Research/Editorial/Traceability process.

## Decision

**English Source Freeze: PASS.** The exact English Version 2 master above is the sole authorized source for Guide 49 `es-419` and `pt-BR` localization. The next permitted gate is **Spanish Localization (`es-419`)**.
