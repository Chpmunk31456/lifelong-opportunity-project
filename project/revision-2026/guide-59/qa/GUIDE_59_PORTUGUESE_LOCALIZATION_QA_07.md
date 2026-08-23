# Guide 59 — Brazilian Portuguese Localization QA 07

**Stage:** Portuguese Localization — **PASS**  
**Locale:** pt-BR  
**Date:** 2026-08-20

## Source control

Localization was produced directly from the frozen English master:

`project/revision-2026/guide-59/working-masters/GUIDE_59_SOCIAL_AND_HUMAN_SERVICE_ASSISTANT_ENGLISH_v2.md`

Frozen English blob SHA: `d7cd465b809a77c72d6968c22fbb342e64fd6bec`

Portuguese master:

`project/revision-2026/guide-59/working-masters/GUIDE_59_SOCIAL_AND_HUMAN_SERVICE_ASSISTANT_PTBR_v2.md`

## Controlled parity checks

PASS:

- occupation remains a support/navigation role and is not broadened into licensed social work, psychotherapy, legal practice, clinical practice, benefits adjudication, or emergency-command authority;
- O*NET `21-1093.00`, Canada `NOC 42201`, and Colombia `CNO 4211` mappings are preserved;
- U.S. official wage/outlook values remain semantically unchanged: `USD $22.08`, `USD $45,930`, `449,600`, `5% to 6%`, and `50,600`;
- supplementary Indeed estimate remains clearly labeled non-government and preserves `USD $21.40` and the August 1, 2026 update date;
- Canada wage values remain `CAD $19.00`, `CAD $26.00`, and `CAD $36.06` with November 19, 2025 update context;
- Colombia correctly retains the controlled finding that no clean directly comparable national official salary series was identified and no salary is invented;
- mandatory-reporting, safeguarding, crisis, legal, clinical, and benefits-authority boundaries are preserved;
- privacy, cybersecurity, and AI restrictions remain intact;
- all controlled source URLs are retained;
- public funding and training locators remain framed as locators rather than guarantees;
- assurance boundary continues to disclaim independent human certification, accreditation, certified translation, legal review, clinical review, financial advice, and guaranteed employment outcomes.

## Language review

Brazilian Portuguese uses natural `pt-BR` syntax and vocabulary while preserving jurisdiction-specific English program/job names where translating them could create false equivalence.

## Result

**PASS.** Guide 59 may proceed to trilingual Technical QA.
