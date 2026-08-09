# Guide 15 — English v2 Technical, Link, Freshness, Structure, and Encoding QA

**Guide:** 15 — Insurance Claims and Policy Processing Specialist  
**Revision date:** 2026-08-09  
**Branch:** `revision/guide-00-100-2026`  
**Input:** `references/english-v2-working-master.md`  
**Evidence ledger:** `references/source-review-summary.md`

## Gate result

**PASS — English v2 technical/source QA.** The English v2 working master is suitable for controlled source freeze and localization. This QA record does **not** certify translations, DOCX/PDF artifacts, publication packaging, independent human review, accreditation, endorsement, or employment outcomes.

## Checks completed

### 1. Occupational scope and terminology — PASS

- Primary U.S. mapping remains **SOC/O*NET 43-9041.00 — Insurance Claims and Policy Processing Clerks**.
- The guide consistently distinguishes clerical/processing work from licensed insurance sales, underwriting, claims adjustment/examination, legal interpretation, fraud determination, and other consequential authority.
- Canada is separately mapped to **NOC 14201** and OaSIS **14201.02 — Insurance clerks**; the text does not imply statistical or legal equivalence with U.S. SOC.
- Colombia and broader Latin America are presented as jurisdiction-specific pathways, not as extensions of U.S. licensing or wage data.

### 2. Income labeling and freshness — PASS

Official U.S. figures were revalidated against the BLS May 2025 OEWS material:

- national employment: **214,260**;
- mean hourly wage: **$25.44**;
- mean annual wage: **$52,920**;
- median hourly wage: **$23.67**.

The BLS insurance-carriers-and-related-activities profile was also revalidated for 2025:

- median hourly / annual: **$23.97 / $49,860**;
- mean hourly / annual: **$25.92 / $53,920**.

The current private-market indicator remains separately labeled as non-government. ZipRecruiter reported **$46,461/year ($22.34/hour)** for **Insurance Claims Processor** as of **July 21, 2026**, with a reported majority range of approximately **$38,000–$53,000**. It is not merged with BLS data.

The Bogotá Servicio Público de Empleo example remains explicitly labeled as a **single vacancy example, not a national salary benchmark**.

### 3. Funding, training, and apprenticeship claims — PASS

- Federal Student Aid material reflects the **2026–27 FAFSA** and correctly describes access to grants, work-study, and federal student loans for eligible students/programs without promising eligibility.
- U.S. Department of Labor WIOA material supports career/training services, including classroom and work-based learning, while the guide correctly states that local eligibility and provider rules vary.
- IRS Publication 15-B (2026) confirms the **$5,250 annual educational-assistance exclusion**; the guide correctly states that employer programs are optional and plan-specific.
- Apprenticeship.gov remains the official federal apprenticeship portal. The guide does not claim that a claims-processing Registered Apprenticeship exists in every location.
- SENA's insurance pathway references remain framed as current public training resources whose cohort, modality, and location availability must be rechecked before enrollment.

### 4. Link/freshness review — PASS with one crawler note

The principal links used for occupational mapping, wages, funding, apprenticeship, SENA enrollment, SENA Resolution 3779 of 2025, and the Colombia vacancy example were rechecked on 2026-08-09.

The direct OaSIS 2025 profile URL returned a crawler-side internal error during one automated fetch, but Canada's indexed OaSIS 2025 search result independently confirmed **14201.02 — Insurance clerks** and its 2025 profile status. This is recorded as a tooling observation, not evidence that the public profile is invalid. The guide's instruction to revalidate important links before spending remains appropriate.

### 5. Structure and readability — PASS

- The master uses a clear H1/H2 hierarchy and 19 numbered topical sections.
- Headings are descriptive and ordered logically from role definition through pathways, funding, safety, AI, advancement, and source controls.
- Lists are used for tasks and checks rather than dense inline strings.
- Acronyms are introduced in context or linked to the responsible official program.
- Income sections identify geography, source type, measure, and date/context.
- Accessibility guidance includes headings, meaningful links, screen-reader structure, non-color-only status communication, captions/transcripts, keyboard access, alternative formats, and accommodation processes.

### 6. Encoding and publication-safety language — PASS

- Controlled Markdown text is UTF-8 and no intentional mojibake or replacement-character content was introduced in the v2 master.
- The guide includes explicit no-guarantee language for employment, income, admission, funding, licensing, certification, promotion, and other outcomes.
- No claim of independent human certification, accreditation, regulator endorsement, or guaranteed employment/funding was identified.
- Responsible-AI language prohibits treating AI output as authoritative for coverage, liability, claim disposition, policy interpretation, fraud, or customer rights/obligations and requires authorized handling of sensitive data.

## Sources revalidated for this gate

- O*NET OnLine 43-9041.00: https://www.onetonline.org/link/summary/43-9041.00
- BLS May 2025 national OEWS table: https://www.bls.gov/news.release/ocwage.t01.htm
- BLS Insurance Carriers and Related Activities profile: https://www.bls.gov/iag/tgs/iag524.htm
- ZipRecruiter, Insurance Claims Processor Salary: https://www.ziprecruiter.com/Salaries/Insurance-Claims-Processor-Salary
- Canada OaSIS search/profile family: https://noc.esdc.gc.ca/OaSIS/
- Federal Student Aid FAFSA steps: https://studentaid.gov/articles/fafsa-student-steps/
- DOL WIOA programs: https://www.dol.gov/agencies/eta/wioa/programs
- IRS Publication 15-B (2026): https://www.irs.gov/publications/p15b
- Apprenticeship.gov: https://www.apprenticeship.gov/
- SENA enrollment portal: https://www.sena.edu.co/es-co/formacion/Paginas/inscripcionProgramas.aspx
- SENA Resolution 3779 of 2025: https://normograma.sena.edu.co/compilacion/docs/resolucion_sena_3779_2025.htm
- Servicio Público de Empleo vacancy example: https://personas.serviciodeempleo.gov.co/detalle_oferta.aspx?dep_id=11&proceso_id=129&sede_id=1625928173

## Next controlled gate

Freeze the English v2 source with its evidence references intact. Only after that freeze should neutral Latin American Spanish (`es-419`) and Brazilian Portuguese (`pt-BR`) localization begin. Translation parity, terminology, links, generated DOCX/PDF files, metadata, checksums, visual rendering, and release audit remain **not yet passed** for Guide 15.
