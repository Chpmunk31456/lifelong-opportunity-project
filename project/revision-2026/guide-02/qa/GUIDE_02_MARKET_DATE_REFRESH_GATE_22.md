# Guide 02 — Market-Date Refresh Gate 22

Date: 2026-08-07  
Branch: `revision/guide-00-100-2026`

## Gate purpose

This record captures the controlled freshness correction identified during the final external-link and source revalidation for Guide 02. It is a factual-source maintenance gate, not a publication approval and not an independent certification.

## Verified change

The non-government ZipRecruiter Peer Support Specialist market estimate still reports **US$41,023/year (US$19.72/hour)**, but its page now displays **As of Aug 7, 2026**. At the time this gate opened, the Guide 02 working masters still contained the older July 16, 2026 as-of date.

Required trilingual source corrections at gate opening:

- English: `August 7, 2026`
- Neutral Latin American Spanish: `7 de agosto de 2026`
- Brazilian Portuguese: `7 de agosto de 2026`

No wage amount or source-classification change was required. ZipRecruiter remains clearly labeled as a current **non-government market estimate**, not an official wage statistic or guarantee.

## Control improvement completed

The reusable `scripts/guide02_translation_parity.py` control was updated to require the August 7, 2026 date in all three language masters. This intentionally made the then-current source set fail closed until the three working masters were corrected. The checker was not weakened merely to restore a green workflow.

## Gate-opening decision

**HOLD — source-date refresh required before DOCX/PDF generation.**

This HOLD records the state when Gate 22 opened. It is retained for audit history and is superseded by the resolution below.

## Resolution

**RESOLVED — the required source-date refresh was applied in all three controlled masters, the focused trilingual parity control passed, and the publication candidates were regenerated from the corrected current sources.**

Post-editorial publication rebuild workflow run `31228466140` completed successfully on 2026-08-07. The refreshed publication-candidate package landed in commit `3ea5bed76c1b22bab1b2fb95b4ffab039c5efb3d` after trilingual parity, DOCX/PDF generation, document/link/encoding/metadata QA, PDF extractability/title/page checks, checksum generation, and first-page rendering all passed.

The factual correction did not reopen the previously completed Guide 02 English source research, translation-intake, terminology, structural, numeric, source-ledger, or claims-control reviews except where later controlled editorial corrections were explicitly reviewed and rebuilt.

## Completed next-gate sequence

1. Stale July 16, 2026 market as-of dates were replaced in the English, Spanish, and Brazilian Portuguese working masters.
2. Focused trilingual parity passed.
3. DOCX/PDF generation, rendering inspection evidence, metadata, checksums, publication manifest, and final Guide 02 publication-candidate QA completed successfully.

No independent human certification, professional translation certification, accreditation, legal review, medical review, or accessibility certification is claimed by this gate.
