# Guide 16 — English v2 Editorial and Accessibility QA

**Guide:** 16 — Loan Processing Specialist and Loan Clerk  
**Branch:** `revision/guide-00-100-2026`  
**QA date:** 2026-08-09  
**Artifact reviewed:** `references/english-v2-working-master.md`  
**Gate:** Editorial, readability, accessibility, structural, and high-risk factual spot-check QA  
**Disposition:** **PASS**

## Scope of this PASS

This record closes the English v2 editorial/accessibility gate for the working master. It does **not** close the separate claim-to-source traceability, exhaustive link/freshness, translation/localization, DOCX, PDF, metadata, publication, or release-audit gates. It does not claim independent human certification, professional linguistic certification, accreditation, legal review, or regulator endorsement.

## Editorial review

The working master was reviewed for:

- spelling, punctuation, grammar, and sentence clarity;
- natural human readability and removal of unnecessary jargon;
- descriptive headings and consistent hierarchy;
- manageable paragraph and list length;
- plain-language explanations of mortgage licensing boundaries;
- consistent treatment of role titles and jurisdiction-specific terminology;
- explicit separation of official wage statistics from private estimates;
- non-guarantee language for employment, income, funding, admission, apprenticeships, licensing, certification, and promotion;
- clear distinction between a working master and a publication edition; and
- consistent author/AI-assistance disclosure.

No blocking editorial defect was identified in this gate.

## Accessibility and inclusion review

The working master uses:

- a single H1 followed by logical H2/H3 structure;
- descriptive link text rather than bare “click here” wording;
- short, scannable paragraphs and lists;
- plain-language definitions before or alongside specialized concepts;
- text-only presentation that does not depend on color or images;
- Unicode/UTF-8 text without an intentional BOM;
- wording intended to remain usable for career changers, older learners, neurodivergent readers, readers with disabilities, and assistive-technology users; and
- explicit discussion of reasonable accommodations and sustainable work practices without making medical or legal determinations.

No accessibility barrier requiring a content rewrite was identified at this stage. Final DOCX/PDF accessibility remains a separate gate because generated-document styles, tags, reading order, links, pagination, and rendering cannot be certified from Markdown alone.

## High-risk factual spot checks completed

The following claims were rechecked against current authoritative/public sources during this QA pass:

1. **O*NET-SOC 43-4131.00 — Loan Interviewers and Clerks** remains the relevant U.S. occupational mapping and is marked updated 2026. O*NET lists titles including Loan Clerk, Loan Processor, Mortgage Loan Processor, and Mortgage Processor.
2. **CFPB Regulation H / SAFE Act boundary:** current CFPB § 1008.103 and Appendix C support the guide’s controlled statement that licensing depends on activities and circumstances; Appendix C specifically distinguishes covered independent-contractor processing/underwriting activity from examples of employees performing only qualifying clerical/support duties under appropriate supervision.
3. **BLS May 2025 OEWS:** Loan Interviewers and Clerks — employment 164,790; mean hourly $25.25; mean annual $52,520; median hourly $24.05.
4. **Canada Job Bank:** Loan clerk - financial sector maps to NOC 14201, lists a national median wage of C$25.33/hour, and describes the broad occupation as usually requiring secondary school or several weeks of on-the-job training. The wage table states November 19, 2025 as its update date and 2023–2024 as the national reference period.
5. **2026–27 FAFSA:** Federal Student Aid confirms the FAFSA is free and gives access, subject to eligibility, to federal grants, work-study, and federal student loans for college, career school, or trade school.
6. **IRS Section 127:** IR-2026-55 and the April 2026 FAQ confirm a $5,250 gross-income exclusion limit for qualifying educational-assistance benefits for calendar years 2025 and 2026, with the rule subject to the qualifying employer plan and statutory conditions.
7. **Registered Apprenticeship:** Apprenticeship.gov confirms paid work experience, mentoring, progressive wage increases, related/classroom instruction, and a portable nationally recognized credential; the guide correctly avoids claiming that a loan-processing apprenticeship is available in every location.

These checks support the editorial gate but do not substitute for the forthcoming line-by-line claim-to-source traceability and exhaustive link/freshness gate.

## Controlled-risk findings

- The private ZipRecruiter figure remains deliberately labeled **non-government** and title-specific. Its methodology and scope are not treated as equivalent to BLS.
- Colombia SENA programs are deliberately described as **adjacent financial-services pathways**, not as a dedicated national loan-processor credential.
- The guide does not convert U.S. or Canadian wage figures into a Latin American salary claim.
- The mortgage licensing section uses verification language and does not attempt individualized legal advice.
- AI guidance prohibits confidential borrower data in public/unapproved AI systems and rejects AI-only consequential credit/compliance decisions.

## Gate result

**PASS — English v2 editorial/accessibility working-master gate.**

### Next controlled gate

Run full claim-to-source traceability against `guide-16-v2-current-source-ledger.md`, followed by exhaustive link/freshness, encoding, terminology, and structural QA. Only after those gates pass should the English v2 source be frozen for neutral Latin American Spanish (`es-419`) and Brazilian Portuguese (`pt-BR`) localization.
