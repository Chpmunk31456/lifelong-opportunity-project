# Guide 97 — Portuguese Localization QA 07

## Guide
Mechanical Engineering Technician

## Locale
Brazilian Portuguese (`pt-BR`)

## Source control
- Frozen English source: `project/revision-2026/guide-97/working-masters/GUIDE_97_MECHANICAL_ENGINEERING_TECHNICIAN_ENGLISH_v2.md`
- Frozen English blob: `f923ec4bbe08cd81d881091f204a4aa3d0c6c7cb`
- Portuguese master: `project/revision-2026/guide-97/working-masters/GUIDE_97_MECHANICAL_ENGINEERING_TECHNICIAN_PORTUGUESE_pt-BR_v2.md`
- Portuguese blob: `183a888d50148d4059c041b850548bef87e2cb09`

## Predecessor gates
- Baseline Inventory: **PASS**
- Current-source Research: **PASS**
- English Editorial: **PASS**
- Evidence / Traceability: **PASS**
- English Source Freeze: **PASS**
- Spanish Localization (`es-419`): **PASS**

## Localization controls checked
The Brazilian Portuguese edition was reviewed against the frozen English source for semantic and controlled-value parity.

### Occupation and jurisdiction identifiers
- O*NET-SOC **17-3027.00** preserved.
- Canada **NOC 22301** preserved.
- Colombia **CUOC 31150** preserved.
- Technician/technologist versus licensed/registered engineer authority boundary preserved.

### Controlled compensation values
- U.S. 2025 official median preserved as **$35.82/hour / $74,510/year**.
- Earlier BLS OOH May 2024 median preserved as **$68,730/year** and clearly dated separately.
- Canada Job Bank national values preserved as **C$23.08 low / C$35.00 median / C$51.28 high per hour**, updated November 19, 2025.
- ZipRecruiter context preserved as **$75,124/year ($36.12/hour)** as of August 7, 2026.
- Salary.com context preserved as **$58,275/year ($28/hour)** with **$51,667–$65,216** 25th–75th percentile range as of August 1, 2026.
- Colombia Computrabajo broader-title context preserved as approximately **COP 1.4M–1.8M/month**, with the non-equivalence caveat to CUOC 31150 retained.

### Training and pathway values
- SENA **Mantenimiento Mecánico Industrial** preserved as Tecnólogo, **3,984 hours**.
- SENA **Mantenimiento Electromecánico Industrial** preserved as Tecnólogo, **3,984 hours**.
- U.S. associate-degree/other postsecondary-training pathway preserved.
- Canadian two-/three-year technologist and one-/two-year technician program distinctions preserved.
- WIOA/American Job Center, Government of Canada training agreements, SENA, and OIT/Cinterfor locators retained without funding/admission guarantees.

### Safety and professional-scope semantics
The Portuguese edition preserves the fail-safe boundaries for:
- hazardous-energy control and lockout/tagout;
- stored electrical, hydraulic, pneumatic, gravitational, thermal, chemical, spring, rotational, and pressure energy;
- machine guarding and rotating equipment;
- pressure systems and stored mechanical force;
- lifting/rigging, welding and hot work;
- controlled engineering changes and drawing revisions;
- calibration and measurement traceability;
- PLC/controller, firmware, network and safety-system change authorization;
- stop-work and escalation when authority or safety is unclear.

### Cybersecurity and responsible AI
The edition preserves:
- approved-device/account controls, MFA, removable-media caution, controlled software/firmware changes and protection of engineering data;
- the prohibition on treating AI as final authority for dimensions, tolerances, loads, stresses, material selection, pressure/temperature limits, torque, safety factors, lifting limits, maintenance intervals, test criteria, guarding, LOTO, engineering changes, regulation or production release;
- confidentiality restrictions for proprietary drawings, specifications, customer data, credentials, export-controlled information and production-system data.

### Accessibility and action plan
- Variable physical-demand and accommodation-process language preserved without legal-entitlement claims.
- All **six action-plan steps** and their measurable milestones are present, repairing the legacy `Action Plan 1 To 6: False` defect.

### Source parity
All **26 reader-verification destinations** from the frozen English source are retained with unchanged URLs across U.S., Canada, Colombia/Latin America and non-government compensation sections.

### Assurance boundary
No unsupported claim was introduced for independent human certification, certified translation, engineering accreditation, professional licensure, accessibility certification, legal/safety review, guaranteed funding, guaranteed employment or guaranteed income.

## Gate result
**PASS — Portuguese Localization (`pt-BR`)**

No blocker identified for Trilingual Technical QA.

## Post-freeze source-link correction revalidation — 2026-08-22

NIST moved the reader-verification page for *Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile*. The obsolete URL ending in `-profile` returned HTTP 404 during Publication QA. The official NIST publication page was reverified on 2026-08-22 and the URL-only correction was applied in English, `es-419`, and `pt-BR` with no change to occupational claims, wage/training values, safety/professional-scope controls, cybersecurity/AI guidance, action-plan milestones, or assurance boundaries.

- Revalidated English blob: `f923ec4bbe08cd81d881091f204a4aa3d0c6c7cb`
- Revalidated Spanish blob: `f851c168d366ee8ab551a63c842a7df830bcba91`
- Revalidated Portuguese blob: `183a888d50148d4059c041b850548bef87e2cb09`
- Correct official NIST destination: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
- Result: **PASS — affected gate revalidated after URL-only source correction.**
