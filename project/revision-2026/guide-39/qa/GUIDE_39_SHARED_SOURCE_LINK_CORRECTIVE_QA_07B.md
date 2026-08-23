# Guide 39 — Shared Source-Link Corrective QA 07B

**Guide:** 39 — Heavy Equipment Operator
**Date:** 2026-08-13
**Result:** PASS

## Technical QA finding

Trilingual Technical QA discovered inconsistent and failed live-link behavior for the former OIT/Cinterfor vocational-training-institution locator URL. The earlier Spanish-only corrective record remains preserved as part of the audit history.

- Old URL: `https://www.oitcinterfor.org/statsfp/instituciones`
- Replacement URL: `https://www.oitcinterfor.org/red-institucional`

The replacement resolves on the official `oitcinterfor.org` domain and is the current OIT/Cinterfor institutional-network page supporting the intended vocational-training-institution locator function.

## Exact repair scope

The old URL was replaced once in each of these three controlled masters:

- `project/revision-2026/guide-39/working-masters/GUIDE_39_HEAVY_EQUIPMENT_OPERATOR_ENGLISH_v2.md`
- `project/revision-2026/guide-39/working-masters/GUIDE_39_HEAVY_EQUIPMENT_OPERATOR_ES419_v2.md`
- `project/revision-2026/guide-39/working-masters/GUIDE_39_HEAVY_EQUIPMENT_OPERATOR_PTBR_v2.md`

Diff review confirmed that the three master-file changes are one-for-one URL substitutions only. No other wording, claim, number, date, wage, funding condition, occupational scope, safety content, AI/privacy/cybersecurity boundary, metadata, or filename changed.

## Post-repair validation

- Exact source URL-set parity: PASS — English 16, `es-419` 16, `pt-BR` 16.
- Replacement live-link behavior: PASS — HTTP 200 after redirect handling.
- Official-source identity: PASS — HTTPS page on the official OIT/Cinterfor domain.
- Old-URL absence from all three controlled masters: PASS.
- Three-file diff scope: PASS.
- Unrelated-content preservation: PASS.

This corrective record supplements rather than erases the earlier localization and corrective QA records.
