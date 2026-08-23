# Guide 93 — Portuguese Localization QA 07

**Guide:** 93 — Surveying and Mapping Technician  
**Locale:** Brazilian Portuguese (`pt-BR`)  
**Controlled branch:** `revision/guide-00-100-2026`  
**Review date:** 2026-08-22  
**Frozen English source:** blob `effdfcd7908596a0285100e7856d898ee60abfe7`  
**Portuguese master:** blob `078beb1c948b118021437a2a552240f14aeec403`

## Localization review
The Brazilian Portuguese v2 edition was localized from the frozen English semantic source rather than from the legacy Portuguese publication candidate.

### Terminology controls
- Guide title localized as **Técnico em Agrimensura e Mapeamento**.
- Brazil section preserves official CBO terminology: **3123 — Técnicos em geomática**, **3123-05 Técnico em Agrimensura**, **3123-10 Técnico em Geodésia e Cartografia**, **3123-20 Topógrafo**.
- Professional-scope language uses `profissional habilitado` / jurisdiction-dependent authority rather than implying that a technician automatically has legal boundary-signing authority.
- Technical terms such as estação total, GNSS/GPS, poligonal, fechamento, georreferenciamento, datum, sistema de coordenadas, locação/replanteio, fotogrametria, ortomosaico, CAD and GIS are used consistently.
- Foreign formal titles and product/platform names remain untranslated where translation could alter meaning.

## Controlled numeric parity
The Portuguese edition preserves:
- U.S. BLS May 2024 median **$51,940** and **$24.97/hour**;
- U.S. employment 2024 **59,400**;
- U.S. projected employment 2034 **62,100**;
- U.S. projected growth **5%**;
- U.S. projected annual openings about **7,600**;
- Civil 3D **23%**, AutoCAD **20%**, MicroStation **13%**;
- Canada **C$22.00 / C$29.75 / C$46.00**;
- Colombia OCUPACOL **COP $350,000–$2,910,053** together with the mandatory non-representative-data warning;
- SENA Tecnólogo **3,984 hours**;
- SENA Técnico **2,304 hours**;
- ChileValora validity through **2028-12-30**;
- SENCICO **3 years**.

## Semantic parity controls
PASS for preservation of:
- technician-versus-authorized-professional boundary;
- measurement/units/control concepts;
- total-station, level and GNSS quality controls;
- CRS/datum/transformation concepts;
- traverse/closure controls;
- construction-layout revision/tolerance controls;
- raw-observation, field-note and data-lineage requirements;
- CAD/GIS/photogrammetry boundaries;
- separate drone/aviation authorization requirements;
- data privacy/security controls;
- heat/traffic/utility/remote-work safety guidance;
- equipment-serviceability/calibration boundary;
- responsible-AI restrictions against invented coordinates, control points, monuments, legal boundaries or survey-grade accuracy;
- accessibility/inclusion without weakening essential safety/professional requirements;
- U.S., Canada, Colombia, Chile, Peru and Brazil pathway content;
- safe portfolio, starter plan, interview and employer-due-diligence sections;
- non-guarantee/non-certification language.

## Source-link parity
The Portuguese edition preserves the same **19 reader-verification URLs** as the frozen English source, without translated or altered destinations.

## Language-quality result
- Natural Brazilian Portuguese: PASS.
- UTF-8/diacritics: PASS.
- Brazil CBO terminology: PASS.
- No placeholder localization language: PASS.
- No certified/professional translation claim: PASS.
- No unsupported Brazilian legal/professional-registration interpretation: PASS.

## Gate result
**PASS — Portuguese Localization (`pt-BR`)**

**Blockers:** none.

Guide 93 may proceed to Trilingual Technical QA.
