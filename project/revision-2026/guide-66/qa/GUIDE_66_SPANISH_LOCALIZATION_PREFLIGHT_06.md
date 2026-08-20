# Guide 66 — Spanish Localization Preflight 06

**Occupation:** Food Service Manager Trainee and Restaurant Supervisor  
**Locale:** neutral Latin American Spanish (`es-419`)  
**Review date:** 2026-08-20  
**Stage:** Spanish localization preflight — COMPLETE; localization gate remains PENDING

## Authoritative source

Spanish Version 2 must be localized only from the frozen English master:

`project/revision-2026/guide-66/working-masters/GUIDE_66_FOOD_SERVICE_MANAGER_TRAINEE_AND_RESTAURANT_SUPERVISOR_ENGLISH_v2.md`

Frozen Git blob identity:

`eb9cf81c6015636bfb7c239415fcf9b04041eafd`

Legacy Spanish material is historical reference only and must not be used as the factual source of truth.

## Required terminology controls

Use neutral Latin American Spanish and preserve role distinctions:

- Food Service Manager → gerente de servicios de alimentos / gerente de servicio de alimentos, according to context;
- Restaurant Supervisor → supervisor/a de restaurante;
- Management Trainee → aprendiz de gerencia / persona en formación gerencial, choosing natural wording by sentence rather than creating a false formal credential;
- Food Service Managers (`11-9051.00`) → retain the official English occupation name alongside the O*NET-SOC identifier where classification precision matters;
- NOC `60030` → retain the official Canadian classification identifier and avoid implying that every trainee/supervisor automatically belongs to the manager occupation;
- Registered Apprenticeship → preserve as the U.S. program concept and do not translate it into a claim of automatic apprenticeship availability;
- SENA program names → retain official Spanish program names exactly where they are formal titles.

Do not translate employer-specific or legal authority into broader powers than the English source grants.

## Controlled numeric and classification parity set

The Spanish draft must preserve, without conversion or silent normalization:

- O*NET-SOC `11-9051.00`;
- Canada NOC `60030`;
- U.S. official wage values: `$33.36`, `$69,390`, `$56,870`, `$86,800`;
- U.S. employment/outlook values: `352,800`, `375,300`, `6%`, `2024–2034`, `42,000`;
- BLS May 2024 comparison: `$65,310`, `$31.40`;
- Salary.com estimate: `$42,306`, `$20`, `$37,639–$49,149`, August 1, 2026;
- ZipRecruiter estimate: `$54,962`, `$26.42`, `$45,000–$63,500`, August 5, 2026;
- Canada wages: `CAD $18.00`, `CAD $26.00`, `CAD $48.08`;
- SENA durations: `2,208 horas` and `330 horas`.

Government and non-government compensation figures must remain clearly separated. No Colombia national salary figure may be invented.

## Controlled URL parity set

All 15 frozen source URLs must remain unchanged in the Spanish master:

1. https://www.onetonline.org/link/summary/11-9051.00
2. https://www.onetonline.org/link/localwages/11-9051.00
3. https://www.onetonline.org/link/localtrends/11-9051.00
4. https://www.bls.gov/ooh/management/food-service-managers.htm
5. https://www.salary.com/research/salary/position/restaurant-supervisor-salary
6. https://www.ziprecruiter.com/Salaries/Restaurant-Supervisor-Salary
7. https://www.fda.gov/food/retail-food-protection/fda-food-code
8. https://www.fda.gov/food/fda-food-code/food-code-2022
9. https://www.fda.gov/food/hfp-constituent-updates/fda-releases-supplement-2022-food-code
10. https://www.jobbank.gc.ca/marketreport/summary-occupation/2031/ca
11. https://www.jobbank.gc.ca/wagereport/occupation/2025?wbdisable=true
12. https://www.jobbank.gc.ca/marketreport/requirements/2031/ca
13. https://betowa.sena.edu.co/oferta/servicio-de-restaurante-y-bar?modality=P&programId=137214
14. https://betowa.sena.edu.co/oferta/emprendedor-en-tecnicas-de-mesa-y-bar-para-el-servicio-de-alimentos-y-bebidas?programId=66655
15. https://www.careeronestop.org/LocalHelp/EmploymentAndTraining/find-WIOA-training-programs.aspx

## Safety and scope boundaries that must survive localization

The Spanish master must preserve the English meaning that a trainee or supervisor does not automatically have authority to:

- hire, dismiss, suspend, or formally discipline employees;
- alter wages, payroll, time records, contracts, menu prices, taxes, discounts, or major purchases outside delegated authority;
- override food-safety controls;
- authorize alcohol service contrary to applicable law or employer policy;
- access unrestricted HR, payroll, payment-card, or customer data;
- represent the employer to regulators unless formally designated;
- conceal injuries, food-safety incidents, harassment reports, theft, or other reportable events.

Food-safety certification and responsible-beverage requirements must remain jurisdiction- and employer-dependent. The FDA Food Code must remain described as a model code, not a single nationwide restaurant law.

## Privacy, cybersecurity, accessibility, and AI controls

Localization must retain restrictions on sharing credentials, payment-card data, employee/payroll records, customer personal information, unpublished business information, incident reports, confidential recipes, internal investigations, and other restricted information.

AI must not be framed as an autonomous decision-maker for hiring, firing, discipline, promotion, medical status, allergy status, food safety, alcohol-service legality, safety incidents, or legal/regulatory applicability. Human review remains required for AI-assisted schedules, policies, training materials, menu descriptions, customer communications, and operational decisions.

Accessibility language must remain operational and inclusive without creating legal advice or promising a particular accommodation outcome.

## Mechanical QA required before PASS

Before `spanish_localization` may be marked PASS, verify:

1. heading and section-sequence parity against the frozen English source;
2. all 15 URLs unchanged and present;
3. all controlled classifications, figures, dates, currencies, percentages, and ranges preserved;
4. no unintended untranslated English prose except official names/classification labels intentionally retained;
5. no mojibake or malformed diacritics;
6. neutral `es-419` terminology rather than country-specific slang;
7. no semantic drift in food-safety, alcohol-service, worker-safety, authority, privacy, cybersecurity, accessibility, allergen, or responsible-AI boundaries;
8. SENA and other official program names preserved accurately;
9. assurance language does not claim professional translation certification, legal review, food-safety certification, accessibility certification, accreditation, funding approval, employment, or earnings guarantees.

## Result

**COMPLETE as preflight only.** The frozen source, terminology map, controlled figures, URL parity set, and high-risk semantic boundaries are ready for Spanish drafting and QA. The Guide 66 `spanish_localization` gate remains **PENDING** until the full `es-419` master and separate localization QA evidence are completed and reviewed.
