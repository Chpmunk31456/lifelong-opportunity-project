# Guide 46 — Baseline Inventory 01

**Guide:** 46 — Environmental Field Technician  
**Branch:** `revision/guide-00-100-2026`  
**Date:** 2026-08-18  
**Stage:** Baseline Inventory  
**Result:** PASS

## Legacy inventory reviewed

The live legacy directory is `46-environmental-field-technician/`. It contains a guide-level README plus English, neutral Latin American Spanish, and Brazilian Portuguese packages. Each language package contains a README, a legacy QC record, one DOCX, and one searchable-PDF artifact.

### English

- `english/README.md`
- `english/QC.md`
- `english/docx/Environmental Field Technician.docx` — 42,285 bytes; Git blob `93fe17a6d42283d985276e3e332c08ecccf23b55`
- `english/pdf/Environmental Field Technician.pdf` — 289,714 bytes; Git blob `214fbc84e5760cd97ee631b13cddfb4d88206238`

The English README identifies Version 1.0, July 2026, and says DOCX/PDF are present. Its review-status language says exact source equivalence and human linguistic review should not be assumed unless separately documented. English QC records an eight-page visual render review, searchable PDF text, no broken field errors, and release-candidate status pending final owner approval.

### Neutral Latin American Spanish

- `spanish/README.md`
- `spanish/QC.md`
- `spanish/docx/Guia_46_T_cnico_de_Campo_Ambiental.docx` — 46,403 bytes; Git blob `705979c399d47801c61d5df53bff6f20ce531825`
- `spanish/pdf/Guia_46_T_cnico_de_Campo_Ambiental.pdf` — 186,189 bytes; Git blob `0796d0fa69714b20534ecfe549616228f62676e5`

The Spanish README identifies Version 1.0, July 2026. Its legacy filename encodes `Técnico` as `T_cnico`; the controlled revision must not preserve that filename defect. Spanish QC says the neutral-Spanish translation was reviewed, records six rendered pages and selectable PDF text, and says there are no field/marker errors. It also contains the anomalous line `Plan de doce semanas numerado del 1 al 6: sí`; this must not be accepted as evidence that a twelve-week plan is complete or correctly numbered. The publication candidate remained pending owner review.

### Brazilian Portuguese

- `portuguese/README.md`
- `portuguese/QC.md`
- `portuguese/docx/Guia_46_T_cnico_de_Campo_Ambiental_PTBR.docx` — 43,503 bytes; Git blob `6d053a355cd7a44e8e389006af3ac5eb60a0c0f1`
- `portuguese/pdf/Guia_46_T_cnico_de_Campo_Ambiental_PTBR.pdf` — 150,610 bytes; Git blob `880d05ca217d29fe0fb3169962a45b3de9e8b907`

The Portuguese README identifies Version 1.0, July 2026. Its legacy filename also preserves `T_cnico` rather than the correctly accented title. Portuguese QC records a six-page render and searchable PDF, says Brazilian Portuguese was reviewed, and leaves the artifact as a publication candidate pending owner review.

## Baseline defects and revision requirements

1. All three legacy editions are Version 1.0 and predate the controlled sequential 2026 revision framework used for Guides 00–45.
2. No editable Markdown source master is present in the legacy package. A controlled Version 2 English master must be reconstructed from current authoritative evidence rather than treating the legacy DOCX/PDF text as current evidence.
3. The legacy directory contains no controlled publication manifest, SHA-256 release inventory, exact source-URL parity record, current-source evidence map, or release-audit record.
4. Legacy QC primarily addresses layout, pagination, searchable text, and document fields. It does not independently establish current occupational classification, wages, employment outlook, education/entry requirements, jurisdictional credentials, work-based learning, funding, sampling methods, chain-of-custody requirements, environmental regulations, field-safety controls, source freshness, or source traceability.
5. English, Spanish, and Portuguese edition metadata uses `Technically reviewed publication edition`, but the legacy QC files simultaneously identify the artifacts as release/publication candidates pending owner review. The controlled revision must therefore re-establish technical QA and publication status rather than inheriting either label.
6. The Spanish and Portuguese statements that the translations were reviewed do not identify a reviewer, method, independence, competence standard, or certification. They cannot be represented as independent human linguistic review or professional translation certification.
7. Spanish and Portuguese filenames contain the legacy `T_cnico` encoding/substitution defect. Controlled Version 2 filenames and displayed titles must use valid UTF-8 and correct language orthography.
8. Spanish QC contains an internal inconsistency: `Plan de doce semanas numerado del 1 al 6: sí`. The controlled revision must rebuild any learning plan from the frozen English source and verify exact sequence parity rather than carrying this claim forward.
9. Current-source research must independently establish the occupation's most defensible classification and scope, U.S./Canada/Colombia/LATAM entry pathways, current compensation/outlook where authoritative data exists, education expectations, employer or public training routes, and jurisdiction-specific credential or regulatory boundaries.
10. Version 2 must distinguish ordinary supervised field-support work from tasks requiring employer authorization, qualified-person oversight, laboratory accreditation/procedures, hazardous-material training, respiratory protection, confined-space programs, electrical qualification, environmental permits, sampling plans, site-specific health-and-safety plans, or other jurisdiction-specific controls.
11. Safety research must cover only evidence-supported hazards applicable to environmental field work, including site assessment, traffic and driving, slips/trips/falls, weather and heat/cold, wildlife/insects, contaminated media, chemicals, biological hazards, sharp objects, lifting/ergonomics, water bodies, excavation/openings, noise, field instrumentation, decontamination, PPE, hygiene, emergency communications, and stop-work/escalation conditions. Specialized hazards such as hazardous-waste operations, respirator use, confined spaces, energized electrical work, or rescue must be presented conditionally and never as universal duties.
12. The guide must not teach unsupervised hazardous-material handling, permit or regulatory compliance determinations, confined-space entry/rescue, energized work, intrusive sampling beyond training/authorization, laboratory release decisions, falsification or alteration of field records, bypassing quality controls, or unsafe collection/decontamination procedures.
13. Environmental data integrity requires explicit controls for field notes, sample identification, timestamps, preservation/holding-time instructions where applicable, chain of custody, calibration/verification records, photographs/location data, corrections, privacy, and escalation of anomalies. AI must never invent, overwrite, backfill, or silently normalize measurements, observations, chain-of-custody information, or compliance conclusions.
14. New `es-419` and `pt-BR` editions must derive from a frozen English source and pass structural, terminology, numeric/date/currency, source-URL, safety, authorization, environmental-data-integrity, AI/privacy, assurance, DOCX/PDF, rendering, metadata, checksum, Publication, and Release Audit controls.

## Legacy file inventory

The live Guide 46 package contains 13 files:

1. `README.md`
2. `english/README.md`
3. `english/QC.md`
4. `english/docx/Environmental Field Technician.docx`
5. `english/pdf/Environmental Field Technician.pdf`
6. `spanish/README.md`
7. `spanish/QC.md`
8. `spanish/docx/Guia_46_T_cnico_de_Campo_Ambiental.docx`
9. `spanish/pdf/Guia_46_T_cnico_de_Campo_Ambiental.pdf`
10. `portuguese/README.md`
11. `portuguese/QC.md`
12. `portuguese/docx/Guia_46_T_cnico_de_Campo_Ambiental_PTBR.docx`
13. `portuguese/pdf/Guia_46_T_cnico_de_Campo_Ambiental_PTBR.pdf`

## Disposition

**Baseline Inventory: PASS.** Guide 46 may advance to Current-source Research. No legacy artifact, classification, wage, credential, safety statement, translation claim, review label, or source is accepted as controlled Version 2 evidence without current authoritative verification.

This inventory is internal controlled evidence. It does not claim independent human review, professional translation certification, accessibility certification, legal or environmental review, laboratory or engineering approval, industrial-hygiene or medical review, hazardous-waste qualification, respiratory-protection qualification, confined-space or rescue qualification, regulatory or licensing determination, accreditation, guaranteed funding, employment, or earnings.
