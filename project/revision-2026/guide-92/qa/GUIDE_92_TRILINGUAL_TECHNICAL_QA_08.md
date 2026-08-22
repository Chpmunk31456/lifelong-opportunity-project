# Guide 92 — Trilingual Technical QA 08

**Guide:** 92 — Geographic Information Systems Technician  
**Controlled branch:** `revision/guide-00-100-2026`  
**Frozen English source:** blob `5fc776670bc33d9e2b01a5dda8084a9099627165`  
**Locales:** English, neutral Latin American Spanish (`es-419`), Brazilian Portuguese (`pt-BR`)  
**Review date:** 2026-08-22

## Occupation mapping parity — PASS
All three editions preserve:
- U.S. **O*NET-SOC 15-1299.02 — Geographic Information Systems Technologists and Technicians**;
- Canada **NOC 22214 — Technical occupations in geomatics and meteorology**;
- Colombia **CUOC 31123 — Técnicos en cartografía**, explicitly including Técnico sistemas de información geográfica.

## U.S. statistical crosswalk — PASS
All three editions explicitly state that O*NET wage and employment statistics for 15-1299.02 are collected from **Computer Occupations, All Other**. No edition presents the $116,580 O*NET median as a pure title-only GIS Technician median.

## Numeric parity — PASS
All editions preserve:

### U.S. crosswalked 2025 official wages
- $55,940 / $26.89
- $79,370 / $38.16
- median $116,580 / $56.05
- $157,500 / $75.72
- $188,470 / $90.61

### U.S. crosswalked 2024–2034 outlook
- 472,000 employment in 2024
- 510,500 projected employment in 2034
- 8% growth
- 31,300 annual openings

### Current title-specific Indeed GIS Technician context
- $25.88/hour average
- $17.60/hour low
- $38.06/hour high
- 749 observations
- prior 36 months
- updated August 2, 2026

All editions explain that the O*NET and Indeed datasets represent different populations/methodologies and are not averaged together.

### Canada
All editions preserve NOC 22214 national wages:
- C$23.08/hour low
- C$38.10/hour median
- C$53.85/hour high

All preserve the current national **strong risk of labour surplus** outlook and the Quebec Professional Technologist title/regulatory-body caveat without overgeneralizing regulation to all GIS jobs in Canada.

### SENA
All editions preserve:
- Introducción a los Sistemas de Información Geográfica — **80 hours/horas**;
- Sistemas de Información Geográfica — **48 hours/horas**;
- Aplicación de SIG en Sistemas Forestales y Agroecológicos — **48 hours/horas**;
- live cohort/centre/modality/prerequisite/seat verification caveats.

## Technology-signal parity — PASS
All editions preserve key 2025 posting signals including ArcGIS 75%, GIS systems 67%, Python 34%, SQL 22%, GIS software 21%, Office/Excel 14%, JavaScript 13%, AutoCAD 10%, ArcMap/QGIS 7%, Survey123/Access/PowerPoint 6%, and Azure/ArcPy/Outlook/AWS 5%. They are labelled posting signals, not universal requirements.

## Source parity — PASS
English, es-419 and pt-BR preserve the same **23 reader-facing verification URLs**. The Research pack retains the same **23 controlled evidence URLs**.

## Spatial-data and CRS parity — PASS
All editions preserve:
- vector point/line/polygon concepts;
- raster/cell/resolution concepts;
- attributes and spatial databases;
- geographic versus projected coordinate systems;
- datum/reference framework;
- units and EPSG identifiers conceptually;
- transformation/reprojection;
- projection distortion and fitness for purpose;
- warning that visual alignment does not prove CRS metadata correctness.

## Data-quality and lineage parity — PASS
All editions preserve source/provenance, capture date, positional/attribute accuracy, completeness, consistency, scale/resolution, CRS/datum, transformations, processing/edit history, authoritative-versus-derived status and limitations.

They preserve the boundary against silently changing authoritative source data without the proper owner/change process.

## Geometry, georeferencing and cartography parity — PASS
All editions preserve geometry/topology defects, domain-specific topology rules, snapping/tolerance, control-point selection, transformation/residual review, independent validation, false-precision warnings, cartographic purpose/audience, scale/symbology/classification, uncertainty and accessible map communication.

## Analysis and automation parity — PASS
All editions preserve buffers, overlays, proximity, spatial joins, network/raster/terrain analysis; SQL/spatial database work; Python/ArcPy automation; parameter/input/output/version evidence; and the rule that technically successful processing can still answer the wrong question.

## Sharing, privacy and professional-authority parity — PASS
All editions preserve web-GIS sharing/permission review, protection of sensitive personal/asset/critical-infrastructure/environmental/cultural locations, field/mobile-data controls, authoritative-layer change authority, and the boundary that GIS work does not itself create survey/legal/cadastral authority or survey-grade accuracy.

## Responsible-AI parity — PASS
All editions prohibit protected coordinates/layers/credentials/restricted imagery in unapproved AI tools; require validation of generated code, CRS, units, spatial assumptions and feature extraction/classification; preserve lineage; prohibit invented authoritative coordinates/legal boundaries/survey-grade accuracy; and require human/domain validation.

## Accessibility parity — PASS
All editions preserve contrast, non-color-only encoding, labels/legends, static-map context/alt text, text/table alternatives and keyboard-accessible web controls where relevant. No edition claims that automated checks prove legal accessibility compliance.

## Portfolio and claims parity — PASS
All editions restrict portfolio work to public/open, lawfully collected personal or synthetic data and prohibit publication of protected employer/client layers, private addresses, critical-infrastructure locations, restricted cultural/environmental sites or proprietary schemas. No employment, compensation, funding, professional-status, legal, surveying, cadastral, geospatial-accuracy or accessibility guarantee/certification is claimed.

## Gate result
**PASS — Trilingual Technical QA**

**Blockers:** none.

Guide 92 is cleared for controlled Publication QA and Release Audit.

**Publication trigger synchronization:** 2026-08-22.  
**Diagnostic trigger synchronization:** 2026-08-22.  
**Link diagnostic trigger synchronization:** 2026-08-22.  
**Conflict-safe publication v3 trigger synchronization:** 2026-08-22.  
**Post-diagnostic-cleanup release trigger:** 2026-08-22.  
**Post-legacy-workflow-retirement release trigger:** 2026-08-22.  
**Final clean release trigger after Guide 02 workflow retirement:** 2026-08-22.
