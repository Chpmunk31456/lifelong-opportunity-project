# Guide 100 — Baseline Inventory

## Occupation
Clinical Laboratory Technician

## Controlled branch
`revision/guide-00-100-2026`

## Sequential-entry prerequisite
Guide 99 — Food Science Technician is recorded on the live controlled branch as **PASS through Publication and Release Audit**, with no blockers, so Guide 100 may enter controlled revision.

## Legacy publication baseline
The legacy published collection contains Guide 100 at `100-clinical-laboratory-technician/` with English, neutral Latin American Spanish, and Brazilian Portuguese publication directories and DOCX/PDF structure.

Verified live controlled-branch records on 2026-08-22:

- Legacy package tree: `100-clinical-laboratory-technician/` — tree `a2a24b6ee4989b87ff4395acc1e17fbe9b9090bd`
- Root README: `100-clinical-laboratory-technician/README.md` — blob `4bd876bc3f85cce639bd48462b557ed70d381f28`
- English README: `100-clinical-laboratory-technician/english/README.md` — blob `c889c24bb1e5c72b7932b83e8f1f8dcb4a7653e9`
- English legacy QA: `100-clinical-laboratory-technician/english/QC.md` — blob `1131ea00c7b0058d7774ac09a5c802689947c047`
- Spanish README: `100-clinical-laboratory-technician/spanish/README.md` — blob `40975fadf8e72d6418019b6f2b9234ae5bcc8a2c`
- Portuguese README: `100-clinical-laboratory-technician/portuguese/README.md` — blob `5e29bfff99800695cbb4563e9fc5a2bba34b3e86`
- English, Spanish, and Portuguese DOCX/PDF directories are present.

## Baseline defects and limitations

1. The root, Spanish, and Portuguese README files carry a leading UTF-8 BOM in their current text representation; controlled publication must normalize encoding.
2. Legacy Spanish and Portuguese download filenames visibly lost accented characters, for example `T_cnico`, `cl_nico`, and `Laborat_rio`. Controlled publication must use clean UTF-8 filenames and metadata.
3. The legacy English QA record reports **7 pages**, **23,571 searchable characters**, **0 TOC self entries**, and **no broken fields**, but records **`Action Plan 1 To 6: False`**. The controlled English revision must repair and explicitly verify a complete six-step action plan.
4. Spanish and Portuguese edition metadata identify Version 1.0, July 2026, and explicitly state that exact source equivalence and independent human linguistic review should not be assumed unless separately documented.
5. The legacy package does not contain a controlled Markdown source master or current-source traceability package under the 2026 controlled-revision standard.
6. Legacy files are evidence inputs only. They do not establish current factual accuracy, current licensing/certification requirements, source currency, trilingual equivalence, accessibility certification, clinical competence, or controlled-revision completion.

## Controlled-revision requirements
Guide 100 must be rebuilt under the expanded opportunity standard, including:

- current occupation scope and labour-market evidence for clinical laboratory technician / medical laboratory technician work;
- clear distinction between technician, technologist/scientist, phlebotomy, laboratory assistant, and licensed/authorized clinical roles;
- official U.S. occupation, wage, outlook, education, certification/licensure, and work-context evidence;
- current CLIA and other applicable U.S. laboratory-quality/regulatory boundaries presented as educational guidance rather than legal advice;
- official Canadian occupation, wage, requirements, certification/regulation, and training-support evidence;
- Colombia occupation, education/training, health-sector, and professional-boundary evidence where supportable from official sources;
- Latin America and Caribbean vocational-training locators where relevant;
- current non-government compensation estimates, clearly labelled as estimates and separated from official statistics;
- funding, free/low-cost training, scholarships, employer-supported learning, clinical placements, internships, apprenticeships or other work-based-learning routes without promising availability or eligibility;
- specimen identification, chain of custody, biosafety, sharps, bloodborne pathogens, chemical hazards, quality control, calibration, proficiency testing, data integrity, patient privacy, cybersecurity, and responsible-AI boundaries appropriate to the occupation;
- explicit protection against diagnosing, interpreting or releasing results outside authorized scope, changing validated methods, overriding failed quality controls, fabricating data, or using unapproved AI with patient or laboratory information;
- repair of the legacy six-step action-plan defect;
- plain-language, dysgraphia-friendly structure, natural readability, accessibility, encoding, links, and versioning controls;
- neutral Latin American Spanish and Brazilian Portuguese localization only after English source freeze;
- terminology, structural, link, DOCX, PDF, metadata, checksum, rendering, publication, and release-audit QA;
- no unsupported claim of independent human certification, certified translation, accreditation, professional licensure review, legal/regulatory review, laboratory certification, accessibility certification, guaranteed funding, employment, or income.

## Gate result
**PASS — Baseline Inventory**

No blocker identified for current-source research.
