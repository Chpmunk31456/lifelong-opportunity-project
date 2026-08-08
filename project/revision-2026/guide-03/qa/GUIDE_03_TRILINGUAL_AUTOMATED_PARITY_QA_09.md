# Guide 03 — Trilingual Automated Parity QA 09

Date: 2026-08-07
Branch: `revision/guide-00-100-2026`
Guide: 03 — Medical Billing and Coding Specialist
Workflow: `.github/workflows/guide03-translation-parity.yml`
Script: `scripts/guide03_translation_parity.py`
Run: `31230074016`
Job: `93032048145`

## Gate purpose

Record the first fail-closed automated parity check across the frozen English source and the newly created neutral Latin American Spanish (`es-419`) and Brazilian Portuguese (`pt-BR`) working masters. This automated gate does not constitute professional translation certification, independent human linguistic review, accreditation, accessibility certification, legal review, coding certification, or publication approval.

## Inputs

- English: `project/revision-2026/guide-03/source/GUIDE_03_ENGLISH_WORKING_MASTER_v2.md`
- Spanish: `project/revision-2026/guide-03/source/GUIDE_03_SPANISH_LATAM_WORKING_MASTER_v2.md`
- Portuguese: `project/revision-2026/guide-03/source/GUIDE_03_PORTUGUESE_BR_WORKING_MASTER_v2.md`

The English source is controlled by `GUIDE_03_ENGLISH_TRANSLATION_SOURCE_FREEZE_08.md` at blob SHA `f74f6f7d9cc1e8be011ec4eea726904365b6521e`.

## Automated result

GitHub Actions run `31230074016` completed successfully. The job log reports:

- `Guide 03 English↔es-419↔pt-BR automated parity checks: PASS`
- numbered sections per language: **19**
- shared external URLs: **19**
- high-impact numeric/date controls per language: **20**

## Controls checked

The parity script fails closed for:

- UTF-8 BOM, invalid UTF-8, replacement characters, or CR line endings;
- a numbered-section sequence other than 1 through 19;
- missing high-impact wage, employment, percentage, date, NOC, Job Bank, or SENA duration controls;
- any URL-set difference between English and either translation;
- missing formal-term anchors including BLS, CMS, HIPAA, ICD-10-CM, ICD-10-PCS, CPT, HCPCS, AHIMA, AAPC, WIOA, NOC 12111, SENA and Registered Apprenticeship; and
- missing anti-guarantee/jurisdictional-control language in Spanish or Portuguese.

## Controlled decision

**PASS — automated trilingual structural/numerical/URL parity.** The three masters are structurally aligned and preserve the tested high-impact controls.

This gate does not by itself establish natural linguistic quality. The next gate is targeted es-419 and pt-BR natural-language/terminology review, followed by any required correction and a post-edit parity rerun before DOCX/PDF generation.