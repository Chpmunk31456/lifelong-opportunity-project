# Guide 01 — Trilingual Market-Income Reconciliation QA 03

**Guide:** Community Health Worker / Trabajador comunitario de salud / Agente comunitário de saúde  
**Branch:** `revision/guide-00-100-2026`  
**Review date:** August 5, 2026  
**Status:** Completed controlled reconciliation; market-estimate integration passes evidence and parity review, with publication-format gates still open

## Purpose

This record reconciles the current Guide 01 working masters with the income evidence register and corrects stale statements in earlier QA records that said no non-government income estimate had been inserted or approved.

This is an internal editorial and automated-assistance QA artifact. It is not independent human certification, professional translation certification, accessibility certification, accreditation review, legal review, clinical review, or publication approval.

## Files reviewed

- `INCOME_AND_OUTLOOK_EVIDENCE_REGISTER_01.md`
- `MARKET_INCOME_INTEGRATION_EXECUTION_QA_02.md`
- `TRILINGUAL_STRUCTURAL_PARITY_QA_01.md`
- `TRILINGUAL_TERMINOLOGY_QA_02.md`
- `working-masters/GUIDE_01_COMMUNITY_HEALTH_WORKER_ENGLISH_WORKING_MASTER.md`
- `working-masters/GUIDE_01_TRABAJADOR_COMUNITARIO_DE_SALUD_ES419_WORKING_MASTER.md`
- `working-masters/GUIDE_01_AGENTE_COMUNITARIO_DE_SAUDE_PTBR_WORKING_MASTER.md`

## Reconciliation finding

The three current working masters include the same two supplementary United States market estimates:

1. **Glassdoor** — estimated average annual pay of **USD 52,306**, based on **1,936 anonymously submitted salaries**, with the source showing a June 2026 estimate date.
2. **ZipRecruiter** — estimated average annual pay of **USD 44,925**, with the source showing a July 27, 2026 estimate date and describing the estimate as derived from employer job postings and third-party data.

The masters keep these figures separate from the primary official U.S. Bureau of Labor Statistics median of **USD 51,030** for May 2024. They explicitly state that the estimates use different methodologies, are not official statistics, must not be averaged together, and do not represent guaranteed offers or local salary promises.

## Trilingual numerical parity

| Data point | English | es-419 | pt-BR | Result |
|---|---:|---:|---:|---|
| BLS median annual wage | USD 51,030 | USD 51.030 | USD 51.030 | PASS |
| Glassdoor estimated average | USD 52,306 | USD 52.306 | USD 52.306 | PASS |
| Glassdoor reported sample | 1,936 | 1.936 | 1.936 | PASS |
| ZipRecruiter estimated average | USD 44,925 | USD 44.925 | USD 44.925 | PASS |
| Glassdoor estimate date | June 2026 | junio de 2026 | junho de 2026 | PASS |
| ZipRecruiter estimate date | July 27, 2026 | 27 de julio de 2026 | 27 de julho de 2026 | PASS |

Localized thousands separators are formatting adaptations, not numerical differences.

## Source-type and limitation parity

All three editions preserve the following controls:

- BLS remains the primary official United States reference;
- Glassdoor is identified as an estimate based on anonymous salary submissions;
- ZipRecruiter is identified as an estimate based on employer postings and third-party data;
- the estimates are not averaged with BLS or with each other;
- the figures are not described as entry wages, employer offers, guaranteed compensation, or Colombia salary expectations;
- geography, source date, methodology difference, and occupational-match limitations remain visible;
- Colombia and broader Latin America sections continue to state that no directly equivalent national Colombian wage series was verified in this controlled batch.

## Superseded statements

The following earlier statements are stale and are superseded by this reconciliation record:

- `TRILINGUAL_STRUCTURAL_PARITY_QA_01.md`: “No non-government income estimate is approved by this QA record.”
- `TRILINGUAL_TERMINOLOGY_QA_02.md`: “No current non-government estimate has been inserted.”

Those statements accurately described an earlier workflow state but no longer describe the current working masters after controlled market-income integration. The historical QA files remain unchanged to preserve the audit trail; this record documents the later state transition.

## QA decision

**Decision: PASS for controlled trilingual market-income evidence integration and numerical parity.**

The current English, es-419, and pt-BR working masters contain the same approved supplementary estimates, preserve official-versus-commercial source distinctions, and retain the required limitations. This pass applies only to the content and evidence controls reviewed here.

## Remaining publication gates

Guide 01 still requires:

1. final editorial freeze of all three masters;
2. normalization of the first substantive formal-apprenticeship definition in es-419 and pt-BR;
3. complete final-candidate live-link validation;
4. version change from working draft to publication candidate;
5. DOCX generation and OOXML inspection;
6. searchable PDF generation and text-extraction QA;
7. localized title, filename, metadata, hyperlink, encoding, and page-render inspection;
8. SHA-256 checksums and publication manifest.

Guide 01 has not yet passed publication QA and must not be represented as independently certified, accredited, professionally translated, legally reviewed, clinically reviewed, or accessibility certified.
