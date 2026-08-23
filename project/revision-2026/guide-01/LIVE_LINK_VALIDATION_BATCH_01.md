# Guide 01 — Live-link validation batch 01

**Guide:** 01 — Community Health Worker  
**Validation date:** 2026-08-04  
**Branch:** `revision/guide-00-100-2026`  
**Status:** Completed first controlled live-link batch; final link gate remains open.

## Method

Each URL below was opened against the current public site. A passing result requires the destination to load, identify the expected institution or program, and support the claim made in the working masters. Search-engine snippets alone were not treated as sufficient when a live destination was available.

This is automated editorial and link QA. It is not independent human certification, accessibility certification, accreditation review, professional translation certification, or legal review.

## Results

| Source | URL tested | Result | Claim supported | Action |
|---|---|---:|---|---|
| U.S. Centers for Disease Control and Prevention | https://www.cdc.gov/chronic-disease/php/community-health-worker-resources/index.html | Pass | CHW role, alternate titles, social-determinants-of-health navigation, and official CHW resources | Retain |
| U.S. Bureau of Labor Statistics | https://www.bls.gov/ooh/community-and-social-service/community-health-workers.htm | Pass | Official U.S. occupation, education, wage, employment, and outlook source | Retain; numerical claims remain subject to final pre-publication recheck |
| Government of Canada Job Bank | https://www.jobbank.gc.ca/marketreport/wages-occupation/296075/ca | Pass | Official Canadian wage table for the broader NOC 42201 mapping | Retain with the existing broader-occupation limitation |
| Apprenticeship.gov | https://www.apprenticeship.gov/apprenticeship-job-finder | Pass | Official U.S. apprenticeship opportunity finder | Retain; do not imply nationwide CHW availability |
| Colombia Ministry of Health and Social Protection — RIAS | https://www2.minsalud.gov.co/salud/publica/ssr/Paginas/Rutas-integrales-de-atencion-en-salud-RIAS.aspx | Conditional / legacy host | The page is indexed and supports community, family, intersectoral, and integrated-care claims, but the `www2` host produced an inconsistent live response during direct validation | Replace with the canonical current host below before publication |
| Colombia Ministry of Health and Social Protection — canonical RIAS page | https://www.minsalud.gov.co/salud/publica/ssr/Paginas/Rutas-integrales-de-atencion-en-salud-RIAS.aspx | Pass | Same RIAS subject matter on the current canonical host | Use as replacement canonical URL |
| Colombia Ministry of Health and Social Protection — PPSS | https://www2.minsalud.gov.co/encuestas/Paginas/Consulta-ciudadana-derecho-a-la-informacion-publica.aspx | Pass with legacy-host caution | Resolution 2063 of 2017 and the Policy of Social Participation in Health | Prefer the current `www.minsalud.gov.co` host if the identical route resolves during final validation |

## Findings

1. The CDC, BLS, Job Bank, and Apprenticeship.gov links used in the working masters are currently valid and materially support their associated claims.
2. The RIAS claim is supported, but the working-master URL uses the older `www2.minsalud.gov.co` host. The canonical current URL is:

   `https://www.minsalud.gov.co/salud/publica/ssr/Paginas/Rutas-integrales-de-atencion-en-salud-RIAS.aspx`

3. The PPSS source remains substantively valid, but its host should be normalized if the equivalent canonical route passes during the final batch.
4. A successful HTTP response does not establish that every linked training course, vacancy, scholarship, funding program, or apprenticeship is currently available to every reader. Eligibility and availability language must remain conditional.

## QA disposition

**Batch result:** Conditional pass.

The first controlled link batch is complete and auditable. The final Guide 01 link gate remains open until:

- the canonical RIAS URL is applied consistently to English, es-419, and pt-BR masters;
- the PPSS host is rechecked and normalized where possible;
- every remaining external URL in all three final masters is tested;
- redirects, page identity, claim support, and locale parity are recorded;
- the generated DOCX hyperlinks and PDF-visible URLs are inspected after publication builds.

## Next controlled action

Apply the canonical RIAS correction across the three working masters using a fail-closed edit, then complete the remaining-link inventory and second validation batch.
