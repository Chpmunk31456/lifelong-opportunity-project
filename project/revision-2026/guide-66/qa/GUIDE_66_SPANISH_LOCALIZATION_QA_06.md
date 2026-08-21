# Guide 66 — Spanish Localization QA 06

**Occupation:** Food Service Manager Trainee and Restaurant Supervisor  
**Locale:** neutral Latin American Spanish (`es-419`)  
**Review date:** 2026-08-20  
**Gate:** Spanish Localization — PASS

## Source control

The Spanish Version 2 working master was localized from the frozen English master only:

`project/revision-2026/guide-66/working-masters/GUIDE_66_FOOD_SERVICE_MANAGER_TRAINEE_AND_RESTAURANT_SUPERVISOR_ENGLISH_v2.md`

Frozen English blob:

`eb9cf81c6015636bfb7c239415fcf9b04041eafd`

Spanish master reviewed:

`project/revision-2026/guide-66/working-masters/GUIDE_66_FOOD_SERVICE_MANAGER_TRAINEE_AND_RESTAURANT_SUPERVISOR_ES419_v2.md`

The legacy Spanish package was not used as the factual source of truth. No public translation service or external translation API was used.

## Structural and semantic parity

PASS. The Spanish master retains the frozen English section sequence and substantive coverage, including:

- occupation definition and trainee/supervisor/manager distinctions;
- opportunity framing and work-environment realities;
- typical responsibilities and explicit authority limits;
- people/service, operational, business, and leadership skills;
- U.S. entry pathways and low-cost progression;
- food-safety certification and jurisdiction verification;
- alcohol-service boundary;
- Canada, Colombia, and broader Latin America pathways;
- free-first and employer-supported training strategy;
- U.S. official compensation, non-government market estimates, and Canada wages;
- food safety, allergens, worker safety, privacy, cybersecurity, accessibility, and responsible AI;
- 12-week start plan, experience-building ideas, career progression, and pre-acceptance verification;
- controlled sources, important notice, and assurance boundary.

No substantive English section was intentionally omitted or collapsed into a materially narrower Spanish statement.

## Classification, figure, date, and range parity

PASS. Controlled values were preserved without currency conversion or silent normalization:

- O*NET-SOC `11-9051.00`;
- Canada NOC `60030`;
- U.S. official wages: `USD $33.36`, `USD $69,390`, `USD $56,870`, `USD $86,800`;
- U.S. outlook: `352,800`, `375,300`, `6%`, `2024–2034`, `42,000`;
- BLS May 2024 comparison: `$65,310`, `$31.40`;
- Salary.com estimate: `$42,306`, `$20`, `$37,639–$49,149`, August 1, 2026;
- ZipRecruiter estimate: `$54,962`, `$26.42`, `$45,000–$63,500`, August 5, 2026;
- Canada wages: `CAD $18.00`, `CAD $26.00`, `CAD $48.08`;
- SENA program durations: `2,208 horas` and `330 horas`.

Government and non-government compensation remain clearly separated. The Spanish master does not invent a national Colombia wage figure.

## URL parity

PASS. All 15 controlled URLs are present unchanged and in the same numbered source set:

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

## Terminology and language quality

PASS. The Spanish uses neutral Latin American wording and avoids unnecessary country-specific slang. Role terminology is kept natural rather than implying a credential that does not exist:

- `Restaurant Supervisor` → `supervisor/a de restaurante`;
- `Management Trainee` → `persona en formación gerencial` / `formación gerencial` according to sentence context;
- `Food Service Manager` is translated contextually while the official O*NET label remains in English beside the classification identifier where precision matters;
- NOC `60030` retains the official Canadian classification label where needed;
- formal SENA program titles remain in their official Spanish wording;
- U.S. `Registered Apprenticeship` remains identifiable as the U.S. program concept and is not presented as universally available.

No malformed diacritics or obvious mojibake were identified in the controlled Spanish master.

## Safety and authority boundaries

PASS. The localization preserves that a trainee or supervisor does not automatically have authority to hire/fire, formally discipline, alter payroll or time records, sign contracts, approve major purchases, change menu pricing or taxes, override food-safety controls, authorize unlawful alcohol service, access unrestricted HR/payment/customer data, represent the employer to regulators, or conceal reportable incidents.

The FDA Food Code remains described as a model rather than a single nationwide restaurant law. Food-safety certification and responsible-beverage requirements remain dependent on jurisdiction and employer requirements.

Allergen language continues to prohibit diagnosis or unsupported medical claims and instructs the reader to rely on approved ingredient/preparation information and escalation when uncertain.

## Privacy, cybersecurity, accessibility, and AI boundaries

PASS. The Spanish master preserves least-privilege and data-handling controls for POS, payment, payroll, employee, customer, reservation, loyalty, delivery, and other restricted information.

It preserves the prohibition on placing payment-card data, payroll data, employee records, customer personal information, unpublished sales data, incident reports, passwords, confidential recipes, internal investigations, or other restricted business information into a public AI system without explicit organizational approval.

It also preserves that AI must not independently decide hiring, firing, discipline, promotion, medical status, allergy status, food safety, alcohol-service legality, whether a safety incident can be ignored, or whether a legal/regulatory requirement applies. Human review remains required for AI-assisted schedules, policies, training materials, menu descriptions, customer communications, and operational decisions.

Accessibility wording remains practical and inclusive without creating a promise of a particular accommodation outcome or claiming legal review.

## Assurance boundary

PASS. The Spanish master states that the work is internally machine-assisted and does not claim independent human certification, professional translation certification, professional food-safety certification, legal review, accessibility certification, accreditation, licensing advice, regulatory approval, funding approval, employment, earnings, or promotion guarantees.

## Result

**PASS.** Guide 66 Spanish localization has sufficient structural, factual, terminology, safety, link, numeric, and assurance parity with the frozen English Version 2 source to close the `spanish_localization` gate.

This is an internal machine-assisted controlled-project localization review; it is not independent human linguistic certification or professional translation certification.