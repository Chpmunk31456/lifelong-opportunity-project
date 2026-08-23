# Guide 03 — Legacy Source Reconciliation Decision 04

Date: 2026-08-07
Branch: `revision/guide-00-100-2026`
Guide: 03 — Medical Billing and Coding Specialist

## Gate purpose

Close the legacy DOCX/PDF source-reconciliation hold before construction of the revised 2026 English working master. This control compares the deterministic extracts already committed under QA 02 and identifies whether either legacy artifact contains unique substantive content that must be preserved.

## Evidence reviewed

- `project/revision-2026/guide-03/qa/evidence/guide03_legacy_docx_extract.txt`
- `project/revision-2026/guide-03/qa/evidence/guide03_legacy_pdf_extract.txt`
- `project/revision-2026/guide-03/qa/GUIDE_03_LEGACY_ENGLISH_EXTRACTION_RECONCILIATION_02.md`
- `project/revision-2026/guide-03/qa/GUIDE_03_CURRENT_SOURCE_EVIDENCE_INTAKE_03.md`

QA 02 reported normalized character-sequence similarity of 0.7265 and unique-token Jaccard similarity of 0.9711. The lower character score is consistent with PDF pagination, headers, line wrapping, bullets, table flattening, hyphenation and other extraction noise. The substantially higher token overlap is more consistent with the two artifacts carrying the same underlying substantive edition.

## Substantive reconciliation

A section-by-section review of the extracts found the same 19-section structure, the same core prose, the same role-definition language, the same work-cycle controls, the same pay/outlook statements, the same education and employer-support guidance, the same accessibility/privacy/AI controls, the same portfolio/interview/30-60-90-day material, the same enrollment checklist, the same twelve-week plan, the same worksheets and the same source list.

No material PDF-only paragraph, table entry, instruction, wage fact, credential statement, legal/privacy statement, source URL or reader-protection control was identified that is absent from the DOCX-derived content.

The automated fact-set items reported as PDF-only (`0`, `4.0`) are extraction artifacts associated with formatting/license text and do not establish unique occupational content.

The DOCX extraction is therefore the cleaner reconstruction base because it preserves paragraph and table semantics without repeated page headers, line-wrap fragmentation or PDF hyphenation artifacts. The searchable PDF remains corroborating layout/visible-edition evidence.

## Controlled decision

**PASS — legacy source reconciliation complete.** The DOCX-derived substantive content may be used as the principal legacy reconstruction base, with the PDF retained as corroborating evidence and checked whenever layout, table interpretation, pagination or extraction ambiguity matters.

This decision closes the QA 02 HOLD for source reconciliation. It does not validate the legacy facts as current and does not authorize publication of the old edition without revision.

## Next gate

Construct the 2026 English working master from the reconciled legacy content plus the current-source controls in QA 03. Preserve useful reader-protection material, correct outdated or overbroad claims, distinguish exact-title evidence from occupational proxies, and keep jurisdiction-specific information explicitly qualified.
