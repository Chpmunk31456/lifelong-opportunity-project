# Guide 02 — External Link and Freshness Revalidation QA 21

Date: 2026-08-07  
Branch: `revision/guide-00-100-2026`

## Gate purpose

Revalidate the controlled source ledger before DOCX/PDF generation, distinguishing an actually broken link from an automated-client fetch restriction, and recheck time-sensitive market values/dates.

This is internal project QA. It is not independent certification, accreditation, legal review, accessibility certification, or professional translation certification.

## Result

**PASS — external links and freshness have been revalidated, and the required ZipRecruiter date refresh has been applied.**

The current ZipRecruiter Peer Support Specialist page still reports the same national market estimate used by the guide — **US$41,023/year and US$19.72/hour** — but its displayed freshness date has advanced from **July 16, 2026** to **August 7, 2026**. The three controlled language masters have been refreshed to the current market-source as-of date before DOCX/PDF generation.

No value change was identified for that market estimate.

## Revalidation findings

### U.S. Bureau of Labor Statistics — PASS

URL: `https://www.bls.gov/ooh/community-and-social-service/community-health-workers.htm`

Direct retrieval succeeded. Current page content continues to support:

- Community Health Workers median annual wage: **US$51,030** in May 2024;
- hourly equivalent displayed by BLS: **US$24.54**;
- projected employment growth: **11% from 2024 to 2034**;
- BLS text explicitly identifies **peer support specialists** as one type/title within community health work; and
- BLS states that some community health workers participate in apprenticeships or other hands-on programs.

The guide's use remains a clearly labeled official occupational proxy rather than a dedicated peer-support wage series.

### SAMHSA peer-support sources — PASS with automated-client restriction noted

Controlled URLs:

- `https://www.samhsa.gov/substance-use/recovery/peer-support-workers/core-competencies`
- `https://www.samhsa.gov/substance-use/recovery/peer-support-workers`

Direct automated retrieval returned HTTP 403 in this QA environment, but current search-index retrieval resolves both official SAMHSA pages and confirms the content remains live. The core-competencies page still presents recovery-oriented, person-centered, voluntary, relationship-focused, and trauma-informed principles and reports **Last Updated: 03/24/2026**. The peer-support-workers page likewise resolves as current SAMHSA content and reports **Last Updated: 03/24/2026**.

A 403 from an automated client is therefore recorded as a retrieval restriction, not evidence that the public source is broken.

### Apprenticeship.gov — PASS

URL: `https://www.apprenticeship.gov/`

Direct retrieval succeeded. The guide continues to use it only as a locator for Registered Apprenticeship opportunities and does not claim that a peer-support apprenticeship exists in every jurisdiction.

### CareerOneStop / American Job Centers — PASS with redirect/index behavior noted

Controlled URL: `https://www.careeronestop.org/LocalHelp/AmericanJobCenters/american-job-centers.aspx`

The direct automated open did not return normal page content in this environment, but current indexed content resolves the American Job Center finder and states that AJCs provide free career/employment assistance and training-navigation support. The source remains appropriate as a public workforce-services locator.

### Federal Student Aid — PASS

URL: `https://studentaid.gov/`

Direct retrieval succeeded. The guide appropriately treats this as an aid-information source and expressly warns that not every peer-support training program is aid-eligible.

### ZipRecruiter — PASS

URL: `https://www.ziprecruiter.com/Salaries/Peer-Support-Specialist-Salary`

Direct retrieval succeeded on 2026-08-07. Current displayed figures are:

- average annual pay: **US$41,023**;
- approximate hourly pay: **US$19.72**;
- displayed current date: **As of Aug 7, 2026**;
- majority range remains approximately **US$35,000 to US$45,000**.

The guide correctly labels this as a **non-government market estimate**, not an official wage statistic or guarantee. The source-freshness date has been updated in the three controlled masters.

### Government of Canada Job Bank — PASS

Controlled wage URL: `https://www.jobbank.gc.ca/marketreport/wages-occupation/24973/ca`

Direct retrieval succeeded and continues to report:

- national low: **C$19.00/hour**;
- national median: **C$26.00/hour**;
- national high: **C$36.06/hour**;
- wage update date: **November 19, 2025**;
- reference period: **2023–2024**;
- source: Statistics Canada Labour Force Survey.

Current indexed Job Bank material for the same Peer Support Worker occupation continues to show a page modification date of **June 2, 2026** and province/territory-specific outlooks. The guide retains the required broader-NOC-42201 qualification.

### Colombia — Ministerio de Salud y Protección Social — PASS

Controlled URLs:

- `https://www.minsalud.gov.co/salud/publica/salud-mental/Paginas/salud-mental-comunitaria.aspx`
- `https://www.minsalud.gov.co/salud/publica/salud-mental/Paginas/politica-salud-mental.aspx`

The Política de Salud Mental page retrieved directly. The Salud Mental Comunitaria page did not return normally through direct automated open but resolves through current indexed content. Current community-mental-health content continues to list:

- community-based rehabilitation guidance;
- 2025 community mental-health device guidance;
- 2025 psychological first-aid technical guidance; and
- 2025 integrated territorial health-network materials.

This supports the guide's community/mutual-help pathway discussion but does not establish a U.S.-style national Peer Support Specialist credential.

### SENA — PASS

URL: `https://www.sena.edu.co/`

The official domain resolves. The guide uses SENA only as a public training locator and expressly requires readers to verify current course availability and relevance.

### Servicio Público de Empleo — PASS with automated-client restriction noted

URL: `https://www.serviciodeempleo.gov.co/`

The direct automated client did not return normal content in this environment. The controlled use is limited to a public employment/opportunity locator; no specific current vacancy or training entitlement is asserted from the URL alone.

### World Health Organization — PASS

URL: `https://www.who.int/publications/i/item/9789240025783`

Direct retrieval succeeded. The page remains the WHO publication **Peer support mental health services: Promoting person-centred and rights-based approaches**, dated **9 June 2021**, and describes peer-support services emphasizing hope, shared experience, empowerment, human rights, legal capacity, and avoidance of coercive practices.

The guide correctly treats WHO material as an international conceptual framework rather than a portable national occupational credential.

## Applied correction before artifact generation

The ZipRecruiter source date was updated in all three controlled masters:

- English: `as of July 16, 2026` → `as of August 7, 2026`
- Spanish: `al 16 de julio de 2026` → `al 7 de agosto de 2026`
- Brazilian Portuguese: `em 16 de julho de 2026` → `em 7 de agosto de 2026`

The same date refresh has been applied while preserving **US$41,023/year** and **US$19.72/hour** and the explicit non-government/market-estimate qualification.

## Controlled decision

External-source revalidation is complete and the required source-date corrections have been applied. Guide 02 may proceed to the focused post-correction parity check and downstream DOCX/PDF artifact QA.
