# Guide 04 — Composite Source Decision 05

Date: 2026-08-08
Branch: `revision/guide-00-100-2026`
Guide: 04 — Project Coordinator

## Purpose

Close the substantive reconciliation gate between the legacy English DOCX and PDF before the 2026 English working master is constructed. This record is an internal source-control decision. It is not factual revalidation, publication approval, independent human review, certification, accreditation, or accessibility certification.

## Inputs reviewed

- Legacy DOCX Git blob SHA: `6fe21ac155c8962d65b6a13d389239dc6b710cbd`
- Legacy PDF Git blob SHA: `f1119a0b8a2ee680d7bec3acd67d8844e8508fc8`
- Deterministic extraction record: `GUIDE_04_LEGACY_ENGLISH_EXTRACTION_RECONCILIATION_04.md`
- DOCX extraction: `evidence/guide04_legacy_docx_extract.txt`
- PDF extraction: `evidence/guide04_legacy_pdf_extract.txt`
- Extraction workflow run: `31243218561`
- Extraction evidence commit: `471cbead5bdc324d2520acab34dcbf4c13035942`

## Reconciliation findings

The extraction workflow reported:

- 258 non-empty DOCX blocks.
- 10 searchable PDF pages.
- 19,329 extracted DOCX characters.
- 27,352 extracted PDF characters.
- normalized character-sequence similarity of `0.7084`.
- normalized unique-token Jaccard similarity of `0.9721`.
- no material token/fact set detected only in the DOCX.
- automated PDF-only fact tokens `0` and `4.0`.

The lower character-sequence score is consistent with PDF pagination, repeated page headers, line wrapping, bullet/table serialization, and table-of-contents leader noise. The PDF repeatedly contains the page header `Lifelong Opportunity Guides | Project Coordinator v1.0` and the license line `CC BY-NC-SA 4.0`; those rendering-layer strings account for the detected `4.0` token rather than a separate occupational claim. The isolated `0` is likewise non-substantive numeric/layout noise in the extracted PDF and does not identify a distinct career fact or requirement.

The substantive section inventory is aligned across the two artifacts: career definition and duties; fit and boundaries; pay/outlook; education and credentials; employer-supported learning; accessibility; privacy/cybersecurity/ethical AI; portfolio evidence; interview preparation; 30/60/90-day entry plan; advancement and portability; enrollment verification; decision scorecard; twelve-week action plan; worksheets; and sources/version maintenance. The PDF additionally preserves visual table order and repeated headers that should be treated as presentation evidence, not separate source content.

## Controlled source decision

**PASS — composite-source reconciliation is cleared.**

For the 2026 English reconstruction:

1. Treat the legacy DOCX extraction as the primary textual baseline because it preserves paragraph and table structure without pagination noise.
2. Use the legacy PDF extraction as a secondary parity/layout source to confirm table content, pagination-era presentation, headers, and any apparent omissions.
3. Do not inherit legacy wage, outlook, education, funding, credential, apprenticeship, jurisdictional, or link claims merely because both artifacts agree. Those claims must still pass the current-source evidence gate before inclusion.
4. Do not carry forward the legacy statement that a service period “may last up to two years” as a general rule; employer repayment/service obligations are contract- and jurisdiction-dependent and require current, source-specific wording.
5. Do not carry forward healthcare-specific pathway language unless it is relevant to Project Coordinator work in the section where it appears.
6. Preserve uncertainty where the title spans industries and does not map cleanly to a single occupation, NOC, credential, license, or wage series.

## Next gate

The legacy extraction/reconciliation HOLD is closed. The next controlled gate is construction of the expanded 2026 English working master from this reconciled baseline plus the already completed Guide 04 current-source evidence intake, followed by factual/editorial/link/accessibility QA before translation.
