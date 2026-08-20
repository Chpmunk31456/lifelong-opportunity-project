# Guide 56 — Baseline Inventory 01

**Guide:** 56 — Nursing Assistant and Patient Care Technician  
**Branch:** `revision/guide-00-100-2026`  
**Date:** August 19, 2026  
**Gate:** Baseline Inventory — **PASS**

## Authoritative legacy package identified

The live repository contains the published Guide 56 package at:

- `56-nursing-assistant-and-patient-care-technician/README.md`
- `56-nursing-assistant-and-patient-care-technician/english/`
- `56-nursing-assistant-and-patient-care-technician/spanish/`
- `56-nursing-assistant-and-patient-care-technician/portuguese/`

The English edition contains:

- `english/README.md`
- `english/QC.md`
- `english/docx/Nursing Assistant and Patient Care Technician.docx`
- `english/pdf/Nursing Assistant and Patient Care Technician.pdf`

The English README identifies the career as **Nursing Assistant And Patient Care Technician**, version **1.0**, publication month **July 2026**, with DOCX and PDF present.

## Baseline observations

1. The published package exists in all three language directories and is suitable as the legacy publication baseline.
2. No controlled Guide 56 revision workspace or helper-status manifest existed at the start of this gate.
3. No editable English Version 2 Markdown master existed under `project/revision-2026/guide-56/`; therefore the controlled revision must reconstruct a new English source master rather than silently treating the publication README as the source master.
4. The legacy English README contains a UTF-8 BOM at the beginning of the file. Encoding normalization must be enforced in the Version 2 master and publication QA.
5. The current review language says the edition was "technically reviewed" while also warning that exact source equivalence and human linguistic review should not be assumed. The controlled revision must preserve the stronger project assurance boundary: no claim of independent human certification, professional translation certification, accreditation, accessibility certification, legal review, or guaranteed outcomes unless separately obtained.
6. Nursing assistant / patient-care technician work is safety-sensitive and jurisdiction-dependent. The revision must distinguish role titles and scopes rather than imply that "patient care technician" is a uniform regulated occupation across countries or employers.
7. The current-source research gate must verify U.S., Canada, Colombia, and broader Latin America pathways; training/funding options; employer-supported routes; current official wage data where available; and separately labeled non-government market estimates.
8. The controlled English master must include explicit boundaries against independent diagnosis, medication decisions, invasive procedures outside authorized scope, falsification of observations/vital signs, unsafe lifting/transfers, and use of AI as a substitute for licensed clinical judgment or employer procedure.

## Required controlled sequence

The Guide 56 revision will proceed fail-closed through:

1. Current-source Research
2. English Editorial / Version 2 reconstruction
3. Evidence / Traceability QA
4. English Source Freeze
5. Spanish Localization (`es-419`)
6. Portuguese Localization (`pt-BR`)
7. Trilingual Technical QA
8. Publication
9. Release Audit

## Decision

**Baseline Inventory: PASS.**

The occupation, legacy package, known source limitations, encoding concern, assurance boundary, and safety-sensitive revision requirements are identified. No downstream gate is implied by this PASS.
