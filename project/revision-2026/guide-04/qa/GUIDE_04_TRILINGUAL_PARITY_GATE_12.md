# Guide 04 — Trilingual Parity Gate 12

Date: 2026-08-08  
Branch: `revision/guide-00-100-2026`  
Guide: 04 — Project Coordinator

Controlled inputs:

- English: `working/GUIDE_04_ENGLISH_WORKING_MASTER_06.md`
- English freeze QA: `GUIDE_04_ENGLISH_MASTER_QA_07.md`
- ES-419: `working/GUIDE_04_ES_419_WORKING_MASTER_08.md`
- ES-419 translation QA: `GUIDE_04_ES_419_TRANSLATION_QA_09.md`
- PT-BR: `working/GUIDE_04_PT_BR_WORKING_MASTER_10.md`
- PT-BR translation QA: `GUIDE_04_PT_BR_TRANSLATION_QA_11.md`

## Purpose

Verify that the three controlled Markdown masters preserve the same substantive guide, source distinctions, numerical claims, risk controls, and publication limitations before any DOCX/PDF publication-candidate build. This is internal source-parity QA, not independent human translation certification, accreditation, accessibility certification, legal review, or publication approval.

## Structural parity

**PASS.** All three editions preserve the same substantive progression:

1. guide use and decision rules;
2. role definition and title variability;
3. duties, tools, and work cycles;
4. career fit and sustainability;
5. ethics, boundaries, and escalation;
6. income, benefits, and outlook;
7. education, credentials, and free-first learning;
8. funding, scholarships, employer support, and apprenticeships/work-based learning;
9. Canada pathways;
10. Colombia pathways;
11. broader Latin America and portability;
12. accessibility and inclusion;
13. privacy, cybersecurity, records, and ethical AI;
14. evidence/portfolio development;
15. interview preparation;
16. first 30/60/90 days;
17. advancement, portability, and exit planning;
18. pre-enrollment/payment/signature verification;
19. twelve-week action plan;
20. worksheets; and
21. source/maintenance controls.

Headings are naturally translated rather than forced into word-for-word wording, but no substantive guide section is intentionally absent from ES-419 or PT-BR.

## Income and numeric parity

**PASS.** The editions preserve the same source identities and caveats:

- official U.S. occupational anchor/proxy: BLS `Project Management Specialists (SOC 13-1082)`, **US$100,750 / US$100.750 median annual wage in May 2024**, **6% employment growth from 2024 to 2034**, and about **78,200 / 78.200 average annual openings**;
- exact-title U.S. market estimate: ZipRecruiter `Project Coordinator`, **US$59,915 / US$59.915 per year** and **US$28.81 / US$28,81 per hour**, displayed `As of Jul 20, 2026` and checked August 8, 2026;
- SENA examples: **4,656 / 4.656 hours**, **48 hours**, **48 hours**; and
- February 2026 SENA statement of more than **41,000 / 41.000 free places**, with intake/admission variability retained.

Punctuation follows language convention; the underlying values do not change. None of the three editions presents the broader BLS occupation as an exact Project Coordinator wage, the ZipRecruiter estimate as government data, or U.S./Canadian figures as Colombian/Latin American salary promises.

## Funding and apprenticeship parity

**PASS.** The three editions retain the same controls for:

- American Job Centers and WIOA eligibility/program dependence;
- FAFSA and federal student-aid program participation cautions;
- scholarships/grants as non-guaranteed;
- employer tuition/reimbursement as employer-specific;
- written verification of service/repayment terms before enrollment;
- no universal service-period duration;
- Registered Apprenticeship as the specific U.S. registered model rather than a synonym for any internship or training; and
- verification of current apprenticeship availability rather than implying a generic Project Coordinator apprenticeship exists everywhere.

## Canada, Colombia, and Latin America parity

**PASS.** The three editions:

- require Canadian duty/location/NOC matching before using wage data;
- avoid treating `Project Coordinator` as one standardized Canadian occupation;
- identify SENA and Servicio Público de Empleo as Colombia public-first pathways;
- keep Colombia contract/pay-period/benefit context separate from U.S./Canadian conventions; and
- instruct readers elsewhere in Latin America to begin with official labor/employment/training systems and then compare current local vacancies.

## Credential and regulated-work parity

**PASS.** The editions do not create a universal Project Coordinator license or mandatory degree. CAPM, PMP, Scrum, Agile, and software/tool certificates remain optional or employer-dependent unless a specific vacancy, regulator, sponsor, or progression path says otherwise. The sector-specific warning remains: coordination does not authorize regulated engineering, clinical, legal, financial, safety, procurement, or other professional work.

## Accessibility parity

**PASS at Markdown/source level.** The editions retain:

- full-path accessibility review, not admission-only review;
- assistive technology, screen-reader compatibility, captions/transcripts, alternate communication, ergonomic support, schedule flexibility where viable, testing accommodations where applicable, transport/site/emergency accessibility, and written accommodation records;
- accessible-document practices such as descriptive links, meaningful headings, readable tables, and avoiding color-only communication; and
- explicit avoidance of any claim that accessibility has been independently certified.

Rendered DOCX/PDF accessibility remains a later gate.

## Privacy, cybersecurity, records, and ethical-AI parity

**PASS.** All three preserve approved-account/device/repository requirements, multifactor authentication, least privilege/role-based access, restrictions on personal storage and public AI, meeting-note/recording controls, retention/legal hold, handling of confidential/regulated information, human verification of AI output, prohibition on invented project evidence, disclosure when required, and human accountability.

## Source/link parity

**PASS for controlled source inclusion.** The editions preserve the same core official/public source families and the separately labeled ZipRecruiter market source. No translation silently substitutes a different salary, credential, funding, accreditation, legal, or training authority. Automated HTTP validation must still run on the publication-candidate build because live endpoints can change independently of source parity.

## Encoding and human-readability parity

**PASS at Markdown stage.** English, ES-419, and PT-BR are stored as UTF-8 repository text. Spanish and Portuguese diacritics and punctuation are preserved as Unicode. Translation QA records natural-language review rather than asserting literal machine equivalence or professional human certification.

## Controlled decision

**PASS — Guide 04 trilingual Markdown source parity is cleared.**

**HOLD — the guide is not yet a publication candidate.** The remaining controlled gate is the publication build and artifact QA: DOCX/PDF generation, OOXML/package integrity, link checks, PDF extraction/page/title checks, rendered first-page evidence, metadata, checksums, manifest, and final trilingual publication-candidate review.

## Next sequential gate

Generate the Guide 04 trilingual DOCX/PDF publication candidates from Working Masters 06, 08, and 10 using a fail-closed build. Commit artifacts only after the publication workflow passes all required QA checks.
