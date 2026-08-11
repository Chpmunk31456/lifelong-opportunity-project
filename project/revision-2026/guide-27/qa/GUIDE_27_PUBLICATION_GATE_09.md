# Guide 27 Publication Gate 09

**Guide:** 27 — Diesel Service Technician and Mechanic  
**Branch:** `revision/guide-00-100-2026`  
**Gate:** Publication Helper  
**Status:** PASS  
**QA date:** August 11, 2026

## Preconditions

The Guide 27 helper manifest records PASS for all predecessor gates through Technical QA. Technical evidence is recorded in `GUIDE_27_TECHNICAL_QA_GATE_08.md`.

## Publication package

The successful controlled build run `31467777126` generated and committed the Guide 27 publication package in commit `0c1829d472997d283f2a96c0e9fff9b5f625179e` under:

`project/revision-2026/guide-27/publication-candidate/`

The committed package contains the three controlled Markdown source editions plus, for each language edition, a DOCX and searchable PDF publication candidate. It also contains:

- `GUIDE_27_PUBLICATION_QA_MANIFEST.json`; and
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

- English: 12 pages, 29,420 extractable characters;
- es-419: 13 pages, 33,634 extractable characters;
- pt-BR: 13 pages, 33,183 extractable characters.

All three editions are marked PASS in the publication QA manifest. SHA-256 hashes are committed for all six DOCX/PDF artifacts.

## Publication conclusion

**Publication Helper: PASS.**

The controlled Guide 27 publication candidates, QA manifest, and checksums exist on the revision branch and match successful controlled-build evidence. This gate does not merge PR #17 and does not imply completion of the separate Release Auditor gate.

## Assurance boundary

This is internal controlled-publication QA. It is not independent human certification, professional translation certification, accessibility certification, legal review, trade licensing approval, accreditation, or a guarantee of employment, admission, funding, certification, or earnings.
