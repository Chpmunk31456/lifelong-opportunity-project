# Guide 56 — Trilingual Technical QA 08

**Guide:** 56 — Nursing Assistant and Patient Care Technician  
**Branch:** `revision/guide-00-100-2026`  
**Date:** August 19, 2026  
**Gate:** Technical QA — **PASS**

## Controlled inputs

- English frozen master: `project/revision-2026/guide-56/working-masters/GUIDE_56_NURSING_ASSISTANT_AND_PATIENT_CARE_TECHNICIAN_ENGLISH_v2.md`
- Spanish `es-419` master: `project/revision-2026/guide-56/working-masters/GUIDE_56_NURSING_ASSISTANT_AND_PATIENT_CARE_TECHNICIAN_ES419_v2.md`
- Brazilian Portuguese `pt-BR` master: `project/revision-2026/guide-56/working-masters/GUIDE_56_NURSING_ASSISTANT_AND_PATIENT_CARE_TECHNICIAN_PTBR_v2.md`
- Spanish localization QA 06
- Portuguese localization QA 07
- Current-source evidence 02

## Technical controls

PASS — all three controlled masters are present as complete UTF-8 Markdown sources; no placeholder, truncation, replacement-character, or language-edition omission is recorded in the localization QA evidence.

PASS — structural coverage is equivalent across the three editions for career scope, work realities, U.S. pathway, Canada pathway, Colombia pathway, Latin America/Caribbean locators, training/funding, safety, privacy, cybersecurity, responsible AI, scam prevention, résumé/job-search preparation, accessibility, source list, and assurance boundaries.

PASS — controlled U.S. values remain semantically consistent across editions: nursing-assistant median annual wage USD $39,530; orderly median annual wage USD $37,700; 2% projected 2024–2034 combined growth; approximately 211,800 annual openings; non-government Salary.com estimate USD $34,701/year / $17/hour and USD $31,120–$36,431 25th–75th percentile range.

PASS — controlled Canada values remain semantically consistent: NOC 33102; CAD $19.00/hour low, CAD $24.00/hour median, CAD $28.84/hour high. Locale punctuation differences do not constitute numeric mismatch when meaning is unchanged.

PASS — controlled Colombia values and identifiers remain consistent: CNO 3311, SENA/Betowa Enfermería technical program, 2,640-hour program duration, delegation/supervision boundary, and ReTHUS verification requirement.

PASS — the Patient Care Technician title remains explicitly employer-defined/non-universal. No edition treats the title alone as authorization for phlebotomy, ECG, specimen handling, medication activity, invasive procedures, or other regulated clinical work.

PASS — fail-closed clinical safety language is preserved across languages: no independent diagnosis, prescribing or medication-treatment selection/change, unauthorized invasive procedures, falsification of care records, unsafe transfer/infection practices, or generative-AI substitution for licensed clinical judgment or patient-specific orders.

PASS — credential portability is not implied between the United States, Canada, Colombia, or other jurisdictions.

PASS — WIOA, American Job Centers, employer support, SENA/Betowa, public training, and other funding/training locators remain eligibility- and availability-dependent rather than guaranteed.

PASS — privacy/cybersecurity controls prohibit patient information, images, records, identifiers, credentials, internal schedules, proprietary care documents, or other protected/confidential health information from public or unapproved AI tools.

PASS — authoritative and secondary/non-government sources remain clearly differentiated. Source URL parity was explicitly verified in both localization QA gates, including the complete 13-source controlled set.

PASS — publication parser control is required to use Pandoc reader `gfm-tex_math_dollars` so currency dollar signs are not interpreted as TeX inline math.

PASS — publication must perform DOCX integrity checks, searchable-PDF validation, all-page raster rendering, strict edge-clipping inspection with fail threshold below 2 pixels, rendered-page/page-count reconciliation, metadata generation, and SHA-256 checksum coverage before Publication may pass.

## Decision

**Technical QA: PASS.**

Guide 56 may advance to Publication. Publication and Release Audit remain fail-closed until the controlled trilingual DOCX/PDF package, rendering evidence, manifest, checksums, and release-audit evidence pass.

No independent human certification, certified translation, clinical/legal review, accreditation, accessibility certification, licensure approval, employment guarantee, or earnings guarantee is claimed.
