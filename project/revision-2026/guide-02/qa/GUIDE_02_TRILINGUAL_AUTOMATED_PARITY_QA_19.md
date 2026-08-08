# Guide 02 — Trilingual Automated Parity QA 19

Date: 2026-08-07  
Branch: `revision/guide-00-100-2026`  
Languages: English, neutral Latin American Spanish (`es-419`), Brazilian Portuguese (`pt-BR`)

## Result

**PASS — deterministic trilingual parity workflow completed successfully and remains green after the final controlled source/editorial corrections.**

GitHub Actions workflow: `Guide 02 translation parity QA`  
Initial successful controlled run: `31205048941`  
Latest verified successful run after final Guide 02 QA reconciliation: `31228632766`  
Checker: `scripts/guide02_translation_parity.py`

This is an automated consistency gate. It is **not** professional translation certification, independent human review, accreditation, accessibility certification, legal review, medical review, or publication approval.

## Automated controls passed

- exact numbered-section sequence 1 through 19 in all three working masters;
- strict UTF-8 decoding, no BOM, no Unicode replacement characters, and LF line endings;
- high-impact income values and dates preserved across all three languages;
- BLS official-proxy values and 2024–2034 outlook period preserved;
- ZipRecruiter non-government market values and **August 7, 2026** source date preserved;
- Canada NOC 42201 wage values and source/reference dates preserved;
- exact external-URL set preserved across English, Spanish, and Portuguese;
- required credential/scope/portability limitation anchors preserved; and
- required no-guarantee / no-independent-certification disclaimer language preserved.

## Diagnostic hardening completed before PASS

Earlier runs exposed two false-positive classes in the checker rather than content defects:

1. Markdown emphasis around negative terms such as `**no**` broke literal substring matching.
2. Generic forbidden substrings such as `emprego garantido` could match warning or negated language.

The checker was corrected to normalize lightweight Markdown before claims-anchor testing and to require affirmative safety/disclaimer anchors instead of relying on context-blind forbidden substrings. The workflow path filters were also corrected so changes to the Brazilian Portuguese source directly trigger parity QA.

These changes improve semantic reliability without lowering any content threshold.

## Downstream Guide 02 gates — completed

Detailed trilingual terminology/natural-language review, external-link revalidation, market-date refresh, DOCX/PDF generation, structural/link/encoding/metadata checks, PDF render/extractability checks, checksums, publication manifest, repository landing, and final publication-candidate Gate 24 have all completed successfully.

The synchronized post-editorial publication build is run `31228466140`, and the current publication package was committed at `3ea5bed76c1b22bab1b2fb95b4ffab039c5efb3d`.

## Controlled decision

Guide 02 passed deterministic trilingual parity and all downstream controlled publication-candidate gates. Final Guide 02 publication status is recorded in `GUIDE_02_FINAL_PUBLICATION_CANDIDATE_GATE_24.md`.
