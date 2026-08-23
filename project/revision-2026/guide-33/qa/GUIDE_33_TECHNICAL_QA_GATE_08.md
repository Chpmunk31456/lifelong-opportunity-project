# Guide 33 Technical QA Gate 08

**Guide:** 33 — Machinist and CNC Machine Operator  
**Branch:** `revision/guide-00-100-2026`  
**Gate:** Technical QA Helper  
**Status:** PASS  
**QA date:** August 12, 2026

## Preconditions

English source freeze, es-419 localization, and pt-BR localization were already recorded PASS before this gate.

## Workflow evidence

Controlled workflow: `.github/workflows/guide33-publication-build.yml`  
Successful GitHub Actions run: `31569279653`  
Run conclusion: **success**  
Publication-candidate commit: `4c8701e2d71ee22ed7a791c4fffb6144f7d041ce`

The workflow passed exact trilingual section parity for sections 1–22, source URL-set parity, source-domain presence, locale-aware controlled numerical values, locale-aware technical-marker parity including translated lockout/tagout terminology, UTF-8/BOM controls, placeholder scanning, DOCX/PDF generation, DOCX ZIP/package validation, searchable-PDF validation, all-page raster rendering, metadata manifest generation, SHA-256 checksum generation, render-artifact upload, and controlled publication commit.

## Publication artifact controls

The committed publication manifest records:

| Language | PDF pages | Extractable PDF characters | Status |
|---|---:|---:|---|
| English | 15 | 33,684 | PASS |
| es-419 | 17 | 39,436 | PASS |
| pt-BR | 16 | 37,840 | PASS |

Each DOCX passed ZIP/package integrity. Each PDF passed searchable-text validation and all pages were raster-rendered by the controlled workflow.

Render evidence was uploaded as artifact `guide33-rendered-pages`, artifact ID `9130705426`, digest `sha256:56ea5260f5b84228ac7cf41ead628c61c21a89c0314f3b3638955bbe8f021e55`. This records successful automated render coverage; it does not claim independent human visual certification.

The publication package includes `GUIDE_33_PUBLICATION_QA_MANIFEST.json` and `SHA256SUMS.txt` for metadata and integrity verification.

## Technical conclusion

**Technical QA Helper: PASS.** Guide 33 meets the controlled structural, source, locale-aware numerical, terminology, encoding, DOCX, PDF, rendering, metadata, and checksum requirements to proceed to Publication Helper.

## Assurance boundary

This is internal automated technical/publication-artifact QA. It is not independent human review, professional translation certification, accessibility certification, legal review, machine-tool safety certification, trade licensing approval, accreditation, or a guarantee of employment, admission, funding, certification, licensing, or earnings.
