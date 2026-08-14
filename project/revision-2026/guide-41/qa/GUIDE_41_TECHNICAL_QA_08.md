# Guide 41 — Trilingual Technical QA Gate 08

**Guide:** 41 — Carpenter and Cabinetmaking Technician  
**Branch:** `revision/guide-00-100-2026`  
**Date:** 2026-08-14  
**Stage:** Technical QA Helper  
**Result:** PASS

## Evidence basis

Controlled workflow run `31837393020` completed successfully after retained render evidence identified Pandoc dollar-sign math parsing as the cause of the English wage-bullet overflow. The publication reader was repaired to preserve currency as ordinary text, and the complete trilingual technical and publication workflow was rerun from the authoritative branch state.

## Controls completed

- Structural parity: PASS — English, `es-419`, and `pt-BR` each contain 18 level-two sections and controlled version 2.0 metadata.
- Exact frozen-English source URL-set parity: PASS — all three editions contain the same 13 controlled source URLs.
- Numeric, date, currency, training-hour, wage, certification, apprenticeship, and funding controls: PASS for O*NET/BLS, NOC/Job Bank, SENA, Registered Apprenticeship, Canadian apprenticeship supports, and supplementary private-market values.
- Occupation and qualification boundaries: PASS — construction carpentry, cabinetmaking, jurisdiction-specific certification, Red Seal, and credential limitations remain distinct.
- Safety controls: PASS — machine guarding, PPE, respiratory/hearing/fall protection, lockout/tagout, hazardous equipment training, and stop/escalate boundaries remain intact.
- AI, privacy, cybersecurity, and assurance-boundary controls: PASS.
- UTF-8/BOM/replacement-character and unresolved-placeholder controls: PASS.
- Live-link behavior: PASS — official/public links returned successful responses; CareerOneStop and Salary.com were access-controlled with HTTP 403 rather than explicitly broken; no HTTP 404/410 source failure remained.
- DOCX package integrity: PASS for all three editions.
- Searchable PDF integrity: PASS for all three editions; each exceeded the controlled extractable-text threshold and contained no Unicode replacement character.
- All-page raster rendering: PASS — 29 of 29 pages rendered without blank-page, malformed-page, or edge-clipping failure. The repaired English page 6 retained 112 pixels of right margin at the controlled render resolution.
- Lists, headings, links, and page layout: PASS under rendered-page inspection; no remaining character-spaced currency text, clipped source link, malformed list, or table defect was detected.
- Publication metadata, filenames, byte counts, page counts, artifact inventory, and SHA-256 checksum generation: PASS.

The controlled publication build produced commit `545c9dbaf8f480a2158dc16cc134a471a8928d8c` and publication manifest status `PASS` for all three editions: 9 English pages, 10 Spanish pages, and 10 Portuguese pages.

## Disposition

**Technical QA: PASS.** Guide 41 may advance to the Publication Helper gate.

This is internal controlled QA evidence. It does not claim independent human certification, professional translation certification, accessibility certification, legal review, accreditation, certification-body approval, or guaranteed employment or earnings outcomes.
