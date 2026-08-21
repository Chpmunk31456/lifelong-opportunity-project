# Guide 68 — Baseline Inventory 01

**Occupation:** Baker and Pastry Production Worker  
**Review date:** 2026-08-21  
**Gate:** Baseline Inventory — PASS

## Legacy package identified

Legacy source package: `68-baker-and-pastry-production-worker/`.

Repository inventory confirms a trilingual package with:

- root `README.md` identifying Guide 68 as **Baker And Pastry Production Worker**;
- `english/`, `spanish/`, and `portuguese/` language directories;
- editable DOCX and searchable PDF editions referenced by the root README;
- English legacy files identified as `english/docx/Baker and Pastry Production Worker.docx` and `english/pdf/Baker and Pastry Production Worker.pdf`.

## Baseline defects and risks

The root README currently begins with a UTF-8 BOM and contains a clear legacy metadata/link defect: its Spanish edition links point to filenames beginning `Guia_66_...` and describe the prior food-service-manager/supervisor guide rather than Guide 68. Those Spanish links must not be treated as authoritative Guide 68 localization evidence.

The Brazilian Portuguese filenames contain normalized/garbled-looking `Produ_o` text in the link target. Downstream localization and publication must use fresh controlled Version 2 filenames and UTF-8 text rather than propagating legacy naming or encoding defects.

Legacy Spanish and Portuguese editions are historical reference material only. They are not factual source-of-truth inputs for Version 2 localization.

## Controlled-revision starting point

No prior Guide 68 controlled helper manifest, current-source research record, Version 2 English working master, localization master, trilingual technical QA, publication candidate, or release-audit evidence was identified before this step.

Guide 68 combines the standard occupation **Baker** with a broader employer-defined **pastry production worker** label. Downstream research must distinguish bakery production duties from pastry-chef, executive-chef, food-service-manager, dietitian/nutritionist, and other higher-authority or regulated roles.

Later stages must verify current U.S. occupation/wage/outlook data, current non-government market estimates, Canada comparison, Colombia/SENA pathways, food-safety and allergen controls, worker-safety hazards, public/free-first training and apprenticeship pathways, accessibility, privacy/cybersecurity, responsible AI, and role/authority boundaries.

## Result

**PASS.** The legacy package and controlled-revision starting point are sufficiently identified to begin current-source research. The noted Spanish-link and encoding defects are downstream repair requirements, not blockers to research.

## Assurance boundary

This is an internal machine-assisted repository inventory. It is not independent human certification, professional translation certification, culinary or food-safety certification, legal review, accessibility certification, accreditation, or publication approval.
