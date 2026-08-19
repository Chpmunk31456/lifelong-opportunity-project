# Guide 49 — Trilingual Technical QA 08

**Guide:** 49 — Dental Assistant  
**Branch:** `revision/guide-00-100-2026`  
**Date:** August 19, 2026  
**Gate status:** **PASS**

## Controlled run

Final Technical QA is based on corrected Guide 49 publication workflow run **32253559985**, head `fd39a6a3b87b8070a5f661d81feedd1c55c0f703`, conclusion **success**. The earlier run `32253244346` is not treated as a content failure; it failed on a context-insensitive safety validator that matched scam-warning text. The validator was corrected without weakening substantive clinical-scope controls and the full workflow was rerun.

## Trilingual structural and source parity

The successful run recorded:

- English H2 sections: **34**
- `es-419` H2 sections: **34**
- `pt-BR` H2 sections: **34**
- direct source URLs in each edition: **26**, with exact trilingual URL-set parity

Controlled occupation identifiers, wage/outlook values, Canada NOC/OaSIS values, Colombia CUOC/ReTHUS values, funding values, clinical-scope markers, AI/privacy boundaries, and the fail-closed Colombia program-duration limitation all passed automated presence/parity checks.

## Live-link behavior

No source returned a hard **404** or **410** failure. Multiple official/public sources returned HTTP 200. Some sources were access-controlled or transport-unverified from the GitHub runner, including BLS/CDC/HHS/Salary.com HTTP 403 responses and Government of Canada NOC/OaSIS TLS certificate-chain limitations. The workflow records these as verification limitations rather than silently claiming live validation. These limitations did not indicate a broken 404/410 source.

## DOCX, PDF, and rendering controls

All document-generation and integrity steps passed:

- three DOCX editions generated;
- three searchable PDF editions generated;
- all DOCX archives passed ZIP integrity and contained `word/document.xml`;
- all PDFs passed `pdfinfo` and searchable-text thresholds;
- all PDF pages rendered successfully;
- all-page render QA passed with **49 pages** total and no blank-page or clipping failure;
- publication metadata recorded exact PDF/render page-count equality for every edition.

`GUIDE_49_PUBLICATION_QA_MANIFEST.json` records overall status `PASS`:

- English: **16 PDF pages / 16 rendered pages** — PASS
- `es-419`: **17 / 17** — PASS
- `pt-BR`: **16 / 16** — PASS

## Checksums and render artifact

`SHA256SUMS.txt` records SHA-256 checksums for all six generated DOCX/PDF deliverables.

GitHub Actions artifact `guide49-rendered-pages`, artifact ID **9365427212**, was uploaded successfully from run `32253559985` with 50 files and SHA-256 artifact digest `70fbeb0c85da12d82cbb191a87448b3cf793645565c71a3c4380930656e78acf`.

## Safety and assurance boundary

The successful context-safe validator still rejects affirmative independent-scope statements. The guide continues to state that dental-assisting scope, radiography, expanded functions, credentialing, and delegated duties are jurisdiction-dependent; AI does not replace dentist judgment; and Colombia CUOC 53292 must not inherit higher-scope functions from a different occupational profile.

The package does not claim independent human review, professional translation certification, accessibility certification, accreditation, dental/legal review, clinical-practice authorization, certification-body approval, credential transfer, or guaranteed employment or earnings.

## Decision

**Technical QA: PASS.** The corrected complete Guide 49 trilingual publication run passed structural, source-set, numeric, scope, link-behavior, DOCX, searchable-PDF, all-page rendering, metadata, checksum, and artifact controls. The next permitted gate is **Publication**.
