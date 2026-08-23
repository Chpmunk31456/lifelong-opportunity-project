# Guide 42 — Shared Source-Link Corrective QA 07B

**Guide:** 42 — Painter and Coating Worker  
**Branch:** `revision/guide-00-100-2026`  
**Correction date:** August 16, 2026  
**Result:** **PASS after corrective repair**

## Trigger

Guide 42 controlled publication workflow run `31960056936` passed trilingual structural/source/numeric/terminology parity, then failed closed during live-link validation because the previously frozen OIT/Cinterfor locator returned an explicit **HTTP 404**:

`https://www.oitcinterfor.org/statsfp/instituciones`

This was treated as a genuine source-locator defect rather than an access-control or transient-network condition.

## Corrective source

OIT/Cinterfor's current institutional-network page is:

`https://www.oitcinterfor.org/red-institucional`

The current page directly documents OIT/Cinterfor's institutional network and identifies vocational-training institutions by country, including SENA in Colombia. It therefore supports the controlled Guide 42 claim that OIT/Cinterfor can be used as a regional public-system locator for vocational-training institutions. The correction does not expand the claim into a guarantee of program availability, credential portability, admission, funding, employment, or earnings.

## Files corrected

The obsolete locator was replaced with the current institutional-network locator in all three controlled masters:

- `project/revision-2026/guide-42/working-masters/GUIDE_42_PAINTER_AND_COATING_WORKER_ENGLISH_v2.md`
- `project/revision-2026/guide-42/working-masters/GUIDE_42_PAINTER_AND_COATING_WORKER_ES419_v2.md`
- `project/revision-2026/guide-42/working-masters/GUIDE_42_PAINTER_AND_COATING_WORKER_PTBR_v2.md`

No occupational scope, wage figure, date, currency, safety boundary, regulatory reference, jurisdiction qualifier, AI/privacy/cybersecurity boundary, or credential/non-guarantee statement was changed by this repair.

## Gate implications

- **Research evidence:** original intake remains historical evidence of the source set checked on August 15; this corrective QA supersedes the obsolete OIT/Cinterfor locator for subsequent controlled use.
- **Evidence/Traceability:** remains PASS with this corrective evidence added to the chain.
- **English Source Freeze:** remains PASS after controlled source-link correction; substantive English claims were unchanged.
- **Spanish Localization:** remains PASS because the identical source correction was applied to the `es-419` master.
- **Portuguese Localization:** remains PASS because the identical source correction was applied to the `pt-BR` master.
- **Technical QA:** remains PENDING until the corrected trilingual source set passes a new controlled workflow run.

## Assurance boundary

This correction records an internal source-maintenance and QA action. It does not claim independent human certification, professional translation certification, accessibility certification, legal review, environmental approval, accreditation, guaranteed employment, or guaranteed earnings.
