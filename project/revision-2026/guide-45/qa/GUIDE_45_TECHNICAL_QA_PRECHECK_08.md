# Guide 45 — Trilingual Technical QA Precheck 08

**Guide:** 45 — Water and Wastewater Treatment Plant Operator  
**Branch:** `revision/guide-00-100-2026`  
**Date:** August 17, 2026  
**Stage:** Technical QA precheck  
**Result:** PENDING — controlled publication build required

## Preconditions

The following controlled stages are complete and recorded as PASS before technical artifact work:

- Baseline Inventory
- Current-source Research
- English Editorial
- Evidence/Traceability
- English Source Freeze
- Spanish Localization (`es-419`)
- Portuguese Localization (`pt-BR`)

## Trilingual source precheck

The three controlled Markdown masters are present:

- `project/revision-2026/guide-45/working-masters/GUIDE_45_WATER_WASTEWATER_TREATMENT_PLANT_OPERATOR_ENGLISH_v2.md`
- `project/revision-2026/guide-45/working-masters/GUIDE_45_WATER_WASTEWATER_TREATMENT_PLANT_OPERATOR_ES419_v2.md`
- `project/revision-2026/guide-45/working-masters/GUIDE_45_WATER_WASTEWATER_TREATMENT_PLANT_OPERATOR_PTBR_v2.md`

Localization QA records preserve the controlled **24/24 H2-section architecture**, **21/21 exact direct source URLs**, SOC **51-8031**, O*NET **51-8031.00**, NOC **92101**, U.S. BLS wage/outlook values, Canadian Job Bank values, SENA **12-month / 2,208-hour / 48-hour** pathway values, jurisdiction boundaries, safety controls, AI/privacy boundaries, and non-guarantees.

No content-level blocker is recorded at this precheck.

## Required technical gate — not yet satisfied

Technical QA must remain fail-closed until an auditable controlled build completes all of the following:

1. Freeze the three Markdown publication candidates from the controlled masters.
2. Validate H2 structural parity and exact source-URL set parity across all three editions.
3. Validate controlled numeric/classification/terminology markers and UTF-8 integrity.
4. Probe the 21 official source URLs, failing explicit broken links and recording access-controlled or transport-only limitations without treating them as verified content.
5. Generate three DOCX files and three searchable PDF files.
6. Validate each DOCX archive and document structure.
7. Validate searchable PDF text and page counts.
8. Render every PDF page and inspect for blank pages, clipping, malformed pages, missing glyphs, and page/render mismatches.
9. Generate publication metadata and SHA-256 checksums for all DOCX/PDF publication artifacts.
10. Retain rendered-page evidence and commit the controlled publication-candidate package.

## Workflow handoff specification

The established Guide 44 controlled-publication workflow is the approved pattern to adapt for Guide 45. The Guide 45 variant must use the Guide 45 file paths and occupation identifiers above and must validate these controlled values in every edition:

- `51-8031`
- `51-8031.00`
- `92101`
- `$58,260`
- `$28.01`
- `$37,870`
- `$86,160`
- `132,400`
- `123,800`
- `-8,700`
- `-7 percent` / localized equivalent
- `10,700`
- `CAD $25.00`
- `CAD $36.06`
- `CAD $48.00`
- `12 months` / localized equivalent
- `2,208 hours` / localized equivalent, allowing locale thousands punctuation where semantically identical
- `48 hours` / localized equivalent

The workflow must not weaken safety, authorization, credential, source, or non-guarantee controls merely to make a build pass.

## Decision

**Technical QA remains PENDING.** Content and localization are ready, but no PASS may be recorded until the controlled DOCX/PDF build, searchable-text checks, all-page render QA, metadata, checksums, and committed publication artifacts complete successfully.

This precheck is internal project evidence. It does not claim independent human review, professional translation certification, accessibility certification, legal or environmental review, laboratory or engineering approval, electrical authorization, industrial-hygiene or medical review, confined-space or rescue qualification, operator licensing determination, accreditation, guaranteed funding, employment, or earnings.
