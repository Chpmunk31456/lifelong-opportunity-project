# Guide 45 — Trilingual Technical QA Gate 08

**Guide:** 45 — Water and Wastewater Treatment Plant Operator  
**Branch:** `revision/guide-00-100-2026`  
**Workflow:** `Guide 45 controlled publication build`  
**Workflow-source commit:** `5c19373221c9654cc9bc94dfa4569a2cd062c650`  
**Publication-candidate commit:** `2bd1407ca5bff82e1abaa30e8199011702a4107b`  
**Gate result:** **PASS**

## Preconditions

Baseline Inventory, Current-source Research, English Editorial, Evidence/Traceability, English Source Freeze, Spanish Localization (`es-419`), and Portuguese Localization (`pt-BR`) were PASS before this gate. The prior technical precheck remained fail-closed until a controlled publication build produced auditable artifacts.

## Corrective QA history

The initial Guide 45 workflow validator inherited a wording assumption that did not match the controlled English source: it looked for `using ai responsibly`, while the frozen English edition correctly uses the heading `Responsible use of AI`. The validator was corrected in `5c19373221c9654cc9bc94dfa4569a2cd062c650` without changing or weakening Guide 45 content, safety controls, authorization boundaries, source requirements, licensing caveats, AI/privacy controls, or non-guarantee language.

The corrected workflow also preserves the precheck rule for source probing: explicit HTTP 404/410 results fail as broken links, while access-controlled, transport-only, server-side, or other non-content-verifiable responses are recorded as unverified rather than misrepresented as verified content.

## Successful controlled-build evidence

The publication-candidate commit `2bd1407ca5bff82e1abaa30e8199011702a4107b` was created by the controlled workflow with message `Build and validate Guide 45 publication candidates` after the final commit step.

The controlled workflow performed:

- trilingual publication-candidate freeze;
- exact 24-H2 structural parity checks;
- exact 21-source-URL set parity checks;
- controlled numeric, occupational-classification, terminology, placeholder, and UTF-8 checks;
- live source-link behavior probing under the fail-closed rules above;
- three DOCX and three PDF builds;
- DOCX archive/document-structure validation;
- searchable-PDF validation;
- every-page PDF rendering with automated blank-page, clipping, malformed-render, and page-count checks;
- publication metadata generation;
- SHA-256 generation for all six DOCX/PDF publication artifacts; and
- controlled publication-candidate commit.

The editions preserve the controlled occupation and pathway evidence, including SOC `51-8031`, O*NET `51-8031.00`, NOC `92101`, U.S. wage/outlook values, Canada Job Bank wage values, and the Colombia/SENA 12-month, 2,208-hour, and 48-hour pathway values.

## Artifact and render QA

`GUIDE_45_PUBLICATION_QA_MANIFEST.json` reports overall **PASS** and exact PDF/render page agreement:

- English: DOCX 25,196 bytes; PDF 193,561 bytes; 14 PDF pages / 14 rendered pages.
- Spanish (`es-419`): DOCX 26,514 bytes; PDF 199,380 bytes; 15 PDF pages / 15 rendered pages.
- Portuguese (`pt-BR`): DOCX 26,457 bytes; PDF 199,774 bytes; 15 PDF pages / 15 rendered pages.

`SHA256SUMS.txt` records SHA-256 digests for all three DOCX and all three PDF files. The publication-candidate directory contains the three frozen Markdown editions, three DOCX files, three searchable PDFs, the manifest, and checksums.

## Decision

**Trilingual Technical QA: PASS.** Guide 45 may proceed to Controlled Publication.

This is internal automated project QA. It does not claim independent human review, professional translation certification, accessibility certification, legal or environmental review, laboratory or engineering approval, electrical authorization, industrial-hygiene or medical review, confined-space or rescue qualification, operator licensing determination, accreditation, guaranteed funding, employment, or earnings.
