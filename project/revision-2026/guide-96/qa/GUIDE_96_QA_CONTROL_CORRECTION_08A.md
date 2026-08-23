# Guide 96 — QA Control Correction 08A

## Date
2026-08-22

## Purpose
This note corrects a QA metadata overstatement discovered by the fail-closed Publication preflight. It does **not** change any frozen reader-facing master.

## Frozen master status
The English source remains frozen at blob:
`8a29c6130e2e38327e2faaadc12d2b3fdc28281e`

Spanish and Portuguese remain derived from that source at their previously recorded blobs. No reader-facing content drift occurred.

## Correction
The research evidence pack records three non-government market-title estimates:
- U.S. Electrical Technician — approximately $30.67/hour;
- U.S. Electronics Technician — approximately $27.58/hour;
- Colombia Técnico/a electrónico/a — approximately COP 1,711,841/month.

The frozen reader-facing English, Spanish and Portuguese masters intentionally carry the **two U.S. Indeed estimates in narrative form**. The Colombia Indeed figure remains in the research evidence pack and reader-verification source list, but is **not promoted as a controlled numeric claim in the reader-facing wage narrative** because it is a narrower title estimate with limited cross-role comparability.

Therefore, any wording in QA03, QA04, QA06, QA07 or QA08 implying that `COP 1,711,841/month` was numerically carried into all three reader-facing masters is superseded by this correction note.

## Publication-validator consequence
Publication QA must validate only controlled numeric claims that are actually present in the frozen masters. It must **not** require `COP 1,711,841` as a trilingual numeric control.

The Colombia Indeed URL remains part of the 23-link reader-verification parity set.

## Gate impact
- English Editorial: remains PASS.
- Evidence / Traceability: remains PASS with this correction.
- English Source Freeze: remains PASS; source blob unchanged.
- Spanish Localization: remains PASS.
- Portuguese Localization: remains PASS.
- Trilingual Technical QA: remains PASS with this correction attached.
- Publication: remains PENDING until a fresh build passes.
- Release Audit: remains PENDING until publication closes.

## Result
**PASS — QA control correction recorded without frozen-source drift.**
