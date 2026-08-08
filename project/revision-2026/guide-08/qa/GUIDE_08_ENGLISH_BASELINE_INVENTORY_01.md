# Guide 08 — English Baseline Inventory 01

Date: 2026-08-08  
Branch: `revision/guide-00-100-2026`  
Guide: 08 — Human Resources Assistant

## Gate purpose

Establish an auditable inventory of the legacy English publication assets before substantive 2026 revision work begins. This gate records what exists; it does not treat the legacy edition as factually current, equivalent across formats, independently reviewed, certified, accredited, or publication-ready for the 2026 revision.

## Legacy English assets

- Markdown landing page: `08-human-resources-assistant/english/README.md`
  - Git blob SHA: `a89e1b615b262c33244bfcb9d40452bcdf3074f4`
  - Size: 2,086 bytes
  - Declared version: 1.0
  - Declared publication month: July 2026
  - The file begins with a UTF-8 BOM and therefore requires encoding normalization during controlled revision.
- DOCX: `08-human-resources-assistant/english/docx/Lifelong_Opportunity_Human_Resources_Assistant_Guide_English_v1.0.docx`
  - Git blob SHA: `f67a535e09890ea2a837dad341f3115e5c963b53`
  - Size: 47,365 bytes
- Searchable PDF: `08-human-resources-assistant/english/pdf/Lifelong_Opportunity_Human_Resources_Assistant_Guide_English_v1.0.pdf`
  - Git blob SHA: `0a46009a61de1c4cc592381c7d2c77660b6b57f7`
  - Size: 361,925 bytes

## Legacy README controls already present

The legacy English README states that the guide is free and accessible; identifies Human Resources Assistant as the career; links to DOCX and searchable PDF assets; includes a no-guarantee notice; invites correction and accessibility reports; attributes AI assistance; and references the CC BY-NC-SA 4.0 license.

The README also correctly warns that exact source equivalence and human linguistic review should not be assumed unless separately documented. That assurance boundary remains controlling for this revision.

## Required 2026 reconstruction sequence

1. Extract and reconcile the legacy DOCX and PDF deterministically.
2. Review substantive differences rather than relying on format similarity alone.
3. Research current official occupational, training, funding, apprenticeship, accessibility, privacy, labor-market, and Colombia pathway sources.
4. Build and fact-check a revised English v2 working master.
5. Complete editorial, claim-traceability, link, encoding, accessibility-readability, and source-freeze QA.
6. Produce neutral Latin American Spanish and Brazilian Portuguese editions from the frozen English source.
7. Run terminology and structural parity QA.
8. Build DOCX/PDF publication candidates and complete technical, metadata, checksum, render, and visual QA.

## Status

**PASS — baseline inventory established.**

Next controlled gate: deterministic extraction and reconciliation of the legacy English DOCX and PDF.
