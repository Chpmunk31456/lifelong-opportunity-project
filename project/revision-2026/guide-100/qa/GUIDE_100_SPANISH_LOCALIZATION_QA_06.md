# Guide 100 — Spanish Localization QA

**Occupation:** Clinical Laboratory Technician  
**Frozen English source blob:** `45257f599c046eb255d10e1e070dc2d470ccb5fb`  
**Spanish master:** `project/revision-2026/guide-100/working-masters/GUIDE_100_TECNICO_DE_LABORATORIO_CLINICO_ES419_v2.md`  
**Locale:** neutral Latin American Spanish (`es-419`)  
**Review date:** 2026-08-22  
**Gate:** Spanish Localization

## Result

**PASS.** The Spanish master preserves the controlled meaning, clinical boundaries, numeric values, source framework and six-step action plan of the frozen English source.

## Localization checks

- Occupation title is localized naturally as **Técnico/a de Laboratorio Clínico** while O*NET/NOC/CUOC official identifiers and official English occupational names remain intact where useful for verification.
- The distinction between técnico, tecnólogo/científico, auxiliar, flebotomista, patólogo, director de laboratorio and other authorized roles is preserved.
- The text does not broaden a technician’s authority to diagnosis, patient interpretation, result release, method approval, QC override, proficiency-testing manipulation, transfusion decisions or other regulated/high-consequence functions.
- CLIA terminology is explained in Spanish while retaining the official acronym and `waived` term where translation alone could obscure U.S. regulatory meaning.
- OSHA bloodborne-pathogen, sharps and chemical-safety controls retain the same fail-safe boundaries as the English source.
- Specimen identity, pre-analytical handling, QC, calibration, data-integrity, LIS/privacy, cybersecurity and downtime concepts are preserved.
- Responsible-AI restrictions remain explicit: patient identifiers/results and consequential clinical decisions are excluded from unapproved AI use.
- U.S. official wage/employment values and dates are unchanged, including the combined technologist/technician-series caveat.
- Private U.S. salary estimates remain separately labelled as non-government, title-sensitive context.
- Canada NOC 32120 and NOC 33101 remain separate comparison pathways with the same wage values, education/regulation caveats and non-equivalence warning.
- Colombia CUOC 32120 and CUOC 53294 remain distinct; the SENA 48-hour course is clearly described as complementary rather than a complete technician qualification.
- WIOA, Apprenticeship.gov, Canada training, SENA and OIT/Cinterfor pathways retain non-guarantee/eligibility caveats.
- Accessibility and dysgraphia-friendly strategies preserve specimen identity, infection control, competency, QC, audit-trail and patient-safety constraints.
- The safe portfolio and résumé sections continue to prohibit real patient/confidential information and unsupported competence/credential claims.
- The dedicated **Plan de acción de seis pasos** contains explicit **Paso 1** through **Paso 6**, preserving the repair of the legacy action-plan defect.
- The verification-source list preserves the direct official/private URLs used by the English master.
- No unsupported claim of certified translation, independent human linguistic review, accreditation review, licensure review, legal/medical review or accessibility certification is introduced.
- Authorship, AI-assistance disclosure and CC BY-NC-SA 4.0 licensing remain explicit.

## Language quality

The Spanish is neutral Latin American professional language rather than country-specific slang. Clinical terms are translated where a stable Spanish term is clear; official acronyms and source-system names remain untranslated where needed for accurate verification. Sentences favor direct instructions and clear escalation language suitable for the guide’s accessibility goals.

## Encoding and filename repair

The controlled Markdown filename is clean UTF-8:

`GUIDE_100_TECNICO_DE_LABORATORIO_CLINICO_ES419_v2.md`

It does not reproduce the legacy accent-damaged filename pattern (`T_cnico`, `cl_nico`). Publication must continue this UTF-8-safe naming discipline.

## Gate result

**PASS — Spanish Localization**

No blocker identified for Portuguese (`pt-BR`) localization.
