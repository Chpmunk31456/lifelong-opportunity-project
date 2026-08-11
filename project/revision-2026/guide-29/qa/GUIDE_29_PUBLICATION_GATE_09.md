# Guide 29 Publication Gate 09

**Guide:** 29 — HVAC Technician and Refrigeration Mechanic  
**Branch:** `revision/guide-00-100-2026`  
**Gate:** Publication Helper  
**Status:** PASS  
**QA date:** August 11, 2026

## Preconditions

Technical QA is PASS in `GUIDE_29_TECHNICAL_QA_GATE_08.md`.

## Publication package

Successful controlled build run `31505735657` generated and committed the Guide 29 publication package in commit `27cc66346ff82813c7277e4a4be41a0630aabfc6` under:

`project/revision-2026/guide-29/publication-candidate/`

The package contains the three controlled Markdown editions, three DOCX publication candidates, three searchable PDFs, `GUIDE_29_PUBLICATION_QA_MANIFEST.json`, and `SHA256SUMS.txt`.

## Publication checks

The committed publication manifest reports overall status **PASS** for:

- trilingual structural parity;
- required source URLs and URL parity;
- UTF-8/BOM controls;
- placeholder scan;
- DOCX ZIP integrity;
- searchable PDF text;
- all-page raster rendering;
- metadata manifest; and
- SHA-256 checksums.

PDF results are:

- English: 13 pages, 29,831 extractable characters;
- es-419: 14 pages, 34,222 extractable characters;
- pt-BR: 14 pages, 32,650 extractable characters.

All three editions are marked PASS. SHA-256 hashes are committed for all six binary artifacts. Rendered-page evidence is retained in workflow artifact `guide29-rendered-pages` from run `31505735657`.

## Publication conclusion

**Publication Helper: PASS.**

The Guide 29 controlled publication package exists on the live revision branch and matches successful controlled-build evidence. This gate does not merge PR #17 and remains separate from the Release Auditor gate.

## Assurance boundary

This is internal controlled-publication QA. It is not independent human certification, professional translation certification, accessibility certification, legal review, environmental-regulatory approval, trade licensing approval, accreditation, or a guarantee of employment, admission, funding, certification, or earnings.
