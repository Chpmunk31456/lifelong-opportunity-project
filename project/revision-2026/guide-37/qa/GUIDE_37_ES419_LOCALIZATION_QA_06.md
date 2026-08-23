# Guide 37 — Spanish Localization QA — Gate 06

**Guide:** 37 — Shipping, Receiving, and Traffic Clerk  
**Locale:** es-419  
**Branch:** `revision/guide-00-100-2026`  
**QA date:** 2026-08-12  
**Result:** PASS

## Files reviewed

- English source freeze: `project/revision-2026/guide-37/working-masters/GUIDE_37_SHIPPING_RECEIVING_AND_TRAFFIC_CLERK_ENGLISH_v2.md`
- Spanish controlled master: `project/revision-2026/guide-37/working-masters/GUIDE_37_SHIPPING_RECEIVING_AND_TRAFFIC_CLERK_ES419_v2.md`
- Current-source evidence: `project/revision-2026/guide-37/research/GUIDE_37_CURRENT_SOURCE_EVIDENCE_02.md`

## Localization controls

- Neutral Latin American Spanish maintained; Colombia-specific terminology is limited to the Colombia pathway and clearly contextualized.
- Occupation scope, physical-demand cautions, powered-equipment authorization, dangerous-goods/customs caveats, and employer-specific requirements were preserved without expanding legal claims.
- Official U.S. O*NET/BLS wage and outlook figures were preserved numerically and labeled as official national occupational statistics.
- Indeed and Salary.com figures remain visibly separated as non-government estimates and are not presented as guaranteed wages.
- Canada NOC 14400 requirements and CAD wage figures were preserved with their official-source status.
- SENA, Sistema Nacional de Cualificaciones, OCUPACOL, and OIT/Cinterfor pathways remain framed as current locators/pathways rather than mandatory credentials.
- WIOA and Canada Student Grants and Loans language preserves eligibility and non-guarantee controls.
- Apprenticeship language distinguishes U.S. Registered Apprenticeship from broader international work-based learning.
- AI/privacy/cybersecurity controls preserve the prohibition on unauthorized disclosure of shipment, customer, supplier, credential, customs, inventory, and security information.
- No independent human certification, certified translation, accreditation, legal review, accessibility certification, financial advice, or guaranteed employment claim was introduced.

## Structural and language QA

- Major section sequence matches the controlled English source.
- Lists, numbered steps, wage figures, dates, program names, occupation codes, acronyms, and URLs are retained in auditable form.
- Decimal and thousands separators were localized for Spanish prose without changing numeric meaning.
- UTF-8 diacritics and punctuation render correctly in the Markdown source.
- Terminology is natural for a broad Latin American audience; employer-specific English system acronyms such as ERP, WMS and EDI remain unchanged where appropriate.
- Readability was checked for direct, plain-language instructions and avoidance of literal machine-translation phrasing.

## Gate decision

**Spanish Localization Helper: PASS.** The es-419 Version 2 controlled master is complete and suitable to advance to Brazilian Portuguese localization. Publication-format, trilingual parity, live-link, DOCX/PDF, rendering, metadata, checksum, and final release controls remain downstream gates and are not implied by this PASS.
