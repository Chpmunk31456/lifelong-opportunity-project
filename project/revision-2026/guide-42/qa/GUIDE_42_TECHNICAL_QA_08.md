# Guide 42 — Trilingual Technical QA Gate 08

**Guide:** 42 — Painter and Coating Worker  
**Branch:** `revision/guide-00-100-2026`  
**Workflow:** `Guide 42 controlled publication build`  
**Successful run:** `31960427122`  
**Publication-candidate commit:** `03f93f1f05dd5c8c5b626b975fe8110729025b5b`  
**Gate result:** **PASS**

## Preconditions

The following predecessor gates were already PASS before this gate:

- Baseline Inventory
- Current-source Research
- English Editorial
- Evidence/Traceability
- English Source Freeze
- Spanish Localization (`es-419`)
- Portuguese Localization (`pt-BR`)

Shared source-link corrective evidence is recorded in `GUIDE_42_SOURCE_LINK_CORRECTIVE_QA_07B.md`. That corrective action replaced one obsolete OIT/Cinterfor locator consistently across all three masters without changing the supported claim, occupational scope, figures, safety boundaries, jurisdiction qualifiers, or assurance limitations.

## Automated trilingual controls

Successful workflow run `31960427122` completed all of the following controls with success:

- controlled-branch checkout;
- trilingual publication-candidate freeze;
- English / `es-419` / `pt-BR` structural parity;
- occupation terminology and pathway separation;
- controlled SOC/NOC/CIUO identifiers;
- controlled numerical, date, currency, growth, opening, and 12-week-plan values;
- source URL-set parity across all three languages;
- required safety and jurisdiction markers;
- AI/privacy/cybersecurity boundary markers;
- non-certification / non-guarantee assurance language;
- UTF-8, BOM, Unicode replacement-character, and placeholder controls;
- live source-link behavior after corrective source maintenance;
- DOCX generation for all three languages;
- PDF generation for all three languages;
- DOCX ZIP/document integrity validation;
- searchable PDF text validation;
- raster rendering of every PDF page;
- automated blank-page, possible-clipping, and malformed-render controls;
- publication metadata generation;
- SHA-256 checksum generation;
- rendered-page QA artifact upload; and
- controlled publication-candidate commit.

## Publication-artifact evidence

`GUIDE_42_PUBLICATION_QA_MANIFEST.json` records overall **PASS**:

- English: DOCX `23,121` bytes; PDF `176,727` bytes; `12` PDF pages; `12` rendered pages.
- Spanish (`es-419`): DOCX `24,113` bytes; PDF `180,616` bytes; `13` PDF pages; `13` rendered pages.
- Portuguese (`pt-BR`): DOCX `24,069` bytes; PDF `182,163` bytes; `13` PDF pages; `13` rendered pages.

The rendered-page workflow artifact is:

- Name: `guide42-rendered-pages`
- Artifact ID: `9267094513`
- Size: `8,239,683` bytes
- Digest: `sha256:e96e3fb9476a75aef3771b5abbfcdd832ed2a9abfe75d4df4bf0f0e4acb849ad`
- Retention expiration: August 30, 2026

This gate records successful automated all-page rendering and automated page-integrity checks. It does **not** claim independent manual visual review of every rasterized page.

## Checksums

`project/revision-2026/guide-42/publication-candidate/SHA256SUMS.txt` records SHA-256 checksums for all six generated DOCX/PDF deliverables.

## Defects encountered and resolved

Two defects were detected by fail-closed QA before this PASS:

1. The first workflow run exposed a validator expression that did not recognize the correct English `12-week` form. The validator was repaired to continue requiring the controlled 12-week value while accepting valid language-specific punctuation/plural forms. No content requirement was removed.
2. The next run found an explicit HTTP 404 for an obsolete OIT/Cinterfor locator. The source was replaced across English, Spanish, and Portuguese with the current OIT/Cinterfor institutional-network locator and documented in corrective QA 07B. The full workflow was then rerun from the corrected source set and passed.

No QA control was weakened to obtain PASS.

## Technical QA decision

**Trilingual Technical QA: PASS.**

Guide 42 is technically eligible to proceed to the controlled Publication gate. This is internal automated QA evidence; it is not independent human review, professional translation certification, accessibility certification, legal review, certification-body approval, accreditation, or a guarantee of employment or earnings.
