# Guide 01 — Live Link Validation Batch 02

**Guide:** 01 — Community Health Worker  
**Branch:** `revision/guide-00-100-2026`  
**Validation date:** August 4, 2026  
**Scope:** Previously open or time-sensitive official links in the trilingual working masters  
**Status:** Controlled follow-up completed; one Ministry policy source remains open for direct-source replacement review

## Method and evidence controls

This follow-up used fresh browser retrieval and search-engine indexing evidence against official government domains. A result is marked **PASS** only when the destination and content purpose were identifiable. Automated retrieval failures are recorded separately from confirmed broken links. Search-result snippets were used only when they exposed current official-page titles, dates, and content from the relevant government domain.

## Results

| Source | Final URL checked | Result | Evidence and disposition |
|---|---|---|---|
| CareerOneStop — American Job Centers | https://www.careeronestop.org/LocalHelp/AmericanJobCenters/american-job-centers.aspx | PASS WITH DELIVERY NOTE | The primary host returned an automated 403 during direct retrieval, but the official CareerOneStop content resolved through its current CDN-backed official page and current finder pages. The page states that American Job Centers provide free job-search and training assistance and that nearly 2,300 centers operate nationwide. Retain the canonical `www.careeronestop.org` URL; recheck embedded hyperlinks from generated DOCX/PDF. |
| Government of Canada Job Bank — Summary | https://www.jobbank.gc.ca/marketreport/summary-occupation/296075/ca | PASS | Official Job Bank page resolved and identified the occupation as Community Health Worker mapped to NOC 42201. Current indexed and direct versions differed temporarily in displayed median wage and job-count snippets, so the summary page must not be used as the controlling wage source. Retain for occupation mapping only. |
| Government of Canada Job Bank — Requirements | https://www.jobbank.gc.ca/marketreport/requirements/296075/ca | PASS VIA OFFICIAL REGIONAL HOST | The official Job Bank requirements content resolved through the Government of Canada regional host. It states that a college or university program in social work, child and youth care, psychology, or another social-science or health-related discipline is usually required, while relevant volunteer or support experience may replace formal education in some occupations. Retain the national canonical URL and verify the final redirect in publication QA. |
| Government of Canada Job Bank — Wages | https://www.jobbank.gc.ca/marketreport/wages-occupation/296075/ca | PASS — CONTROLLING WAGE SOURCE | Fresh official indexing identifies the national wage table as updated November 19, 2025, with Canada low CAD 19.00/hour, median CAD 26.00/hour, high CAD 36.06/hour, and 83.6% receiving at least one non-wage benefit. The page date is June 2, 2026. These figures match all three working masters. Retain. A temporary maintenance page observed during one direct retrieval does not invalidate the official wage page. |
| Colombia Ministry of Health — RIAS | https://www.minsalud.gov.co/salud/publica/ssr/Paginas/Rutas-integrales-de-atencion-en-salud-RIAS.aspx | PASS | The canonical `www.minsalud.gov.co` host is already present in all three working masters following the controlled normalization. Retain and recheck from generated DOCX/PDF. |
| Colombia Ministry of Health — citizen participation / information page | https://minsalud.gov.co/Participa/Paginas/Consulta-ciudadana-derecho-a-la-informacion-publica.aspx | OPEN — DIRECT-SOURCE SPECIFICITY | Fresh automated retrieval did not return the page content. The URL remains on the official Ministry domain, but this batch did not establish that it is the most direct evidence for the statement about the Social Participation in Health Policy and Resolution 2063 of 2017. Keep the source provisional and continue searching for a direct Ministry policy or resolution page before publication. |

## Income-data reconciliation

The controlled Canada wage source remains the dedicated Job Bank wage page, not the summary-card snippet. The working-master figures remain:

- low: **CAD 19.00 per hour**;
- median: **CAD 26.00 per hour**;
- high: **CAD 36.06 per hour**;
- workers receiving at least one non-wage benefit: **83.6%**.

No content change is required from this batch. The dedicated wage page is more specific and provides the source period and update date. Any temporary summary-card discrepancy is treated as a presentation or cache inconsistency, not as authority to overwrite the detailed wage table.

## QA conclusion

Four previously open or time-sensitive official destinations now have sufficient evidence for controlled retention. The dedicated Canada wage page remains the controlling source and the trilingual figures remain aligned. The Colombia citizen-participation source remains open because source specificity—not merely reachability—has not yet passed.

Guide 01 therefore remains at a **conditional live-link QA pass**. Final publication QA must still open every hyperlink from the generated DOCX and PDF, record redirects and final destinations, and replace the provisional Colombia policy link if a more direct official source is verified.

This record documents automated editorial validation. It is not independent accessibility certification, legal review, medical review, accreditation review, professional translation certification, or third-party publication certification.
