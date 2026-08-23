# Guide 29 Technical QA Gate 08

**Guide:** 29 — HVAC Technician and Refrigeration Mechanic  
**Branch:** `revision/guide-00-100-2026`  
**Gate:** Technical QA Helper  
**Status:** PASS  
**QA date:** August 11, 2026

## Preconditions

The live Guide 29 helper manifest records PASS for English source freeze, Spanish localization, and Portuguese localization before this gate.

## Workflow evidence

Controlled workflow: `.github/workflows/guide29-publication-build.yml`  
GitHub Actions run: `31505735657`  
Run conclusion: **success**  
Publication-candidate commit: `27cc66346ff82813c7277e4a4be41a0630aabfc6`

Every workflow step completed successfully, including trilingual structural/link/encoding/source controls, DOCX/PDF generation, DOCX package validation, searchable-PDF validation, all-page raster rendering, metadata-manifest generation, SHA-256 checksum generation, rendered-page artifact upload, and controlled publication-candidate commit.

## Structural and source controls

The automated gate required all three controlled Version 2.0 editions to preserve:

- 18 numbered content sections;
- required BLS, EPA Section 608, OSHA, Federal Student Aid, WIOA, Apprenticeship.gov, IRS Section 127, Canada Job Bank, Red Seal, SENA, and current private-market source URLs;
- controlled markers including SENA, Apprenticeship.gov, NOC 72402, OSHA 1910.147, EPA Section 608, and Version 2.0;
- matching section and URL counts across languages;
- valid UTF-8 without unexpected BOM or Unicode replacement characters; and
- no known TODO, insertion, unfinished-translation, or placeholder markers.

The structural/link/source-control step concluded **success**.

## DOCX and PDF controls

The run generated three DOCX and three searchable PDF editions. Each DOCX passed ZIP/package integrity validation and contained `word/document.xml`; each PDF passed `pdfinfo` and searchable-text extraction thresholds.

The committed publication manifest records:

| Language | PDF pages | Extractable PDF characters | Status |
|---|---:|---:|---|
| English | 13 | 29,831 | PASS |
| es-419 | 14 | 34,222 | PASS |
| pt-BR | 14 | 32,650 | PASS |

All PDF pages were raster-rendered during the successful workflow. Render evidence was uploaded as artifact `guide29-rendered-pages`, artifact ID `9106972966`, digest `sha256:c825b0e008f590770fe80d651a93e37fbdc6a0f216e491e3f38af67fd2cd3cb4`. The successful all-page rendering step demonstrates that every generated PDF page could be rasterized by the controlled toolchain. No separate claim of independent human visual certification is made by this gate.

## Metadata and integrity controls

The successful build committed:

- `GUIDE_29_PUBLICATION_QA_MANIFEST.json` with overall status PASS;
- `SHA256SUMS.txt` covering all six DOCX/PDF artifacts;
- three DOCX publication candidates; and
- three searchable PDF publication candidates.

## QA conclusion

**Technical QA Helper: PASS.**

Guide 29 passed the controlled structural, source-link, encoding, DOCX-package, PDF-searchability, all-page raster-rendering, metadata, and checksum controls required to proceed to Publication Helper.

## Assurance boundary

This is internal technical and publication-artifact QA. It is not independent human review, professional translation certification, accessibility certification, legal review, environmental-regulatory approval, trade licensing approval, accreditation, or a guarantee of employment, admission, funding, certification, or earnings.
