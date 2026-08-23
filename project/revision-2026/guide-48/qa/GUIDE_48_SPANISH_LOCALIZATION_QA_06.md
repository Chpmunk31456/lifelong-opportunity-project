# Guide 48 — Spanish Localization QA 06

**Guide:** 48 — Medical Assistant  
**Locale:** neutral Latin American Spanish (`es-419`)  
**Branch:** `revision/guide-00-100-2026`  
**Date:** August 19, 2026  
**Gate:** Spanish Localization  
**Result:** **PASS**

## Controlled source

The frozen English source is:

`project/revision-2026/guide-48/working-masters/GUIDE_48_MEDICAL_ASSISTANT_ENGLISH_v2.md`

The localized working master is:

`project/revision-2026/guide-48/working-masters/GUIDE_48_MEDICAL_ASSISTANT_ES419_v2.md`

## QA controls completed

The `es-419` edition was reviewed against the frozen English source for:

- occupation scope and the distinction between U.S. Medical Assistant duties and other licensed clinical roles;
- explicit limits on diagnosis, prescribing, treatment selection, interpretation of diagnostic results, invasive/restricted procedures, and unsupported credential claims;
- patient-safety, infection-prevention, escalation, supervision, delegation, privacy, cybersecurity, and AI-use boundaries;
- United States education, Registered Apprenticeship, WIOA, employer-support, wage, employment-outlook, and private-market-estimate content;
- Canada duty-based comparisons for NOC 13112, 14101, and 33102, including the warning against direct credential/title transfer;
- Colombia CUOC 42291 / Auxiliares administrativos en salud coverage, SENA public-employment/training pathways, and the distinction between vacancy examples and national wage statistics;
- Latin America/OIT-Cinterfor vocational-training locator language;
- free-first and lower-cost training strategy, funding cautions, and scam-avoidance content;
- neutral Latin American Spanish, natural readability, spelling, grammar, punctuation, headings, lists, and UTF-8 characters;
- numeric parity for controlled values including `31-9092.00`, NOC `13112`, `14101`, `33102`, CUOC `42291`, Canada medians `CAD $25.00`, `$21.00`, `$24.00`, Canada Student Grant `CAD $4,200` / `$525`, U.S. wages `$21.97`, `$45,690`, `$36,050`, `$59,310`, jobs/openings `811,000`, `912,200`, `12%`, `112,300`, BLS reference `$44,200`, Salary.com `$45,918`, `$22`, `$41,684–$50,505`, and Colombia vacancy bands `COP $1,500,001–$2,000,000` / `$2,000,001–$2,500,000`;
- preservation of the full frozen-English current-source URL set, including O*NET/BLS, Apprenticeship.gov, CareerOneStop, Canadian Job Bank/student-aid pages, OCUPACOL, SENA, OIT/Cinterfor, and Salary.com; and
- assurance language that does not claim independent human certification, professional accreditation, certified translation, medical/legal review, or guaranteed outcomes.

## Localization decisions

- `Medical Assistant` is translated contextually as **asistente médico** while retaining the English title where required to prevent false equivalence across jurisdictions.
- Canadian occupational titles and U.S. program names such as `Registered Apprenticeship`, `Medical administrative assistant`, and `Medical office assistant` are retained where preserving official classification meaning is safer than inventing a localized credential.
- Colombian occupational terminology follows the source wording `Auxiliares administrativos en salud` / `Auxiliar Administrativo en Salud` and does not imply U.S.-style delegated clinical scope.
- `externship`, CPR, EKG, WIOA, BLS, O*NET, NOC, CUOC, and official program names are retained or explained without changing their underlying meaning.

## Decision

**Spanish Localization: PASS.**

The localized master preserves the frozen source's occupational, regulatory, safety, funding, wage, source, and assurance boundaries while reading naturally in neutral Latin American Spanish. This is an internal AI-assisted localization and QA record; it is not independent professional translation certification.