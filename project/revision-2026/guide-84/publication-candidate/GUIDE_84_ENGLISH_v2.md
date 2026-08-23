# Lifelong Opportunity Guide 84 — Business Intelligence Analyst

**Version:** 2.0 controlled working master  
**Language:** English  
**Primary U.S. benchmark:** O*NET-SOC 15-2051.01 — Business Intelligence Analysts  
**Canada comparison:** NOC 21221 — Business systems specialists  
**Colombia comparison:** CUOC 25110 — Analistas de sistemas  
**Review date:** 2026-08-21

## What this career is

A business intelligence (BI) analyst turns business questions into reliable metrics, reports, dashboards and decision-support information. The work usually requires understanding what decision a stakeholder is trying to make, finding the relevant data, validating definitions, querying and transforming information, building understandable outputs, checking that the result reconciles to authoritative sources, and explaining what the data does—and does not—show.

This guide uses **O*NET-SOC 15-2051.01 — Business Intelligence Analysts** as its primary United States occupation. Canada Job Bank maps the IT-oriented title **Business Intelligence Analyst - Information Technology (IT)** to **NOC 21221 — Business systems specialists**. Colombia has a direct occupational fit within **CUOC 25110 — Analistas de sistemas**, whose official denominations explicitly include **Analista de inteligencia de negocios**, **Analista de inteligencia de negocio TI**, **Analista de Power BI** and **Analista de analytics**.

BI work sits between business operations, data, technology and communication. A strong analyst is not merely a dashboard builder. The analyst should understand where a number came from, what rules produced it, whether the data is complete and current, and how a reasonable reader could misinterpret it.

## Why this can be a strong opportunity

Organizations increasingly collect data across finance, sales, marketing, operations, supply chain, customer service, HR, technology and risk. They need people who can convert those data into trustworthy information rather than simply produce more charts.

BI can provide a path from:

- business operations;
- finance or accounting support;
- reporting;
- data entry or records work;
- customer operations;
- IT support;
- database/report development;
- quality/process improvement;
- analytics or research.

A practical progression can look like:

**reporting/data support → BI analyst → senior BI analyst / analytics engineer / BI developer → analytics lead, data product, data engineering, data science, business systems or management roles.**

The exact path depends on technical depth, domain expertise, education, employer expectations and the ability to deliver reliable decision support.

## BI analyst, data analyst, BI developer, analytics engineer and data scientist are not identical roles

### Business intelligence analyst

Typically emphasizes:

- business requirements;
- KPI and metric definitions;
- SQL/querying;
- recurring reports;
- dashboards and visualization;
- trend analysis;
- stakeholder communication;
- data validation and reconciliation;
- decision support.

### Data analyst

May overlap heavily with BI but can include broader ad hoc analysis, experimentation, statistics, operational analysis or research depending on the employer.

### BI developer

Often goes deeper into:

- semantic models;
- report architecture;
- DAX/calculation layers;
- ETL/ELT integration;
- deployment and performance;
- BI platform administration.

### Analytics engineer

Often focuses on transforming raw warehouse data into documented, tested, reusable analytical models for downstream analysts and reporting tools.

### Data scientist

May use more advanced statistics, machine learning, experimentation and predictive modeling. O*NET's official BI wage and employment reference data are currently collected from **Data Scientists**, but that statistical crosswalk does not make BI analysts and data scientists the same occupation.

## The most important rule: define the business question first

A dashboard should not begin with "What chart can I make?"

Start with:

1. What decision or action is the stakeholder trying to support?
2. What business question must be answered?
3. What metric or evidence would answer it?
4. What population, time period and grain are relevant?
5. Which source is authoritative?
6. What exclusions or business rules apply?
7. How current must the data be?
8. Who is allowed to see the result?
9. How will the number be validated?
10. What limitations must be disclosed?

Good BI reduces ambiguity before it creates visuals.

## Source of truth and data lineage

Every important metric should be traceable.

Document:

- source system;
- source table/file/API;
- business owner;
- extraction timestamp or refresh schedule;
- transformation steps;
- joins and keys;
- filters/exclusions;
- calculation rules;
- output/report;
- version or change history where relevant.

A number without lineage may be difficult to defend when finance, operations, audit or leadership asks why it changed.

Do not silently replace an authoritative source with a convenient spreadsheet because the results look better.

## Relational data fundamentals

A BI analyst should understand:

- tables and rows;
- columns/fields;
- primary keys;
- foreign keys;
- one-to-one, one-to-many and many-to-many relationships;
- normalization concepts;
- duplicates;
- nulls/missing values;
- data types;
- date/time values;
- grain or level of detail.

A common analytical error is joining two tables at incompatible grains and unintentionally multiplying records.

Before joining, ask:

- What does one row represent in each table?
- Is the key unique?
- What happens to unmatched records?
- Could the join duplicate measures?

## SQL

SQL is the strongest current employer-posting signal for O*NET's BI occupation at **35%** of linked U.S. postings in 2025.

Useful SQL concepts include:

- `SELECT`;
- filtering;
- sorting;
- aggregation;
- `GROUP BY`;
- joins;
- `CASE` logic;
- common table expressions;
- subqueries;
- window functions;
- date logic;
- null handling;
- deduplication;
- query validation.

The goal is not just to make a query run. The goal is to make it return the correct population and measure.

Validate important queries by checking:

- row counts;
- duplicate keys;
- known records;
- totals against an authoritative report;
- expected date boundaries;
- missing values;
- unexpected category values;
- effect of every join and filter.

## Data cleaning and transformation

Common work includes:

- standardizing categories;
- parsing dates;
- handling missing values;
- correcting approved mapping tables;
- reshaping data;
- joining reference data;
- deriving fields;
- removing true duplicates;
- validating ranges;
- documenting transformation logic.

Do not "clean" data by deleting legitimate unusual observations just because they make a chart messy.

If a source record is wrong, follow the authorized correction process. Do not silently rewrite production source data from the reporting layer.

## Reproducibility

A trustworthy analytical result should be reproducible.

Prefer:

- saved SQL or governed queries;
- documented transformation logic;
- version-controlled scripts where appropriate;
- named data sources;
- refresh timestamps;
- controlled parameter values;
- reusable calculations;
- test cases;
- change history.

Avoid critical reports that depend on undocumented manual spreadsheet edits known only to one person.

## Dimensional modeling and star schemas

BI systems often organize analytical data into:

- **fact tables** — measurable events such as sales, orders, calls or transactions;
- **dimension tables** — descriptive context such as customer, product, location or date.

Useful concepts include:

- grain;
- surrogate keys;
- date dimensions;
- slowly changing dimensions;
- conformed dimensions;
- additive versus non-additive measures;
- star schema versus highly normalized operational design.

You do not need to be a data architect to benefit from understanding why a clean semantic model makes dashboards more reliable.

## Semantic models and calculation layers

A semantic model gives business-friendly meaning to underlying data.

It may define:

- relationships;
- measures;
- hierarchies;
- calculated columns;
- business labels;
- security roles;
- time intelligence;
- reusable KPI logic.

Centralizing a metric definition reduces the risk that five dashboards calculate "active customer" five different ways.

## KPI and metric governance

A KPI is not just a formula.

For important metrics, define:

- name;
- business purpose;
- formula;
- numerator/denominator;
- population;
- exclusions;
- time basis;
- source;
- refresh frequency;
- owner;
- target/threshold if applicable;
- known limitations.

Do not change a KPI definition because a stakeholder dislikes the result. If the business definition changes, document the owner, effective date and impact on historical comparability.

## Filters and date logic

Filters can materially alter conclusions.

Be explicit about:

- date range;
- fiscal versus calendar period;
- time zone;
- active/inactive status;
- geography;
- product/business unit;
- test/internal records;
- cancellations/returns;
- late-arriving data;
- snapshot versus transaction logic.

A dashboard should not hide a filter that changes the apparent story.

## Data quality

Common data-quality dimensions include:

- completeness;
- accuracy;
- consistency;
- validity;
- timeliness;
- uniqueness;
- integrity;
- traceability.

A field being populated does not mean it is correct.

A useful QA routine can include:

1. compare current row counts with expected ranges;
2. check duplicate business keys;
3. inspect null rates;
4. validate categories;
5. reconcile totals to an authoritative source;
6. test boundary dates;
7. sample individual records;
8. compare refresh timestamps;
9. document exceptions;
10. stop publication if a material discrepancy remains unresolved.

## Reconciliation

Before publishing a decision-critical dashboard, reconcile it.

Examples:

- BI revenue to the approved finance source;
- order counts to the operational system;
- headcount to the designated HR source;
- customer counts to the governed customer master;
- inventory to the approved inventory record.

Small differences may have legitimate causes. The analyst's job is to explain them, not conceal them.

## Descriptive statistics and trend interpretation

Useful concepts include:

- mean;
- median;
- percentiles;
- rate/ratio;
- distribution;
- variance;
- standard deviation;
- growth rate;
- moving average;
- seasonality;
- cohort comparison;
- denominator effects.

Avoid statistical overclaiming. A visible relationship between two variables does not prove that one caused the other.

## Dashboards and visualizations

A useful dashboard answers questions quickly.

Good practices include:

- clear title and purpose;
- visible reporting period;
- meaningful units;
- consistent scales;
- restrained chart variety;
- readable labels;
- useful sorting;
- clear filters;
- definitions for ambiguous metrics;
- a path to detail where appropriate.

### Common chart choices

- bar chart: category comparison;
- line chart: trend over time;
- scatter plot: relationship between two numeric measures;
- table: exact detail;
- KPI card: one clearly defined headline measure;
- histogram: distribution;
- map: only when geography is genuinely relevant and geographic interpretation is valid.

Avoid decorative charts that make comparison harder.

## Avoid misleading visualizations

Do not:

- truncate axes in ways that exaggerate small differences without clear disclosure;
- use inconsistent scales to create a desired impression;
- compare incompatible periods without explanation;
- hide missing data;
- use area/volume effects that distort magnitude;
- use color alone to encode critical meaning;
- display excessive precision unsupported by the source;
- present cumulative and period values as if they were the same thing.

Visualization is part of analytical integrity.

## Power BI, Tableau and vendor-neutral skills

O*NET's 2025 employer-posting signals include **Power BI 20%** and **Tableau 19%**.

Transferable concepts matter more than memorizing one interface:

- connecting to sources;
- relationships/modeling;
- measures/calculations;
- filters and context;
- drill-down/drill-through;
- row-level security concepts;
- refresh;
- performance;
- deployment/workspaces;
- visualization design;
- governed sharing.

A person strong in these concepts can learn additional BI platforms more efficiently.

## Current U.S. employer-posting technology signals

O*NET's nationwide 2025 Lightcast postings for 15-2051.01 show:

- SQL **35%**;
- Microsoft Power BI **20%**;
- Python **20%**;
- Tableau **19%**;
- SAP software **19%**;
- Microsoft Excel **17%**;
- R **10%**;
- AWS **9%**;
- Microsoft PowerPoint **8%**;
- Microsoft Office **8%**;
- Microsoft Azure **8%**;
- Snowflake **5%**;
- SAS **5%**;
- Salesforce **5%**.

These are market signals, not a universal checklist. A candidate does not need every tool.

## Excel and spreadsheets

Excel remains relevant at **17%** of current linked postings.

Useful capabilities include:

- structured tables;
- formulas;
- lookup concepts;
- pivot tables;
- data validation;
- charts;
- Power Query concepts;
- reconciliation;
- controlled imports/exports.

Spreadsheets become risky when they act as undocumented databases or contain critical hidden manual logic. Use them deliberately.

## Python and R

O*NET posting signals include **Python 20%** and **R 10%**.

They can help with:

- data cleaning;
- repeatable analysis;
- API/file processing;
- statistical work;
- automation;
- validation;
- visualization.

Many BI roles do not require advanced programming. Learn coding in proportion to the target role.

## Cloud and modern data platforms

Current signals include AWS **9%**, Azure **8%** and Snowflake **5%**.

Useful concepts include:

- cloud storage/warehouse basics;
- identity and access;
- compute/query separation;
- scheduled pipelines;
- data refresh;
- cost awareness;
- governed sharing;
- logs/monitoring;
- secrets management.

A BI analyst should understand enough architecture to use data safely without pretending to be the cloud or security architect.

## Requirements and stakeholder communication

BI work often fails because the technical output answers a different question than the stakeholder intended.

Clarify:

- desired decision;
- audience;
- definitions;
- required frequency;
- latency tolerance;
- detail level;
- security scope;
- export needs;
- success criteria;
- acceptance testing.

Use examples and mockups when requirements are ambiguous.

## Analytical storytelling without distortion

A BI analyst may explain findings and recommend next steps, but should separate:

- observed facts;
- calculated metrics;
- assumptions;
- interpretation;
- recommendation.

Use language such as:

- "The data show..."
- "This calculation assumes..."
- "A possible explanation is..."
- "The data do not establish causation..."
- "This result excludes..."

Clarity builds trust.

## Privacy and confidential data

BI can expose sensitive information even when a dashboard seems harmless.

Follow approved rules for:

- customer data;
- employee data;
- financial data;
- health or other regulated data;
- commercially sensitive data;
- confidential contracts/pricing;
- identifiers;
- row-level access.

Good practice includes:

- least privilege;
- approved data sources;
- controlled exports;
- secure storage;
- approved sharing;
- masking/aggregation where required;
- retention/deletion rules;
- incident reporting.

A technical ability to query a table does not prove authorization to use every field.

## Cybersecurity in BI work

Practical controls include:

- protect credentials and tokens;
- use MFA where required;
- never embed secrets in shared reports or public repositories;
- restrict service-account permissions;
- use approved connectors;
- report unexpected access or data exposure;
- validate unusual bulk-export requests;
- do not bypass row-level security;
- avoid copying production data into unmanaged personal tools.

NIST Cybersecurity Framework and Privacy Framework can provide governance context. Employer policy and applicable law remain controlling.

## Responsible AI and automation

AI can assist with:

- drafting SQL;
- explaining query logic;
- suggesting DAX/formulas;
- creating test cases;
- summarizing non-sensitive findings;
- drafting dashboard documentation;
- generating synthetic training examples.

Controls:

- use only approved systems and data classes;
- do not put confidential data, credentials or protected extracts into unapproved public AI services;
- validate AI-generated SQL before execution;
- validate calculations and formulas;
- reconcile results to authoritative data;
- distinguish generated narrative from observed evidence;
- check unsupported causal claims;
- review systematic error and bias;
- require human approval before publishing decision-critical output where policy requires it.

NIST's AI Risk Management Framework and Generative AI Profile are voluntary risk-management guidance. They do not replace organizational data governance.

## Accessibility and inclusive BI

Accessible BI benefits more users, not only people who identify as disabled.

Useful practices include:

- readable contrast;
- adequate text size;
- meaningful chart titles;
- descriptive labels;
- keyboard access where the platform supports it;
- logical navigation/order;
- avoid color-only distinctions;
- text/table alternatives for critical information where practical;
- meaningful alt text for exported graphics/documents where appropriate;
- concise language and understandable units.

Automated accessibility checking does not prove complete legal conformance. WCAG 2.2 and Section 508 resources can provide design/testing context where applicable.

## Ethical portfolio projects

Use public, synthetic or explicitly authorized data.

Portfolio ideas:

- sales dashboard from synthetic transaction data;
- customer-support dashboard using invented ticket data;
- inventory KPI model;
- finance-style reconciliation exercise using synthetic accounts;
- SQL analysis with documented tests;
- star-schema design;
- Power BI/Tableau dashboard with an accessibility checklist;
- dashboard correction case showing how a bad join duplicated revenue;
- data-quality report showing missing/duplicate values;
- metric dictionary and source-lineage document.

Do not publish employer data, customer records or confidential screenshots without authorization.

## United States pathway

O*NET places BI analysts in **Job Zone Four — Considerable Preparation Needed**.

Current education responses for new hires are:

- **68% bachelor's degree**;
- **23% master's degree**;
- **5% associate degree**.

These are preparation patterns rather than universal legal requirements. A candidate with strong domain experience, technical skill and a convincing portfolio may encounter employers with different requirements.

O*NET lists **Business Intelligence Engineer** as an approved example Registered Apprenticeship title. An approved title does not guarantee an open local apprenticeship.

CareerOneStop can help identify WIOA-eligible and other training programs. Eligibility, funding and employer recognition must be confirmed directly.

## United States wages and outlook — important crosswalk disclosure

O*NET explicitly states that its wage and employment data for **Business Intelligence Analysts** are collected from **Data Scientists**.

Therefore, the following figures are official BLS/O*NET reference data for the mapped series, **not a BI-only sampled wage/employment population**.

### BLS 2025 national wage series used by O*NET

| Percentile | Annual | Hourly |
|---|---:|---:|
| 10th | $67,240 | $32.33 |
| 25th | $85,660 | $41.18 |
| Median | $120,230 | $57.80 |
| 75th | $158,880 | $76.39 |
| 90th | $199,130 | $95.74 |

### 2024–2034 employment projections used by O*NET

- employment 2024: **245,900**;
- projected employment 2034: **328,300**;
- projected growth: **34%**, much faster than average;
- projected **annual openings: 23,400**.

Do not convert annual openings into a guaranteed ten-year total or imply that each opening is specifically titled "Business Intelligence Analyst."

### Current BI-title-specific non-government context

Indeed reported an average base salary of **$94,707/year** for **Business Intelligence Analyst** in the United States, with a displayed range of **$61,569–$145,682/year**, based on approximately **1.6k salaries** from job postings in the prior 36 months, updated **August 3, 2026**.

This is a current non-government BI-title estimate. It is useful because it is more title-specific, but it is not a substitute for official statistics and should not be mixed with the O*NET/Data Scientists series as if both measured the same population.

## Canada pathway

Canada Job Bank maps the IT-oriented title **Business Intelligence Analyst - Information Technology (IT)** to **NOC 21221 — Business systems specialists**.

Current typical requirements state:

- a bachelor's degree in computer science, business administration, information systems or a related discipline **or** completion of a college computer-science program is usually required;
- vendor certification/training may be required by some employers;
- according to current Job Bank records, the occupation is **not regulated in Canada**.

Current national wages, updated November 19, 2025:

- low: **C$30.67/hour**;
- median: **C$45.13/hour**;
- high: **C$62.50/hour**.

The NOC scope is broader than BI-only reporting, so treat this as a Canadian occupational comparison. Regional prospects vary by province/territory.

## Colombia pathway

### CUOC 25110 — Analistas de sistemas

OCUPACOL explicitly includes:

- Analista de analytics;
- Analista de inteligencia de negocio TI;
- **Analista de inteligencia de negocios**;
- Analista de Power BI;
- Analista de información comercial;
- Analista de procesamiento de información;
- Analista informático para análisis de negocio;
- Especialista en inteligencia comercial.

Relevant official functions include requirements analysis, business-process analysis, functional specifications, testing, integrating data using visualization/analysis methodologies, systematizing large data using analytics tools, and managing organizational data representations.

OCUPACOL displays a historical/derived salary range of **COP 800,000–7,113,801**, but explicitly states that the figures **do not have statistical representativeness** under the applied methodology. This guide does **not** use that range as a representative current Colombian BI wage benchmark.

### SENA — Programación para analítica de datos

SENA Betowa lists **Programación para analítica de datos** as:

- **Técnico**;
- **2,208 hours**;
- titulada training;
- data processing, statistical methodology and data visualization/analysis competencies.

The page may show no open cohorts at a given moment. Verify current intake and location.

### SENA — Visualización de datos usando Power BI

SENA Betowa lists **Visualización de datos usando Power BI** as:

- complementary/special course;
- **48 hours**;
- current 2026 offerings in some locations/modalities;
- basic office-tool knowledge expected, with database/statistics foundations recommended.

This is a focused skills course, not a complete BI professional qualification.

### SENA — Analítica de datos para procesos logísticos

SENA Betowa lists **Analítica de datos para procesos logísticos** as:

- complementary virtual training;
- **48 hours**;
- data storage/treatment, querying, homogenization and analytics presentation.

It is a useful domain-specific supplement, not a universal BI credential.

## Broader Latin America pathway

Training systems vary by country. ILO/Cinterfor's country resources can help locate national vocational-training institutions. Verify program status, cost, modality, admission and employer recognition directly.

## Resume evidence

Strong BI resume bullets show business impact and evidence, for example:

- reconciled executive dashboard metrics to the governed finance source;
- reduced recurring manual reporting by automating a validated data pipeline;
- defined KPI logic with business owners and documented lineage;
- identified a join defect that overstated transaction totals;
- built role-restricted dashboards for different stakeholder groups;
- improved data-quality monitoring for missing and duplicate records.

Use only supportable facts. Do not invent revenue impact, user counts, certifications or tool experience.

## Interview preparation

Be ready to explain:

- how you turn a vague request into a metric definition;
- how you validate a SQL query;
- the risk of many-to-many joins;
- difference between fact and dimension tables;
- how you reconcile a dashboard to a source system;
- how you handle conflicting KPI definitions;
- how you choose a chart;
- how you prevent misleading interpretation;
- how you protect sensitive data;
- how you validate AI-generated SQL or narrative;
- what you do when a result contradicts stakeholder expectations.

A good analyst explains method and limitations, not just tools.

## Questions to ask an employer

Ask about:

- authoritative data platforms;
- BI/reporting tools;
- warehouse/lakehouse architecture;
- metric ownership/governance;
- data-quality process;
- deployment/review standards;
- access/security model;
- analyst versus engineering responsibilities;
- expected SQL depth;
- statistics/experimentation expectations;
- AI-tool policy;
- documentation/version control;
- training/certification support;
- accessibility standards.

## First 30 days in a BI role

Priorities:

1. learn the business model and major decisions;
2. identify authoritative systems and owners;
3. learn metric definitions;
4. understand refresh schedules and data latency;
5. learn access/security rules;
6. review recurring dashboards and known reconciliation issues;
7. learn deployment/review process;
8. understand stakeholder expectations;
9. document lineage and assumptions as you learn;
10. avoid changing production KPI logic without approval.

## 90-day progression plan

Aim to be able to:

- independently clarify common BI requirements;
- write and validate reliable SQL;
- explain source lineage;
- build or maintain governed metrics;
- reconcile dashboards;
- identify data-quality issues;
- communicate limitations clearly;
- produce accessible, decision-focused visuals;
- handle sensitive data correctly;
- use AI/automation under approved controls;
- identify your next path: senior BI, analytics engineering, data engineering, data science, systems or leadership.

## Pre-application checklist

Confirm that you can discuss:

- business question and KPI definition;
- SQL joins/aggregation;
- grain and duplicate risk;
- data cleaning/transformation;
- star-schema basics;
- reconciliation;
- dashboard design;
- descriptive statistics;
- misleading-visualization risks;
- privacy/access control;
- responsible AI;
- a portfolio project with documented source and validation.

## Questions before buying training

Ask:

- Does the program teach SQL with hands-on exercises?
- Does it cover data modeling and not only dashboard clicking?
- Are data-quality and reconciliation included?
- Which BI platforms are used?
- Is there a portfolio/capstone with public or synthetic data?
- Are instructors and outcomes verifiable?
- What is the total cost including exams/software?
- Is funding available and what are the eligibility rules?
- What accessibility accommodations are offered?
- Does the credential match target employer requirements?

Do not rely on guaranteed-job or guaranteed-income claims.

## Controlled sources

1. https://www.onetonline.org/link/details/15-2051.01
2. https://www.onetonline.org/link/summary/15-2051.01
3. https://www.onetonline.org/link/localwages/15-2051.01
4. https://www.onetonline.org/link/localtrends/15-2051.01
5. https://www.onetonline.org/link/hot_tech/15-2051.01
6. https://www.onetonline.org/link/demand/15-2051.01
7. https://www.careeronestop.org/LocalHelp/EmploymentAndTraining/find-WIOA-training-programs.aspx
8. https://www.careeronestop.org/FindTraining/find-training.aspx
9. https://www.indeed.com/career/business-intelligence-analyst/salaries
10. https://www.jobbank.gc.ca/marketreport/summary-occupation/296881/ca
11. https://www.jobbank.gc.ca/marketreport/requirements/296881/ca
12. https://www.jobbank.gc.ca/marketreport/wages-occupation/296881/ca
13. https://www.canada.ca/en/services/jobs/training.html
14. https://ocupacol.mintrabajo.gov.co/Profile/OccupationalProfile/25110
15. https://betowa.sena.edu.co/oferta/programacion-para-analitica-de-datos?location=57054001&modality=P&programId=133094
16. https://betowa.sena.edu.co/oferta/visualizacion-de-datos-usando-power-bi?modality=V&offertype=company&programId=160058
17. https://betowa.sena.edu.co/oferta/analitica-de-datos-para-procesos-logisticos?modality=V&offertype=company
18. https://www.oitcinterfor.org/statsfp/paises
19. https://www.cisa.gov/secure-our-world
20. https://www.nist.gov/cyberframework
21. https://www.nist.gov/privacy-framework
22. https://www.nist.gov/itl/ai-risk-management-framework
23. https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
24. https://www.section508.gov/create/
25. https://www.w3.org/TR/WCAG22/

## Assurance and no-guarantee notice

This guide provides educational and career-planning information. It does not guarantee employment, income, admission, funding, certification, licensing, promotion or any other result. Requirements, compensation and opportunities vary by jurisdiction, employer and time.

It does not provide legal, accounting, privacy, cybersecurity, regulatory or accessibility certification. Follow applicable law, employer policy, approved metric/data governance and assigned authority.

Created and directed by **Alberto “Al” Leiva**. ChatGPT supported research, organization, editing, translation support and document preparation under the author's direction. The author remains responsible for editorial and publication decisions.

Unless a file states otherwise, these materials are licensed under **CC BY-NC-SA 4.0**.
