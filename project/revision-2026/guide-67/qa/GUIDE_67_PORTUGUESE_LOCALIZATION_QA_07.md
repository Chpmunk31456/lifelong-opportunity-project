# Guide 67 — Brazilian Portuguese Localization QA 07

**Occupation:** Cook and Culinary Specialist  
**Locale:** Brazilian Portuguese (`pt-BR`)  
**Review date:** 2026-08-20  
**Gate:** Portuguese Localization — PASS

## Controlled source

The Portuguese Version 2 master was localized from the frozen English source:

`project/revision-2026/guide-67/working-masters/GUIDE_67_COOK_AND_CULINARY_SPECIALIST_ENGLISH_v2.md`

Frozen English blob:

`c3ec49ab039676cf35b831bae0ab5250089fd90d`

Portuguese master reviewed:

`project/revision-2026/guide-67/working-masters/GUIDE_67_COOK_AND_CULINARY_SPECIALIST_PTBR_v2.md`

Legacy Portuguese files were not used as the factual source of truth.

## Structural and semantic parity

PASS. The Portuguese master retains the English guide's major section sequence and substantive coverage: occupation scope; role/authority limits; work environment and safety; skills; U.S. education and apprenticeship pathways; food-safety and jurisdiction checks; allergen controls; Canada, Colombia, and Latin America pathways; free-first training; compensation; privacy; cybersecurity; accessibility; responsible AI; 12-week plan; experience-building; progression; verification checklist; sources; notice; and assurance boundary.

The localization does not broaden `culinary specialist` into chef, head cook, food-service manager, dietitian, nutritionist, or another higher-authority or regulated role.

## Identifier, numeric, date, and range parity

PASS. Controlled values remain materially identical without currency conversion:

- O*NET-SOC `35-2014.00`;
- Canada NOC `63200`;
- U.S. official values `USD $17.98`, `USD $37,390`, `USD $34,010`, `USD $44,620`;
- employment/outlook values `1,460,200`, `7% or higher`, `2024–2034`, `250,700`;
- broader BLS comparison `USD $35,760`, `$17.19`, `2,805,100`, `5%`, `130,600`;
- ZipRecruiter estimate `USD $33,340`, `$16.03`, `$28,000–$37,500`, dated August 4, 2026;
- Canada values `CAD $15.00`, `CAD $18.00`, `CAD $25.00`;
- SENA durations `2,200 horas` and `40 horas`.

Government statistics remain distinct from the non-government estimate. No national Colombia wage is introduced.

## URL parity

PASS. All 17 frozen source URLs are present unchanged:

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

PASS. Portuguese preserves the prohibition on independently diagnosing allergies/medical conditions, designing therapeutic diets without qualified clinical authority, declaring food safe when controls failed, overriding food-safety rules, exercising undelegated employment/contract/purchasing/payroll authority, accessing unrestricted sensitive data, representing the employer to regulators without designation, or hiding reportable incidents.

The FDA Food Code remains a model code rather than a single national restaurant law. Credential requirements remain jurisdiction- and employer-dependent. Allergen uncertainty is escalated and approved ingredient/recipe/preparation information is used rather than guessing.

Least-privilege access, no credential sharing, secure handling of payment/employee/customer/scheduling/ordering/inventory/delivery/business data, and verification of suspicious vendor/payment/password/payroll/bank-change requests remain explicit.

Accessibility language remains inclusive without claiming legal review or a guaranteed accommodation outcome.

Public-AI restrictions remain explicit for payment-card data, employee records, customer personal information, unpublished recipes, business data, incident reports, passwords, internal investigations, and other restricted information. AI may not independently decide food safety, allergen presence, medical status, legal applicability, or whether a reportable injury/food-safety incident can be ignored. Human review remains required for AI-assisted recipes, menus, training, schedules, labels, customer communications, and operational decisions.

## Language and encoding review

PASS. The master uses natural Brazilian Portuguese for a general audience. Official U.S./Canadian occupation/program labels and formal SENA program names are retained where precision matters. Accents and UTF-8 text are readable; no mojibake or replacement-character defect was identified.

## Assurance boundary

PASS. No independent human linguistic certification, professional translation certification, culinary/food-safety certification, legal review, accessibility certification, accreditation, licensing approval, funding approval, employment, earnings, apprenticeship placement, or promotion guarantee is claimed.

## Result

**PASS.** Guide 67 Brazilian Portuguese localization is sufficiently complete and controlled to advance to trilingual technical QA.

This is internal machine-assisted localization and QA, not independent human linguistic certification or professional translation certification.
