# Guide 62 — Spanish Localization QA 06

**Guide:** 62 — Teacher Assistant and Instructional Aide  
**Locale:** es-419  
**Review date:** 2026-08-20  
**Result:** PASS

## Scope

Controlled review of `GUIDE_62_TEACHER_ASSISTANT_AND_INSTRUCTIONAL_AIDE_ES419_v2.md` against the frozen English Version 2 master.

## Controls completed

- PASS — complete neutral Latin American Spanish localization produced from the frozen English source.
- PASS — role-boundary language preserved: support role, not independent teacher-of-record, clinical, legal, or regulated-professional authority.
- PASS — safeguarding, mandatory-reporting, privacy, disability-support, higher-risk procedure, and escalation controls preserved without expanding scope.
- PASS — U.S. classification `25-9042.00`, Canada `NOC 43100`, SENA/Colombia pathway language, and all controlled wage/employment values preserved.
- PASS — official wage data remains distinct from the August 2026 Indeed non-government market estimate.
- PASS — WIOA funding remains explicitly non-guaranteed and Registered Apprenticeship status remains accurately described as not currently approved for O*NET 25-9042.00.
- PASS — exact source URLs from the frozen English source set are preserved in the localized source section, including query parameters.
- PASS — AI safety boundary preserved: no identifiable/confidential student data in unapproved AI tools and AI does not replace licensed teacher/specialist judgment or formal school processes.
- PASS — cybersecurity/privacy safeguards preserved.
- PASS — no independent human certification, professional translation certification, accreditation, legal review, accessibility certification, employment guarantee, or earnings guarantee is claimed.
- PASS — visible text is UTF-8 and no translation placeholders, TODO markers, or unfinished localization notes are present.

## Terminology decisions

- `Teacher assistant / instructional aide` localized as **asistente docente / auxiliar de apoyo educativo** while retaining common English job-title examples where useful for job searching.
- `Teacher of record` rendered as **docente responsable del curso** rather than implying a separate Latin American licensure category.
- `Safeguarding` rendered as **salvaguarda**, with the surrounding text explaining reporting and emergency escalation duties.
- `Registered Apprenticeship` and official occupation/classification labels remain in English where they identify specific U.S. programs or datasets.
- `IEP` is retained as an official U.S. acronym and explained through **Programa de Educación Individualizado**.

## Gate decision

Spanish Localization (`es-419`) is approved as **PASS**. The next sequential gate is Brazilian Portuguese Localization (`pt-BR`).
