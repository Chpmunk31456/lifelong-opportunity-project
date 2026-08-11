# Guide 31 — Spanish Localization QA 06

**Guide:** 31 — Plumber, Pipefitter, and Plumbing Technician  
**Language:** neutral Latin American Spanish (`es-419`)  
**Date:** 2026-08-11  
**Frozen English source blob:** `c4e41d6b9c6bed68b17feea82566f09bd3597072`  
**Candidate:** `project/revision-2026/guide-31/publication-candidate/GUIDE_31_SPANISH_es-419_v2.md`  
**Result:** **PASS**

## Structural parity

PASS. The localization retains the frozen English source's 18 numbered sections in the same sequence, including occupation definition, task distinctions, safety and stop/escalate controls, U.S. licensing boundaries, entry routes, labor-market evidence, free/low-cost support, apprenticeship, Canada, Colombia, Latin America, technical/professional skills, cybersecurity/privacy, responsible AI, accessibility, job-search preparation, twelve-week planning, and verification/source controls.

## Safety and legal-authority parity

PASS. The Spanish edition preserves the frozen source's material safety boundaries for hazardous energy, pressure/hot systems, confined spaces, excavations/trenches, fuel gas, medical gas, fire protection, backflow, specialty piping, contamination, permits, inspection, supervision, and scope escalation. It retains OSHA 29 CFR 1910.147, 1926.1201, Subpart P, and 1926.651 references without converting them into universal rules outside their stated U.S. context.

The localization also preserves that the United States has no single national plumbing license authorizing independent plumbing everywhere and that a school certificate does not itself establish legal work authority.

## Apprenticeship and funding parity

PASS. The Spanish edition retains:

- BLS's statement that apprenticeship is the typical on-the-job training route;
- the BLS description of a 4- or 5-year apprenticeship and approximately 2,000 paid on-the-job hours per year;
- the controlled caution that the current public Apprenticeship.gov fetch did not support a new blanket occupation-specific approval claim for O*NET 47-2152.00;
- FAFSA as a free application process whose aid eligibility depends on the student, institution, and program;
- WIOA/American Job Center support as locally variable;
- the IRS Section 127 2026 amount of up to USD 5,250 under a qualifying employer plan, without implying that every employer offers it;
- paid apprenticeship and public/employer-supported routes as options to compare before private-school debt.

## Controlled numerical parity

PASS. The material semantic values are preserved:

- U.S. 2024 employment: 504,500;
- BLS median: USD 62,970/year and USD 30.27/hour;
- lowest 10%: below USD 40,670;
- highest 10%: above USD 105,150;
- projected 2034 employment: 527,200;
- projected growth: 4%, numeric 22,700;
- approximately 44,000 openings/year;
- Indeed non-government estimate: approximately USD 30.53/hour with displayed low/high values around USD 16.77–55.59/hour;
- Canada: C$21.00 low / C$34.00 median / C$46.00 high;
- SENA complementary-course durations: 48, 48, and 60 hours;
- SENA Construcción de edificaciones Técnico: 2,160 hours;
- apprenticeship duration: 4 or 5 years and approximately 2,000 paid on-the-job hours per year;
- Section 127: up to USD 5,250 for calendar year 2026 under qualifying conditions.

Private wage evidence remains explicitly non-government and no wage is presented as guaranteed.

## Canada and Colombia parity

PASS. NOC 72300 and Red Seal Plumber remain distinct from province/territory-specific apprenticeship, compulsory-trade, certification, gas, medical-gas, backflow, contractor, permit, inspection, and specialty requirements.

For Colombia, SENA Betowa offerings remain free/public-first learning evidence rather than a claim of international plumber status or a universal Colombian license. The short 48/60-hour complementary courses remain explicitly distinct from the broader 2,160-hour Técnico program and from a U.S. 4- or 5-year apprenticeship. Local technical regulations, permits, utility rules, gas authorization, employer/contractor conditions, and competence/certification requirements remain verification items.

## Latin America, cybersecurity, AI, and accessibility parity

PASS. The localization preserves the instruction not to transplant U.S. OSHA/licensing, Canadian Red Seal, or Colombian SENA rules into other jurisdictions. It retains privacy and cybersecurity controls for connected building/water systems and customer/facility information.

The responsible-AI section preserves the prohibition on treating AI as sole authority for fuel-gas/medical-gas work, pressure isolation/testing, hot tapping, backflow/cross-connection decisions, potable-water contamination control, sizing/code compliance, trench/confined-space entry, hazardous-energy isolation, welding/brazing/hot work, permits/inspections, or licensing/credential scope.

Accessibility language remains supportive without implying that accommodations remove essential safety requirements or legal-scope restrictions.

## Source/link parity

PASS. The controlled direct URLs from the frozen English edition are retained unchanged, including BLS, Indeed, Apprenticeship.gov, Federal Student Aid, DOL WIOA/American Job Centers, IRS, OSHA, Government of Canada Job Bank, Red Seal, and the four SENA Betowa sources. Source labels may be localized, but source identity and jurisdiction remain intact.

## Language, terminology, encoding, and claims boundary

PASS. The candidate uses neutral Latin American Spanish and retains selected English regulatory/trade terms such as `pipefitter`, `steamfitter`, `journey`, Registered Apprenticeship, LOTO, OSHA, NOC, Red Seal, HVAC, IT/OT, MFA, FAFSA, and WIOA where translation could obscure the underlying legal or program identity. UTF-8 punctuation and accents are intact; no mojibake was observed in the committed candidate.

The edition does not assert independent human review, professional translation certification, accessibility certification, legal review, licensing approval, code approval, accreditation, employment, funding, or wage guarantees.

## Conclusion

**Spanish Localization Helper: PASS.** The `es-419` edition is suitable to advance to Brazilian Portuguese localization while the English frozen source remains authoritative for factual and structural parity.
