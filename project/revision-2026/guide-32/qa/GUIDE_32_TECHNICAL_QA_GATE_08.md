# Guide 32 Technical QA Gate 08

**Guide:** 32 — Welder and Fabrication Technician  
**Branch:** `revision/guide-00-100-2026`  
**Gate:** Technical QA Helper  
**Status:** PASS  
**QA date:** August 11, 2026

## Preconditions

English source freeze, es-419 localization, and pt-BR localization were already recorded PASS before this gate.

## Workflow evidence

Controlled workflow: `.github/workflows/guide32-publication-build.yml`  
Successful GitHub Actions run: `31545457373`  
Run conclusion: **success**  
Publication-candidate commit: `1c1b1a6e365dedf33b6504cf62d17ef98bb0d33e`

The workflow passed exact trilingual section parity for sections 1–22, source URL-set parity, source-domain presence, locale-aware controlled numerical values, technical-marker parity, UTF-8/BOM controls, placeholder scanning, DOCX/PDF generation, DOCX ZIP/package validation, searchable-PDF validation, all-page raster rendering, metadata manifest generation, SHA-256 checksum generation, render-artifact upload, and controlled publication commit.

## Publication artifact controls

The committed publication manifest records:

| Language | PDF pages | Extractable PDF characters | Status |
|---|---:|---:|---|
| English | 14 | 31,059 | PASS |
| es-419 | 13 | 31,389 | PASS |
| pt-BR | 15 | 34,353 | PASS |

Each DOCX passed ZIP/package integrity. Each PDF passed searchable-text validation and all pages were raster-rendered by the controlled workflow.

Render evidence was uploaded as artifact `guide32-rendered-pages`, artifact ID `9122306373`, digest `sha256:b0ec5baa5a6fc0d86f7a0fe34881b669f0675176a9a12613dbcf81ca6c2b0232`. This records successful automated render coverage; it does not claim independent human visual certification.

The publication package also includes `GUIDE_32_PUBLICATION_QA_MANIFEST.json` and `SHA256SUMS.txt` for metadata and integrity verification.

## Technical conclusion

**Technical QA Helper: PASS.** Guide 32 meets the controlled structural, source, locale-aware numerical, encoding, DOCX, PDF, rendering, metadata, and checksum requirements to proceed to Publication Helper.

## Assurance boundary

This is internal automated technical/publication-artifact QA. It is not independent human review, professional translation certification, accessibility certification, legal review, welding-code approval, trade licensing approval, accreditation, or a guarantee of employment, admission, funding, certification, licensing, or earnings.
