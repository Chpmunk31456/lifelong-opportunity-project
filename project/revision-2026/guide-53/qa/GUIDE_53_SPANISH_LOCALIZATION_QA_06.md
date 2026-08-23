# Guide 53 — Spanish Localization QA 06

**Occupation:** Physical Therapist Assistant  
**Locale:** neutral Latin American Spanish (`es-419`)  
**Date:** 2026-08-19  
**Source:** `GUIDE_53_PHYSICAL_THERAPIST_ASSISTANT_ENGLISH_v2.md`  
**Localized master:** `GUIDE_53_PHYSICAL_THERAPIST_ASSISTANT_SPANISH_es-419_v1.md`

## Gate result

**PASS**

## Controlled checks

- PASS — All major English-source sections are represented in the Spanish localization in the same substantive sequence.
- PASS — U.S. role identity is preserved as `Physical Therapist Assistant (PTA)` where literal translation could create regulatory ambiguity.
- PASS — The localization explicitly avoids presenting a U.S. PTA as a Colombian `fisioterapeuta`.
- PASS — Colombia's regulated physiotherapy distinction under Ley 528 de 1999 is preserved.
- PASS — U.S. CAPTE, FSBPT, NPTE, BLS, WIOA, FAFSA and state-licensure concepts remain jurisdiction-specific and are not generalized to Latin America.
- PASS — Canada NOC 32109 language remains explicitly group-level and does not imply a universal Canadian PTA licensing rule.
- PASS — Official wage figures, dates, exam fee, employment counts and growth figures retain their source values and currency context.
- PASS — Salary.com remains clearly labeled as a supplementary non-government market estimate, separate from BLS official data.
- PASS — Patient-safety escalation language remains conservative and does not create independent clinical authority.
- PASS — Privacy, cybersecurity and responsible-AI safeguards are preserved.
- PASS — Funding and public-training locators remain framed as eligibility/exploration resources rather than guaranteed benefits.
- PASS — Source URLs from the English master are retained without intentional substitution.
- PASS — The final source/review disclaimer preserves the no-certification, no-legal/medical/financial-advice and no-guarantee limitations.
- PASS — Spanish is written for broad Latin American readability rather than Spain-specific usage.

## Terminology controls

The localization deliberately retains certain English institutional and credential names where translation could obscure legal identity, including `Physical Therapist Assistant`, `physical therapist`, `CAPTE`, `FSBPT`, `NPTE`, `WIOA`, `FAFSA`, `Job Bank`, and named government programs.

The term `fisioterapeuta` is used for the regulated Colombian profession only in the jurisdictional explanation and is not treated as a direct equivalent of the U.S. PTA title.

## Blockers

None.

## Conclusion

The Spanish localization is suitable to advance to controlled status. This QA does not claim certified professional translation or independent human legal/clinical review.