# Guide 46 — Technical QA Precheck 08

**Guide:** 46 — Environmental Field Technician  
**Branch:** `revision/guide-00-100-2026`  
**Date:** August 18, 2026  
**Stage:** Technical QA Precheck  
**Result:** **PENDING / FAIL-CLOSED**

## Preconditions

At this precheck:

- Baseline Inventory: PASS
- Current-source Research: PASS
- English Editorial: PASS
- Evidence/Traceability: PASS
- English Source Freeze: PASS
- Spanish Localization: corrective action in progress; **not yet PASS**
- Portuguese Localization: PASS

Technical QA may not receive PASS until Spanish corrective QA is complete.

## Required deterministic controls

When the trilingual set is ready, the controlled Technical QA must independently verify:

1. exactly three controlled Markdown source editions: English, `es-419`, and `pt-BR`;
2. exactly **24 H2 sections** in each edition;
3. exact section-order/functional parity across all three editions;
4. exact equality of the **26 direct authoritative source URLs** across all three editions;
5. valid UTF-8 with no replacement characters, BOM defects in generated controlled files, legacy `T_cnico` substitutions, placeholders, or translation-pending markers;
6. controlled occupational identifiers: `19-4042`, `19-4042.00`, and `22300`;
7. U.S. controlled values: `49,490`, `23.79`, `36,130`, `85,630`, `40,400`, `42,100`, `+1,600`, `+4 percent`, and about `5,600` openings per year, preserving 2024/2034 context;
8. Canadian controlled values: `CAD $22.00`, `CAD $33.89`, and `CAD $51.10` hourly, preserving the NOC 22300 boundary;
9. Colombia/SENA controlled values: `2,208 hours`, `2,208 hours`, and `2,112 hours`, tied to the correct programs;
10. presence in every edition of sampling/chain-of-custody controls, data-integrity limits, stop-and-escalate language, conditional HAZWOPER, employer-controlled PPE/respirators, confined-space boundaries, responsible-AI restrictions, privacy/cybersecurity protections, funding caveats, and outcome non-guarantees;
11. absence of hazardous step-by-step instructions, universal HAZWOPER claims, self-selected respirator guidance, compliance authority, fabricated-field-data permission, or cross-border credential equivalence;
12. live source-link behavior probing with explicit 404/410 treated as broken; access-controlled, transport-limited, server-side, or otherwise non-content-verifiable responses recorded as unverified rather than falsely claimed verified;
13. controlled generation of three DOCX and three searchable PDF editions;
14. DOCX archive/document-structure validation;
15. searchable-text and Unicode sanity checks for all PDFs;
16. rendering of **every PDF page** to images with malformed/blank/clipping checks and exact rendered-page/PDF-page-count agreement;
17. publication metadata manifest with edition-level PASS state, file sizes, page counts, and assurance boundary;
18. SHA-256 checksums for all six DOCX/PDF publication artifacts; and
19. controlled publication-candidate commit before Publication or Release Audit may pass.

## Current blocker

The Spanish v2 source originally contained one untranslated common noun (`sewer`) in the high-risk location list. A first controlled replacement removed the English word but produced a duplicated Spanish noun. A refined one-time correction has been triggered to normalize the list to distinct Spanish terms while preserving the frozen English hazard meaning.

This is a localization-quality blocker only. No English source, research evidence, occupational value, safety boundary, or environmental-data-integrity rule is being altered.

## Decision

**Technical QA remains PENDING.** It must fail closed until Spanish Localization is formally PASS and the deterministic trilingual build completes successfully.

This precheck does not claim independent human review, professional translation certification, accessibility certification, legal or environmental review, laboratory or engineering approval, industrial-hygiene or medical review, hazardous-waste qualification, respiratory-protection qualification, confined-space or rescue qualification, sampling-method approval, regulatory/licensing determination, accreditation, guaranteed funding, employment, or earnings.
