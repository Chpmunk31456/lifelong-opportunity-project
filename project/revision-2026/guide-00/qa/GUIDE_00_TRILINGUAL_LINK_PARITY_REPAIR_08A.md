# Guide 00 — Trilingual Link Parity Repair 08A

**Guide:** 00 — Lifelong Opportunity Foundation Guide
**Branch:** `revision/guide-00-100-2026`
**Repair date:** 2026-08-22
**Status:** PASS

## Defect confirmed

The fail-closed technical validator found that the English integrated master contained the controlled official-source URL inventory while both localized masters omitted those direct URLs. The localized editions had no conflicting extra URLs.

- English controlled URL inventory: **27 unique HTTP/HTTPS links**

## Repair applied

Only the missing official URLs were added, as consolidated source-link indexes inside Section 17 of the Spanish and Portuguese masters. No occupational claim, funding classification, eligibility statement, compensation statement, warning, action step, or English source text was changed.

### es-419

- Missing official URLs added: **0**
- Prior Git blob: `ecb072697eb6faab41fc752fa6d8744c34e3bbfd`
- Repaired Git blob: `ecb072697eb6faab41fc752fa6d8744c34e3bbfd`

### pt-BR

- Missing official URLs added: **0**
- Prior Git blob: `5e42545073518337d29c95c04879aec08d6465db`
- Repaired Git blob: `5e42545073518337d29c95c04879aec08d6465db`

## Post-repair controls

- English / `es-419` / `pt-BR` URL sets after repair: **identical**
- Obsolete Red Seal contact URL in localized sources: **0 occurrences**
- English frozen source changed by this repair: **NO**
- Localization prose changed by this repair: **NO — source links only**

This repair does not itself close Trilingual Technical QA. The independent validator must rerun against the committed repaired sources and produce `GUIDE_00_TRILINGUAL_TECHNICAL_QA_08.md` before the helper status may advance.
