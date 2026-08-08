# Guide 03 — Source Reconciliation Decision 04

Date: 2026-08-07
Branch: `revision/guide-00-100-2026`
Guide: 03 — Medical Billing and Coding Specialist

## Gate purpose

Resolve the legacy English DOCX/PDF source-reconciliation HOLD before the revised 2026 English working master is treated as the controlled drafting source. This gate reconciles source content only. It does not represent independent human certification, accreditation, legal review, coding certification, accessibility certification, translation certification, or final publication approval.

## Inputs reviewed

- Legacy DOCX extraction: `project/revision-2026/guide-03/qa/evidence/guide03_legacy_docx_extract.txt`
- Legacy searchable-PDF extraction: `project/revision-2026/guide-03/qa/evidence/guide03_legacy_pdf_extract.txt`
- Automated extraction/reconciliation record: `project/revision-2026/guide-03/qa/GUIDE_03_LEGACY_ENGLISH_EXTRACTION_RECONCILIATION_02.md`
- Current-source evidence intake: `project/revision-2026/guide-03/qa/GUIDE_03_CURRENT_SOURCE_EVIDENCE_INTAKE_03.md`
- Revised English working master: `project/revision-2026/guide-03/source/GUIDE_03_ENGLISH_WORKING_MASTER_v2.md`

## Deterministic extraction evidence

The successful extraction workflow reported:

- DOCX extracted non-empty blocks: **258**
- PDF pages: **10**
- DOCX extracted characters: **19,396**
- PDF extracted characters: **27,602**
- normalized character-sequence similarity: **0.7265**
- normalized unique-token Jaccard similarity: **0.9711**
- material token/fact set only in DOCX: **none detected**
- material token/fact set only in PDF: **`0, 4.0`**

The lower character-sequence score is consistent with PDF pagination, repeated headers/footers, table flattening, line wrapping, bullets and spacing artifacts. The much higher token overlap and the absence of substantive DOCX-only fact tokens support using the DOCX as the cleaner structural baseline while checking the PDF for presentation-derived or table-derived material.

## Substantive reconciliation

Review of the extracted content confirms that the same substantive legacy guide structure is present across both formats: introductory material, Sections 1–19, occupational description, duties/work cycle, fit/safety, ethics/boundaries, pay/outlook, education/credentials, employer-supported learning, accessibility, privacy/cybersecurity/ethical AI, portfolio/interview guidance, 30/60/90-day planning, advancement/exit planning, verification checklist, decision scorecard, twelve-week plan, worksheets, and source/versioning material.

The PDF extraction contains expected layout-derived repetition and flattening, including repeated page headers/footers, page markers, table text rendered in reading order, spacing around punctuation/hyphens, and duplicated table-label text. Those artifacts explain most of the character-level divergence and are not treated as independent substantive source content.

No material PDF-only occupational claim, wage claim, credential requirement, legal requirement, privacy rule, education pathway, funding promise, or career recommendation was identified that must be preserved separately from the DOCX baseline.

The PDF-only fact tokens `0` and `4.0` do not establish a separate substantive claim requiring incorporation into the 2026 source master; they arise within formatting/license/version extraction context and are not treated as occupational evidence.

## Composite-source decision

**PASS — legacy source reconciliation complete.** The legacy DOCX is accepted as the primary structural/content baseline because it preserves the cleaner document hierarchy and tables. The searchable PDF is retained as corroborating audit evidence and a check against missing presentation-derived content.

The 2026 revision is not a verbatim republication of either legacy artifact. The revised English working master may restructure, qualify, correct, expand, or remove legacy language when supported by current authoritative evidence and the project’s expanded opportunity standard.

## Working-master status

`project/revision-2026/guide-03/source/GUIDE_03_ENGLISH_WORKING_MASTER_v2.md` may now serve as the controlled English drafting master for factual, editorial, terminology, accessibility, link, translation-readiness, and publication QA.

It is **not yet frozen for translation**. Current-source facts, links, occupational mappings, wage figures, credential descriptions, coding-system statements, privacy language, Canada/Colombia pathways, and natural-language quality still require their downstream gates before translation begins.

## Next gate

Perform focused current-source revalidation against primary/official sources where available, reconcile any changed values or scope language into the English working master, and record a factual/source-control PASS before English freeze.
