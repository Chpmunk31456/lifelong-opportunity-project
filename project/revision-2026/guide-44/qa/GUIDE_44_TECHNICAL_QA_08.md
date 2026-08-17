# Guide 44 — Trilingual Technical QA Gate 08

**Guide:** 44 — Wind Turbine Service Technician  
**Branch:** `revision/guide-00-100-2026`  
**Workflow:** `Guide 44 controlled publication build`  
**Successful run:** `32065233489`  
**Workflow-source commit:** `a597244d3dc7b94303040e2a0a23e721bcd62efa`  
**Publication-candidate commit:** `3385da695a0dc06c0e89696c3fc8a38f73574805`  
**Gate result:** **PASS**

## Preconditions

Baseline Inventory, Current-source Research, English Editorial, Evidence/Traceability, English Source Freeze, Spanish Localization (`es-419`), and Portuguese Localization (`pt-BR`) were PASS before this gate.

## Corrective QA history

Runs `32064681248` and `32064859765` failed closed before artifact generation because inherited Guide 43 validator markers and localized unit expressions were too narrow. Commits `1eb2c16f` and `011dc408` corrected the validator without changing or weakening Guide 44 content. Run `32064998082` passed the substantive build; the audit then detected a residual Guide 43 manifest filename. Commit `a597244d` corrected the filename, and run `32065233489` completed successfully.

## Successful workflow evidence

Every substantive step passed: trilingual candidate freeze; structural, source, numeric, terminology, UTF-8, placeholder, and live-link controls; three DOCX and three PDF builds; DOCX archive and searchable-PDF validation; all-page rendering and automated blank/clipping/malformed-render checks; publication metadata and SHA-256 generation; artifact upload; and controlled candidate commit.

The editions preserve 23/23 section and 23/23 exact-source parity, including SOC 49-9081 / O*NET 49-9081.00, NOC 72400, U.S. 6-foot/1.8-m and 4-foot/1.2-m boundaries, Colombia above-2.0-m control, wage/outlook values, and related 3,984-hour SENA pathways.

## Artifact and visual QA

The manifest records overall PASS:

- English: DOCX 23,374 bytes; PDF 163,547 bytes; 11 pages / 11 rendered pages.
- Spanish (`es-419`): DOCX 24,538 bytes; PDF 168,891 bytes; 12 pages / 12 rendered pages.
- Portuguese (`pt-BR`): DOCX 23,060 bytes; PDF 164,437 bytes; 11 pages / 11 rendered pages.

Workflow artifact `guide44-rendered-pages` has artifact ID `9299680237`, size 7,814,744 bytes, digest `sha256:829ebfd5cd71fb5932b433c82b142c30dd3d2d2c171ba9b70a1d92ec4b01576c`, and expiration August 31, 2026. Automated all-page render checks found no blank page, clipping, malformed rendering, page-count mismatch, or missing searchable text.

## Decision

**Trilingual Technical QA: PASS.** Guide 44 may proceed to Publication. This is internal project QA and does not claim independent human review, professional translation certification, accessibility certification, legal review, electrical or engineering approval, licensing determination, accreditation, or guaranteed employment or earnings.
