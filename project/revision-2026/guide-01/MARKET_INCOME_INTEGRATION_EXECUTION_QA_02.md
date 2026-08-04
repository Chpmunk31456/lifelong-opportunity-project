# Guide 01 market-income integration execution QA 02

**Guide:** 01 — Community Health Worker  
**Recorded:** 2026-08-04  
**Branch:** `revision/guide-00-100-2026`  
**PR:** #17 (draft)

## Scope

This record verifies whether the committed deterministic integration script has produced a controlled trilingual content change.

## Evidence reviewed

- Branch head observed before this record: `b9c80af5fa9574b8c55ecbf5c1e95382b5a7558e`.
- That head is an automated Guide 00 publication rebuild (`build(guide-00): add trilingual publication candidates and QA manifest`) and does not integrate Guide 01 income content.
- The committed Guide 01 script is `scripts/guide01_integrate_market_income.py` at blob `dbda38f79f7cc5ce38879dc8abdb445648f54c4e`.
- The English working master at blob `66c7c3a05eed44968616300e5b8a70ce3ce53f52` still contains the pending QA instruction to add a defensible current non-government estimate and does not contain the planned Glassdoor or ZipRecruiter paragraph.
- Pull-request workflow runs associated with script commit `ba7a981678dc25970cbccf6ef3ea61a16e3472dc` did not include the Guide 01 market-income integration workflow. The observed runs were Guide 00 publication build, Guide 00 Red Seal correction, repository metadata audit, publication preflight, and Guide 01 English extraction.

## Gate result

**Trilingual supplementary market-income integration: NOT PASSED.**

No English, es-419, or pt-BR working master may be represented as containing the supplementary market estimates until all three files receive the deterministic insertion and pass numerical, source, terminology, and non-guarantee parity checks.

## Genuine blocker

The integration workflow exists only on the revision branch and is not being executed by the currently observable pull-request workflow set. The available GitHub connector can replace complete files but does not provide a safe patch-level write action for applying the script to three long working masters. Therefore, no content mutation was attempted through partial or reconstructed file replacement.

## Next controlled action

Execute `python scripts/guide01_integrate_market_income.py` in a checked-out copy of the revision branch, inspect the three-file diff, run the script a second time to confirm idempotence, then commit the three masters together. After that, run trilingual numerical and terminology parity QA before beginning legacy comparison or publication generation.
