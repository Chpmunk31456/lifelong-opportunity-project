# Lifelong Opportunity Guide 92 — Geographic Information Systems Technician

**Version:** 2.0 controlled working master  
**Language:** English  
**Primary U.S. benchmark:** O*NET-SOC 15-1299.02 — Geographic Information Systems Technologists and Technicians  
**Canada comparison:** NOC 22214 — Technical occupations in geomatics and meteorology  
**Colombia comparison:** CUOC 31123 — Técnicos en cartografía  
**Review date:** 2026-08-22

## What this career is

A Geographic Information Systems (GIS) Technician helps collect, organize, check, analyze, map and maintain information connected to location. The work can include editing map layers, maintaining spatial databases, digitizing features, georeferencing imagery, checking geometry and attributes, producing maps and reports, supporting GIS users, running spatial analyses, automating repeatable tasks and publishing approved web maps or services.

The title overlaps with GIS Technologist, Geomatics Technician, Mapping Technician, Cartographic Technician and junior geospatial-analysis roles. Some jobs are strongly production-oriented; others involve more analysis, programming, database work or user support. Read the actual duties rather than assuming every GIS Technician job uses the same tools or has the same level of analytical responsibility.

The United States has a direct occupational profile in **O*NET-SOC 15-1299.02 — Geographic Information Systems Technologists and Technicians**. Canada maps directly to **NOC 22214 — Technical occupations in geomatics and meteorology**, which includes Geographic Information Systems (GIS) Technician. Colombia has a direct comparison in **CUOC 31123 — Técnicos en cartografía**, which explicitly includes **Técnico sistemas de información geográfica**.

## A critical U.S. statistics disclosure

O*NET explicitly states that wage and employment data for 15-1299.02 are collected from **Computer Occupations, All Other**. Those figures are official, but they are not a pure title-only GIS Technician statistical population.

That matters because a current title-specific non-government GIS Technician estimate is much lower than the O*NET crosswalked median. The correct response is not to average the two datasets together. They represent different populations, definitions and methodologies.

## What GIS technicians actually do

Current O*NET duties support work such as:
- creating and updating layers, maps, tables and reports;
- maintaining GIS databases;
- digitizing or converting features;
- checking data currency, usefulness, quality and documentation;
- assisting users and clients;
- analyzing spatial relationships;
- integrating spatial and non-spatial information;
- interpreting aerial or orthophoto imagery;
- supporting remote-sensing/cartographic workflows;
- developing scripts or GIS applications where assigned;
- publishing or supporting web GIS products;
- documenting methods and limitations.

The strongest technicians understand the data model behind the map. A visually attractive map can still be wrong if the coordinate system, source lineage, attributes, geometry or classification method is wrong.

## Spatial data models

### Vector data
Vector data represent discrete features as:
- **points** — locations such as hydrants, trees, sensors or addresses;
- **lines** — roads, streams, pipes, routes or boundaries represented as linear features;
- **polygons** — parcels, zones, lakes, service areas or administrative regions.

Each feature can have attributes stored in a table.

### Raster data
Raster data use cells/pixels and commonly represent imagery, elevation, temperature, land cover or other continuous surfaces. Resolution and cell size matter. Enlarging a low-resolution raster does not create new spatial detail.

### Attribute data
Attributes describe features. Useful skills include field types, domains/coded values, null handling, validation, joins/relates, identifiers and data dictionaries.

### Spatial databases
GIS may use file-based geodatabases, enterprise geodatabases or spatially enabled relational databases. Understand tables, keys, indexes, permissions, transactions and version/edit workflows at the level required by the role.

## Coordinate reference systems

Coordinate reference system errors can invalidate otherwise competent work.

Know the difference between:
- **geographic coordinate systems** using angular coordinates such as latitude/longitude;
- **projected coordinate systems** representing locations on a plane with linear units;
- **datum** and reference framework;
- **map projection**;
- **units**;
- **coordinate-reference identifiers** such as EPSG codes conceptually;
- **transformation/reprojection** between reference systems.

A layer appearing in the expected place on screen does not prove its CRS metadata is correct. Modern GIS software can reproject layers dynamically for display, hiding metadata mistakes.

## Projection distortion and fitness for purpose

Every map projection makes tradeoffs. Depending on the projection and extent, distortion can affect area, shape, direction or distance.

Before measuring or analyzing, ask:
- What is the intended use?
- What is the geographic extent?
- What units are required?
- Does the selected projection preserve the property that matters for this task?

Do not report precise area or distance from an unsuitable coordinate system simply because the software returns a number.

## Data lineage and metadata

A defensible GIS dataset should preserve what is known about:
- source/provenance;
- capture date or time period;
- responsible organization;
- positional accuracy;
- attribute accuracy;
- completeness;
- logical consistency;
- scale/resolution;
- CRS and datum;
- transformations;
- processing steps;
- edit history;
- authoritative versus derived status;
- known limitations.

If data are transformed, generalized, clipped, joined, classified or derived, document enough information for another person to understand how the output was produced.

## Data quality

Quality is fitness for the intended purpose, not a single universal score.

Check:
- missing or invalid attributes;
- duplicate records/features;
- impossible values;
- stale data;
- mismatched units;
- mismatched CRS;
- geometry defects;
- incomplete coverage;
- inconsistent naming/coding;
- source conflicts;
- unexpected outliers.

Do not silently “fix” authoritative source data when the correct action is to flag the issue and route it to the source owner.

## Geometry and topology

Common geometry/topology issues can include:
- self-intersections;
- duplicate features;
- invalid rings;
- overlaps;
- gaps;
- dangling lines;
- undershoots/overshoots;
- sliver polygons;
- disconnected network segments;
- snapping/tolerance problems.

Topology rules are domain-specific. Parcel polygons may require no overlaps, while habitat polygons might legitimately overlap. An automated topology tool can identify conditions; it cannot determine every business rule without requirements.

## Georeferencing

Georeferencing connects an image or scanned map to real-world coordinates.

A defensible workflow:
1. identify source imagery/map and target CRS;
2. choose reliable control points distributed appropriately;
3. select a suitable transformation;
4. review residual/error information;
5. inspect the transformed result;
6. validate against independent known references where feasible;
7. document source, method, control points and limitations.

A low residual does not automatically prove real-world positional accuracy. Poor control points can produce a mathematically tidy but wrong result.

## Digitizing and feature capture

When digitizing:
- use appropriate scale/zoom;
- follow required snapping/tolerance rules;
- capture attributes consistently;
- respect source accuracy/resolution;
- avoid false precision;
- validate geometry and attributes;
- document source and method.

Tracing a blurry source at extreme zoom does not create survey-grade accuracy.

## Cartography and communication

A professional map should have a clear purpose and audience. Consider:
- extent and scale;
- symbology;
- classification method;
- label hierarchy;
- legend;
- title/subtitle;
- source and date;
- units;
- uncertainty/limitations;
- north arrow/scale bar when useful;
- color/contrast;
- accessibility;
- supporting text or tables.

Avoid misleading visual choices. Large symbols, dramatic color ramps, inappropriate classification breaks or truncated context can exaggerate differences.

## Classification methods

Choropleth and thematic maps can change meaning depending on classification. Methods may include equal interval, quantile, natural breaks or custom domain-defined ranges.

Before choosing a method:
- inspect the distribution;
- understand whether values are counts, rates or normalized measures;
- identify outliers;
- consider the audience;
- document the classification where interpretation depends on it.

Mapping raw counts can mislead when regions have very different population or area sizes.

## Spatial analysis

GIS analysis may include:
- buffers;
- overlays/intersections;
- clipping;
- dissolve/aggregation;
- proximity/nearest feature;
- spatial joins;
- network/routing analysis;
- raster algebra;
- terrain/surface analysis;
- interpolation conceptually;
- density/hotspot methods where appropriate.

Before interpreting results, verify CRS, units, source quality, assumptions and analysis parameters. A technically successful geoprocessing job can still answer the wrong question.

## SQL and spatial databases

SQL can support attribute queries, joins, validation and spatial database operations. Depending on the platform, spatial SQL can work with geometry/geography types and spatial relationships.

Use read-only or non-production environments for practice. Do not run destructive updates against authoritative enterprise data without permission, backups/change control and a validation plan.

## Python and automation

Python, ArcPy and other scripting approaches can automate repetitive GIS work.

A repeatable workflow should preserve:
- input datasets;
- parameters;
- code/script version;
- software/environment version where relevant;
- output path/version;
- warnings/errors;
- validation/check results.

Automation can scale mistakes as easily as correct processing. Test on a controlled subset before applying a destructive or large batch change.

## Current technology signals

O*NET/Lightcast 2025 employer postings for 15-1299.02 include:
- ESRI ArcGIS software **75%**;
- GIS systems **67%**;
- Python **34%**;
- SQL **22%**;
- GIS software **21%**;
- Microsoft Office **14%**;
- Excel **14%**;
- JavaScript **13%**;
- AutoCAD **10%**;
- ArcMap **7%**;
- QGIS **7%**;
- ArcGIS Survey123 **6%**;
- Microsoft Access **6%**;
- PowerPoint **6%**;
- Azure **5%**;
- ArcPy **5%**;
- Outlook **5%**;
- AWS **5%**.

These are current posting signals, not universal requirements. Transferable concepts—CRS, quality, spatial reasoning, lineage and reproducibility—remain more durable than one software interface.

## Web GIS and sharing

Web GIS can involve hosted feature layers, tile/map services, dashboards, web maps, sharing groups and public/private permissions.

Before publishing or changing sharing:
- confirm audience;
- verify permission scope;
- inspect sensitive fields;
- verify location precision is appropriate;
- check service dependencies;
- document owner/source;
- confirm the public view does not expose protected data.

A public layer can expose sensitive locations even if the underlying database is private.

## Privacy and sensitive locations

Geospatial information can reveal:
- home/person locations;
- customer or asset locations;
- critical infrastructure;
- operational routes;
- sensitive environmental resources;
- cultural or archaeological resources;
- vulnerable populations.

Controls may include need-to-know access, approved publication, aggregation, generalization, redaction, removal of unnecessary identifiers, credential protection and incident escalation.

Do not place protected coordinates, private customer layers or critical-infrastructure details in public map services, personal cloud storage, public repositories or unapproved AI tools.

## Field and mobile data

When GIS technicians collect or manage field data, consider:
- device/account security;
- offline copies;
- sync conflicts;
- timestamps;
- GPS/position accuracy;
- form validation;
- photos/attachments;
- personal information;
- lost-device procedures;
- data retention and upload authorization.

A GPS coordinate is not automatically survey-grade. Know the accuracy requirements of the task.

## Versioning and change control

For authoritative GIS data, understand who may edit, approve or publish changes. Depending on the system, versioning, branch workflows, edit tracking or formal change tickets may apply.

Technical write access does not automatically mean authority to modify official boundaries, legal parcels, utility locations or other controlled datasets.

## Boundaries with surveying and legal records

GIS technicians may work with survey, parcel, engineering or legal-boundary data, but GIS display/editing does not itself create legal survey authority.

Do not claim survey-grade accuracy, alter legal boundaries or certify cadastral/legal records unless the required professional authority and source evidence exist. Route legal/survey interpretation to the responsible licensed or authorized professional.

## Remote sensing and imagery

Remote-sensing work can involve aerial imagery, satellite data, orthophotos, spectral bands and derived classifications.

Check:
- acquisition date;
- resolution;
- cloud/obstruction issues;
- geometric correction;
- coordinate system;
- classification method;
- ground-truth/reference evidence where needed;
- uncertainty.

Automated classification should be validated against appropriate reference data before operational conclusions are drawn.

## Responsible AI

Policy-approved AI can assist with code explanation, metadata drafts, geoprocessing ideas, geocoding review, feature-extraction assistance, classification support, documentation and synthetic practice datasets.

Controls:
- do not upload protected coordinates, customer/asset locations, proprietary layers, credentials or restricted imagery to unapproved tools;
- validate generated code and geoprocessing logic;
- verify CRS, units and spatial assumptions;
- check hallucinated function names/packages;
- assess bias/error in automated feature extraction or classification;
- preserve source lineage;
- do not let AI invent authoritative coordinates, legal boundaries or survey-grade accuracy;
- human/domain validation remains required.

AI output is not evidence that a spatial operation was executed correctly.

## Accessibility

Maps can be difficult for people who cannot perceive color, small text or dense visual layouts.

Useful practices include:
- readable font sizes;
- sufficient contrast;
- non-color-only encoding;
- clear labels/legends;
- patterns/shapes where helpful;
- descriptive context/alt text for static maps;
- text or table alternatives for key information when practical;
- keyboard-accessible web-map controls where supported;
- avoiding unnecessary animation or clutter.

Automated accessibility checks are useful but do not establish legal compliance by themselves.

## United States — education and workforce pathways

O*NET 15-1299.02 is a direct GIS occupation profile, but education requirements vary by employer. GIS jobs may be entered through geography, GIS/geospatial technology, environmental science, planning, computer/information systems, surveying/mapping or related programs depending on duties.

CareerOneStop/American Job Centers can help investigate WIOA-supported training and local resources. Eligibility and funding vary; a locator does not guarantee payment for a specific program.

## United States — official crosswalked wages and outlook

O*NET's official 2025 wage values for 15-1299.02 are collected from **Computer Occupations, All Other**:

| Percentile | Annual | Hourly |
|---|---:|---:|
| 10 | $55,940 | $26.89 |
| 25 | $79,370 | $38.16 |
| Median | $116,580 | $56.05 |
| 75 | $157,500 | $75.72 |
| 90 | $188,470 | $90.61 |

O*NET's 2024–2034 employment/outlook values are also crosswalked from that broader group:
- employment 2024: **472,000**;
- projected employment 2034: **510,500**;
- growth: **8%**;
- projected annual openings: **31,300**.

These are official but not a pure GIS Technician wage/employment series.

### Current title-specific non-government context

Indeed's current **GIS Technician** page, updated **August 2, 2026**, reports approximately:
- **$25.88/hour average**;
- **$17.60/hour low**;
- **$38.06/hour high**;
- **749** salary observations;
- prior **36 months**.

The large difference from the O*NET median reflects different populations and methodologies. Do not average these figures or imply one is the exact correction for the other. Use the official crosswalk for O*NET occupational context and the Indeed page as current title-specific, non-government market context.

## Canada

Canada Job Bank directly maps GIS Technician to **NOC 22214 — Technical occupations in geomatics and meteorology**.

National wages:
- **C$23.08/hour** low;
- **C$38.10/hour** median;
- **C$53.85/hour** high.

Typical GIS/geomatics technician preparation can include a college program in geomatics, cartography, photogrammetry, aerial survey, remote sensing, GIS or related geomatics training. Secondary school completion is required in the current Job Bank profile.

In Quebec, Job Bank notes membership in the regulatory body for professional technologists is required to use the title **Professional Technologist**. Treat this as a title/professional-status issue; do not imply that all GIS Technician work throughout Canada is identically regulated.

### Canada outlook

The current national 2024–2033 projection for NOC 22214 indicates a **strong risk of labour surplus**. Provincial/territorial three-year prospects vary and are Limited or Moderate in many locations. Readers should verify the target region rather than assume national wages imply strong demand everywhere.

## Colombia

**CUOC 31123 — Técnicos en cartografía** is a direct, competence-level-3 comparison and explicitly includes **Técnico sistemas de información geográfica**.

Functions include map design/content support, collecting information from aerial photographs and records, producing digital maps/graphics/charts, checking completeness/accuracy, interpreting aerial imagery, operating digital cartographic systems and supporting remote-sensing work.

Do not fabricate a representative national GIS Technician salary from historical labour-market indicators if the methodology does not support that claim.

## Colombia — SENA pathways

### Introducción a los Sistemas de Información Geográfica
Current SENA evidence identifies:
- complementary/special-course training;
- **80 hours**;
- in-person current listings;
- competency to operate GIS according to end-user needs.

### Sistemas de Información Geográfica
Current SENA evidence identifies:
- complementary special course;
- **48 hours**;
- current 2026 in-person listings;
- basic GIS prerequisites in some cohorts.

### Aplicación de SIG en Sistemas Forestales y Agroecológicos
Current SENA evidence identifies:
- complementary virtual training;
- **48 hours**;
- spatial data structure, capture, geospatial data management, evaluation and quality requirements for forestry/agroecological projects.

These are useful current pathways but are supplemental courses, not universal professional credentials. Verify the live cohort, centre, modality, prerequisites, dates and seats.

## Latin America and the Caribbean

OIT/Cinterfor can help identify national vocational-training institutions. It does not guarantee a specific GIS program, funding, admission or current cohort.

## Safe portfolio ideas

Use public/open, lawfully collected personal or synthetic data. Examples:
- thematic map using open data with documented CRS/source;
- georeferencing exercise using non-sensitive imagery;
- vector topology/QA project;
- spatial SQL/Python workflow on open data;
- accessible map with a text/table alternative;
- metadata and lineage record;
- synthetic asset-inspection map;
- public web-map sharing/permission exercise with non-sensitive data.

Do not publish protected employer/client layers, private personal addresses, exact critical-infrastructure locations, restricted cultural/environmental sites or proprietary database schemas.

## Four-week starter plan

### Week 1 — spatial foundations
Learn vector/raster/attributes, coordinate systems, datums, projections and basic metadata. Load open datasets and inspect their CRS and source information.

### Week 2 — editing and quality
Practice digitizing, attribute validation, geometry/topology checks, joins, georeferencing and basic cartography. Document what changed and why.

### Week 3 — analysis and automation
Practice buffers, overlays, spatial joins and one reproducible SQL/Python workflow. Verify units, CRS and analysis parameters before interpreting the output.

### Week 4 — communication and portfolio
Create a safe map/report, document sources/limitations, add an accessible text/table alternative, verify sharing permissions and prepare interview examples showing data-quality judgment.

## Interview preparation

Be ready to explain:
- vector versus raster;
- geographic versus projected CRS;
- datum and reprojection;
- why a layer displaying correctly does not prove its CRS metadata is correct;
- common topology errors;
- how you would validate a georeferencing result;
- source lineage and metadata;
- how classification choices can mislead;
- how you would protect sensitive locations;
- how you validate Python/AI-generated geoprocessing;
- why GIS output is not automatically survey-grade or legally authoritative.

## Employer due diligence

Ask:
- Which GIS platforms/databases are used?
- Is the role production mapping, analysis, data management, support or development-heavy?
- Which datasets are authoritative?
- Who approves changes to official layers?
- What CRS/datums are standard?
- What QA/topology rules apply?
- Is field data collected?
- What privacy/sensitive-location controls apply?
- Are web layers public-facing?
- Is scripting/SQL expected?
- What training support exists?
- What survey/legal boundary responsibilities are explicitly outside the role?

## Reader verification links

1. https://www.onetonline.org/link/details/15-1299.02
2. https://www.onetonline.org/link/summary/15-1299.02
3. https://www.onetonline.org/link/localwages/15-1299.02
4. https://www.onetonline.org/link/localtrends/15-1299.02
5. https://www.onetonline.org/link/demand/15-1299.02
6. https://www.indeed.com/career/gis-technician/salaries
7. https://www.careeronestop.org/LocalHelp/EmploymentAndTraining/find-WIOA-training-programs.aspx
8. https://www.jobbank.gc.ca/marketreport/summary-occupation/3493/ca
9. https://www.jobbank.gc.ca/marketreport/wages-occupation/3493/ca
10. https://www.jobbank.gc.ca/marketreport/requirements/3493/AB
11. https://www.jobbank.gc.ca/marketreport/outlook-occupation/3493/ca
12. https://www.canada.ca/en/services/jobs/training.html
13. https://ocupacol.mintrabajo.gov.co/Profile/OccupationalProfile/31123
14. https://betowa.sena.edu.co/oferta/introduccion-a-los-sistemas-de-informacion-geografica?modality=P&offertype=company&programId=85021
15. https://betowa.sena.edu.co/oferta/sistemas-de-informacion-geografica?modality=P&offertype=company&programId=164857
16. https://betowa.sena.edu.co/oferta/aplicacion-de-sig-en-sistemas-forestales-y-agroecologicos?modality=V&programId=173415
17. https://www.oitcinterfor.org/statsfp/paises
18. https://www.nist.gov/privacy-framework
19. https://www.nist.gov/itl/ai-risk-management-framework
20. https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
21. https://www.cisa.gov/secure-our-world
22. https://www.section508.gov/create/
23. https://www.w3.org/TR/WCAG22/

## Important limits

This guide provides educational and career-planning information. It does not guarantee employment, compensation, admission, funding, training availability, professional status or promotion. It does not provide legal, surveying, cadastral, privacy, cybersecurity, geospatial-accuracy or accessibility certification. The U.S. O*NET wage/employment values are explicitly crosswalked from Computer Occupations, All Other and are not represented as a pure GIS Technician statistical population. Language editions are controlled project localizations, not certified translations.
