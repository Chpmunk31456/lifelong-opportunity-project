# Guide 16 — Spanish (es-419) Localization QA 06

**Guide:** 16 — Loan Processing Specialist and Loan Clerk  
**Locale:** neutral Latin American Spanish (`es-419`)  
**Controlled review:** 2026-08-09  
**Frozen English source:** `project/revision-2026/guide-16/source/GUIDE_16_ENGLISH_WORKING_MASTER_v2.md`  
**Frozen English blob:** `d2de371f5476bc19ea16c02a3c9be7057e8ff6f7`  
**Localized master:** `project/revision-2026/guide-16/source/GUIDE_16_SPANISH_LATAM_WORKING_MASTER_v2.md`  
**Initial reviewed localized blob:** `6fd24d6a334118065631792cded2503264981fd4`  
**Gate result:** **PASS**

## Scope

This gate evaluates controlled localization parity, natural readability, terminology, factual/numerical preservation, jurisdictional boundaries, accessibility-oriented language, encoding, and publication-claim discipline. It does **not** claim independent human translation certification, professional linguistic certification, accreditation, legal review, accessibility certification, mortgage licensing review, or regulator approval.

## Structural parity

**PASS.**

The es-419 master preserves the frozen English source's introductory controls and all **19 numbered substantive sections** in the same controlled sequence. The localization retains occupation mapping, workflow, compatibility/accessibility, licensing boundaries, U.S. official income/outlook evidence, separate private-market evidence, Canada, Colombia, broader Latin America, free-first learning, funding/employer support/apprenticeship, borrower communication, privacy/cybersecurity/responsible AI, capability evidence, job-search preparation, 30/60/90-day measures, advancement, the 12-week plan, pause points, current sources, and the publication rule.

## Occupational and licensing-boundary parity

**PASS.**

The localization preserves **O*NET/SOC 43-4131.00 — Loan Interviewers and Clerks** as the U.S. occupational reference and keeps the distinction between administrative loan-processing/support work and separately regulated or delegated functions. It preserves the CFPB Regulation H controls concerning residential-mortgage clerical/support duties, actual direction/supervision, independent-contractor implications, and activities involving application-taking, rate/term negotiation or counseling.

The Spanish text does not imply that a job title, course or optional credential automatically grants mortgage-loan-originator authority, underwriting authority, credit-approval authority, appraisal authority, closing authority or another regulated power.

## Numerical and income parity

**PASS.**

The es-419 master preserves the controlled figures and their source distinctions:

- BLS 2024 employment: **177,600**;
- BLS projected 2034 employment: **173,500**;
- BLS projected change: **-4,100 / -2.3%**;
- BLS projected annual openings: **13,300**;
- BLS 2024 median annual wage: **US$48,950**;
- BLS typical entry education, related-experience and short-term on-the-job-training statements;
- separate ZipRecruiter estimate dated **July 19, 2026**: **US$44,308/year**, approximately **US$21.30/hour**, with **US$37,500 / US$50,000 / US$58,000** 25th/75th/90th-percentile figures;
- Canada Job Bank national wage figures: **C$18.46 / C$25.33 / C$36.62 per hour** and **88.4%** receiving at least one non-wage benefit;
- SENA published program duration: **2,208 hours**;
- IRS Section 127 educational-assistance ceiling for 2025 and 2026: up to **US$5,250**; and
- the **12-week** action plan plus **30/60/90-day** onboarding framework.

Government and nongovernment evidence remain clearly separated. No wage is presented as guaranteed.

## Geographic and pathway parity

**PASS.**

The localization preserves:

- United States occupational, licensing, funding, accreditation and apprenticeship sources;
- Canada Job Bank mapping to **NOC 14201 — Banking, insurance and other financial clerks**, including the caution that occupation-level regulatory guidance does not replace verification of mortgage/product/employer/provincial requirements;
- Colombia's SENA **Contabilización de Operaciones Comerciales y Financieras** pathway, correctly described as a broad financial-operations program rather than a mortgage-originator license or one-to-one loan-processing credential; and
- broader Latin America guidance to verify country-specific credit/mortgage regulation and prioritize public or recognized learning and employment systems before paying for private credentials.

## Funding, free-first learning, employer support and apprenticeship parity

**PASS.**

The es-419 edition retains Federal Student Aid, state/local workforce training, Registered Apprenticeship, IRS Section 127 employer educational assistance, U.S. accreditation verification, free-first portfolio practice, and cautions about eligibility, availability, repayment terms and private training costs. It does not promise funding or apprenticeship availability.

## Accessibility, privacy, cybersecurity, fraud-awareness and AI parity

**PASS.**

The localization preserves accessibility-oriented accommodations and communication guidance, scope-aware borrower communication, protected-characteristic/fair-treatment safeguards, confidential-data handling, identity and document-integrity risks, phishing/business-email-compromise risks, secure escalation, and the rule not to place borrower data in an unapproved AI system.

It preserves the requirement that authorized humans remain responsible for consequential lending decisions and communications and that AI must not independently decide approval, denial, pricing, rate, terms, eligibility, fraud, appraisal, exceptions, disclosure or closing readiness.

## Link and identifier parity

**PASS for localization parity.**

Official and supporting source URLs from the frozen English master are preserved without translating or rewriting the destination URLs. O*NET/SOC, NOC, CFPB section identifiers, dates and program names needed for traceability remain recognizable.

Source freshness remains governed by the English evidence/traceability/source-freeze gates and will be rechecked again at publication/release audit as required by the publication rule.

## Natural-language and terminology review

**PASS for controlled AI-assisted editorial review.**

The text uses neutral Latin American Spanish rather than country-specific slang; regulated U.S./Canadian labels remain in their official English form where changing them would weaken traceability. `Prestatario`, `procesamiento`, `suscripción`, `tasación`, `desembolso`, `condiciones`, `escalación`, `licenciamiento/registro` and related financial-operational terminology are used consistently and in context. Local job-title equivalents are offered as search terms rather than represented as universal legal classifications.

## Encoding and publication claims

**PASS.**

The localized master is UTF-8 text with normal Unicode Spanish punctuation/diacritics. It contains explicit controlled-status language and no claim of independent human certification, accreditation, guaranteed employment, guaranteed income, guaranteed funding, regulator endorsement or professional translation certification.

## Gate decision

**PASS — Guide 16 es-419 localization is complete for the controlled localization gate.**

Next controlled gate: Brazilian Portuguese (`pt-BR`) localization from the same frozen English blob, followed by pt-BR localization QA and deterministic trilingual parity/technical QA.
