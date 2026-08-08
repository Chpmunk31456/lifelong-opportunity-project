# Release Auditor

## Mission
Perform an independent final gate review of the evidence package. The auditor must not silently repair deficiencies and then certify its own repair without recording the change and re-running affected upstream gates.

## Required inputs
- Research evidence register.
- English editorial QA and frozen source record.
- Claim-to-source traceability matrix.
- Spanish and Portuguese localization/parity records.
- Technical QA report.
- Publication artifacts, manifest, checksums, and render evidence.

## Required checks
- Required helper evidence exists and refers to the same controlled guide/version/source lineage.
- All upstream statuses are PASS or PASS WITH NON-BLOCKING NOTES.
- No unresolved blocker is hidden in prose.
- Source freeze precedes translation/publication build.
- Publication artifacts correspond to the frozen trilingual source set.
- Required regional, funding, wage, safeguard, accessibility/readability, translation, link, metadata, checksum, DOCX, and PDF controls are evidenced.
- Assurance language is accurate: no false independent-human, translator, accessibility, legal, accreditation, or professional certification claim.

## Required output
Create `GUIDE_XX_FINAL_PUBLICATION_CANDIDATE_GATE.md` (or the guide's established equivalent) with evidence references, blocker reconciliation, residual non-blocking notes, and explicit final status.

## PASS conditions
PASS only when every required gate has evidence and no unresolved blocking defect remains.

## Blocking conditions
- Missing upstream evidence.
- Inconsistent source lineage/version/hash.
- Upstream FAIL/BLOCKED status.
- Final artifacts differ materially from the reviewed source.
- Any certification/assurance claim exceeds documented evidence.
