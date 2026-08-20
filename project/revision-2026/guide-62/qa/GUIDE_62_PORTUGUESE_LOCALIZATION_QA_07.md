# Guide 62 — Portuguese Localization QA 07

**Guide:** 62 — Teacher Assistant and Instructional Aide  
**Locale:** pt-BR  
**Review date:** 2026-08-20  
**Result:** PASS

## Scope

Controlled review of `GUIDE_62_TEACHER_ASSISTANT_AND_INSTRUCTIONAL_AIDE_PTBR_v2.md` against the frozen English Version 2 master.

## Controls completed

- PASS — complete Brazilian Portuguese localization produced from the frozen English source.
- PASS — support-role boundary preserved; the text does not grant teacher-of-record, clinical, legal, counselling, special-education, or other regulated authority.
- PASS — safeguarding/protection, mandatory-reporting, privacy, disability-support, personal-care, higher-risk procedure, and escalation controls preserved.
- PASS — U.S. O*NET `25-9042.00`, Canada `NOC 43100`, SENA/Colombia pathways, and controlled wage/employment values preserved.
- PASS — official compensation data remains separate from the August 2026 Indeed non-government market estimate.
- PASS — WIOA funding remains explicitly non-guaranteed; Registered Apprenticeship status remains accurately described as not currently approved for O*NET 25-9042.00.
- PASS — exact frozen-English source URLs are preserved, including query parameters.
- PASS — AI privacy and judgment boundaries preserved; identifiable/confidential student data is excluded from unapproved AI tools and AI does not replace licensed teacher/specialist judgment or formal school processes.
- PASS — cybersecurity and student-record safeguards preserved.
- PASS — no independent human certification, professional translation certification, accreditation, legal review, accessibility certification, employment guarantee, or earnings guarantee is claimed.
- PASS — visible content is UTF-8 and contains no TODOs, placeholders, untranslated drafting notes, or unfinished sections.

## Terminology decisions

- `Teacher assistant / instructional aide` localized as **assistente de professor / auxiliar de apoio educacional**, while common English job titles remain where they improve searchability.
- `Teacher of record` rendered as **professor responsável pela turma**, avoiding an unsupported Brazilian licensure equivalence.
- `Safeguarding` rendered as **proteção**, with reporting/emergency duties explained in context.
- Official U.S. program and occupation labels such as `Registered Apprenticeship`, `O*NET`, `FERPA`, and `IEP` are retained where they identify specific systems or records.
- `IEP` is retained as the U.S. acronym and contextualized as **Programa Educacional Individualizado**.

## Gate decision

Brazilian Portuguese Localization (`pt-BR`) is approved as **PASS**. The next sequential gate is Trilingual Technical QA.
