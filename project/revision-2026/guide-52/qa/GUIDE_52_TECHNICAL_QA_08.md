# Guide 52 — Trilingual Technical QA 08

**Guide:** 52 — Surgical Technologist  
**Branch:** `revision/guide-00-100-2026`  
**Date:** August 19, 2026  
**Stage:** Technical QA — **PASS**

## Controlled inputs

- English: `project/revision-2026/guide-52/working-masters/GUIDE_52_SURGICAL_TECHNOLOGIST_ENGLISH_v2.md`
- Spanish `es-419`: `project/revision-2026/guide-52/working-masters/GUIDE_52_SURGICAL_TECHNOLOGIST_ES419_v2.md`
- Portuguese `pt-BR`: `project/revision-2026/guide-52/working-masters/GUIDE_52_SURGICAL_TECHNOLOGIST_PTBR_v2.md`
- English source-freeze, Spanish-localization QA, and Portuguese-localization QA records.

## Structural results

| Control | English | Spanish | Portuguese | Result |
|---|---:|---:|---:|---|
| Lines | 314 | 314 | 314 | PASS |
| H2 sections | 20 | 20 | 20 | PASS |
| H3 sections | 6 | 6 | 6 | PASS |
| Bullets | 103 | 103 | 103 | PASS |
| Numbered items | 18 | 18 | 18 | PASS |
| Source URLs | 15 | 15 | 15 | PASS |
| UTF-8 replacement characters | 0 | 0 | 0 | PASS |
| Zero-width / embedded BOM characters | 0 | 0 | 0 | PASS |
| Tab characters | 0 | 0 | 0 | PASS |
| Pandoc GFM-to-HTML parse | PASS | PASS | PASS | PASS |

The URL sequence is identical in all three editions. No source URL was omitted, added, reordered, or translated.

## Controlled-value parity

PASS — all editions preserve O*NET-SOC `29-2055.00`, CST, CAAHEP, ABHES, NBSTSA, WIOA, `NOC 32101`, `CUOC 22402`, SNIES, OCUPACOL, and the named government portals.

PASS — all editions preserve the certificate-or-associate-degree description, supervised laboratory and clinical education, and the warning that online-only demonstrations cannot replace required hands-on clinical training.

PASS — U.S. official values remain `USD $62,830` median annual pay, `$43,290` lower-decile boundary, `$90,700` upper-decile boundary, `115,600` jobs in 2024, `120,800` projected jobs in 2034, and `4%` growth.

PASS — the non-government Salary.com estimate remains approximately `USD $62,143` annually and `$30` hourly, with the stated `$55,721–$68,991` 25th–75th percentile range and August 1, 2026 reference date, visibly separated from official data.

PASS — Canadian national values remain `CAD $25.00` low, `CAD $31.32` median, and `CAD $38.00` high, with the November 19, 2025 update date and the explicit limitation to Operating Room Technician as mapped to Licensed practical nurses (`NOC 32101`).

PASS — Colombia retains the professional Instrumentación Quirúrgica distinction, `CUOC 22402`, competence level 4, SNIES verification, and the warning against assuming equivalence with a short U.S. pathway.

## Link review

All 15 unique source URLs were requested through browser retrieval on August 19, 2026.

- Eleven resolved to the intended official, recognized credential/accreditation, or named non-government source: O*NET, BLS, Apprenticeship.gov, both CAAHEP resources, NBSTSA, the Job Bank occupation summary, OCUPACOL, SNIES, OIT/Cinterfor, and Salary.com.
- The two CareerOneStop URLs returned retrieval-tool internal errors. They are official U.S. Department of Labor-sponsored locators already verified in the controlled research stage; the error does not identify a malformed URL or an unrelated destination.
- The Job Bank requirements and wage routes returned retrieval-tool internal errors while the corresponding Operating Room Technician summary resolved on the same official domain. The values and occupation mapping were verified in the controlled research stage.
- SNIES redirected from HTTPS to its official portal endpoint. No domain mismatch or unrelated destination was observed.

No confirmed 404/410, unrelated redirect, or domain mismatch was found. Transient access and retrieval behavior is documented rather than mislabeled as content failure.

## Safety and prohibited-content checks

PASS — no edition introduces an unsupervised procedure, device-specific instruction, medication direction, exposure parameter, sterile-processing cycle, or independent clinical decision.

PASS — all editions preserve authorized supervision, employer procedures, demonstrated competency, sterile-field protection, count escalation, specimen controls, exposure reporting, privacy, and cybersecurity boundaries.

PASS — no edition claims that CST is a universal national license, that every employer accepts the same credential, or that CAAHEP, ABHES, and NBSTSA are interchangeable bodies.

PASS — no edition presents U.S., Canadian, or Colombian titles as one-to-one equivalents; a U.S. credential is not represented as automatic authority to work in Canada or Colombia.

PASS — no edition presents national wage data as guaranteed starting pay, a program locator as funding approval, Registered Apprenticeship as universally available, or credential recognition as automatic.

PASS — protected patient, operative, credential, access, incident, proprietary, and employer-confidential information remains prohibited from unapproved public AI services.

## Accessibility and formatting checks

PASS — heading hierarchy is sequential and consistent.

PASS — paragraphs are concise, lists use native Markdown, source links expose their authoritative URLs, and information is not encoded only by color or images.

PASS — acronyms and credential names are explained in context, while searchable official names remain intact.

PASS — punctuation and language usage are appropriate to English, neutral Latin American Spanish, and Brazilian Portuguese without changing controlled values.

Publication rendering, DOCX accessibility checks, PDF searchability and tagging, page-level visual inspection, metadata, and final checksums remain duties of the Publication and Release Audit stages.

## Assurance boundary

This QA is an internal, AI-assisted technical review. It does not claim independent human certification, clinical review, legal review, professional translation certification, accreditation, accessibility certification, or approval for healthcare practice.

## Decision

**PASS.** The trilingual Markdown masters satisfy the controlled technical gate and may proceed to publication artifact generation.
