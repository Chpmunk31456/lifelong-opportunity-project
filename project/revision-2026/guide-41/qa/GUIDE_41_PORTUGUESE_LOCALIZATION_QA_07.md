# Guide 41 — Portuguese Localization QA

**Edition:** Brazilian Portuguese (`pt-BR`)  
**QA date:** August 14, 2026  
**Controlled source:** `GUIDE_41_CARPENTER_AND_CABINETMAKING_TECHNICIAN_ENGLISH_v2.md`  
**Localized master:** `GUIDE_41_CARPENTER_AND_CABINETMAKING_TECHNICIAN_PTBR_v2.md`

## Gate objective

Verify that the Brazilian Portuguese localization preserves the frozen English source's occupational scope, numeric facts, source URLs, safety boundaries, funding/apprenticeship distinctions, regional coverage, AI/privacy controls, and assurance limitations while reading naturally in Brazilian Portuguese.

## Structural parity

PASS.

The localized master preserves the complete controlled sequence and substantive coverage of the English v2 source, including:

- occupation scope and distinction between construction carpentry and cabinetmaking/bench carpentry;
- duties, work environment, physical demands, and skills;
- United States, Canada, Colombia, and Latin America/Caribbean pathways;
- free-first/low-cost learning strategy;
- apprenticeship and work-based learning;
- funding and employer support;
- official and non-government income evidence;
- 12-week starter plan;
- transferable experience and advancement;
- responsible AI use, cybersecurity/privacy, scam controls, and pause-before-spending guidance;
- current-source inventory and source/review disclaimer.

No source section was intentionally omitted.

## Numeric and classification parity

PASS.

Verified preserved facts include:

- O*NET occupation `47-2031.00`;
- Canada `NOC 72310`;
- Canada apprenticeship/certification pathway of three to four years or more than four years of experience plus relevant courses;
- SENA `Básico de carpintería y ebanistería`, 60-hour in-person complementary program;
- Canada Apprentice Loan: up to CAD $4,000 per eligible technical-training period;
- U.S. official median: $29.12/hour and $60,580/year;
- approximately 959,000 U.S. workers in 2024;
- projected U.S. growth of 5% to 6% for 2024–2034;
- approximately 74,100 annual openings;
- Salary.com adjacent-title estimates: $41,709/year / $20/hour with $34,226–$51,809 25th–75th percentile range, and $60,290/year / $29/hour with $54,219–$66,817 range;
- Canada Job Bank wage points: CAD $22.00 low, $32.12 median, $44.23 high per hour, updated November 19, 2025;
- all 12-week plan intervals.

Portuguese number formatting changes punctuation for readability where appropriate but does not change value.

## Certification, apprenticeship, and funding parity

PASS.

The localization preserves that:

- Registered Apprenticeship is paid and employer-driven in the United States but availability is not guaranteed;
- Carpenter trade certification is compulsory in Quebec and available but voluntary elsewhere in Canada;
- qualified carpenters may pursue Red Seal endorsement through the interprovincial examination process;
- cabinetmaking can be a separate trade pathway;
- legacy Canadian Apprenticeship Incentive Grant and Apprenticeship Completion Grant programs are closed to new applications;
- the federal Apprenticeship Service is described as not accepting applications while renewal work proceeds, rather than as an active guaranteed subsidy;
- WIOA and other public supports are presented as eligibility-dependent locators, not guaranteed funding;
- reimbursement/retention terms should be obtained in writing before spending money.

## Regional and training parity

PASS.

The localized master retains:

- U.S. O*NET, Apprenticeship.gov, WIOA/American Job Center pathways;
- Canada Job Bank, skilled-trades, apprenticeship, EI/loan/support distinctions;
- Colombia SENA/Betowa pathway and Ministry of Labour qualification/occupation-system direction;
- OIT/Cinterfor regional locator and examples of SENA, SENCE, INTECAP, INFOTEP, and INEFOP.

## Safety parity

PASS.

The Portuguese edition retains explicit controls for machine guarding, PPE/EPI, respiratory and hearing protection, fall protection, lockout/tagout, chemical handling, ventilation, dust collection, housekeeping, equipment training, and prohibition on bypassing guards/interlocks or improvising hazardous procedures.

The guide does not provide unsafe machine-operating instructions or encourage unsupervised hazardous-equipment practice.

## AI, cybersecurity, and privacy parity

PASS.

The localization preserves the boundary that AI may support general study or non-sensitive planning but must not replace approved drawings, structural calculations, engineering specifications, safety procedures, machine instructions, measurements, code requirements, or employer quality controls. Proprietary drawings, customer/supplier data, credentials, bids, schedules, access details, and protected project information are explicitly excluded from unauthorized public-AI use.

Cybersecurity guidance retains MFA, credential protection, phishing, approved file-sharing, customer information, proprietary drawings/files, removable media, incident reporting, personal-device controls, and verification of unusual payment/bank-account/file instructions.

## Source URL parity

PASS.

The pt-BR master retains the current source URLs from the controlled research/source set:

- https://www.onetonline.org/link/summary/47-2031.00
- https://www.jobbank.gc.ca/wagereport/occupation/6388
- https://www.jobbank.gc.ca/marketreport/requirements/6408/ca
- https://www.canada.ca/en/services/jobs/training/support-skilled-trades-apprentices.html
- https://www.canada.ca/en/services/jobs/training/support-skilled-trades-apprentices/grants.html
- https://www.canada.ca/en/services/jobs/training/support-skilled-trades-apprentices/funding-opportunities.html
- https://www.canada.ca/en/employment-social-development/programs/apprentice-service-program.html
- https://betowa.sena.edu.co/oferta/basico-de-carpinteria-y-ebanisteria?offertype=company&programId=12174
- https://www.apprenticeship.gov/
- https://www.oitcinterfor.org/
- https://www.salary.com/research/salary/benchmark/cabinetmaker-and-bench-carpenter-salary
- https://www.salary.com/research/salary/listing/cabinet-maker-salary

Official/public sources remain separated from supplementary non-government salary sources.

## Language, accessibility, and encoding review

PASS.

The edition uses natural Brazilian Portuguese rather than literal word-for-word English syntax. Headings, lists, short paragraphs, explicit cautions, and plain-language sequencing remain accessible. UTF-8 Portuguese characters and accents are used intentionally. No unsupported claim of certified translation or independent human translation review is made.

## Assurance boundary

PASS.

The final note states that the controlled revision used AI assistance and auditable source review and does **not** claim independent human certification, professional accreditation, certified translation, legal review, financial advice, or guaranteed employment.

## Gate decision

**PASS — Portuguese Localization (`pt-BR`).**

The pt-BR Version 2 master is suitable to advance to Trilingual Technical QA. This PASS is limited to localization quality/parity; DOCX/PDF generation, rendering, metadata, checksum, and publication validation remain later controlled gates.
