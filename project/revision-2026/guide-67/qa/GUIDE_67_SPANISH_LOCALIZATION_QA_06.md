# Guide 67 — Spanish Localization QA 06

**Occupation:** Cook and Culinary Specialist  
**Locale:** neutral Latin American Spanish (`es-419`)  
**Review date:** 2026-08-20  
**Gate:** Spanish Localization — PASS

## Controlled source

The Spanish Version 2 master was localized from the frozen English source:

`project/revision-2026/guide-67/working-masters/GUIDE_67_COOK_AND_CULINARY_SPECIALIST_ENGLISH_v2.md`

Frozen English blob:

`c3ec49ab039676cf35b831bae0ab5250089fd90d`

Spanish master reviewed:

`project/revision-2026/guide-67/working-masters/GUIDE_67_COOK_AND_CULINARY_SPECIALIST_ES419_v2.md`

Legacy Spanish files were not used as the factual source of truth.

## Structural and semantic parity

PASS. The Spanish master retains the frozen English guide's major section sequence and substantive coverage, including occupation scope; role and authority boundaries; work environment and safety; skills; U.S. education and apprenticeship pathways; food-safety and jurisdiction checks; allergen controls; Canada, Colombia, and Latin America pathways; free-first training; U.S. and Canada compensation; privacy, cybersecurity, accessibility, and responsible AI; 12-week plan; experience-building; career progression; pre-acceptance checks; source list; important notice; and assurance boundary.

No localization step broadens `culinary specialist` into chef, head cook, food-service manager, dietitian, nutritionist, or another higher-authority or regulated role.

## Identifier, numeric, date, and range parity

PASS. Controlled values remain materially identical to the English source without currency conversion:

- O*NET-SOC `35-2014.00`;
- Canada NOC `63200`;
- U.S. official wages `USD $17.98`, `USD $37,390`, `USD $34,010`, `USD $44,620`;
- employment/outlook values `1,460,200`, `7% or higher`, `2024–2034`, `250,700`;
- broader BLS comparison `USD $35,760`, `$17.19`, `2,805,100`, `5%`, `130,600`;
- ZipRecruiter estimate `USD $33,340`, `$16.03`, `$28,000–$37,500`, dated August 4, 2026;
- Canada wages `CAD $15.00`, `CAD $18.00`, `CAD $25.00`;
- SENA program durations `2,200 horas` and `40 horas`.

Government statistics and the current non-government estimate remain separately labeled. No national Colombia wage figure is invented.

## URL parity

PASS. All 17 frozen source URLs are retained unchanged:

1. https://www.onetonline.org/link/summary/35-2014.00
2. https://www.onetonline.org/link/details/35-2014.00
3. https://www.onetonline.org/link/localwages/35-2014.00
4. https://www.onetonline.org/link/result/35-2014.00?c=we
5. https://www.bls.gov/ooh/food-preparation-and-serving/cooks.htm
6. https://www.ziprecruiter.com/Salaries/Cook-Salary
7. https://www.fda.gov/food/retail-food-protection/fda-food-code
8. https://www.fda.gov/food/fda-food-code/food-code-2022
9. https://www.fda.gov/food/hfp-constituent-updates/fda-releases-supplement-2022-food-code
10. https://www.jobbank.gc.ca/marketreport/summary-occupation/6224/ca
11. https://www.jobbank.gc.ca/wagereport/occupation/6224
12. https://www.jobbank.gc.ca/marketreport/requirements/6229/ca
13. https://betowa.sena.edu.co/oferta/cocina?location=57011001&modality=P&programId=76525
14. https://betowa.sena.edu.co/oferta/cocina-basica-nivel-1?modality=P&programId=14074
15. https://www.careeronestop.org/LocalHelp/EmploymentAndTraining/find-WIOA-training-programs.aspx
16. https://www.careeronestop.org/FindTraining/find-training.aspx
17. https://www.ilo.org/es/centro-interamericano-para-el-desarrollo-del-conocimiento-en-la-formacion

## Safety, allergen, authority, privacy, cybersecurity, accessibility, and AI boundaries

PASS. Spanish retains that a cook must not independently diagnose allergies or medical conditions, design therapeutic diets without qualified authority, declare food safe when required controls have failed, override health or employer food-safety requirements, exercise undelegated employment/contract/purchasing/payroll authority, access unrestricted sensitive data, represent the employer to regulators without designation, or conceal reportable incidents.

The FDA Food Code remains identified as a model code rather than one national restaurant law. Food-safety credentials remain jurisdiction- and employer-dependent. Allergen questions rely on approved ingredient/recipe/preparation information and escalation rather than guessing.

The localization preserves least-privilege handling of POS, payment, employee, customer, scheduling, ordering, inventory, delivery-platform, and business information; prohibits credential sharing; and requires suspicious vendor/payment/password/payroll/bank-change requests to be verified through approved channels.

Accessibility language remains practical and inclusive without claiming legal review or a guaranteed accommodation outcome.

Public-AI restrictions remain explicit for payment-card data, employee records, customer personal information, unpublished recipes, business data, incident reports, passwords, internal investigations, and other restricted information. AI is not allowed to independently decide food safety, allergen presence, medical status, legal applicability, or whether an injury/food-safety incident can be ignored. Human review remains required for AI-assisted recipes, menus, training, schedules, labels, customer communications, and operational decisions.

## Language and encoding review

PASS. The Spanish uses neutral Latin American wording, preserves formal SENA program names, and intentionally retains official U.S./Canadian occupation/program labels where classification precision matters. Diacritics and UTF-8 text are readable; no mojibake or replacement-character defect was identified in the reviewed master.

## Assurance boundary

PASS. The Spanish master does not claim independent human linguistic certification, professional translation certification, culinary or food-safety certification, legal review, accessibility certification, accreditation, licensing approval, funding approval, employment, earnings, apprenticeship placement, or promotion guarantees.

## Result

**PASS.** Guide 67 Spanish localization has sufficient structural, factual, terminology, safety, link, numeric, and assurance parity with the frozen English Version 2 source to close the `spanish_localization` gate.

This is an internal machine-assisted controlled-project localization review, not independent human linguistic certification or professional translation certification.
