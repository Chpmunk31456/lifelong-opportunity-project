# Guide 75 — Spanish Localization QA 06

**Stage:** Spanish Localization (`es-419`) — **PASS**  
**Occupation:** Marketing Coordinator and Digital Marketing Assistant  
**Frozen English source:** `project/revision-2026/guide-75/working-masters/GUIDE_75_MARKETING_COORDINATOR_AND_DIGITAL_MARKETING_ASSISTANT_ENGLISH_v2.md`  
**Frozen English blob:** `384d922df6a8a2f3806c21e74d5bf47b02888e60`  
**Spanish master:** `project/revision-2026/guide-75/working-masters/GUIDE_75_MARKETING_COORDINATOR_AND_DIGITAL_MARKETING_ASSISTANT_ES419_v2.md`  
**QA date:** 2026-08-21

## Controlled localization checks

The neutral Latin American Spanish working master was produced from the frozen English source, not from the legacy Spanish publication package and not through an external public translation API/service.

### Occupational identifiers and geography

PASS:

- U.S. benchmark preserved: **O*NET-SOC 13-1161.00**.
- Canada benchmark preserved: **NOC 11202**.
- Colombia comparisons preserved: **OCUPACOL 24312 and 24311**.
- U.S., Canada, Colombia, and Latin America/Caribbean pathway distinctions remain explicit.

### Controlled wage, outlook, and training values

PASS. The Spanish master preserves the frozen-source controlled values and their context:

- U.S. O*NET 2025 median: **$37.87/hour**, **$78,760/year**.
- U.S. O*NET distribution: **$43,390 / $78,760 / $155,480** annual 10th/median/90th-percentile figures.
- BLS May 2024 median: **$76,950/year**.
- BLS 2024–2034 growth: **7%**.
- BLS annual openings: about **87,200**.
- Indeed U.S. Marketing Coordinator estimate: about **$57,136/year**, displayed range **$40,235–$81,136/year**, about **4.3k** salaries, updated **August 2, 2026**.
- Canada Job Bank: **C$20.50 / C$35.58 / C$57.44 per hour**, updated **November 19, 2025**, reference period 2023–2024.
- Colombia Indeed market estimate: about **COP 3,042,755/month**, updated **May 25, 2026**, only **2 reported salaries**; small-sample limitation preserved.
- SENA Marketing Digital: **48 hours**; both virtual and in-person pathways preserved.

Official statistics and non-government market estimates remain separately labeled; no averaging or unsupported Colombia national wage was introduced.

### Source-link parity

PASS. The Spanish master preserves the frozen controlled source set of **15 URLs**:

1. `https://www.onetonline.org/link/details/13-1161.00`
2. `https://www.onetonline.org/link/localwages/13-1161.00`
3. `https://www.bls.gov/ooh/business-and-financial/market-research-analysts.htm`
4. `https://www.careeronestop.org/LocalHelp/EmploymentAndTraining/find-WIOA-training-programs.aspx`
5. `https://www.jobbank.gc.ca/marketreport/wages-occupation/27114/ca`
6. `https://www.canada.ca/en/services/jobs/training.html`
7. `https://www.canada.ca/en/services/jobs/training/initiatives/skills-success.html`
8. `https://ocupacol.mintrabajo.gov.co/Profile/OccupationalProfile/24312`
9. `https://ocupacol.mintrabajo.gov.co/Profile/OccupationalProfile/24311`
10. `https://betowa.sena.edu.co/oferta/marketing-digital?modality=V&programId=155939`
11. `https://betowa.sena.edu.co/oferta/marketing-digital?modality=P&offertype=open&programId=142014`
12. `https://www.oitcinterfor.org/`
13. `https://www.oitcinterfor.org/statsfp/paises`
14. `https://www.indeed.com/career/marketing-coordinator/salaries`
15. `https://co.indeed.com/career/coordinador-de-mercadotecnia/salaries`

### Authority and risk boundaries

PASS. Spanish localization preserves the source meaning for:

- assistant/coordinator/specialist/analyst/manager authority distinctions;
- campaign and budget approval limits;
- truthful advertising and unsupported-claim restrictions;
- vendor-payment and bank-change verification;
- privacy, consent, unsubscribe, suppression, preference, retention, and customer-data limits;
- least-privilege access, MFA, password/account protection, phishing, fraud and domain/account takeover controls;
- accessibility support without claiming legal conformance or certification;
- responsible-AI limits for factual claims, prices, regulated content, statistics, consequential translation, targeting, accessibility and customer-data decisions;
- prohibition on placing sensitive customer, payment, credential, API-key, unreleased campaign, contract, or protected-personal data into unapproved AI tools.

### Entry pathways and free-first framing

PASS. The Spanish master preserves:

- BLS bachelor’s-degree benchmark for the professional occupation while clearly distinguishing variable junior-role requirements;
- WIOA/CareerOneStop as a locator, not guaranteed funding;
- work-based learning without assuming a dedicated Registered Apprenticeship;
- Canada training/Skills for Success links without admission/funding guarantees;
- SENA live-availability caveat;
- OIT/Cinterfor as a regional institution locator, not a guaranteed course/scholarship/apprenticeship source.

### Language, encoding, and assurance boundary

PASS:

- neutral Latin American Spanish used;
- UTF-8 content; no intended mojibake or placeholder translation text;
- occupational codes, currencies, dates, ranges, percentages and URL targets retained;
- no independent human certification, professional translation certification, legal review, accessibility certification, accreditation, employment guarantee, funding guarantee, or earnings guarantee is claimed.

## Result

**PASS — Spanish Localization (`es-419`).**

Next controlled gate: Brazilian Portuguese localization (`pt-BR`).

This is an internal machine-assisted localization QA record, not independent human or professional translation certification.