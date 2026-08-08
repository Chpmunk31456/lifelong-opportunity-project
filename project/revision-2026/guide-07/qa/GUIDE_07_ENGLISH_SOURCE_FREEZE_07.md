# Guide 07 — English Source Freeze 07

**Guide:** Customer Service Specialist / Customer Service Representative  
**Controlled branch:** `revision/guide-00-100-2026`  
**Freeze date:** 2026-08-08  
**Status:** PASS — English v2 frozen as translation source

## Frozen source

`project/revision-2026/guide-07/source/GUIDE_07_ENGLISH_WORKING_MASTER_v2.md`

Git blob at freeze review: `aceeccff90e784f72792687054dead04c6945524` after the verified freshness corrections.

## Predecessor gates

- Research Helper: PASS — `GUIDE_07_CURRENT_SOURCE_EVIDENCE_03.md`
- English Editorial Helper: PASS — `GUIDE_07_ENGLISH_EDITORIAL_QA_05.md`
- Evidence / Traceability Helper: PASS — `GUIDE_07_CLAIM_TRACEABILITY_QA_06.md`
- Deterministic freshness correction workflow `31261572718`: PASS

## Source controls confirmed

- English master preserves 19 numbered occupational sections.
- Official BLS wage/outlook evidence is separated from commercial market estimates.
- Current ZipRecruiter figures are dated August 8, 2026 and clearly labeled non-government estimates.
- Canada NOC 64409 mapping is qualified and not treated as perfect title equivalence.
- Colombia does not receive an invented wage figure where a directly comparable official series was not verified.
- SENA wording is constrained to the cited 48-hour complementary, in-person special course and does not promise current cohort availability.
- U.S. Section 127 treatment is framed as a qualifying-plan tax rule, not a universal employer benefit.
- Privacy, authentication, payment, recording, fraud/social-engineering, accessibility, safety, and AI boundaries are explicit and jurisdiction-aware.
- Optional credentials are not represented as universal licenses or legal requirements.
- The correction workflow decoded the source as strict UTF-8, rejected BOM/replacement-character defects, and passed `git diff --check` before committing the corrected source.

## External-link freeze review

Fresh retrieval on 2026-08-08 confirmed the BLS, IRS, SENA Betowa, Apprenticeship.gov, and current ZipRecruiter salary sources used for high-impact claims.

Some public/government resources resist automated retrieval:

- CareerOneStop URLs returned automated HTTP 403 responses.
- Federal Student Aid scholarship URL returned an automated HTTP 403 response.
- Government of Canada Job Bank URLs may resist automated retrieval in this environment.

These conditions are recorded as automated-retrieval limitations, not proof that the publication references are dead. The publication gate must recheck links and preserve this distinction.

## Freeze rule

Beginning with this gate, Spanish (`es-419`) and Brazilian Portuguese (`pt-BR`) localization must use this English v2 file as the controlled semantic source. Any later material English factual change invalidates downstream localization/parity evidence and requires affected stages to be rerun.

## Decision

**PASS.** Guide 07 English v2 is frozen for translation production. This is an internal controlled source freeze, not publication approval or independent human certification.
