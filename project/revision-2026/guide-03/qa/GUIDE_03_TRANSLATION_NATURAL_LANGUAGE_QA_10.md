# Guide 03 — Translation Natural-Language and Terminology QA 10

Date: 2026-08-07
Branch: `revision/guide-00-100-2026`
Guide: 03 — Medical Billing and Coding Specialist

## Gate purpose

Perform a targeted natural-language and terminology review of the neutral Latin American Spanish (`es-419`) and Brazilian Portuguese (`pt-BR`) working masters after the first automated trilingual parity PASS. This review checks practical readability and terminology choices; it does not claim professional translation certification, independent human linguistic review, accreditation, accessibility certification, legal review, coding certification, or final publication approval.

## Files reviewed

- `project/revision-2026/guide-03/source/GUIDE_03_SPANISH_LATAM_WORKING_MASTER_v2.md`
- `project/revision-2026/guide-03/source/GUIDE_03_PORTUGUESE_BR_WORKING_MASTER_v2.md`

Controlled English source:

- `project/revision-2026/guide-03/source/GUIDE_03_ENGLISH_WORKING_MASTER_v2.md`
- frozen English blob SHA: `f74f6f7d9cc1e8be011ec4eea726904365b6521e`

## Spanish (`es-419`) review

**PASS — neutral register.** The translation avoids country-specific slang and uses broadly understandable Latin American Spanish for career, education, privacy, security, employment and healthcare-billing concepts.

**PASS — role separation.** `facturación`, `codificación`, `información de salud`, `registros`, `denegaciones` and `ciclo de ingresos` remain distinct rather than being collapsed into one job function.

**PASS — credential language.** `credencial`, `certificación`, `licencia`, `elegibilidad para examen`, `acreditación` and employer preference are not treated as synonyms.

**PASS — risk/consumer language.** Warnings about debt, repayment agreements, unsupported coding, privacy, AI use and speculative salary claims remain direct without becoming promotional or alarmist.

**PASS — retained official terms.** U.S. job titles, HIPAA/CMS coding acronyms, AHIMA/AAPC credentials, WIOA, Registered Apprenticeship and NOC are retained where translating the formal name could make source verification or job searching harder. Surrounding Spanish text explains the practical meaning.

## Brazilian Portuguese (`pt-BR`) review

**PASS — Brazilian register.** The translation uses Brazilian Portuguese vocabulary and grammar rather than European Portuguese forms.

**PASS — role separation.** `faturamento`, `codificação`, `informação em saúde`, `registros`, `negativas` and `ciclo de receita` remain distinct concepts.

**PASS — employment/education terminology.** `treinamento`, `credencial`, `certificação`, `licenciamento`, `elegibilidade para exame`, `acreditação`, `reembolso`, `descontos em folha` and `período de permanência` are used in context rather than treated as interchangeable.

**PASS — scope language.** The translation preserves the distinction between U.S.-oriented coding work and Colombian/Latin American local work and does not imply that HIPAA, Medicare/Medicaid, CPT/HCPCS or U.S. private credentials automatically govern local employment.

**PASS — retained official terms.** U.S. job titles and formal program/acronym names are retained where they are useful search or verification terms. The surrounding Portuguese text supplies the reader-facing explanation.

## Cross-language controls

The review specifically checked that both translations retain:

- anti-guarantee language for employment, salary, funding and credential acceptance;
- the official-vs-market wage distinction;
- the effective-date warning for code sets;
- the distinction between private certification and government licensing;
- minimum-necessary/privacy and role-based-access concepts;
- prohibition on placing real patient information into public AI tools;
- human accountability for coding/billing decisions;
- Canada NOC comparator qualifications;
- SENA as adjacent Colombian training rather than U.S.-credential equivalence; and
- the instruction not to invent an unsupported Colombian national wage series.

## Controlled decision

**PASS — targeted es-419 and pt-BR natural-language/terminology review.** No blocking linguistic or terminology defect was identified that requires changing a tested numeric, URL, structural, credential, jurisdictional or claims-control element.

Automated parity run `31230074016` remains the current parity baseline because this gate did not modify either translation source. The trilingual masters may proceed to DOCX/PDF publication-candidate generation and artifact QA.