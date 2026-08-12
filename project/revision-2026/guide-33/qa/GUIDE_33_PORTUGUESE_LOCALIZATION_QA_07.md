# Guide 33 — Brazilian Portuguese Localization QA 07

**Guide:** 33 — Machinist and CNC Machine Operator  
**Target locale:** Portuguese (Brazil), `pt-BR`  
**Controlled source:** `project/revision-2026/guide-33/publication-candidate/GUIDE_33_ENGLISH_v2.md`  
**Frozen English blob:** `62054bb81fcd0e76629623e285ec2d2a9eab84f9`  
**Candidate:** `project/revision-2026/guide-33/publication-candidate/GUIDE_33_PORTUGUESE_v2.md`  
**QA date:** 11 August 2026

## Result

**PASS** — the Brazilian Portuguese candidate preserves the controlled English guide's 22-section structure, safety boundaries, jurisdictional distinctions, numerical evidence, credential caveats, funding/apprenticeship controls, AI/privacy/cybersecurity cautions, accessibility framing, and source links without adding unsupported guarantees or certification claims.

## Controlled checks

| Control | Result | Evidence / note |
|---|---|---|
| 22 numbered sections present and in source order | PASS | Sections 1–22 preserved. |
| Purpose and educational/non-guarantee disclaimer preserved | PASS | Employment, wages, admission, funding, reimbursement, apprenticeship, certification, licensing, promotion, and authority limitations retained. |
| Occupational title distinctions preserved | PASS | CNC operator, setup technician, machinist, and CNC/CAM programmer scopes remain distinct. |
| Machine safety boundaries preserved | PASS | Guarding, interlocks, rotating equipment, chips, metalworking fluids, lockout/tagout, stop-and-escalate conditions retained. |
| U.S. official wage figures preserved | PASS | US$56,150 median; US$38,100 lower 10%; US$78,760 upper 10%; 0% projected machinist change; 34,200 combined annual openings. |
| Non-government wage estimate labeled separately | PASS | Indeed estimate remains explicitly non-government; US$28.06/hour and US$20.44–US$38.53 range retained with 20 July 2026 date. |
| U.S. training/funding boundaries preserved | PASS | Apprenticeship.gov status distinction, WIOA eligibility/approval limits, CareerOneStop scholarships, public-college and employer-support routes retained. |
| NIMS credential boundaries preserved | PASS | Industry credential vs. government license distinction retained; 30 June 2026 five-year validity rule preserved without retroactive overclaim. |
| Canada pathway preserved | PASS | Red Seal Machinist/NOC 72100, 4 technical levels, 7,200 hours, Job Bank C$21.00/C$30.00/C$41.50, and Canada Apprentice Loan up to C$4,000 retained. |
| Closed Canada grant warning preserved | PASS | No implication that the former Apprenticeship Incentive/Completion Grants remain open for post-31 March 2025 progression/completion dates. |
| Colombia/SENA pathway preserved | PASS | SENA machining/CNC training and APE free employment service retained with cohort/vacancy freshness caveats. |
| Latin America jurisdiction caveat preserved | PASS | No regional licensing/apprenticeship/wage system is implied; country-by-country verification remains explicit. |
| Skills, 90-day plan, training-program due diligence and portfolio controls preserved | PASS | No unsupported scope or credential inflation introduced. |
| Responsible AI controls preserved | PASS | G-code, toolpaths, feeds/speeds, workholding, offsets, dimensional interpretation, safety, recovery and inspection decisions remain high-risk/unverified uses. |
| Privacy/cybersecurity boundaries preserved | PASS | Proprietary drawings, CAD/CAM, programs, customer/export/defense/medical/aerospace data, credentials and network information remain protected. |
| Accessibility and realistic job-fit framing preserved | PASS | No self-exclusion instruction; essential functions, accommodations and adjacent roles retained without promising accommodation outcomes. |
| Remote-work caution preserved | PASS | Hands-on machining remains described as primarily site-based; remote/hybrid exceptions remain employer-dependent. |
| Source URLs preserved | PASS | BLS, O*NET, Apprenticeship.gov, DOL/WIOA, OSHA, NIMS, Red Seal, Canada Job Bank, Canada Apprentice Loan, SENA/APE and Indeed URLs retained. |
| Encoding / natural pt-BR readability | PASS | UTF-8 text; Brazilian Portuguese wording and punctuation reviewed for natural readability; unavoidable U.S./Canadian institutional names kept in their official forms. |
| Independent-certification claims | PASS | No claim of independent human translation certification, accreditation, legal review, or accessibility certification introduced. |

## Terminology decisions

- `machinist` is rendered contextually as **profissional de usinagem** rather than forcing a single Brazilian regulated title where equivalence may vary.
- `machine operator` / `CNC operator` is rendered as **operador de máquina / operador CNC**.
- `setup` and technical CNC/CAM terms are retained where they are normal workplace terminology in Brazilian manufacturing, with surrounding Portuguese explanation.
- `journeyperson` is not presented as a Brazilian credential; references remain tied to foreign credential-scope cautions.
- `lockout/tagout` is described as **bloqueio e etiquetagem (lockout/tagout)** rather than implying a direct Brazilian regulatory equivalence.

## Gate decision

Portuguese Localization Helper: **PASS**.

This PASS authorizes progression to the Guide 33 Technical QA stage only. It does not certify DOCX/PDF generation, links, metadata, rendering, checksums, or final publication artifacts; those remain fail-closed under subsequent gates.