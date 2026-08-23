# Guide 26 - Portuguese localization QA 07

**Guide:** 26 - Automotive Service Technician and Mechanic

**Date:** 2026-08-10

**Stage:** Portuguese Localization Helper (`pt-BR`)

**Status:** **PASS**

## Controlled source

English frozen source:

`26-automotive-service-technician-and-mechanic/english/Guide_26_Automotive_Service_Technician_and_Mechanic_English_v2.0.md`

Frozen English blob SHA: `0288089e3b2577a715cfcc0916973b715f2a47ad`

## Controlled localization

`26-automotive-service-technician-and-mechanic/portuguese/Guide_26_Tecnico_de_Servicos_Automotivos_e_Mecanico_Portuguese_v2.0.md`

Portuguese blob SHA at QA review: `05de70c6cb703cc308d4597436ee1084014bae95`

## Localization checks

### Locale and readability

The edition uses natural Brazilian Portuguese (`pt-BR`). Automotive terminology is readable for Brazilian users while official foreign program and occupational names remain traceable where translation could create ambiguity.

**Result: PASS.**

### Structural parity

All 15 numbered sections, safety subsections, 30/60/90-day plan, United States/Canada/Colombia source groups, and final reminder from the frozen English source are present. No material safety, wage, funding, credential, privacy, accessibility, or jurisdiction section was omitted.

**Result: PASS.**

### Numeric parity

The Portuguese edition preserves the material values from the frozen English source: BLS USD 49,670 annual / USD 23.88 hourly median, 805,600 employment, 4% growth, 33,600 projected numerical change, about 70,000 annual openings; Indeed USD 28.61 average, USD 17.01-48.11 range, about 53,500 observations, USD 24.09 entry-level and USD 35.59 senior estimates; Canada C$19.00 / C$29.89 / C$43.27 and 85%; and Colombia COP 1.5M-2.5M and COP 4.0M-4.5M vacancy examples. Dates and the July 2026-October 2028 SENA example are retained.

Official statistics remain clearly separate from non-government estimates and vacancy examples.

**Result: PASS.**

### Safety and regulatory boundaries

High-voltage, ADAS, airbags, lifts, fuel, refrigerant, hazardous-material and stored-energy stop-work boundaries are preserved. EPA Section 609 is explicitly framed as a United States requirement for compensated motor-vehicle air-conditioning service and not as Brazilian or cross-border authorization.

**Result: PASS.**

### Funding, scholarships, apprenticeships, and employer support

WIOA, American Job Centers, Apprenticeship.gov, public education, grants, scholarships, paid learning, employer reimbursement and tool support remain conditional possibilities. No entitlement, funding guarantee, scholarship guarantee, apprenticeship placement or employer benefit was invented.

**Result: PASS.**

### Canada, Colombia, and Latin America

NOC 72410 and Red Seal remain Canadian systems with provincial/territorial variation; SENA Betowa and Agencia Publica de Empleo remain Colombian locators; and the Latin America framework remains jurisdiction-first with an explicit warning against automatic credential portability.

**Result: PASS.**

### AI, privacy, cybersecurity, accessibility, and ethical evidence

The Portuguese text retains conservative AI boundaries, customer/employer data protections, accessible-training guidance, truthful portfolio labeling and the requirement to remove personal or confidential vehicle/customer data.

**Result: PASS.**

### Source-link parity

All source URLs from the frozen English master are preserved unchanged: BLS, Apprenticeship.gov, DOL/WIOA, CareerOneStop, EPA, U.S. Department of Education, Indeed, Canada Job Bank, Red Seal, SENA Betowa and SENA Agencia Publica de Empleo.

**Result: PASS.**

### Encoding and unsupported-certification language

The Markdown is UTF-8 and preserves Brazilian Portuguese diacritics. It makes no claim of independent human certification, professional translation certification, accessibility certification, legal review, accreditation or automotive licensing approval.

**Result: PASS.**

## Disposition

The Brazilian Portuguese Version 2.0 localization is semantically aligned with the frozen English source and passes the Portuguese Localization Helper gate.

**Portuguese Localization Helper (`pt-BR`): PASS.**

The next controlled gate is trilingual technical QA. Publication remains fail-closed until technical QA passes.
