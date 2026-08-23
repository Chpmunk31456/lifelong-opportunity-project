# Guide 39 — Spanish Localization Corrective QA 06B

**Guide:** 39 — Heavy Equipment Operator  
**Locale:** `es-419`  
**Date:** 2026-08-13  
**Result:** PASS for the narrowly scoped localization correction

## Defect discovered by Technical QA

The first full trilingual Technical QA precheck found that the Spanish controlled master had 14 source URLs while the frozen English and Brazilian Portuguese masters each had 16. This contradicted the earlier Spanish Localization QA statement that the source URL set was unchanged. The earlier record is retained for auditability and is not rewritten or erased.

The two URLs missing from the Spanish source list were:

- Canada Student Aid — how funding works: `https://www.canada.ca/en/services/benefits/education/student-aid/grants-loans/how-funding-works.html`
- OIT/Cinterfor — training institutions: `https://www.oitcinterfor.org/statsfp/instituciones`

## Exact repair

Only `project/revision-2026/guide-39/working-masters/GUIDE_39_HEAVY_EQUIPMENT_OPERATOR_ES419_v2.md` was corrected. Two semantically corresponding source-list bullets were added under `Fuentes oficiales/públicas`. No claim, number, date, wage, funding condition, safety boundary, privacy/AI/cybersecurity statement, jurisdictional qualifier, occupational scope, version label, or filename was changed.

## Post-repair validation

- Exact URL-set parity: PASS — English, `es-419`, and `pt-BR` each contain the same 16 URLs.
- Structural parity: PASS — all three masters contain 19 level-two sections.
- UTF-8 and placeholder scan: PASS for the corrected Spanish artifact.
- Controlled numeric/date/currency preservation: PASS for the corrected Spanish artifact.
- Official versus non-government compensation distinction: preserved.
- Occupation scope, terminology, safety, AI/privacy/cybersecurity, jurisdictional qualifiers, and assurance/non-guarantee boundaries: unchanged.
- Diff-scope review: PASS — the Spanish controlled-master diff contains exactly two added source-list lines and no other content change.

## Technical QA continuation finding

The full live-link rerun found a separate pre-existing collection-wide source defect: `https://www.oitcinterfor.org/statsfp/instituciones` returns HTTP 404. Direct retries returned HTTP 200 for the other initially ambiguous government links, including both Canada Student Aid pages and the Colombia qualifications site. Because the dead OIT/Cinterfor URL is present in all three controlled masters and the corrective authorization prohibits changes to English and Portuguese, Trilingual Technical QA remains fail-closed and PENDING.

Spanish Localization remains PASS on the basis of the corrected artifact plus this explicit corrective record. Publication and Release Audit may not begin until the shared dead-link defect is authoritatively remediated and the entire Technical QA gate is rerun.
