# Generalized Manual Pipeline — Guides 08–100

This directory defines the configuration-driven pipeline used to reduce per-guide setup while preserving the controlled revision standard in `project/MANUAL_REVISION_STANDARD.md` and the helper contracts in `project/helpers/`.

## Standing rule

Use this generalized pipeline for every remaining manual unless a guide has a documented exception that requires a specialized control. Deterministic checks and publication steps should be reused rather than reimplemented per guide.

## Design principles

- **Fail closed.** Missing sources, evidence, localization files, checksums, renders, or PASS statuses stop the requested stage.
- **Configuration-driven.** Guide-specific facts live in `project/pipeline/configs/GUIDE_XX.json`; shared logic lives in `scripts/manual_pipeline.py`.
- **No false automation claims.** Research, editorial judgment, claim traceability, and localization remain explicit helper gates. This pipeline verifies their evidence; it does not claim independent human review.
- **Deterministic automation only.** Structural parity, URL parity, UTF-8 checks, required tokens, document conversion, PDF searchability, rendering, checksums, and release-evidence reconciliation are automated.
- **No auto-merge or auto-publication.** Output remains on the controlled revision branch and PR #17 remains Draft until the collection-level completion gate is satisfied.

## Standard sequence

1. Research Helper
2. English Editorial Helper
3. Evidence / Traceability Helper
4. English source freeze
5. Spanish Localization Helper (`es-419`)
6. Portuguese Localization Helper (`pt-BR`)
7. Technical QA Helper
8. Publication Helper
9. Full-page visual review
10. Release Auditor

## Controller

`scripts/manual_pipeline.py` exposes reusable subcommands:

- `validate-config --guide XX`
- `parity --guide XX`
- `build --guide XX`
- `release-audit --guide XX`
- `status --guide XX`

The controller reads `project/pipeline/configs/GUIDE_XX.json` and the guide helper-status manifest. It must not create a PASS for a subjective helper stage that lacks explicit evidence.

## GitHub Actions

`.github/workflows/manual-pipeline.yml` provides a single workflow-dispatch entry point with:

- guide number
- requested deterministic stage

The workflow installs publication dependencies only for stages that need them and uploads publication evidence without merging or publishing.

## Guide configuration

Each guide config contains:

- guide number and occupation
- English/es-419/pt-BR source paths
- helper-status manifest path
- expected numbered-section range
- output stem
- critical tokens that must survive localization
- optional required URL set
- visual-review evidence path
- publication directory

Add configuration; do not clone a guide-specific workflow unless a documented exception makes the generalized pipeline insufficient.
