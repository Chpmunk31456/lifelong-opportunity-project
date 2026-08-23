# Lifelong Opportunity Guide Helper Framework

These helper contracts operationalize `project/MANUAL_REVISION_STANDARD.md` for the controlled Guides 00–100 revision program.

They are role contracts, not claims that an independent person or autonomous system performed a review. A helper may be executed by ChatGPT with approved tools, by a GitHub Actions workflow, by a script, or by a qualified human reviewer. Every execution must leave auditable evidence in the applicable guide QA directory.

## Required order

1. Research Helper
2. English Editorial Helper
3. Evidence / Traceability Helper
4. Spanish Localization Helper
5. Portuguese Localization Helper
6. Technical QA Helper
7. Publication Helper
8. Release Auditor

A later helper must not convert an unresolved earlier blocker into PASS.

## Status vocabulary

Use only: `NOT STARTED`, `IN PROGRESS`, `BLOCKED`, `PASS`, `PASS WITH NON-BLOCKING NOTES`, or `FAIL`.

## Evidence rule

Each helper execution must record: guide number/title, date, source commit/ref, inputs reviewed, checks performed, findings, blockers, output artifacts, and explicit status. Never claim independent human certification, professional translation certification, legal review, accessibility certification, accreditation, or publication approval unless separately obtained and documented.

## Fail-closed rule

Missing required evidence is not PASS. Unverifiable factual claims must be removed, qualified, or recorded as blockers. Broken or materially redirected authoritative links must be corrected or explicitly blocked. Translation parity must be demonstrated, not assumed. Publication artifacts must be generated from the frozen source and technically inspected before release.
