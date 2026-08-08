# Guide 01 — Publication Gate Reconciliation 01

**Guide:** Community Health Worker / Trabajador comunitario de salud / Agente comunitário de saúde  
**Branch:** `revision/guide-00-100-2026`  
**Review date:** August 5, 2026  
**Status:** Controlled gate reconciliation completed; publication candidate not yet approved

## Purpose

This record reconciles the Guide 01 working-master and QA records before final editorial freeze and document generation. It identifies completed controls, stale statements that must not be treated as current, and the exact remaining publication gates.

This is an internal automated and editorial control record. It is not independent human certification, professional translation certification, accessibility certification, accreditation review, legal review, or publication approval.

## Controlled files in scope

- `working-masters/GUIDE_01_COMMUNITY_HEALTH_WORKER_ENGLISH_WORKING_MASTER.md`
- `working-masters/GUIDE_01_TRABAJADOR_COMUNITARIO_DE_SALUD_ES419_WORKING_MASTER.md`
- `working-masters/GUIDE_01_AGENTE_COMUNITARIO_DE_SAUDE_PTBR_WORKING_MASTER.md`
- `TRILINGUAL_STRUCTURAL_PARITY_QA_01.md`
- `TRILINGUAL_TERMINOLOGY_AND_TRANSLATION_CONTROL_01.md`
- `TRILINGUAL_TERMINOLOGY_QA_02.md`
- `MARKET_INCOME_TRILINGUAL_RECONCILIATION_QA_03.md`
- `LINK_VALIDATION_REGISTER_01.md`
- `LIVE_LINK_VALIDATION_BATCH_01.md`
- `LIVE_LINK_VALIDATION_BATCH_02.md`
- `LIVE_LINK_VALIDATION_BATCH_03_COLOMBIA_PPSS.md`
- `RIAS_URL_NORMALIZATION_QA_01.md`

## Completed controls confirmed by repository evidence

The following controls have completed records in the controlled revision directory:

1. English baseline extraction and inventory.
2. English official-source fact-check evidence.
3. English integrated-master construction and QA.
4. Neutral Latin American Spanish and Brazilian Portuguese baseline extraction.
5. Trilingual structural-parity review.
6. Trilingual terminology controls and follow-up terminology QA.
7. U.S. official wage and outlook integration.
8. Canada official wage and occupational-group limitation integration.
9. Clearly labelled U.S. non-government income estimates and trilingual reconciliation.
10. Colombia RIAS URL normalization and Colombia PPSS link review.
11. Funding, scholarships, employer support, apprenticeships, and regional-pathway coverage in the controlled working masters.

## Superseded or stale statements

The following statements remain in earlier working or QA records but no longer describe the latest controlled state:

- Any statement that translation has not begun is superseded by the committed es-419 and pt-BR working masters and trilingual QA records.
- Any statement that no non-government income estimate has been integrated is superseded by `MARKET_INCOME_TRILINGUAL_RECONCILIATION_QA_03.md`.
- Any statement that terminology normalization has not been performed is superseded by `TRILINGUAL_TERMINOLOGY_QA_02.md` and the associated normalization workflow and script.

These older statements must not be copied into publication metadata, release notes, or final QA conclusions.

## Remaining mandatory gates

Guide 01 must remain at draft status until all of the following are completed and recorded:

1. **Editorial freeze**
   - Reconcile the status line and review date in all three working masters.
   - Confirm spelling, grammar, punctuation, heading sequence, plain-language readability, and internal consistency.
   - Confirm that no unsupported certification, accreditation, licensing, immigration, employment, or income guarantee appears.

2. **Translation freeze**
   - Complete sentence-level es-419 and pt-BR comparison against the approved English master.
   - Record any intentional localization exceptions.
   - Confirm numerical, date, limitation, and source-type parity.

3. **Live-link freeze**
   - Re-run all links from the final frozen masters.
   - Record status code, final destination, access date, redirects, and any regional or anti-bot limitation.
   - Replace or remove broken, obsolete, or misleading links before document generation.

4. **Version and metadata freeze**
   - Change working status only after the content freeze passes.
   - Use consistent version, language, review date, title, author, license, subject, and keywords across Markdown, DOCX, PDF, manifest, and checksums.

5. **DOCX QA**
   - Generate one DOCX per language from the frozen source.
   - Inspect OOXML structure, heading styles, lists, hyperlink relationships, document properties, language metadata, and absence of corruption.

6. **PDF QA**
   - Generate one searchable PDF per language.
   - Confirm extractable text, correct title, page count, link behavior where supported, and no missing or clipped content.

7. **Rendered-page inspection**
   - Render all pages or a controlled inspection set sufficient to detect layout defects.
   - Check headings, page breaks, lists, URLs, tables if present, orphaned text, clipping, and unreadable characters.

8. **Publication manifest**
   - Record filenames, versions, languages, page counts, SHA-256 checksums, source commit, build workflow, build date, and QA outcome.
   - State explicitly that automated QA is not independent certification or accreditation.

## Current gate decision

**Guide 01 status: NOT YET A PUBLICATION CANDIDATE.**

The content and trilingual control work are sufficiently advanced to proceed to final editorial and translation freeze. The next controlled action is to reconcile the three working-master status blocks, complete final sentence-level review, and run final live-link validation before generating DOCX and PDF candidates.

PR #17 must remain in Draft.
