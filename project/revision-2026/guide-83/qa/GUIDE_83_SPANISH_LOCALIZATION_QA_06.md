# Guide 83 — Spanish Localization QA 06

**Occupation:** Network Support Technician  
**Locale:** neutral Latin American Spanish (`es-419`)  
**Source:** frozen English blob `6c6f9e83d4084d0a8215a045e621605fc1360c40`  
**Localized master:** `GUIDE_83_TECNICO_DE_SOPORTE_DE_REDES_ES419_v2.md`  
**Review date:** 2026-08-21  
**Stage:** Spanish Localization — **PASS**

## Language and structure — PASS

The Spanish edition is a complete reader-facing localization in neutral Latin American Spanish. It contains no translator instructions, placeholders or English-only dependency for core meaning. Technical acronyms and product/protocol names are retained where industry usage requires them.

## Occupation parity — PASS

The edition preserves:

- O*NET-SOC **15-1231.00**;
- Canada NOC **22220**;
- Colombia CUOC **35130**;
- network-support scope and the distinctions from administrator, engineer/architect and security roles.

## Numeric parity — PASS

All frozen U.S. wage values, 2024–2034 employment/outlook figures, Indeed related-title market values, Canadian wage values and SENA durations are preserved exactly.

Specifically:

- U.S. wages: $47,120/$22.65; $58,240/$28.00; $76,220/$36.64; $98,750/$47.48; $127,780/$61.43;
- 152,700 → 155,500; 2%; 9,600 annual openings;
- Indeed: $26.30/hour, $17.46–$39.60/hour, approximately 2.1k salaries, August 3, 2026;
- Canada: C$21.00 / C$36.00 / C$55.00 per hour;
- SENA: Técnico 2,208 hours and Tecnólogo 3,984 hours.

## Technology-signal parity — PASS

The Spanish edition preserves all controlled O*NET posting signals from 13% through 1% and labels them as market signals rather than universal requirements.

## Technical semantic parity — PASS

Equivalent coverage is present for troubleshooting discipline, OSI/TCP-IP, addressing/subnetting, DHCP/DNS, VLAN/switching, routing/BGP awareness, wireless, VPN, performance, monitoring/logs, cloud/hybrid networking, backup/recovery, change/rollback and ticket documentation.

## Security and authority parity — PASS

The localization preserves least privilege, credential protection, approved change control, rollback/validation, incident escalation and explicit prohibitions on unauthorized access bypass, offensive testing, disabling safeguards, unapproved production changes, evidence destruction and false restoration claims.

## Canada/Colombia boundary parity — PASS

The Saskatchewan regulatory-registration caveat remains explicit. The Colombia edition mapping remains CUOC 35130 and does not convert OCUPACOL's non-representative historical salary indicators into a representative current wage claim.

## AI/accessibility/assurance parity — PASS

Approved-system/data restrictions, no secrets in unapproved AI, human verification and no unauthorized autonomous production changes remain intact. Accessibility concepts and the no-certification boundary are preserved. Educational-only/no-guarantee, author/AI-assistance disclosure and CC BY-NC-SA 4.0 remain present.

## URL parity — PASS

The localized master carries the same **22 controlled external URLs** as the frozen English source.

## Gate decision

**PASS — Spanish Localization**

The `es-419` edition is cleared for trilingual reconciliation after Portuguese localization.

**Blockers:** none.
