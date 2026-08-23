# Guide 37 — Portuguese Localization QA — Gate 07

**Guide:** 37 — Shipping, Receiving, and Traffic Clerk  
**Locale:** pt-BR  
**Branch:** `revision/guide-00-100-2026`  
**QA date:** 2026-08-12  
**Result:** PASS

## Files reviewed

- English source freeze: `project/revision-2026/guide-37/working-masters/GUIDE_37_SHIPPING_RECEIVING_AND_TRAFFIC_CLERK_ENGLISH_v2.md`
- Portuguese controlled master: `project/revision-2026/guide-37/working-masters/GUIDE_37_SHIPPING_RECEIVING_AND_TRAFFIC_CLERK_PTBR_v2.md`
- Current-source evidence: `project/revision-2026/guide-37/research/GUIDE_37_CURRENT_SOURCE_EVIDENCE_02.md`

## Localization controls

- Brazilian Portuguese usage is natural and avoids European-Portuguese administrative phrasing.
- Occupation scope, physical-demand cautions, equipment-authorization language, dangerous-goods/customs controls, and employer-specific requirements were preserved.
- Official U.S. O*NET/BLS wage and outlook figures were preserved numerically and remain identified as official national occupational statistics.
- Indeed and Salary.com figures remain explicitly non-government estimates, separate from official data and without guaranteed-income language.
- Canada NOC 14400 requirements and CAD wage figures were preserved with official-source status.
- Colombia SENA, Sistema Nacional de Cualificaciones, OCUPACOL, and OIT/Cinterfor references remain contextualized as pathways/locators rather than mandatory credentials.
- WIOA and Canada Student Grants and Loans language preserves eligibility and non-guarantee controls.
- U.S. Registered Apprenticeship terminology is not generalized internationally; broader work-based learning language is used outside the United States.
- AI, cybersecurity, privacy, customer/supplier, shipment, customs, credential, inventory, and security-data controls were preserved.
- No claim of independent human certification, professional accreditation, certified translation, legal review, accessibility certification, financial advice, or guaranteed employment was introduced.

## Structural and language QA

- Major section sequence follows the controlled English source and es-419 companion edition.
- Lists, numbered steps, occupation codes, wage figures, dates, acronyms, program names, and URLs remain auditable.
- Decimal and thousands separators are localized for Brazilian Portuguese without changing numeric meaning.
- UTF-8 diacritics and punctuation render correctly in Markdown.
- ERP, WMS, EDI and other commonly used system acronyms are retained where appropriate.
- Plain-language readability was checked to avoid literal translation and unnecessary jargon.

## Gate decision

**Portuguese Localization Helper: PASS.** The pt-BR Version 2 controlled master is complete. Guide 37 may advance to trilingual Technical QA. This PASS does not imply DOCX/PDF, live-link, rendering, metadata, checksum, publication, or release-audit completion; those controls remain downstream.
