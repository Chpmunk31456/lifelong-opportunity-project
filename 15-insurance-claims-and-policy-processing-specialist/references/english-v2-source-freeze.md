# Guide 15 — English v2 Source Freeze

**Guide:** 15 — Insurance Claims and Policy Processing Specialist  
**Freeze date:** 2026-08-09  
**Branch:** `revision/guide-00-100-2026`  
**Status:** **PASS — English v2 source frozen for localization**

## Frozen source

The controlled English localization source is:

`15-insurance-claims-and-policy-processing-specialist/references/english-v2-working-master.md`

Frozen Git blob SHA:

`d40f0181e8a7d8e756342f25bbc64f20d8e26262`

Localization must use the exact content represented by that blob. If the English working master changes after this freeze, this gate is invalid until the revised English file is re-reviewed and a new freeze record is committed.

## Required evidence gates completed before freeze

- `source-review-summary.md` — current-source evidence intake PASS
- `english-v2-reconciliation.md` — controlled v1→v2 reconciliation completed
- `english-v2-editorial-qa.md` — English editorial/accessibility QA PASS
- `english-v2-traceability-qa.md` — claim-to-source traceability QA PASS
- `english-v2-technical-source-qa.md` — terminology, structure, encoding, link/freshness, and publication-safety QA PASS

## Freeze controls

The frozen English source:

- preserves the clerical/processing occupational boundary and does not confer regulated authority;
- separates official wage statistics, private market estimates, and individual vacancy examples;
- includes United States, Canada, Colombia, and broader Latin America pathway controls;
- includes free/low-cost learning, scholarships, employer support, WIOA/FAFSA, and apprenticeship guidance with eligibility caveats;
- includes accessibility, privacy, cybersecurity, and responsible-AI safeguards;
- contains no claim of independent human certification, independent linguistic validation, accreditation, regulator endorsement, guaranteed employment, guaranteed funding, or guaranteed income; and
- requires revalidation of time-sensitive information before material career or spending decisions.

## Localization rule

Neutral Latin American Spanish (`es-419`) and Brazilian Portuguese (`pt-BR`) may now be produced from the frozen English blob. Localization must preserve meaning, numerical values, dates, source labels, jurisdiction boundaries, disclaimers, accessibility guidance, security/privacy controls, responsible-AI controls, and the distinction between official and non-government evidence.

The localization gate is **not passed** merely because a translated file exists. Each language must receive its own controlled parity/terminology review before trilingual technical QA.

## Gates not yet passed

The following remain pending for Guide 15:

1. `es-419` controlled localization and localization QA;
2. `pt-BR` controlled localization and localization QA;
3. trilingual terminology, structure, encoding, and link parity QA;
4. DOCX/PDF generation and searchable-text checks;
5. visual rendering/accessibility checks;
6. metadata, checksums, and publication manifest;
7. publication-candidate QA; and
8. final release audit.

This record is an internal controlled-revision checkpoint, not an independent certification or accreditation statement.
