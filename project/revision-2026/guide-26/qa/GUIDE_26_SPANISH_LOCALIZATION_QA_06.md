# Guide 26 - Spanish localization QA 06

**Guide:** 26 - Automotive Service Technician and Mechanic

**Date:** 2026-08-10

**Stage:** Spanish Localization Helper (`es-419`)

**Status:** **PASS**

## Controlled source

English frozen source:

`26-automotive-service-technician-and-mechanic/english/Guide_26_Automotive_Service_Technician_and_Mechanic_English_v2.0.md`

Frozen English blob SHA:

`0288089e3b2577a715cfcc0916973b715f2a47ad`

## Controlled localization

`26-automotive-service-technician-and-mechanic/spanish/Guide_26_Tecnico_de_Servicio_Automotriz_y_Mecanico_Spanish_v2.0.md`

Spanish blob SHA at QA review:

`b3b96f5b1f79e1c6e732a57ca004fe080748f80e`

## Localization checks

### Locale and readability

The edition uses neutral Latin American Spanish (`es-419`) rather than Spain-specific forms. Automotive terminology is understandable across Latin America while retaining official program and occupational names such as BLS, WIOA, Registered Apprenticeship, NOC 72410, Red Seal, SENA Betowa, and Agencia Publica de Empleo where translating the proper name could reduce traceability.

**Result: PASS.**

### Structural parity

The localization preserves the frozen English source's 15 numbered sections, safety subsections, 30/60/90-day plan, source groups for the United States/Canada/Colombia, and final reminder. No English section containing a material safety, funding, employment, wage, privacy, accessibility, or credential boundary was omitted.

**Result: PASS.**

### Numeric parity

Material date-sensitive values were compared with the frozen English source:

| Claim | English | Spanish | Result |
|---|---:|---:|---|
| BLS 2024 median annual pay | USD 49,670 | USD 49,670 | PASS |
| BLS hourly median | USD 23.88 | USD 23.88 | PASS |
| BLS 2024 employment | 805,600 | 805,600 | PASS |
| 2024-2034 growth | 4% | 4% | PASS |
| projected numerical change | 33,600 | 33,600 | PASS |
| annual openings | about 70,000 | aproximadamente 70,000 | PASS |
| Indeed average | USD 28.61/hour | USD 28.61/hora | PASS |
| Indeed displayed range | USD 17.01-48.11 | USD 17.01-48.11 | PASS |
| Indeed observation basis | about 53,500 | aproximadamente 53,500 | PASS |
| entry-level estimate | USD 24.09/hour | USD 24.09/hora | PASS |
| senior estimate | USD 35.59/hour | USD 35.59/hora | PASS |
| Canada wages | C$19.00 / 29.89 / 43.27 | C$19.00 / 29.89 / 43.27 | PASS |
| Canada benefit share | 85% | 85% | PASS |
| Colombia examples | COP 1.5M-2.5M / 4.0M-4.5M | COP 1.5M-2.5M / 4.0M-4.5M | PASS |
| SENA example dates | Jul 2026-Oct 2028 | julio 2026-octubre 2028 | PASS |

Official statistics remain distinct from non-government market estimates and individual Colombian vacancy examples.

**Result: PASS.**

### Safety and regulatory boundaries

The localization preserves the English source's stop-work requirements for high voltage, ADAS, airbags, lifts, fuel, refrigerants, hazardous materials, stored energy, unavailable specifications, and work outside verified competence. The U.S. EPA Section 609 requirement remains explicitly limited to compensated motor-vehicle air-conditioning service in the United States and does not imply cross-border authorization.

**Result: PASS.**

### Funding, scholarships, apprenticeships, and employer support

WIOA, American Job Centers, Apprenticeship.gov, public education, scholarships, grants, employer reimbursement, paid learning, tool programs, and supportive services remain conditional. The Spanish text does not turn a locator or possibility into an entitlement or guarantee.

**Result: PASS.**

### Canada, Colombia, and Latin America

NOC 72410 and Red Seal are framed as Canadian systems with provincial/territorial variation. SENA Betowa and Agencia Publica de Empleo remain Colombian locators. The Latin America section remains jurisdiction-first and explicitly rejects automatic credential portability.

**Result: PASS.**

### AI, privacy, cybersecurity, accessibility, and ethics

The localization retains the prohibition on using general-purpose AI as final authority for safety-critical or regulated work, preserves the restrictions on entering customer/employer-confidential data into public AI systems, and keeps accommodation guidance conditional on applicable law and policy. Portfolio examples remain explicitly fictional or truthful and require removal of personal/confidential data.

**Result: PASS.**

### Source-link parity

All source URLs from the frozen English master are preserved unchanged in the Spanish edition, including BLS, Apprenticeship.gov, DOL/WIOA, CareerOneStop, EPA, U.S. Department of Education, Indeed, Canada Job Bank, Red Seal, SENA Betowa, and SENA Agencia Publica de Empleo.

**Result: PASS.**

### Encoding and unsupported-certification language

The Markdown is UTF-8 and uses normal Spanish diacritics. The localization makes no claim of independent human certification, professional translation certification, accessibility certification, legal review, accreditation, or automotive licensing approval.

**Result: PASS.**

## Disposition

The neutral Latin American Spanish Version 2.0 localization is semantically aligned with the frozen English source and passes the Spanish Localization Helper gate.

**Spanish Localization Helper (`es-419`): PASS.**

The next controlled gate is Brazilian Portuguese (`pt-BR`) localization. Technical/publication QA remains fail-closed until Portuguese localization is completed and separately validated.
