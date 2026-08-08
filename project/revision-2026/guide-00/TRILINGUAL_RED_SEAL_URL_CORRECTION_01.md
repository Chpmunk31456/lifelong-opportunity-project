# Guide 00 — Trilingual Red Seal URL Correction Control

**Date:** 2026-08-03  
**Branch:** `revision/guide-00-100-2026`  
**Status:** Approved source correction; must be applied before DOCX/PDF generation

## Defect

The English, neutral Latin American Spanish (`es-419`), and Brazilian Portuguese (`pt-BR`) integrated masters contain the obsolete Red Seal contact URL:

`https://www.red-seal.ca/eng/contact/c.4nt.1ct.shtml`

That address is not the preferred canonical authority page for the program and must not be carried into publication files.

## Controlled replacement

Replace the obsolete URL in all three Guide 00 integrated masters with:

`https://www.red-seal.ca/eng/about/pr.4gr.1m.shtml`

Link label by edition:

- English: `Red Seal Program — About the Program`
- es-419: `Programa Sello Rojo — Información sobre el programa`
- pt-BR: `Programa Selo Vermelho — Sobre o programa`

## Scope

The replacement applies to:

1. `00-foundation-guide/source/Lifelong_Opportunity_Foundation_Guide_English_v1.1_INTEGRATED_MASTER.md`
2. `00-foundation-guide/source/Lifelong_Opportunity_Foundation_Guide_es-419_v1.1_INTEGRATED_MASTER.md`
3. `00-foundation-guide/source/Lifelong_Opportunity_Foundation_Guide_pt-BR_v1.1_INTEGRATED_MASTER.md`
4. All DOCX, PDF, HTML, metadata, link manifests, and publication candidates generated from those masters.

## QA rule

Document generation is blocked until an exact-string scan confirms:

- obsolete URL occurrences: `0`
- canonical URL occurrences: at least `1` in each language master

After generation, hyperlink relationship targets in each DOCX and clickable annotations in each PDF must be checked for the canonical URL.

## Claim control

This correction does not constitute independent legal, accreditation, translation, or accessibility certification. It is an internal source-maintenance control based on the current official Red Seal program site.
