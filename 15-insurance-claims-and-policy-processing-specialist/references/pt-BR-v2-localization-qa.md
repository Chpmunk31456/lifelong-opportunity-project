# Guide 15 — pt-BR v2 Localization QA

**Guide:** 15 — Insurance Claims and Policy Processing Specialist  
**Locale:** Brazilian Portuguese (`pt-BR`)  
**Controlled review:** August 2026  
**Source:** frozen English v2 working master, blob `d40f0181e8a7d8e756342f25bbc64f20d8e26262`  
**Localized master:** `pt-BR-v2-working-master.md`, initial reviewed blob `ef0b9be33d4ec5db281c52f740b46312f43ac398`  
**Gate result:** **PASS**

## Scope

This gate evaluates controlled localization parity. It does not claim independent human translation certification, professional linguistic certification, accreditation, accessibility certification, legal review, or regulator approval.

## Structural parity

PASS.

The pt-BR master preserves all 19 numbered substantive sections from the frozen English source, followed by source/review notes and the CC BY-NC-SA 4.0 license statement. The career definition, duties, skills, entry boundaries, geographic pathways, income evidence, funding, scholarships, work-based learning, entry plan, portfolio, accessibility, privacy/cybersecurity, responsible AI, walk-away conditions, and advancement sections remain present in the same controlled sequence.

## Occupational-boundary parity

PASS.

The localization preserves the distinction between administrative/processing work and separately regulated activities. It does not imply authority to sell insurance, underwrite risk, determine coverage, make final liability decisions, investigate fraud, or perform licensed claims-adjusting/examining work without the authorization required by the relevant jurisdiction or employer.

Brazilian Portuguese insurance terminology is rendered for readability while official U.S. and Canadian occupational titles/codes remain unchanged where those labels identify source classifications.

## Numerical and income parity

PASS.

The localized master preserves the source distinctions and values:

- U.S. BLS May 2025 national occupation estimate: approximately 214,260 workers;
- BLS national mean hourly wage: US$25.44;
- BLS national mean annual wage: US$52,920;
- BLS national median hourly wage: US$23.67;
- BLS insurance-industry figures: approximately US$23.97 median hourly / US$49,860 median annual and US$25.92 mean hourly / US$53,920 mean annual;
- separate non-government ZipRecruiter estimate dated July 21, 2026: approximately US$46,461/year (US$22.34/hour), with the stated majority range of about US$38,000–US$53,000;
- SENA technical-program duration: 2,208 hours;
- SENA technology program code: 123204;
- Colombia vacancy example: COP 3.0–3.6 million/month plus statutory benefits;
- IRS 2026 employer educational-assistance exclusion: up to US$5,250; and
- 12-week action-plan timing.

The BLS figures remain labeled official survey estimates; ZipRecruiter remains explicitly labeled non-government; and the Colombia figure remains a single-vacancy example rather than a national salary benchmark.

## Geographic and training parity

PASS.

The pt-BR edition preserves:

- United States O*NET/SOC 43-9041.00 mapping;
- Canada NOC 14201 and OaSIS 14201.02 mapping, with a warning not to treat U.S. SOC and Canadian NOC as interchangeable;
- Colombia SENA pathways and Servicio Público de Empleo resources;
- broader Latin America guidance to use the relevant regulator, public employment service, recognized training providers, work-based learning systems, and employer career pages; and
- the instruction not to convert U.S. wage data into a supposed Latin American salary benchmark.

## Funding and opportunity parity

PASS.

The localization retains free/low-cost learning, FAFSA 2026–27, WIOA/American Job Centers, employer educational assistance, scholarship cautions, Registered Apprenticeship, paid internships/trainee programs, and corresponding Canada/Latin America public systems. It preserves the requirement to verify eligibility, provider status, reimbursement terms, repayment conditions, and local availability before spending money.

## Accessibility, privacy, cybersecurity, and AI parity

PASS.

The localized master preserves:

- descriptive headings and meaningful links;
- concise language and acronym explanation;
- screen-reader, keyboard, captioning, transcript, alternative-format and accommodation considerations;
- the warning not to rely on color alone;
- authorized-account/device and approved storage/transfer controls;
- recipient verification, workstation locking, incident reporting, retention and secure-disposal expectations;
- the prohibition on placing protected information into public AI tools unless explicitly authorized with appropriate protections; and
- the requirement for authorized human review of consequential insurance decisions and factual verification of AI-assisted text.

## Link and identifier parity

PASS for localization parity.

The pt-BR master preserves the official/source URLs and identifiers from the frozen English source rather than translating or rewriting destination URLs. Current-source freshness remains governed by the English technical/source QA and source-freeze evidence; this localization gate does not substitute a new independent source audit.

## Natural-language review

PASS for controlled AI-assisted editorial review.

The text uses Brazilian Portuguese rather than European Portuguese conventions, avoids literal sentence-by-sentence calques where they would impair readability, retains necessary English official occupation labels when they are identifiers, and uses understandable insurance/administrative terminology. Where terminology can vary among Brazilian employers, the text avoids presenting a localized job-title choice as a legal classification.

## Encoding and publication claims

PASS.

The file is UTF-8 text, uses normal Unicode punctuation and diacritics, and contains no claim that the translation was independently human-certified or professionally accredited. It remains a working master pending trilingual technical QA, DOCX/PDF publication build, metadata/checksum validation, rendering review, publication QA, and release audit.

## Gate decision

**PASS — pt-BR localization parity is complete.**

Next controlled gate: trilingual technical QA across the frozen English source, es-419 master, and pt-BR master. Publication artifacts must not be treated as final until the later publication and release-audit gates pass.