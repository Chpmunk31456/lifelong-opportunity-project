# Guide 55 — Technical QA 08

**Stage:** Technical QA — **PASS**

Controlled masters:
- English: `GUIDE_55_HOME_HEALTH_AND_PERSONAL_CARE_AIDE_ENGLISH_v2.md` — 28,518 bytes at QA checkpoint
- Spanish `es-419`: `GUIDE_55_HOME_HEALTH_AND_PERSONAL_CARE_AIDE_SPANISH_es-419_v1.md` — 32,617 bytes at QA checkpoint
- Portuguese `pt-BR`: `GUIDE_55_HOME_HEALTH_AND_PERSONAL_CARE_AIDE_PORTUGUESE_pt-BR_v1.md` — 32,582 bytes at QA checkpoint

## Technical controls

- Three required UTF-8 Markdown source masters exist and are non-trivial in size.
- Each edition preserves the 26 numbered substantive sections in the frozen-source sequence.
- English, Spanish, and Portuguese preserve the same material source set and jurisdiction coverage: United States, Canada, and Colombia.
- Controlled URL targets are preserved across localization, including BLS, eCFR, DOL/WIOA, American Job Centers, Canada Job Bank, Canada.ca training/Labour Market Agreements, MinSalud, SENA Normograma, and SENA.
- U.S. federal hour controls preserve the same numeric meaning in all editions: **75 total hours**, **16 classroom hours before 16 supervised practical hours**, and **12 hours annual in-service training**.
- NOC **44101**, **17%** U.S. growth, and all controlled U.S./Canada labor-market values preserve numeric meaning across language editions.
- Locale-aware punctuation is intentional. pt-BR uses period thousands separators and comma decimals where appropriate; this is not a parity failure.
- No replacement-character (`�`) or known mojibake text is intentionally present in the controlled v2/v1 masters. The legacy Portuguese binary filename defect is not propagated into the new controlled master filename or text.
- Markdown contains dollar-denominated wage strings. Publication must use Pandoc reader **`gfm-tex_math_dollars`** (not plain `gfm`) so currency dollar signs cannot be parsed as TeX inline math. This is a mandatory carry-forward control from the Guide 53 publication incident.
- Publication must validate DOCX package integrity, searchable PDF text, all-page rendering, strict edge clipping, page-count reconciliation, metadata, and SHA-256 checksum coverage before either Publication or Release Audit may pass.
- Publication validation must compare localized numeric meaning rather than require English thousands/decimal punctuation in pt-BR.

## Assurance boundary

Technical QA verifies controlled-source structure, localization parity, encoding/formatting risk controls, source/number consistency, and publication prerequisites. It is not independent human certification, professional translation certification, clinical/legal review, accessibility certification, accreditation, licensure approval, or an employment/earnings guarantee.

## Result

**PASS.** Guide 55 may advance to controlled publication. Publication and Release Audit remain fail-closed until generated artifacts pass the publication workflow.
