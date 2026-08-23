# Guide 15 — English v2 Claim-to-Source Traceability QA

**Guide:** 15 — Insurance Claims and Policy Processing Specialist  
**Controlled revision:** August 2026  
**Source reviewed:** `english-v2-working-master.md`  
**Evidence ledger:** `source-review-summary.md`  
**Gate:** Claim-to-source traceability  
**Result:** PASS  

## Purpose

This gate checks that material factual claims in the English v2 working master are traceable to the controlled research ledger and that source types are not blended in ways that could mislead readers. It does not certify downstream localization, DOCX/PDF rendering, metadata, publication packaging, or independent human review.

## Traceability matrix

| Claim area | Working-master treatment | Controlled evidence | Result |
|---|---|---|---|
| U.S. occupation mapping | SOC/O*NET 43-9041.00, Insurance Claims and Policy Processing Clerks | O*NET OnLine 43-9041.00 | PASS |
| U.S. national wage data | May 2025 BLS OEWS: 214,260 employment; $25.44 mean hourly; $52,920 mean annual; $23.67 median hourly | BLS May 2025 national OEWS table | PASS |
| U.S. insurance-industry wage data | Separate industry-specific median/mean figures | BLS insurance carriers and related activities industry profile | PASS |
| Private U.S. market estimate | ZipRecruiter July 21, 2026 estimate for Insurance Claims Processor, explicitly labeled non-government | ZipRecruiter salary page recorded in evidence ledger | PASS |
| Canada mapping | NOC 14201 and OaSIS 14201.02 Insurance clerks | Government of Canada NOC/OaSIS | PASS |
| Colombia training | SENA Técnico en Atención Comercial y Operación en Seguros; 2,208 hours | SENA Betowa | PASS |
| Colombia advanced training | Tecnología en Gestión Administrativa y Comercial de Seguros y Riesgos, code 123204 | SENA Resolution 3779 of 2025 | PASS |
| Colombia income example | COP 3.0–3.6 million/month plus statutory benefits, explicitly identified as one vacancy rather than a national benchmark | Servicio Público de Empleo vacancy recorded in evidence ledger | PASS |
| FAFSA/federal student aid | 2026–27 FAFSA access to grants, work-study, and federal student loans for eligible programs/students | Federal Student Aid | PASS |
| WIOA | Career/training services, including classroom and work-based learning; eligibility/local rules vary | U.S. Department of Labor ETA | PASS |
| Employer educational assistance | Up to $5,250 under a qualifying employer educational-assistance program; employer programs optional | IRS Publication 15-B (2026) | PASS |
| Registered Apprenticeship | Paid work-and-learning model; guide does not promise an insurance-processing apprenticeship in every location | Apprenticeship.gov | PASS |
| Latin America coverage | Requires country-specific regulator, public employment, training, and employer verification; no U.S.-wage conversion into local benchmark | Controlled editorial rule in evidence ledger | PASS |
| Licensing/regulatory boundaries | Role title alone does not establish authority; readers instructed to verify jurisdiction and assigned duties | O*NET scope plus controlled editorial/legal-boundary rule | PASS |
| Responsible AI | Public-AI use restricted for confidential data; AI not treated as authority for coverage, liability, claims, fraud, or rights/obligations | Controlled editorial/privacy rule | PASS |

## Freshness spot checks completed at this gate

Current-source spot checks during this controlled pass reconfirmed:

1. **BLS May 2025 OEWS** still reports the national occupation row used by the master: 214,260 employment, $25.44 mean hourly, $52,920 mean annual, and $23.67 median hourly.
2. **IRS Publication 15-B (2026)** still states an annual $5,250 educational-assistance exclusion under a qualifying program.
3. **Government of Canada OaSIS 2025** still identifies 14201.02 as Insurance clerks and describes the occupation as compiling, processing, and maintaining insurance information.
4. **Federal Student Aid** identifies the 2026–27 FAFSA process and states that FAFSA can provide access to federal grants, work-study, and federal student loans for college, career school, or trade school.
5. **U.S. Department of Labor WIOA** materials continue to describe career and training services, including classroom and work-based learning, with eligibility/local variation.
6. **Apprenticeship.gov** continues to describe Registered Apprenticeship as paid work experience combined with structured on-the-job learning, related instruction, mentorship, progressive wages, and a portable credential.

These checks support the factual claims; they do not replace the separate comprehensive link-status gate.

## Source-type separation controls

PASS — The master keeps the following evidence classes distinct:

- official U.S. occupational statistics;
- private-market salary estimates;
- a single Colombia vacancy example;
- official training/program information; and
- general pathway/funding guidance.

No private estimate is presented as an official statistic, no single vacancy is presented as a national salary benchmark, and no U.S. wage figure is presented as a Latin American compensation benchmark.

## Unsupported-claim review

PASS — No material numeric or jurisdiction-specific claim was found in the working master that lacks a corresponding evidence-ledger source or an explicit caution directing the reader to current local verification.

No claim of independent human certification, accreditation, regulator endorsement, guaranteed employment, guaranteed income, or guaranteed funding was found.

## Next controlled gate

Run comprehensive link/freshness, terminology, structure, and encoding QA across the English v2 working master. If that gate passes, freeze the English v2 source before producing es-419 and pt-BR editions.
