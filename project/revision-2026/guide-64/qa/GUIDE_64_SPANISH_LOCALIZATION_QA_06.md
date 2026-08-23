# Guide 64 — Spanish Localization QA

**Occupation:** Community Service Program Coordinator  
**Locale:** Neutral Latin American Spanish (`es-419`)  
**Review date:** 2026-08-20  
**Gate:** Spanish Localization — PASS

## Source control

Spanish was localized directly from the frozen English Version 2 master:

`project/revision-2026/guide-64/working-masters/GUIDE_64_COMMUNITY_SERVICE_PROGRAM_COORDINATOR_ENGLISH_v2.md`

Frozen English Git content/blob identity:

`cdf86486f8f045addb0e32d9d887829f692a1e30`

No legacy Spanish file was used as source of truth.

## Parity checks

- Top-level section order and controlled meaning: PASS
- Exact controlled-source URL parity: **16/16**
- UTF-8 readability: PASS
- Replacement characters: none introduced
- U.S. occupational identifier preserved exactly: **O*NET-SOC 11-9151.00**
- Canada occupational identifier preserved exactly: **NOC 40030**
- SENA program title and duration preserved: **Gestión comunitaria del riesgo de desastres — 1,920 hours / 1.920 horas**
- SENA program title preserved: **Organización comunitaria sostenible**
- U.S. official benchmark values preserved:
  - USD $38.65/hour 2025 median
  - USD $80,390 annual 2025 median
  - approximately 219,800 workers in 2024
  - 5% to 6% projected growth, 2024–2034
  - approximately 18,600 annual openings
- U.S. non-government estimates remain explicitly identified as non-government:
  - Salary.com: USD $66,947/year, about USD $32/hour, $59,855–$75,965 reported 25th–75th percentile range, August 1, 2026
  - ZipRecruiter: USD $54,966/year, about USD $26.43/hour, July 20, 2026
- Canada official management benchmark values preserved:
  - CAD $27.00/hour low
  - CAD $43.96/hour median
  - CAD $71.43/hour high
- Management-versus-coordinator distinction preserved for both U.S. and Canada: PASS
- Colombia no-invented-national-wage boundary preserved: PASS
- No universal degree requirement introduced for coordinator titles: PASS
- Professional-practice boundaries preserved: PASS
- Grant and procurement authority restrictions preserved: PASS
- Privacy, confidentiality, safeguarding, accessibility, and cybersecurity boundaries preserved: PASS
- AI protected-data restrictions and human-review requirement preserved: PASS
- No guaranteed employment, wages, training funding, certification, licensing, grants, contracts, promotion, accreditation, accessibility certification, or legal review introduced: PASS

## Language quality

The edition uses neutral, broadly understandable Latin American Spanish. Official occupational classifications, source names, program names, and controlled identifiers remain in their official form where translation could alter classification meaning. Colombia-specific SENA program names remain in Spanish. Decimal and thousands separators are localized in prose without altering the underlying numeric values.

Terminology avoids representing a generic coordinator title as licensed social work, clinical practice, legal practice, fiduciary authority, government-benefit adjudication, grantmaking authority, or management authority unless formally assigned.

## Assurance boundary

This QA is internal machine-assisted controlled-project review. It does not claim independent human linguistic certification, professional translation certification, legal review, accessibility certification, or accreditation.

**Result: PASS.** Spanish localization is suitable to advance the controlled sequence to independent Brazilian Portuguese localization from the frozen English source.