# Guide 52 Publication Gate 09

Date: 2026-08-19  
Status: **PASS**

## Package

The publication candidate contains Markdown, DOCX, and PDF editions for controlled English, neutral Latin American Spanish (`es-419`), and Brazilian Portuguese (`pt-BR`). The nine content artifacts are recorded in `GUIDE_52_PUBLICATION_QA_MANIFEST.json` and sealed by `SHA256SUMS.txt`.

## Render and visual inspection

- Canonical DOCX rendering completed through the document render workflow, and the final PDF files were rendered independently with Poppler.
- All 35 pages were inspected in both render paths: English 11, Spanish 12, Portuguese 12.
- Covers, headings, body text, bullets, numbered lists, hyperlinks, running headers, page numbers, and source lists are legible.
- The three numbered sequences restart correctly at 1; bullet markers and spacing are visible in all editions.
- No clipping, overlap, missing glyphs, unintended blank content pages, or overflow was observed.
- Automated PDF bounding-box checks found 0 words outside the page boundaries. All word boxes remained between x=72.1 and x=540.166 points; headers and footers remained within the page.

## Publication defects caught and corrected

The render-and-verify cycle detected and corrected two pre-seal conversion defects:

1. Pandoc initially interpreted paired dollar signs in compensation sentences as inline math. The final build disables dollar-delimited math parsing, contains no Office Math objects, and renders every currency value as ordinary prose.
2. Pandoc's generated list IDs did not render markers reliably through LibreOffice. The final build uses the verified `ListBullet` style and separate restart-safe numbering IDs. All 103 bullets and 18 numbered items are visible and structurally represented in every DOCX edition.

The corrected artifacts were rebuilt, re-audited, and rerendered in full before checksums were sealed.

## Accessibility and structure

- DOCX accessibility audit: 0 high-severity and 0 medium-severity findings in every edition.
- The 15 low-severity findings per edition are visible raw URLs retained in the source list for auditability.
- Each DOCX contains 15 clickable external hyperlinks, 103 bullet paragraphs, 18 numbered-list paragraphs, real heading styles, language metadata, localized document titles, author/subject metadata, running headers, and page-number fields.
- No Office Math objects or encoding replacement characters are present.
- PDF editions are tagged and searchable.

## PDF validation

| Edition | Pages | Extracted text | Metadata title | Result |
|---|---:|---:|---|---|
| English | 11 | 23,581 bytes | Guide 52 — Surgical Technologist | PASS |
| Spanish (`es-419`) | 12 | 27,759 bytes | Guía 52 — Tecnólogo/a quirúrgico/a | PASS |
| Portuguese (`pt-BR`) | 12 | 27,383 bytes | Guia 52 — Tecnólogo/a cirúrgico/a | PASS |

All PDFs are US Letter, PDF 1.7, tagged, and carry the author `Alberto (Al) Leiva` and the subject `Lifelong Opportunity career and education guide`.

## Integrity

- Each publication Markdown file is byte-identical to its corresponding frozen trilingual master.
- SHA-256 checksums were generated for all nine content artifacts and revalidated successfully with `sha256sum -c`.
- File sizes, checksums, page counts, searchable-text counts, corrected pre-seal defects, and validation results are recorded in the publication manifest.
- The publication package is ready for the controlled release audit.

## Decision

**PASS.** Guide 52 meets the publication gate. Release remains controlled by the separate release-audit stage; the pull request must remain draft and unmerged.
