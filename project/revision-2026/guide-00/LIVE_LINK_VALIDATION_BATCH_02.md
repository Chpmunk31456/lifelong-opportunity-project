# Guide 00 Live Link Validation — Batch 02

**Guide:** 00 — Lifelong Opportunity Foundation Guide  
**Branch:** `revision/guide-00-100-2026`  
**Validation date:** 2026-08-02  
**Status:** Completed live-link validation batch; not a publication certificate

## Scope

This batch validates additional official URLs used by the English, neutral Latin American Spanish, and Brazilian Portuguese integrated masters. It records both successful retrievals and inconclusive automated results. An inconclusive automated result is not classified as a broken link without a later browser-based or document-render check.

## Successfully validated

| Region | Resource | URL | Result | Publication control |
|---|---|---|---|---|
| Canada | Canada Apprentice Loan | https://www.canada.ca/en/services/jobs/training/support-skilled-trades-apprentices/loan.html | Active official page. Confirms up to CAD 4,000 in interest-free loans per technical-training period and exclusion of Quebec, which has alternate support. | Keep classified as repayable financing, not a grant. |
| Canada | Employment Insurance for apprentices | https://www.canada.ca/en/services/jobs/training/support-skilled-trades-apprentices/ei-apprentices.html | Active official page. Confirms possible EI eligibility during referred full-time technical training, subject to referral and claim requirements. | Do not imply automatic eligibility or payment. |
| Brazil | Ministry of Labour and Employment — Qualificação Profissional | https://www.gov.br/trabalho-e-emprego/pt-br/servicos/trabalhador/qualificacao-profissional | Active official page. Supports the federal professional-qualification pathway and public-policy context. | Do not describe page availability as proof that a particular course or intake is open. |
| Brazil | Caminho Digital | https://www.gov.br/pt-br/servicos/inscrever-em-curso-do-caminho-digital | Active official service page. | Course availability, prerequisites, completion rules, and certificate terms must be checked on the live service. |
| Mexico | Jóvenes Construyendo el Futuro platform | https://www.jovenesconstruyendoelfuturo.stps.gob.mx/ | Active official platform. | Placement windows, municipality availability, stipend amount, and documentary requirements must still be checked immediately before application. |
| Argentina | Progresar Trabajo application service | https://www.argentina.gob.ar/servicio/inscribirme-en-progresar-trabajo | Active official service page. | Application dates and eligibility remain time-sensitive and must be date-stamped. |

## Inconclusive automated validation

| Region | Resource | URL | Automated result | Required next step |
|---|---|---|---|---|
| Canada | Red Seal provincial and territorial contacts | https://www.red-seal.ca/eng/contact/c.4nt.1ct.shtml | Automated environment did not open the URL because of a safety-resolution limitation. | Recheck in a normal browser and during DOCX/PDF hyperlink inspection. Do not mark broken. |
| Chile | ChileAtiende — Programa Becas Fondo Cesantía Solidario | https://www.chileatiende.gob.cl/fichas/20814-programa-becas-fondo-cesantia-solidario | Automated retrieval returned an internal error. | Recheck in a normal browser and during final document QA. Retain the existing closed-status wording unless the official page confirms a new call. |

## QA conclusions

- Official-domain validation for successful pages: **PASS**
- Loan versus grant classification: **PASS**
- Eligibility and non-guarantee wording: **PASS**
- Time-sensitive application wording: **PASS**
- Inconclusive results incorrectly labeled broken: **PASS — none**
- Independent certification or accreditation claim check: **PASS — none**

## Remaining link gate

The final Guide 00 link gate still requires:

1. Browser-based verification of Red Seal and ChileAtiende links.
2. Recheck of CareerOneStop, Canada Job Bank, and Colombia Servicio Público de Empleo, which were inconclusive in Batch 01.
3. Validation of links after DOCX generation.
4. Validation of clickable hyperlinks after searchable-PDF generation.
5. Recording of redirects, login barriers, and region-specific access behavior in the publication QA manifest.

Guide 00 remains in controlled revision and is not yet a publication candidate.
