# Guide 08 — Composite Source Decision 03

Date: 2026-08-08  
Branch: `revision/guide-00-100-2026`  
Guide: 08 — Human Resources Assistant

## Gate purpose

Resolve the HOLD from the deterministic legacy English DOCX/PDF extraction gate before reconstructing the 2026 English master. This is a source-reconciliation decision only. It is not factual revalidation, publication approval, independent human review, professional translation certification, accessibility certification, accreditation, legal review, or employment advice.

## Evidence reviewed

- Legacy English DOCX extraction from `Lifelong_Opportunity_Human_Resources_Assistant_Guide_English_v1.0.docx`
- Legacy searchable PDF extraction from `Lifelong_Opportunity_Human_Resources_Assistant_Guide_English_v1.0.pdf`
- `GUIDE_08_LEGACY_ENGLISH_EXTRACTION_RECONCILIATION_02.md`
- Deterministic comparison result: normalized character-sequence similarity 0.7289; normalized unique-token Jaccard similarity 0.9682
- DOCX extracted non-empty blocks: 258
- PDF pages: 10

## Substantive reconciliation

The lower character-sequence similarity is explained by PDF pagination, wrapped lines, repeated page headers/footers, table-of-contents dot leaders, duplicated table-cell extraction, and page-layout artifacts. The PDF-only material-token detector surfaced `0` and `4.0`; inspection found these are not substantive occupational facts requiring preservation as independent source content.

The DOCX extraction contains the same substantive 19-section guide structure and occupational content represented in the searchable PDF. No material narrative, duty, pathway, legal caveat, education requirement, wage claim, funding rule, accessibility control, cybersecurity control, or source URL was found solely in the PDF.

The DOCX therefore provides the cleaner textual baseline for reconstruction, while the PDF remains retained as rendering/layout evidence and a secondary cross-check.

## Controlled decision

**PASS — use the legacy English DOCX extraction as the primary textual baseline for Guide 08 reconstruction, with the PDF retained as secondary reconciliation evidence.**

This decision does not authorize reuse of legacy factual claims without current verification. All wage, outlook, education, funding, apprenticeship, accessibility, worker-rights, privacy, AI, and regional-pathway claims must be revalidated before the English v2 source can be frozen.

## Next controlled gate

Build the Guide 08 current-source evidence ledger, then reconstruct the English v2 working master with current official sources and clearly separated current non-government market estimates.