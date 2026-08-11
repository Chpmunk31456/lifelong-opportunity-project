# Guide 28 Publication Gate 09

**Guide:** 28 — Industrial Machinery Mechanic and Maintenance Worker  
**Branch:** `revision/guide-00-100-2026`  
**Gate:** Publication Helper  
**Status:** PASS  
**QA date:** August 11, 2026

## Preconditions

The Guide 28 helper manifest records PASS for all predecessor gates through Technical QA. Technical evidence is recorded in `GUIDE_28_TECHNICAL_QA_GATE_08.md`.

## Publication package

The successful controlled build run `31485527711` generated and committed the Guide 28 publication package in commit `a285916b9268568cdded0cc5dc4eafe933a1ec9b` under:

`project/revision-2026/guide-28/publication-candidate/`

The committed package contains the three controlled Markdown source editions plus, for each language edition, a DOCX and searchable PDF publication candidate. It also contains:

- `GUIDE_28_PUBLICATION_QA_MANIFEST.json`; and
- `SHA256SUMS.txt`.

## Publication checks

The package was reconciled against the live revision branch after the successful build. The committed publication QA manifest reports overall status **PASS** and records these validated controls:

- trilingual structural parity;
- required source URLs and URL parity;
- UTF-8/BOM controls;
- placeholder scan;
- DOCX ZIP integrity;
- searchable PDF text;
- all-page raster rendering;
- metadata manifest; and
- SHA-256 checksums.

The package contains three DOCX and three PDF files. PDF results recorded in the manifest are:

- English: 12 pages, 27,764 extractable characters;
- es-419: 14 pages, 32,444 extractable characters;
- pt-BR: 13 pages, 31,481 extractable characters.

All three editions are marked PASS in the publication QA manifest. SHA-256 hashes are committed for all six DOCX/PDF artifacts. The workflow artifact `guide28-rendered-pages` was also reviewed across all 39 rendered pages as part of Technical QA.

## Publication conclusion

**Publication Helper: PASS.**

The controlled Guide 28 publication candidates, QA manifest, checksums, and rendering evidence exist and match successful controlled-build evidence. This gate does not merge PR #17 and does not imply completion of the separate Release Auditor gate.

## Assurance boundary

This is internal controlled-publication QA. It is not independent human certification, professional translation certification, accessibility certification, legal review, trade licensing approval, accreditation, or a guarantee of employment, admission, funding, certification, or earnings.
