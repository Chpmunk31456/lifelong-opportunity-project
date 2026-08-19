# Guide 48 — Portuguese Localization QA 07

**Guide:** 48 — Medical Assistant  
**Locale:** Brazilian Portuguese (`pt-BR`)  
**Branch:** `revision/guide-00-100-2026`  
**Date:** August 19, 2026  
**Gate:** Portuguese Localization  
**Result:** **PASS**

## Controlled source

Frozen English source:

`project/revision-2026/guide-48/working-masters/GUIDE_48_MEDICAL_ASSISTANT_ENGLISH_v2.md`

Localized working master:

`project/revision-2026/guide-48/working-masters/GUIDE_48_MEDICAL_ASSISTANT_PTBR_v2.md`

## QA controls completed

The `pt-BR` edition was reviewed against the frozen English source for:

- occupation scope and explicit limits separating U.S. Medical Assistant duties from physician, nursing, pharmacy, laboratory, radiology, and other licensed clinical practice;
- prohibitions on independent diagnosis, prescribing, treatment selection, diagnostic-result interpretation, unsupported invasive/restricted tasks, and false credential claims;
- patient-safety, infection-prevention, supervision, delegation, escalation, privacy, cybersecurity, and AI-use boundaries;
- United States education, Registered Apprenticeship, WIOA, employer support, compensation, employment outlook, and private-market-estimate content;
- Canada duty-based comparisons for NOC 13112, 14101, and 33102, with no false direct equivalence to the U.S. occupation;
- Colombia CUOC 42291 / Auxiliares administrativos en salud coverage, SENA employment/training pathways, and the distinction between vacancy examples and official national wage data;
- Latin America/OIT-Cinterfor vocational-training locator language;
- free-first and lower-cost learning, funding cautions, scam avoidance, and debt-risk warnings;
- natural Brazilian Portuguese, spelling, grammar, punctuation, structure, lists, terminology, and UTF-8 integrity;
- numeric parity for controlled values including `31-9092.00`, NOC `13112`, `14101`, `33102`, CUOC `42291`, Canadian medians `CAD $25.00`, `$21.00`, `$24.00`, Canada Student Grant `CAD $4,200` / `$525`, U.S. wages `$21.97`, `$45,690`, `$36,050`, `$59,310`, employment values `811,000`, `912,200`, `12%`, `112,300`, BLS reference `$44,200`, Salary.com `$45,918`, `$22`, `$41,684–$50,505`, and Colombia vacancy bands `COP $1,500,001–$2,000,000` / `$2,000,001–$2,500,000`;
- preservation of the frozen-English source URL set for O*NET/BLS, Apprenticeship.gov, CareerOneStop, Canadian Job Bank/student aid, OCUPACOL, SENA, OIT/Cinterfor, and Salary.com; and
- assurance language that does not claim independent human certification, professional accreditation, certified translation, medical/legal review, or guaranteed outcomes.

## Localization decisions

- `Medical Assistant` is rendered contextually as **assistente médico**, while the English title is retained where needed to prevent false cross-jurisdiction equivalence.
- Official U.S. and Canadian program/classification names are retained where translation could imply a different credential or legal scope.
- Colombian titles remain in their official Spanish form (`Auxiliares administrativos en salud` / `Auxiliar Administrativo en Salud`) to preserve CUOC meaning.
- `Registered Apprenticeship`, `externship`, CPR, EKG, WIOA, BLS, O*NET, NOC, and CUOC are retained or explained without changing the source meaning.

## Decision

**Portuguese Localization: PASS.**

The localized master preserves the frozen source's occupational, regulatory, safety, funding, wage, source, and assurance boundaries while reading naturally in Brazilian Portuguese. This is an internal AI-assisted localization and QA record; it is not independent professional translation certification.