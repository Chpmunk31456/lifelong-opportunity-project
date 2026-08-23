# Guide 84 — Spanish Localization QA 06

**Occupation:** Business Intelligence Analyst  
**Locale:** neutral Latin American Spanish (`es-419`)  
**Source:** frozen English blob `e2240bf0622c80d33dd74230a19c3b42b5ac8818`  
**Localized master:** `GUIDE_84_ANALISTA_DE_INTELIGENCIA_DE_NEGOCIOS_ES419_v2.md`  
**Review date:** 2026-08-21  
**Stage:** Spanish Localization — **PASS**

## Language and structure — PASS

The Spanish edition is a complete reader-facing localization in neutral Latin American Spanish. It contains no translator placeholders or English-only dependency for core meaning. Standard BI/IT terms such as SQL, BI, Power BI, Tableau, DAX, KPI, ETL/ELT, AWS and Azure are retained where industry usage makes that appropriate.

## Occupation parity — PASS

The edition preserves:

- O*NET-SOC **15-2051.01**;
- Canada NOC **21221**;
- Colombia CUOC **25110**;
- distinctions among BI analyst, data analyst, BI developer, analytics engineer and data scientist.

## Mandatory U.S. crosswalk disclosure — PASS

The Spanish master explicitly states that O*NET's BI wage/employment values are collected from **Data Scientists** and that the figures are not a BI-only sampled population.

It preserves the official crosswalked values:

- $67,240/$32.33; $85,660/$41.18; $120,230/$57.80; $158,880/$76.39; $199,130/$95.74;
- 245,900 → 328,300;
- 34% growth;
- 23,400 annual openings.

## BI-specific market parity — PASS

The current non-government Indeed context is preserved separately:

- $94,707/year average;
- $61,569–$145,682/year displayed range;
- approximately 1.6k salaries;
- prior 36 months;
- August 3, 2026.

It is not mixed with the official Data Scientists crosswalk series.

## Preparation/technology parity — PASS

The edition preserves Job Zone Four, 68% bachelor's / 23% master's / 5% associate preparation responses, Business Intelligence Engineer apprenticeship, and all controlled employer-posting technology percentages from SQL 35% through Salesforce 5%.

## Canada/Colombia/SENA parity — PASS

The Spanish edition preserves:

- NOC 21221 and current Canadian not-regulated status;
- C$30.67 / C$45.13 / C$62.50 per hour;
- CUOC 25110 explicit BI/Power BI/analytics titles;
- the OCUPACOL non-representativeness warning rather than using COP 800,000–7,113,801 as a representative national wage;
- SENA Técnico 2,208 hours;
- Power BI 48 hours;
- analytics-for-logistics 48 hours;
- live availability and supplemental-course boundaries.

## BI semantic parity — PASS

Equivalent reader-facing coverage is present for source of truth/lineage, grain and join risk, SQL validation, reproducibility, dimensional modeling, semantic models, KPI governance, filters/date logic, data quality, reconciliation, descriptive statistics, dashboard design, misleading-visualization avoidance and stakeholder communication.

## Integrity/privacy/security parity — PASS

The localization preserves prohibitions on silent source manipulation, unapproved KPI redefinition, hidden material filters and improper sensitive-data access. Least privilege, approved exports/sharing, credential protection and row-level access concepts remain explicit.

## AI/accessibility parity — PASS

AI-generated SQL/formulas/narratives require human validation and reconciliation. Protected data must not be placed in unapproved public AI. Accessibility content preserves readable contrast, labels, keyboard/navigation concepts, non-color-only encoding and alternatives, with no claim of legal certification.

## URL parity — PASS

The Spanish master carries the same **25 controlled external URLs** as the frozen English source.

## Assurance parity — PASS

Educational-only/no-guarantee language, no legal/accounting/privacy/security/regulatory/accessibility certification, author/AI-assistance disclosure and CC BY-NC-SA 4.0 are preserved.

## Gate decision

**PASS — Spanish Localization**

The `es-419` edition is cleared for trilingual reconciliation after Portuguese localization.

**Blockers:** none.
