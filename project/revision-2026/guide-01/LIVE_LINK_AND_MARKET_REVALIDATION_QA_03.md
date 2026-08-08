# Guide 01 live-link and market-estimate revalidation QA 03

**Guide:** 01 — Community Health Worker  
**Validation date:** 2026-08-06  
**Scope:** English working master income sources and the corresponding claims that must remain equivalent in the es-419 and pt-BR editions  
**Status:** Controlled revalidation completed; one market-estimate correction is required before publication-artifact generation  

## Assurance boundary

This record documents source availability and claim-to-source comparison performed on the date above. It is automated/editorial QA evidence only. It is not independent human certification, professional translation certification, accreditation, legal review, medical review, or a guarantee that a third-party page will remain unchanged.

## Revalidation results

| Source | Live-link result | Claim comparison | Disposition |
|---|---|---|---|
| U.S. Bureau of Labor Statistics, Community Health Workers | Reachable | The page continues to report May 2024 median pay of USD 51,030 annually and USD 24.54 hourly, 65,100 jobs in 2024, 11% projected growth for 2024–2034, and approximately 7,800 openings per year. The employment table separately reports numeric employment growth of 7,400; the guide correctly treats 7,800 as annual openings rather than employment change. | Pass |
| Government of Canada Job Bank, Community Health Worker wages, NOC 42201 | Reachable | The national table continues to report CAD 19.00 low, CAD 26.00 median, and CAD 36.06 high hourly wages. It states that wages were updated November 19, 2025 and use a 2023–2024 reference period. | Pass |
| ZipRecruiter, Community Health Worker salary | Reachable | The page continues to report USD 44,925 average annual pay and USD 21.60 hourly as of July 27, 2026. It states that estimates are derived from employer job postings and third-party data. | Pass |
| Glassdoor, Community Health Worker salaries | Reachable | The current page displays a USD 52,000 median total-pay estimate and a USD 44,000–63,000 total-pay range. It no longer substantiates the working masters’ exact statement of USD 52,306 average annual pay based on 1,936 submissions. The visible page also labels the displayed figure as median total pay, not average pay. | **Correction required** |

## Required controlled correction

Before DOCX/PDF generation, replace the stale Glassdoor figure and methodology statement in all three working masters with wording supported by the current page. The correction must:

1. describe the value as an approximate **median total-pay estimate of USD 52,000 per year**, not an average salary;
2. preserve the visible **USD 44,000–63,000 total-pay range** as contextual, non-official information;
3. identify the source as Glassdoor and record access/revalidation in August 2026;
4. avoid asserting an unsupported submission count;
5. retain the warning that non-government estimates use different methods and must not replace BLS data or be treated as guaranteed offers;
6. be applied equivalently to English, neutral Latin American Spanish, and Brazilian Portuguese without changing safety, credential, or income-disclaimer meaning.

## Source URLs

- https://www.bls.gov/ooh/community-and-social-service/community-health-workers.htm
- https://www.jobbank.gc.ca/marketreport/wages-occupation/296075/ca
- https://www.ziprecruiter.com/Salaries/Community-Health-Worker-Salary
- https://www.glassdoor.com/Salaries/community-health-worker-salary-SRCH_KO0,23.htm

## QA gate decision

**Live-link and dated-market gate: conditional hold.** Three income sources remain supported as written. The Glassdoor claim must be corrected in the three working masters and then rechecked for exact occurrence count, trilingual meaning parity, UTF-8 integrity, and Markdown hygiene. Publication-artifact generation remains blocked until that controlled correction passes.
