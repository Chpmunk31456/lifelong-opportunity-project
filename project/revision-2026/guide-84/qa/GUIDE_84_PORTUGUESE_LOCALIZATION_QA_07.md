# Guide 84 — Portuguese Localization QA 07

**Occupation:** Business Intelligence Analyst  
**Locale:** Brazilian Portuguese (`pt-BR`)  
**Source:** frozen English blob `e2240bf0622c80d33dd74230a19c3b42b5ac8818`  
**Localized master:** `GUIDE_84_ANALISTA_DE_BUSINESS_INTELLIGENCE_PTBR_v2.md`  
**Review date:** 2026-08-21  
**Stage:** Portuguese Localization — **PASS**

## Language and structure — PASS

The Portuguese edition is a complete reader-facing Brazilian Portuguese localization with no translation placeholders or dependency on English for core meaning. Standard BI/analytics technical terms remain in industry-appropriate form.

## Occupation parity — PASS

The edition preserves O*NET-SOC **15-2051.01**, Canada NOC **21221**, Colombia CUOC **25110**, and the distinctions among BI analyst, data analyst, BI developer, analytics engineer and data scientist.

## Mandatory U.S. crosswalk disclosure — PASS

The Portuguese master explicitly states that O*NET's BI wage/employment figures are collected from **Data Scientists**, and that the official values therefore do not represent a pure BI-only sampled population.

It preserves:

- $67,240/$32.33; $85,660/$41.18; $120,230/$57.80; $158,880/$76.39; $199,130/$95.74;
- 245,900 → 328,300;
- 34% growth;
- 23,400 annual openings.

## BI-title market parity — PASS

The non-government Indeed context remains separate:

- $94,707/year average;
- $61,569–$145,682/year range;
- approximately 1.6k salaries;
- prior 36 months;
- August 3, 2026.

## Preparation/technology parity — PASS

Job Zone Four, 68% bachelor's / 23% master's / 5% associate responses, Business Intelligence Engineer apprenticeship title and all 14 controlled employer-posting percentages are preserved.

## Canada/Colombia/SENA parity — PASS

The edition preserves:

- NOC 21221, Canadian not-regulated status and C$30.67/C$45.13/C$62.50;
- CUOC 25110 explicit BI titles;
- OCUPACOL's non-representative COP 800,000–7,113,801 boundary;
- SENA 2,208-hour Técnico;
- Power BI 48-hour course;
- logistics analytics 48-hour course;
- live-availability and supplemental-training caveats.

## BI semantic parity — PASS

The edition preserves business-question-first analysis, source lineage, grain/join risk, SQL validation, reproducibility, dimensional modeling, semantic/KPI governance, filters/date logic, data quality, reconciliation, descriptive-statistics limits, dashboard design, misleading-visualization controls and stakeholder communication.

## Integrity/privacy/security parity — PASS

It retains no silent source manipulation, no unapproved KPI changes, no hidden material filters, least privilege, governed exports/sharing, credential protection and row-level access/security concepts.

## AI/accessibility parity — PASS

AI-generated SQL/calculations/narratives require human validation and reconciliation; protected data cannot be sent to unapproved public AI. Accessibility includes labels, contrast, keyboard/navigation concepts, non-color-only encoding and alternatives, without claiming automated checks prove full legal compliance.

## URL parity — PASS

The Portuguese master carries the same **25 controlled external URLs** as the frozen English source.

## Assurance parity — PASS

Educational-only/no-guarantee language, no legal/accounting/privacy/security/regulatory/accessibility certification, author/AI-assistance disclosure and CC BY-NC-SA 4.0 are preserved.

## Gate decision

**PASS — Portuguese Localization**

The `pt-BR` edition is cleared for trilingual technical QA.

**Blockers:** none.
