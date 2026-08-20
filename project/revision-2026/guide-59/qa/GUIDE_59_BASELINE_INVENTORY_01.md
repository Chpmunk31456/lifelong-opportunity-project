# Guide 59 — Baseline Inventory 01

**Guide:** 59 — Social and Human Service Assistant  
**Branch:** `revision/guide-00-100-2026`  
**Date:** August 20, 2026  
**Stage:** Baseline Inventory — **PASS**

## Legacy package identified

The live repository contains the published Guide 59 package at `59-social-and-human-service-assistant/` with separate English, Spanish, and Portuguese edition directories.

The English legacy package includes:

- `english/README.md` identifying Guide 59, Social And Human Service Assistant, English Version 1.0, July 2026;
- `english/docx/Social and Human Service Assistant.docx` (46,811 bytes in the live repository);
- a searchable PDF directory; and
- `english/QC.md`.

The package README states that exact source equivalence and human linguistic review should not be assumed unless separately documented. It also states that ChatGPT assisted with research, organization, editing, translation support, and document preparation under the author's direction.

## Controlled-revision implications

1. There is **no editable English Markdown source master** in the legacy English edition directory. Version 2 therefore requires controlled reconstruction rather than an in-place text edit.
2. The legacy English README begins with a UTF-8 BOM and uses title capitalization `Social And Human Service Assistant`; the controlled master should use natural title capitalization `Social and Human Service Assistant` while preserving the occupational identity.
3. Existing DOCX/PDF files are publication artifacts, not authoritative current-source evidence for the 2026 controlled revision.
4. Existing Spanish and Portuguese packages are legacy editions. They must not be treated as authoritative translations for Version 2; localization follows only after the revised English source is frozen.
5. Current occupational classification, duties, education, compensation, funding/training pathways, privacy/safety, AI-use boundaries, and jurisdiction-specific role limits require fresh evidence before English reconstruction.
6. Because this occupation can involve vulnerable clients, benefits/resources, crisis exposure, confidential case information, and referrals, Version 2 must clearly distinguish supportive/navigation duties from licensed social work, psychotherapy, clinical diagnosis, legal advice, benefits eligibility determinations, emergency response, and other regulated decisions.

## Required Version 2 sequence

- Current-source Research
- English Editorial / controlled Version 2 reconstruction
- Evidence/Traceability QA
- English Source Freeze
- Spanish Localization (`es-419`)
- Brazilian Portuguese Localization (`pt-BR`)
- Trilingual Technical QA
- controlled DOCX/PDF Publication
- Release Audit

## Decision

**Baseline Inventory: PASS.** The occupation and legacy package are identifiable and usable as historical/reference inputs, but not as the controlled Version 2 source of truth. Proceed to fresh current-source Research.
