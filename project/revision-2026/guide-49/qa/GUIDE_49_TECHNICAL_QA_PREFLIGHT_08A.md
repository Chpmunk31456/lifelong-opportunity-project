# Guide 49 — Trilingual Technical QA Preflight 08A

**Guide:** 49 — Dental Assistant  
**Branch:** `revision/guide-00-100-2026`  
**Date:** August 19, 2026  
**Status:** **PREFLIGHT PASS — final Technical QA remains PENDING**

## Inputs now eligible for technical QA

The fail-closed content sequence has reached:

- Baseline Inventory: PASS
- Research: PASS
- English Editorial: PASS
- Evidence / Traceability: PASS
- English Source Freeze: PASS
- Spanish Localization (`es-419`): PASS
- Portuguese Localization (`pt-BR`): PASS

Controlled masters:

- `project/revision-2026/guide-49/working-masters/GUIDE_49_DENTAL_ASSISTANT_ENGLISH_v2.md`
- `project/revision-2026/guide-49/working-masters/GUIDE_49_DENTAL_ASSISTANT_ES419_v2.md`
- `project/revision-2026/guide-49/working-masters/GUIDE_49_DENTAL_ASSISTANT_PTBR_v2.md`

## Publication automation

`.github/workflows/guide49-publication-build.yml` was added in commit `91fec68931e1d7531bd6a30451773f2279e65070` to perform the controlled publication build. It is fail-closed on:

- trilingual H2 structural parity;
- direct source-URL set equality across all three languages;
- required occupation, NOC/OaSIS, CUOC, ReTHUS, apprenticeship, privacy, AI, cybersecurity, and Colombia-duration-control markers;
- controlled wage, employment, percentage, funding, code, and private-market values;
- unsafe affirmative independent-scope markers;
- live source-link behavior, with HTTP 404/410 treated as broken and access-controlled/transient conditions reported as limitations;
- DOCX integrity;
- searchable PDF text;
- all-page rendering and blank/clipping detection;
- trilingual publication metadata;
- page-count/render-count equality;
- SHA-256 checksums; and
- committed publication-candidate scope.

The workflow uses a bounded job timeout and `cancel-in-progress: true` for the Guide 49 concurrency group to prevent stale same-guide runs from indefinitely blocking a corrected run. These controls affect orchestration only and do not relax any substantive QA rule.

`.github/workflows/guide49-publication-status-probe.yml` records the exact publication workflow run ID/status/conclusion into branch evidence without advancing a gate.

## Decision

**Technical preflight: PASS.** The trilingual masters are eligible for the automated build. **Technical QA remains PENDING** until a complete controlled publication run succeeds and its generated package, render evidence/metadata, and checksums are available for review.
