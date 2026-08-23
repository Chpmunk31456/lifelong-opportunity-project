# Guide 83 — Portuguese Localization QA 07

**Occupation:** Network Support Technician  
**Locale:** Brazilian Portuguese (`pt-BR`)  
**Source:** frozen English blob `6c6f9e83d4084d0a8215a045e621605fc1360c40`  
**Localized master:** `GUIDE_83_TECNICO_DE_SUPORTE_DE_REDES_PTBR_v2.md`  
**Review date:** 2026-08-21  
**Stage:** Portuguese Localization — **PASS**

## Language and structure — PASS

The Portuguese edition is a complete reader-facing Brazilian Portuguese localization with no translation placeholders or English-only dependency for core meaning. Industry acronyms, protocols and product names are retained where normal technical usage requires them.

## Occupation parity — PASS

The edition preserves O*NET-SOC **15-1231.00**, Canada NOC **22220**, Colombia CUOC **35130**, and the distinctions among network support, administration, engineering/architecture and security roles.

## Numeric parity — PASS

All frozen U.S. wage values, outlook figures, Indeed related-title values, Canadian wage values and SENA durations are preserved:

- $47,120/$22.65; $58,240/$28.00; $76,220/$36.64; $98,750/$47.48; $127,780/$61.43;
- 152,700 → 155,500; 2%; 9,600 annual openings;
- Indeed $26.30/hour, $17.46–$39.60/hour, approximately 2.1k salaries, August 3, 2026;
- Canada C$21.00 / C$36.00 / C$55.00 per hour;
- SENA Técnico 2,208 hours and Tecnólogo 3,984 hours.

## Technology-signal parity — PASS

The controlled O*NET employer-posting percentages from 13% through 1% are preserved and remain labeled as market signals, not universal requirements.

## Technical semantic parity — PASS

The localization preserves the troubleshooting, OSI/TCP-IP, IP/subnet, DHCP/DNS, switching/VLAN, routing/BGP, wireless, VPN, performance, monitoring/logging, cloud/hybrid, backup/recovery, change/rollback and ticket-documentation concepts.

## Security and authority parity — PASS

Least privilege, credential protection, approved change control, rollback/validation, evidence preservation and incident escalation remain explicit. The edition preserves the prohibitions on unauthorized bypass, scanning/penetration testing, disabling safeguards, unapproved production changes, destroying logs/evidence and false restoration claims.

## Canada/Colombia boundary parity — PASS

The Saskatchewan regulatory-registration caveat remains present. CUOC 35130 is preserved and the OCUPACOL historical/derived salary range is not promoted as representative current Colombian national pay.

## AI/accessibility/assurance parity — PASS

Approved-system/data restrictions, protection of secrets/configurations, human verification and no unauthorized autonomous production changes remain intact. Accessibility content retains its no-certification boundary. Educational-only/no-guarantee, author/AI-assistance disclosure and CC BY-NC-SA 4.0 remain present.

## URL parity — PASS

The Portuguese master carries the same **22 controlled external URLs** as the frozen English source.

## Gate decision

**PASS — Portuguese Localization**

The `pt-BR` edition is cleared for trilingual technical QA.

**Blockers:** none.
