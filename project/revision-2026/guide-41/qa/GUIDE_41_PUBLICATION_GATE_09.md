# Guide 41 — Publication Gate 09

**Guide:** 41 — Carpenter and Cabinetmaking Technician  
**Branch:** `revision/guide-00-100-2026`  
**Date:** 2026-08-14  
**Status:** PASS

Technical QA Gate 08 is PASS.

GitHub Actions run `31837393020` completed successfully and generated the controlled English, `es-419`, and `pt-BR` Markdown freezes plus DOCX/PDF publication candidates. The generated artifacts landed in commit `545c9dbaf8f480a2158dc16cc134a471a8928d8c`.

## Publication controls

- DOCX generation and ZIP/package integrity: PASS for all three editions.
- PDF generation and structural inspection: PASS for all three editions.
- Searchable text: PASS — each PDF exceeded the controlled extractable-text threshold and contained no Unicode replacement-character defect.
- Page counts: PASS — 9 English, 10 Spanish, and 10 Portuguese pages.
- All-page raster rendering: PASS — 29 of 29 pages rendered.
- Automated blank-page, edge-clipping, and malformed-render controls: PASS.
- Manual evidence review of the corrected currency page: PASS — no character-spaced math rendering or overflow remains.
- Source-list rendering, working hyperlinks, and exact 13-URL-set parity: PASS.
- Live source-link behavior: PASS under the fail-closed validator; no explicit 404/410 remained.
- Publication metadata manifest: PASS for English, `es-419`, and `pt-BR`.
- SHA-256 checksums: PASS for all six DOCX/PDF binary artifacts and independently matched after the workflow commit.
- Filenames, byte counts, version metadata, and artifact completeness: PASS.

The controlled publication-candidate directory contains the three Markdown freezes, six DOCX/PDF artifacts, `GUIDE_41_PUBLICATION_QA_MANIFEST.json`, and `SHA256SUMS.txt`.

**Publication Helper: PASS.** Guide 41 may advance to Release Auditor.

This record documents internal controlled publication QA only. It does not represent independent human certification, professional translation certification, accessibility certification, legal review, accreditation, certification-body approval, or guaranteed employment or earnings outcomes.
