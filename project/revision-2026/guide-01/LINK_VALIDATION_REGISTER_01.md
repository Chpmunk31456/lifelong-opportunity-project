# Guide 01 — External Link Validation Register

**Guide:** 01 — Community Health Worker  
**Branch:** `revision/guide-00-100-2026`  
**Validation date:** August 3, 2026  
**Scope:** External URLs cited in the controlled English working master  
**Status:** Completed browser-level validation pass; final publication-candidate link QA remains required

## Validation method and controls

This register records whether each cited external URL resolved to the intended official source during a fresh browser-level validation pass. A successful result means that the destination was reachable and materially matched the cited purpose at the time checked. It does not guarantee future availability, accessibility conformance, or continued accuracy.

A browser retrieval error is not automatically classified as a broken public URL. Some government sites block automated clients, require JavaScript, use redirects, or intermittently reject requests. Those entries remain open for final command-line and publication-environment verification.

## Results

| Source | URL | Result | Evidence and disposition |
|---|---|---|---|
| CDC — Resources for Community Health Workers | https://www.cdc.gov/chronic-disease/php/community-health-worker-resources/index.html | PASS | Official CDC page resolved. Page title and December 3, 2024 date matched the working master. The page defines CHWs and provides topic-specific resources. Retain. |
| CDC archive — Community Health Worker Training Resource | https://archive.cdc.gov/www_cdc_gov/dhdsp/programs/spha/chw_training/index.htm | PASS WITH AGE WARNING | Official CDC archive resolved. It identifies the 2015 cardiovascular training resource and explicitly states that it is not a replacement for basic CHW training. It also warns that some blood-pressure guidance may be outdated. Retain only with the existing limitation language. |
| CareerOneStop — American Job Centers | https://www.careeronestop.org/LocalHelp/AmericanJobCenters/american-job-centers.aspx | OPEN — AUTOMATED RETRIEVAL ERROR | The automated browser returned an internal retrieval error. The URL remains an official CareerOneStop destination and is not classified as broken on this evidence alone. Recheck with `curl -I -L` and rendered-browser QA before publication. |
| Apprenticeship.gov — Apprenticeship Finder | https://www.apprenticeship.gov/apprenticeship-job-finder | PASS | Official Apprenticeship.gov finder resolved and matched the stated purpose. Retain. Availability of CHW opportunities remains regional and must not be implied. |
| U.S. Bureau of Labor Statistics — Community Health Workers | https://www.bls.gov/ooh/community-and-social-service/community-health-workers.htm | PASS | Official Occupational Outlook Handbook page resolved and matched the occupation. Retain as the primary U.S. wage and outlook source. Reconfirm displayed figures during final publication QA. |
| Government of Canada Job Bank — Summary | https://www.jobbank.gc.ca/marketreport/summary-occupation/296075/ca | PASS | Official Job Bank page resolved for Community Health Worker in Canada. Retain with the existing warning that the mapping uses the broader NOC 42201 group. |
| Government of Canada Job Bank — Requirements | https://www.jobbank.gc.ca/marketreport/requirements/296075/ca | OPEN — AUTOMATED RETRIEVAL ERROR | Automated retrieval failed. Because the adjacent official summary and wage pages resolved, this is treated as an unverified retrieval limitation rather than a confirmed broken link. Recheck in the publication environment. |
| Government of Canada Job Bank — Wages | https://www.jobbank.gc.ca/marketreport/wages-occupation/296075/ca | PASS | Official wage page resolved. Retain with geography, occupation-mapping, date, and non-guarantee controls. |
| Colombia Ministry of Health — RIAS | https://www2.minsalud.gov.co/salud/publica/ssr/Paginas/Rutas-integrales-de-atencion-en-salud-RIAS.aspx | OPEN — AUTOMATED RETRIEVAL ERROR | Automated retrieval failed. The URL uses an older Ministry subdomain and requires a final redirect/status check. Do not remove solely because of the browser error. Replace only if a current canonical Ministry page is verified. |
| Colombia Ministry of Health — Citizen participation / information page | https://minsalud.gov.co/Participa/Paginas/Consulta-ciudadana-derecho-a-la-informacion-publica.aspx | PASS, CONTENT-SCOPE REVIEW REQUIRED | Official Ministry page resolved. The page is reachable, but final editorial QA must confirm that it is the most direct source for the specific social-participation policy statement. Retain provisionally, or replace with a direct policy or Resolution 2063 of 2017 source if verified. |

## Required final-candidate checks

Before Guide 01 is declared publication-ready:

1. Run redirect-aware status checks against every final URL, recording final destination and HTTP status.
2. Open every URL from the generated DOCX and PDF, not only from Markdown.
3. Confirm that no link redirects to a generic homepage, login page, error page, unrelated content, or unsafe destination.
4. Replace the older RIAS URL only when a current canonical Ministry source is confirmed.
5. Confirm the most direct official source for Colombia's social-participation policy and Resolution 2063 of 2017.
6. Recheck the BLS and Job Bank figures and page-modification dates immediately before publication.
7. Preserve descriptive link text in DOCX and PDF; do not use ambiguous labels such as “click here.”

## QA conclusion

Six of the ten cited destinations resolved and matched their intended official-source purpose during this pass. Three official destinations produced automated retrieval errors and therefore remain open for redirect-aware publication-environment testing. One reachable Colombian policy link requires a content-specificity review. No URL was classified as definitively broken based solely on an automated-client failure.

This validation is an automated editorial control. It is not independent accessibility certification, legal review, medical review, accreditation review, or third-party publication certification.
