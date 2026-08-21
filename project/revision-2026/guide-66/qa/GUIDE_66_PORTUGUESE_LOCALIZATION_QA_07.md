# Guide 66 — Brazilian Portuguese Localization QA 07

**Occupation:** Food Service Manager Trainee and Restaurant Supervisor  
**Locale:** Brazilian Portuguese (`pt-BR`)  
**Review date:** 2026-08-20  
**Gate:** Portuguese Localization — PASS

## Controlled source

The Portuguese Version 2 master was localized from the frozen English source:

`project/revision-2026/guide-66/working-masters/GUIDE_66_FOOD_SERVICE_MANAGER_TRAINEE_AND_RESTAURANT_SUPERVISOR_ENGLISH_v2.md`

Frozen English blob:

`eb9cf81c6015636bfb7c239415fcf9b04041eafd`

Portuguese master:

`project/revision-2026/guide-66/working-masters/GUIDE_66_FOOD_SERVICE_MANAGER_TRAINEE_AND_RESTAURANT_SUPERVISOR_PTBR_v2.md`

Portuguese master blob at QA review:

`470eb944cb4725a07b164dd605f059878c198ac0`

Legacy Portuguese files were not used as the factual source of truth.

## Structural and semantic parity

PASS. The Portuguese master retains the English guide's major section sequence and substantive content, including:

- occupation definition and trainee/supervisor versus full-manager distinction;
- responsibilities and authority limits;
- work environment and hazards;
- people, operational, business, and leadership skills;
- U.S. education and entry pathways;
- food-safety certification and jurisdiction checks;
- alcohol-service boundary;
- Canada, Colombia, and Latin America pathways;
- free-first and employer-supported training strategy;
- U.S. and Canada compensation sections;
- food safety, allergen awareness, worker safety, privacy, cybersecurity, accessibility, and responsible-AI controls;
- 12-week start plan, experience-building ideas, career progression, and job/training verification checklist;
- controlled source list, notice, and assurance boundary.

No translation step broadened a trainee or supervisor role into unrestricted management authority.

## Classification, numeric, and date parity

PASS. Controlled identifiers and key values were preserved without currency conversion or fabricated normalization, including:

- O*NET-SOC `11-9051.00`;
- Canada NOC `60030`;
- U.S. official values `USD $33.36`, `USD $69,390`, `USD $56,870`, `USD $86,800`;
- employment/outlook values `352,800`, `375,300`, `6%`, `2024–2034`, `42,000`;
- BLS May 2024 comparison `$65,310` and `$31.40`;
- Salary.com estimate `$42,306`, `$20`, `$37,639–$49,149`, dated August 1, 2026;
- ZipRecruiter estimate `$54,962`, `$26.42`, `$45,000–$63,500`, dated August 5, 2026;
- Canada values `CAD $18.00`, `CAD $26.00`, `CAD $48.08`;
- SENA durations `2,208 horas` and `330 horas`.

Government statistics remain distinguished from non-government market estimates. No Colombia national wage was introduced.

## URL parity

PASS. The Portuguese master retains the same 15 controlled URLs as the frozen English source, unchanged:

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

## High-risk boundary review

PASS. The Portuguese localization retains the English controls that a trainee or supervisor does not automatically have authority to hire/fire, alter pay or time records, execute contracts, approve major spending, change pricing/tax/refund rules, override food-safety requirements, authorize unlawful alcohol service, access unrestricted HR/payroll/payment/customer data, represent the employer to regulators without designation, or conceal reportable incidents.

The FDA Food Code remains described as a model code rather than one nationwide restaurant law. Food-safety and responsible-beverage credential requirements remain jurisdiction- and employer-dependent.

Allergen wording remains non-diagnostic and directs uncertainty to approved ingredient/preparation information and escalation rather than guessing.

## Privacy, cybersecurity, accessibility, and AI review

PASS. The Portuguese master retains restrictions on credential sharing and on entering payment-card data, payroll information, employee records, customer personal information, unpublished sales data, incident reports, passwords, confidential recipes, internal investigations, or other restricted business information into public AI systems without organizational approval.

AI is not presented as an autonomous decision-maker for hiring, firing, discipline, promotion, medical status, allergy status, food safety, alcohol-service legality, safety incidents, or legal/regulatory applicability. Human review remains required for AI-assisted schedules, policies, training materials, menu descriptions, customer communications, and operational decisions.

Accessibility language remains practical and inclusive without claiming legal review or a guaranteed accommodation outcome.

## Language and encoding review

PASS. The master uses natural Brazilian Portuguese suitable for a general audience. Official U.S./Canadian occupation labels and formal SENA program names are retained where classification or program-name precision matters. No material unintended English prose was identified outside intentional official names and program concepts. Accents and UTF-8 text render normally; no mojibake was identified in the reviewed master.

## Result

**PASS.** Guide 66 Brazilian Portuguese localization is sufficiently complete and controlled to advance to trilingual technical QA.

## Assurance boundary

This is an internal machine-assisted localization and QA review. It is not independent human linguistic certification, professional translation certification, professional food-safety certification, legal review, accessibility certification, accreditation, licensing advice, regulatory approval, funding approval, or a guarantee of employment or earnings.
