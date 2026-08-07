# Guide 02 — Publication Build Race Diagnostic 23

Date: 2026-08-07  
Branch: `revision/guide-00-100-2026`  
Workflow: `Guide 02 publication build and QA`

## Purpose

This record documents the first Guide 02 trilingual publication-build run after source, terminology, freshness, and translation-parity controls had passed. It separates artifact-quality results from the repository-write failure so that a branch synchronization race is not misrepresented as a content or publication-QA failure.

## Run reviewed

- Workflow run: `31218539732`
- Head at workflow start: `8264dcd0ed7f7f62ae0051c40b71bdccfa949f81`
- Result shown by GitHub: `failure`

## QA result before repository write

The run successfully completed all artifact-quality steps before attempting to push generated files:

1. controlled branch checkout — PASS;
2. document/PDF tooling installation — PASS;
3. English↔es-419↔pt-BR source parity — PASS;
4. three DOCX publication candidates generated — PASS;
5. three PDF publication candidates generated — PASS;
6. DOCX OOXML structure, source hyperlinks, UTF-8/encoding, PDF extractability, page-count, title-presence, refreshed market-date, metadata-manifest and SHA-256 generation checks — PASS;
7. first-page PNG render evidence for all three PDFs — PASS.

The job created a local commit `a6c9d0f` containing 11 Guide 02 publication-candidate files, including the three DOCX files, three PDFs, QA manifest, checksum file, and three first-page renders.

## Failure classification

**Infrastructure/repository synchronization failure — not a content-QA failure.**

The final `git push` was rejected as non-fast-forward because another workflow updated `revision/guide-00-100-2026` after this run checked out the branch. GitHub reported `fetch first`; no artifact-quality check failed.

## Corrective action

The publication workflow was updated in commit `a9b16faf8a0eadf291505fc76791be85b303f0bd` so that, after a successful local artifact commit, it:

1. fetches the current controlled revision branch;
2. rebases the completed artifact commit onto the current remote branch;
3. re-runs the Guide 02 trilingual parity checker after the rebase; and
4. pushes only after those controls pass.

This preserves fail-closed publication QA while reducing false stoppages caused by unrelated workflow commits landing on the same revision branch.

## Controlled decision

Guide 02 publication-candidate artifact QA is **technically PASS through render generation**, but repository publication-candidate completion remains **HOLD** until the corrected workflow successfully lands the generated files on the controlled branch and the committed manifest/checksums are verified at the resulting branch head.

This record does not claim independent human review, professional translation certification, accessibility certification, accreditation, legal review, or publication approval.
