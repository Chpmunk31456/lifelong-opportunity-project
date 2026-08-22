# Guide 93 — Spanish Localization QA 06

**Guide:** 93 — Surveying and Mapping Technician  
**Locale:** neutral Latin American Spanish (`es-419`)  
**Controlled branch:** `revision/guide-00-100-2026`  
**Review date:** 2026-08-22  
**Frozen English source:** blob `effdfcd7908596a0285100e7856d898ee60abfe7`  
**Spanish master:** blob `4f2bfc5abba748332280b3106d15d8625d0d3148`

## Localization review
The Spanish v2 edition was localized from the frozen English semantic source rather than from the legacy Spanish candidate.

### Terminology controls
- Surveying and Mapping Technician localized as **Técnico en Topografía y Cartografía** while official U.S. O*NET title remains visible in metadata.
- Colombia uses the official **CUOC 31122 — Técnicos en topografía** wording.
- `topógrafo/agrimensor autorizado` language preserves the distinction between technical work and jurisdiction-dependent licensed/authorized professional work.
- Technical terms such as estación total, GNSS/GPS, poligonal, cierre, georreferenciación, datum, sistema de coordenadas, replanteo, fotogrametría, ortomosaico, CAD and GIS are used consistently and naturally for a Latin American technical audience.
- English product/platform and formal foreign-program titles remain untranslated where translation could create ambiguity.

## Controlled numeric parity
The Spanish edition preserves:
- U.S. BLS May 2024 median **$51,940** and **$24.97/hour**;
- U.S. 2024 employment **59,400**;
- U.S. 2034 projected employment **62,100**;
- U.S. projected growth **5%**;
- U.S. projected annual openings **~7,600**;
- Civil 3D **23%**, AutoCAD **20%**, MicroStation **13%**;
- Canada **C$22.00 / C$29.75 / C$46.00**;
- Colombia OCUPACOL range **COP $350,000–$2,910,053** together with the mandatory non-representative-data warning;
- SENA Tecnólogo **3,984 hours**;
- SENA Técnico **2,304 hours**;
- ChileValora validity through **2028-12-30**;
- SENCICO **3 years**.

## Semantic parity controls
PASS for preservation of:
- technician-versus-professional legal boundary;
- measurement/units/control concepts;
- total-station, level and GNSS quality controls;
- CRS/datum/transformation concepts;
- traverse/closure controls;
- construction-layout revision and tolerance controls;
- field-note/raw-observation/data-lineage requirements;
- CAD/GIS/photogrammetry boundaries;
- separate drone/aviation authorization requirements;
- privacy/security controls;
- heat/traffic/utility/remote-work safety guidance;
- equipment-serviceability boundary;
- responsible-AI restrictions against invented coordinates, control points, monuments, legal boundaries or survey-grade accuracy;
- accessibility/inclusion language without weakening essential safety/professional requirements;
- U.S., Canada, Colombia, Chile, Peru and Brazil pathway content;
- portfolio, four-week plan, interview and employer-due-diligence sections;
- non-guarantee and non-certification limits.

## Source-link parity
The Spanish edition preserves the same **19 reader-verification URLs** as the frozen English source, without translated or altered destinations.

## Language-quality result
- Neutral Latin American Spanish: PASS.
- Accents/UTF-8 characters: PASS.
- Natural technical phrasing: PASS.
- No placeholder translation language: PASS.
- No claim of certified/professional translation: PASS.
- No unsupported local legal interpretation: PASS.

## Gate result
**PASS — Spanish Localization (`es-419`)**

**Blockers:** none.

Guide 93 may proceed to Brazilian Portuguese (`pt-BR`) localization.
