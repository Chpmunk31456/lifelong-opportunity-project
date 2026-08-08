# Guide 03 — English Translation Source Freeze 08

Date: 2026-08-07
Branch: `revision/guide-00-100-2026`
Guide: 03 — Medical Billing and Coding Specialist
Source: `project/revision-2026/guide-03/source/GUIDE_03_ENGLISH_WORKING_MASTER_v2.md`

## Gate purpose

Freeze the current English working master as the controlled source for neutral Latin American Spanish (`es-419`) and Brazilian Portuguese (`pt-BR`) translation after source reconciliation, current-source revalidation, editorial/terminology review, and link/structure/translation-readiness QA. This is a translation-source control, not final publication approval, independent human certification, professional translation certification, accessibility certification, legal review, or coding certification.

## Freeze fingerprint

- English source Git blob SHA: `f74f6f7d9cc1e8be011ec4eea726904365b6521e`
- Last substantive English edit commit before freeze: `f4c4c5cc30ed139d44633201f477579219a2e0e6`
- Editorial/terminology QA commit: `53af275825c60cf00abe79289419bd512e144d3a`
- Link/structure/translation-readiness QA commit: `4547f8c94e7e7f4d73dbcdf5ca29a88ccd12c2e1`

The English source content must not be silently changed after this gate. Any later substantive English correction must reopen the affected downstream parity/translation/build gates and be explicitly documented.

## Prerequisite gates

- QA 01 — English baseline inventory: completed.
- QA 02 — deterministic legacy DOCX/PDF extraction: completed.
- QA 03 — current-source evidence intake: completed.
- QA 04 — legacy/source reconciliation: completed.
- QA 05 — high-impact source revalidation/source QA: completed.
- QA 06 — English editorial/terminology/natural-language QA: PASS.
- QA 07 — link/structure/translation-readiness QA: PASS.

## Translation controls

The es-419 and pt-BR masters must:

1. preserve all 19 numbered sections and the substantive content of each section;
2. preserve all numerical wage, date, duration, percentage and code-set facts unless a documented source correction is made;
3. retain official acronyms and formal names where translation would create ambiguity;
4. preserve the distinction among government occupational evidence, private professional credentials and non-government market estimates;
5. preserve country/jurisdiction boundaries and avoid implying U.S. rules automatically apply elsewhere;
6. preserve anti-guarantee, verification, privacy, security, documentation-integrity and responsible-AI controls;
7. use natural neutral Latin American Spanish and natural Brazilian Portuguese rather than literal word-for-word translation; and
8. retain the same core URLs unless a documented authoritative localized equivalent is intentionally substituted.

## Controlled decision

**PASS — English source frozen for translation.** The file identified by blob SHA `f74f6f7d9cc1e8be011ec4eea726904365b6521e` is the controlled source for the Guide 03 es-419 and pt-BR working masters.

The next gate is creation of both translations followed by structural, terminology, numerical, URL and high-impact-control parity review before document generation.