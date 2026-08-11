# Guide 31 — Brazilian Portuguese Localization QA 07

**Guide:** 31 — Plumber, Pipefitter, and Plumbing Technician  
**Language:** Brazilian Portuguese (`pt-BR`)  
**Date:** 2026-08-11  
**Frozen English source blob:** `c4e41d6b9c6bed68b17feea82566f09bd3597072`  
**Candidate:** `project/revision-2026/guide-31/publication-candidate/GUIDE_31_PORTUGUESE_BR_v2.md`  
**Result:** **PASS**

## Structural parity

PASS. The localization retains all 18 numbered sections in the same sequence as the frozen English source: occupation definition, task distinctions, safety and stop/escalate controls, U.S. legal/licensing boundaries, entry routes, labor-market evidence, free/low-cost support, apprenticeship, Canada, Colombia, Latin America, technical/professional skills, cybersecurity/privacy, responsible AI, accessibility, job-search preparation, twelve-week planning, and verification/source controls.

## Safety and legal-authority parity

PASS. The Portuguese edition preserves material safety boundaries for hazardous energy, pressure/hot systems, confined spaces, excavations/trenches, fuel gas, medical gas, fire protection, backflow, specialty piping, contamination, permits, inspection, supervision, and scope escalation. OSHA 29 CFR 1910.147, 1926.1201, Subpart P, and 1926.651 remain explicitly U.S.-context references and are not generalized to Brazil or other jurisdictions.

The edition also preserves that the United States has no single national plumbing license authorizing independent plumbing everywhere and that a school certificate does not itself establish legal work authority.

## Apprenticeship and funding parity

PASS. The edition retains:

- BLS apprenticeship as the typical on-the-job training route;
- the BLS description of a 4- or 5-year apprenticeship and approximately 2,000 paid on-the-job hours per year;
- the controlled warning that the public Apprenticeship.gov fetch did not support a new blanket occupation-specific approval claim for O*NET 47-2152.00;
- FAFSA as a free application process with eligibility dependent on student, institution, and program;
- WIOA/American Job Center support as locally variable;
- the IRS Section 127 2026 amount of up to USD 5,250 under a qualifying employer plan without implying universal employer participation;
- paid apprenticeship and public/employer-supported routes as options to compare before private-school debt.

## Controlled numerical parity

PASS. Material values are preserved with locale-appropriate punctuation only:

- U.S. 2024 employment: 504,500;
- BLS median: USD 62,970/year and USD 30.27/hour;
- lowest 10%: below USD 40,670;
- highest 10%: above USD 105,150;
- projected 2034 employment: 527,200;
- projected growth: 4%, numeric 22,700;
- approximately 44,000 openings/year;
- Indeed non-government estimate: approximately USD 30.53/hour with displayed range around USD 16.77–55.59/hour;
- Canada: C$21.00 low / C$34.00 median / C$46.00 high;
- SENA complementary-course durations: 48, 48, and 60 hours;
- SENA Construcción de edificaciones Técnico: 2,160 hours;
- apprenticeship duration: 4 or 5 years and approximately 2,000 paid on-the-job hours per year;
- Section 127: up to USD 5,250 for calendar year 2026 under qualifying conditions.

Private wage evidence remains explicitly non-government and no wage is presented as guaranteed.

## Canada, Colombia, and Latin America parity

PASS. NOC 72300 and Red Seal Plumber remain distinct from province/territory-specific apprenticeship, compulsory-trade, certification, gas, medical-gas, backflow, contractor, permit, inspection, and specialty requirements.

For Colombia, SENA Betowa remains public/free-first learning evidence, not an international plumber credential or universal Colombian license claim. The 48/60-hour complementary courses remain clearly distinct from the broader 2,160-hour Técnico program and from a U.S. 4- or 5-year apprenticeship.

The Latin America section preserves the requirement to verify country/local authority and explicitly warns against transplanting U.S. OSHA/licensing, Canadian Red Seal, or Colombian SENA rules into another jurisdiction.

## Cybersecurity, AI, accessibility, and claims boundary

PASS. Cybersecurity/privacy controls for connected building/water systems and customer/facility information are preserved. Responsible-AI boundaries remain explicit: AI is not sole authority for fuel-gas/medical-gas work, pressure isolation/testing, hot tapping, backflow/cross-connection, potable-water contamination control, sizing/code compliance, trench/confined-space entry, hazardous-energy isolation, welding/brazing/hot work, permits/inspections, or license/credential scope.

Accessibility language remains supportive while preserving essential safety and legal-scope requirements.

The candidate does not claim independent human review, professional translation certification, accessibility certification, legal review, licensing approval, code approval, accreditation, employment, funding, or wage guarantees.

## Source/link, language, terminology, and encoding QA

PASS. Controlled direct URLs from the frozen English edition are retained unchanged: BLS, Indeed, Apprenticeship.gov, Federal Student Aid, DOL WIOA/American Job Centers, IRS, OSHA, Government of Canada Job Bank, Red Seal, and four SENA Betowa sources.

Brazilian Portuguese is natural and readable while selected legal/trade/program identifiers (`pipefitter`, `steamfitter`, `journey`, Registered Apprenticeship, LOTO, OSHA, NOC, Red Seal, HVAC, IT/OT, MFA, FAFSA, WIOA) remain in their source form where translation could obscure identity. UTF-8 accents and punctuation are intact; no mojibake or unfinished localization marker is present.

## Conclusion

**Portuguese Localization Helper: PASS.** The `pt-BR` edition is suitable to advance to Guide 31 Technical QA while the frozen English source remains authoritative for factual and structural parity.