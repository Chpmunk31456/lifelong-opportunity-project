# Guide 02 — English post-correction recheck and source-freeze gate

Date: 2026-08-07
Guide: 02 — Peer Support Specialist
Branch: `revision/guide-00-100-2026`
Status: **PASS — English source freeze**

## Purpose

Close the final factual-source correction identified during the preceding PDF reconciliation and link-retest gate, then record whether the reconstructed 2026 English working master is sufficiently controlled to serve as the translation source for the neutral Latin American Spanish and Brazilian Portuguese editions.

## Correction applied

The English working master previously stated that ZipRecruiter’s non-government Peer Support Specialist estimate was current as of July 30, 2026. The source revalidation evidence identified the correct displayed date as **July 16, 2026** while leaving the supported estimate unchanged at **$41,023/year ($19.72/hour)**.

Both occurrences in the controlled English working master were corrected:

- narrative income section: `as of July 16, 2026`;
- controlled source ledger: `As of July 16, 2026`.

The estimate remains explicitly labeled as a non-government market estimate and is not represented as an official wage statistic or guarantee.

## Focused post-correction recheck

The following checks passed after the correction:

- the narrative and source-ledger dates agree;
- the $41,023/year and $19.72/hour values were not changed;
- BLS remains explicitly labeled as the official Community Health Worker proxy rather than a dedicated peer-support wage series;
- Canada Job Bank remains explicitly labeled as broader NOC 42201 occupational data;
- Colombia and Latin America language continues to prohibit invented national peer-support wage claims where no directly comparable series has been verified;
- the existing role-boundary, credential-portability, funding, apprenticeship, employer-support, accessibility, privacy, ethical-AI, and regional-pathway controls remain intact;
- repository search returned no remaining occurrence of the superseded exact string `July 30, 2026` after the correction.

Fresh BLS revalidation on 2026-08-07 continues to support the Community Health Worker proxy values used in the master: May 2024 median annual wage **$51,030 ($24.54/hour)** and **11%** projected employment growth from 2024 to 2034.

## Structural-parity decision

The English working master retains the controlled 19-section career-guide structure plus the source ledger and versioning controls established in the reconstruction process. The prior PDF-only substantive reconciliation found no missing substantive section requiring restoration. The final source-date correction did not alter structure, section order, scope, or substantive pathway coverage.

**Structural parity: PASS.**

## English source-freeze decision

The cumulative English gates now provide an auditable chain covering baseline selection, reconstruction, source/link revalidation, source-correction closure, editorial/terminology/accessibility/encoding/claim-traceability intake, PDF-only substantive reconciliation, final link retest, and the focused post-correction recheck recorded here.

Accordingly, `project/revision-2026/guide-02/source/GUIDE_02_ENGLISH_WORKING_MASTER_v2.md` is **frozen as the controlled English translation source** for Guide 02.

This freeze does **not** mean the guide is a final publication candidate. DOCX, PDF, rendering, metadata, checksum, trilingual terminology/parity, link, and publication QA remain required after the Spanish and Brazilian Portuguese editions are produced.

## Certification and review control

This gate is repository QA evidence produced with AI assistance. It does not claim independent human certification, professional translation certification, accessibility certification, accreditation, legal review, medical review, or external publication approval.

## Next controlled gate

1. Produce the neutral Latin American Spanish edition from the frozen English source.
2. Produce the Brazilian Portuguese edition from the same frozen English source.
3. Run cross-language terminology and structural-parity QA before DOCX/PDF publication-candidate generation.
