# Guide 02 — Market-Date Refresh Gate 22

Date: 2026-08-07  
Branch: `revision/guide-00-100-2026`

## Gate purpose

This record captures the controlled freshness correction identified during the final external-link and source revalidation for Guide 02. It is a factual-source maintenance gate, not a publication approval and not an independent certification.

## Verified change

The non-government ZipRecruiter Peer Support Specialist market estimate still reports **US$41,023/year (US$19.72/hour)**, but its page now displays **As of Aug 7, 2026**. The previous Guide 02 working masters still contain the older July 16, 2026 as-of date.

Required trilingual source corrections before artifact generation:

- English: `August 7, 2026`
- Neutral Latin American Spanish: `7 de agosto de 2026`
- Brazilian Portuguese: `7 de agosto de 2026`

No wage amount or source-classification change is required. ZipRecruiter must remain clearly labeled as a current **non-government market estimate**, not an official wage statistic or guarantee.

## Control improvement completed

The reusable `scripts/guide02_translation_parity.py` control has been updated to require the August 7, 2026 date in all three language masters. This intentionally makes the current source set fail closed until the three working masters are corrected. The checker must not be weakened merely to restore a green workflow.

## Current decision

**HOLD — source-date refresh required before DOCX/PDF generation.**

The factual correction is small and fully defined. It does not reopen the previously completed Guide 02 English source research, translation-intake, terminology, structural, numeric, source-ledger, or claims-control reviews except for the affected date field.

## Next gate

1. Replace the stale July 16, 2026 market as-of date in the English, Spanish, and Brazilian Portuguese working masters.
2. Run the focused trilingual parity workflow.
3. If parity passes, proceed to DOCX/PDF generation, rendering inspection, metadata, checksums, publication manifest, and final Guide 02 publication-candidate QA.

No independent human certification, professional translation certification, accreditation, legal review, medical review, or accessibility certification is claimed by this gate.
