# Lifelong Opportunity Guide 85 — Data Analyst

**Version:** 2.0 controlled working master  
**Language:** English  
**Primary U.S. quantitative benchmark:** O*NET-SOC 15-2041.00 — Statisticians  
**Adjacent U.S. benchmark:** O*NET-SOC 15-2051.01 — Business Intelligence Analysts  
**Canada comparison:** NOC 21223 — Database analysts and data administrators  
**Colombia comparisons:** CUOC 25210, CUOC 25110, and CUOC 21200, selected by job function  
**Review date:** 2026-08-21

## What this career is

A data analyst turns questions into evidence. The work usually involves locating relevant data, understanding what each field and row means, cleaning and validating the information, analyzing patterns, testing assumptions, creating understandable tables or visualizations, and explaining what the data does and does not support.

The title **Data Analyst** is unusually broad. Some roles are close to business intelligence and reporting. Others are closer to database work, operations research, statistics, finance, marketing analytics, quality, fraud analysis, public policy, health analytics, cybersecurity analytics, supply chain, research, or product analytics. For that reason, this guide does not pretend that one official occupation code perfectly represents every Data Analyst job.

For controlled labour-market comparisons, this guide uses **O*NET-SOC 15-2041.00 — Statisticians** as the primary United States quantitative benchmark because its official duties directly include data preparation, statistical analysis, trend identification, report preparation and data-quality evaluation, and because O*NET explicitly lists approved apprenticeship titles including Data Analyst and Junior Data Analyst. However, the Statisticians benchmark is more mathematically advanced and graduate-heavy than many commercial entry-level Data Analyst positions. That limitation must remain visible whenever official wage, education or outlook data are presented.

Guide 84 covers Business Intelligence Analyst in more depth. The two careers overlap, but they are not interchangeable.

## Why data analysis can be a strong opportunity

Organizations collect data in almost every function, including:

- sales;
- customer service;
- marketing;
- finance;
- accounting;
- operations;
- logistics;
- supply chain;
- quality;
- healthcare;
- education;
- government;
- cybersecurity;
- human resources;
- manufacturing;
- transportation;
- nonprofit programs;
- scientific and social research.

Data creates value only when someone can convert it into trustworthy information. A capable analyst therefore combines technical skills with judgment, documentation and communication.

People may enter data analysis from:

- reporting or spreadsheet-heavy administrative work;
- business operations;
- finance or accounting support;
- customer operations;
- IT support;
- database or records work;
- quality assurance;
- marketing;
- logistics;
- research assistance;
- engineering or technical support;
- statistics or mathematics;
- programming or software support.

A possible progression is:

**data/reporting assistant → junior data analyst → data analyst → senior analyst → analytics lead, BI analyst, analytics engineer, data engineer, data scientist, product analyst, operations analyst, risk analyst or management role.**

The exact path depends on technical depth, domain expertise, education, employer expectations and demonstrated ability to produce reliable analysis.

## Data Analyst is not one single job

### Reporting-oriented analyst

May focus on:

- recurring reports;
- spreadsheets;
- KPI tracking;
- dashboards;
- simple SQL;
- reconciliation;
- operational summaries.

### Business or operations analyst with data emphasis

May focus on:

- process metrics;
- root-cause investigation;
- cost or productivity analysis;
- service levels;
- forecasting support;
- stakeholder recommendations.

### Statistical or research analyst

May use:

- sampling;
- probability;
- statistical inference;
- regression;
- experimental or survey methods;
- R, Python, SAS or SPSS;
- formal research documentation.

### Database/data-management-oriented analyst

May work more deeply with:

- data models;
- database structures;
- SQL;
- warehouses;
- data quality;
- data governance;
- data dictionaries;
- access controls.

### Product, marketing, finance, risk or cybersecurity analyst

Uses the same analytical principles inside a specialized domain. Domain knowledge may be as important as the toolset.

Always read the actual job description rather than assuming the title tells you the full technical level.

## The first rule: define the question before touching the data

Weak analysis often starts with a dataset and asks, “What can I find?” Strong analysis starts with a decision or question.

Before building a query, formula or chart, clarify:

1. What question are we trying to answer?
2. What decision will this analysis support?
3. Who is the audience?
4. What population or process is in scope?
5. What time period matters?
6. What does one row represent?
7. Which data source is authoritative?
8. Which business rules, filters and exclusions apply?
9. What level of accuracy is required?
10. What uncertainty or limitation should be disclosed?
11. Who is allowed to access the data and result?
12. How will the output be validated?

If the question is vague, write down a testable version before continuing.

## Data source, lineage and grain

Every important result should be traceable to its source.

Document, where applicable:

- source system;
- table, file, API or report;
- extraction date/time;
- owner or steward;
- refresh frequency;
- field definitions;
- row grain;
- transformations;
- joins;
- filters;
- exclusions;
- derived fields;
- calculation rules;
- output version;
- corrections or change history.

### Grain

Grain means what one row represents.

One row might represent:

- one customer;
- one order;
- one order line;
- one support case;
- one employee-month;
- one machine reading;
- one payment;
- one survey response.

Joining tables at incompatible grains can multiply rows and inflate totals. Before every important join, ask:

- Is the key unique?
- Is this one-to-one, one-to-many or many-to-many?
- What happens to unmatched rows?
- Can the join duplicate measures?
- Should I aggregate before joining?

## Spreadsheet skills

Spreadsheets remain common in analyst jobs. Useful skills include:

- sorting and filtering;
- tables;
- relative and absolute references;
- `SUM`, `AVERAGE`, `COUNT`, `COUNTIF(S)`, `SUMIF(S)`;
- lookup functions;
- text and date functions;
- logical functions;
- pivot tables;
- charts;
- conditional formatting;
- data validation;
- import/export;
- error checking;
- protected ranges and access discipline;
- Power Query or equivalent transformation tools where available.

A spreadsheet is not automatically a reliable analytical system. Important work should avoid undocumented manual changes, hidden formulas, hard-coded totals, unexplained copied values and uncontrolled versions.

## SQL

SQL is one of the most transferable analyst skills.

Core concepts include:

- `SELECT`;
- `WHERE` filtering;
- sorting;
- aggregation;
- `GROUP BY`;
- joins;
- `CASE` logic;
- common table expressions;
- subqueries;
- window functions;
- date/time logic;
- null handling;
- deduplication;
- row-count validation.

A query is not correct merely because it runs.

Validate important queries by checking:

- expected row counts;
- duplicate keys;
- known sample records;
- totals against an authoritative report;
- date boundaries;
- nulls and missing categories;
- join effects;
- filters and exclusions;
- unit conversions;
- unexpected values.

## Python, R and statistical tools

Some analyst roles use programming for reproducible analysis. Current O*NET posting signals for the Statisticians benchmark show strong demand for R, SAS, Python and SQL, although the benchmark is more statistical than many general Data Analyst roles.

Useful capabilities may include:

- importing data;
- cleaning and reshaping;
- grouping and aggregating;
- joining datasets;
- descriptive statistics;
- visualization;
- reproducible notebooks or scripts;
- simple statistical tests;
- validation;
- export of controlled results.

Do not chase every language at once. A practical progression for many learners is:

1. spreadsheet fundamentals;
2. SQL;
3. visualization;
4. one scripting language such as Python or R;
5. deeper statistics as role requirements increase.

## Data cleaning

Common cleaning tasks include:

- standardizing categories;
- correcting approved mappings;
- parsing dates;
- converting data types;
- handling missing values;
- identifying duplicate records;
- resolving inconsistent identifiers;
- trimming whitespace;
- validating ranges;
- reconciling source totals;
- documenting transformations.

Cleaning should never mean changing legitimate records until the output tells a preferred story.

If source data appears wrong, follow the authorized correction process. Preserve the distinction between the original source, the corrected source and analytical transformations.

## Missing data

Missing values can have different meanings:

- truly unknown;
- not applicable;
- not collected;
- not yet available;
- suppressed for privacy;
- failed data transfer;
- user skipped field;
- system default.

Never assume missing means zero.

Before filling, excluding or imputing missing data, document the reason and assess whether the treatment could bias the result.

## Duplicates

A duplicate is not simply “two rows that look similar.” Two transactions may legitimately have the same customer, amount and date.

A defensible duplicate rule should identify:

- the expected unique key;
- the business event represented;
- which fields determine uniqueness;
- whether multiple records are valid;
- the correction process if duplicates are confirmed.

## Descriptive statistics

Useful fundamentals include:

- count;
- sum;
- mean;
- median;
- minimum;
- maximum;
- percentiles;
- proportions;
- rates;
- variance;
- standard deviation;
- distributions;
- frequency tables.

### Mean versus median

The mean can be heavily influenced by extreme values. The median is often more representative for skewed distributions such as wages, property values or response times.

Use the statistic that fits the question and explain it clearly.

## Outliers

Outliers may indicate:

- true unusual events;
- data-entry errors;
- fraud;
- equipment problems;
- rare but important customers;
- process breakdowns;
- valid extreme outcomes.

Do not remove them solely because they make a chart or model less convenient.

A defensible workflow is:

1. identify the outlier rule;
2. inspect source records;
3. determine whether the value is valid;
4. document any exclusion or correction;
5. compare results with and without the observation when useful;
6. disclose material sensitivity.

## Sampling and selection bias

A dataset can be large and still misleading.

Ask:

- Who had a chance to be included?
- Who is missing?
- Is participation voluntary?
- Does the sample overrepresent certain locations, customers, devices or time periods?
- Did a policy or system change affect who appears in the data?
- Are only successful cases recorded?
- Is there survivorship bias?

More rows do not automatically remove bias.

## Correlation is not causation

Two variables moving together does not prove one caused the other.

A relationship may arise from:

- coincidence;
- a third variable;
- reverse causality;
- selection bias;
- time trends;
- measurement differences.

Use causal language only when the study design and evidence support it. Otherwise use wording such as **associated with**, **correlated with**, **higher among**, or **observed alongside**.

## Confidence and uncertainty

Entry-level analysts do not need to become statisticians immediately, but they should understand that estimates have uncertainty.

Important concepts include:

- sample size;
- variability;
- confidence intervals;
- margin of error;
- statistical versus practical significance;
- model uncertainty;
- forecast error;
- sensitivity to assumptions.

Do not turn a point estimate into false certainty.

## Data visualization

A good chart should make the intended comparison easier, not manipulate the reader.

Useful practices:

- use clear titles;
- label units;
- show relevant date ranges;
- use readable text;
- avoid unnecessary decoration;
- use a zero baseline for bar charts when magnitude comparison depends on bar length;
- disclose broken axes when justified;
- avoid 3D effects that distort size;
- keep category ordering meaningful;
- provide data labels or tables when exact values matter;
- use accessible contrast and patterns;
- include alt text or an accessible text summary when required by the publishing context.

### Avoid misleading charts

Do not:

- truncate axes to exaggerate differences without explanation;
- compare totals from populations of very different sizes when rates are needed;
- cherry-pick date ranges;
- hide categories that weaken the preferred story;
- use inconsistent scales across similar charts;
- imply causation from a visual association.

## Data quality

Common quality dimensions include:

- accuracy;
- completeness;
- consistency;
- timeliness;
- validity;
- uniqueness;
- integrity.

Data quality should be evaluated against the intended use. A field that is adequate for an internal operational count may not be adequate for a regulatory, financial, clinical or public claim.

## Validation and reconciliation

Before publishing an important result:

- compare totals to an authoritative source;
- verify sample records;
- inspect missing and duplicate patterns;
- confirm date boundaries;
- check denominators;
- test edge cases;
- review units and currency;
- verify filters;
- inspect join cardinality;
- compare trends with known events;
- have another qualified reviewer check high-impact logic when the organization requires it.

If the result does not reconcile, investigate before presenting it as final.

## Documentation and reproducibility

A strong analyst leaves a trail another competent person can follow.

Document:

- purpose;
- owner;
- source;
- refresh date;
- definitions;
- logic;
- queries or formulas;
- exclusions;
- assumptions;
- limitations;
- version;
- validation performed;
- correction history.

Where appropriate, use:

- version control;
- saved SQL;
- reusable scripts;
- notebooks;
- data dictionaries;
- metric definitions;
- controlled report repositories;
- change logs.

## Communicating results

A useful analytical summary should answer:

1. What did we analyze?
2. What did we find?
3. How large is the effect or difference?
4. What evidence supports it?
5. What are the limitations?
6. What decision or next step is supported?

Avoid jargon when a plain-language explanation works.

Separate:

- observed facts;
- calculations;
- assumptions;
- interpretations;
- forecasts;
- recommendations.

## Privacy, security and access control

Analysts may work with customer, employee, financial, operational, health, location, authentication, device or business-confidential data.

Practical controls include:

- use employer-approved systems;
- follow least-privilege access;
- do not copy protected datasets into personal storage;
- do not send extracts to personal email;
- do not bypass access controls to “get the job done”;
- use approved encrypted storage and transfer methods;
- minimize data collection;
- remove fields that are not needed;
- respect retention and deletion rules;
- verify recipients before sharing extracts;
- report suspected exposure or unauthorized access;
- use MFA and approved password practices;
- follow organizational policy for exports, screenshots and local files.

An analyst should not invent legal or security policy. Follow the organization’s approved governance and escalate uncertainty.

## Responsible AI and automation

AI can assist with low-risk analytical work when organizational policy allows it.

Possible uses include:

- explaining a formula;
- drafting SQL, Python or R;
- suggesting exploratory questions;
- generating synthetic test data;
- drafting documentation;
- summarizing non-sensitive public information;
- proposing chart alternatives;
- checking code style.

Human validation remains required.

Do not:

- upload confidential data, credentials, private contracts, regulated records or protected extracts to an unapproved AI tool;
- assume AI-generated SQL or code is correct;
- publish an AI-written interpretation without checking the underlying calculations;
- accept invented fields, definitions or source citations;
- let AI choose exclusions that materially alter results without documented human review;
- treat AI output as evidence;
- present AI predictions as observed fact;
- allow autonomous publication of decision-critical analytics outside approved governance.

A practical rule is: **AI may help draft, explain or test; authoritative data, approved logic and accountable human review determine the final result.**

NIST’s AI Risk Management Framework and Generative AI Profile provide voluntary risk-management guidance. They do not replace organizational governance or professional responsibilities.

## Ethical boundaries

A Data Analyst should not:

- alter source data to produce a preferred conclusion;
- hide filters or exclusions;
- remove valid outliers because they weaken the story;
- choose a denominator after seeing which result looks best;
- present correlation as causation;
- fabricate data, records, citations, findings or samples;
- suppress material limitations;
- bypass access controls;
- publish protected or confidential information outside authorization;
- claim statistical certainty unsupported by the method;
- present accounting, legal, clinical, regulatory or engineering conclusions outside assigned expertise;
- manipulate a visualization to mislead;
- represent a forecast or model as guaranteed.

Good analysis is traceable, reproducible, transparent about uncertainty and open to correction.

## Accessibility and inclusive data communication

Accessible analysis improves usability for everyone.

Useful practices include:

- descriptive chart titles;
- meaningful axis labels;
- sufficient contrast;
- not relying on color alone;
- patterns or direct labels where appropriate;
- readable font sizes;
- accessible tables;
- alt text or text summaries for important graphics;
- logical reading order in documents;
- plain-language explanation of important findings;
- keyboard-accessible dashboards when the platform supports them;
- testing with built-in accessibility tools where available.

Accessibility standards and legal obligations vary by jurisdiction and context. This guide does not certify a dashboard, report or system as legally accessible.

## Education and entry pathways — United States

The official Statisticians benchmark is graduate-heavy: O*NET reports that many new hires in that occupation hold master’s degrees. That should **not** be interpreted as a universal requirement for every Data Analyst job.

Commercial and operational Data Analyst roles may accept combinations of:

- bachelor’s degree;
- associate degree;
- technical certificate;
- employer training;
- apprenticeship;
- relevant work experience;
- portfolio evidence;
- strong spreadsheet/SQL/reporting skills;
- domain expertise.

Common study areas include:

- statistics;
- mathematics;
- data analytics;
- computer science;
- information systems;
- business;
- economics;
- finance;
- engineering;
- social science;
- health or other domain-specific fields.

### U.S. free/low-cost and funding locators

CareerOneStop can help readers locate:

- American Job Centers;
- WIOA-eligible training programs;
- local training services;
- career information.

WIOA eligibility and funding are not automatic. An American Job Center can explain local eligibility, approved providers and supportive services.

Search more broadly than “Data Analyst.” Relevant programs may appear under:

- data analytics;
- statistics;
- business analytics;
- computer information systems;
- database technology;
- business intelligence;
- programming;
- Excel/SQL;
- digital skills.

### Apprenticeship and work-based learning

O*NET’s Statisticians profile links approved apprenticeship titles including **Data Analyst**, **Data Analyst (Nof)** and **Junior Data Analyst**.

Availability varies by location and employer. Readers should verify live opportunities through Apprenticeship.gov and local workforce systems.

Other work-based-learning routes may include:

- paid internships;
- analyst trainee roles;
- reporting assistant jobs;
- employer-sponsored upskilling;
- project assignments using authorized internal data;
- supervised research or operations work.

## Canada

Canada Job Bank maps **Data Analyst - Informatics and Systems** to **NOC 21223 — Database analysts and data administrators**. This is a useful comparison but is more data-management oriented than many general analytical roles.

Current Job Bank requirements indicate that a university degree or college program, usually in computer science, computer engineering or mathematics, is commonly required, along with programming or related experience. Job Bank currently identifies this occupation as not regulated nationally, although employer requirements still vary.

### Canada wage benchmark

Current Job Bank national wages, updated November 19, 2025, show approximately:

- **C$25.00/hour low**;
- **C$40.87/hour median**;
- **C$61.03/hour high**.

These values are for NOC 21223, not every possible Data Analyst title.

### Canada training and funding supports

Canada.ca provides national links to:

- student aid;
- skills training;
- employment services;
- provincial/territorial training programs;
- short-term recognized training opportunities;
- Employment Insurance and training information where applicable.

Eligibility, funding and program design vary by province, territory and individual circumstances.

## Colombia

A generic **Analista de datos** title spans multiple CUOC groups. This guide uses function-based comparisons rather than claiming one exclusive Colombian code.

### CUOC 25210 — Diseñadores y administradores de bases de datos

Relevant when the job emphasizes:

- database structures;
- data architecture;
- warehouses;
- data administration;
- data quality;
- cleaning/extraction/transformation;
- visualization and communication;
- database security and integrity.

The official group includes the title **Analista de datos comerciales**.

### CUOC 25110 — Analistas de sistemas

Relevant to analytics and BI-oriented roles. Official denominations include:

- Analista de analytics;
- Analista de inteligencia de negocios;
- Analista de Power BI;
- Analista de información comercial;
- Analista de procesamiento de información.

### CUOC 21200 — Matemáticos, actuarios y estadísticos

Relevant when the work is strongly statistical or research-oriented. It includes **Analista estadístico**.

OCUPACOL warns that occupation-level market indicators shown on its profiles do not have statistical representativeness under the applied methodology. This guide therefore does not present those profile ranges as a representative national Data Analyst salary.

### SENA pathways

SENA Betowa currently lists pathways relevant to data analysis, including:

**Programación para analítica de datos**  
- Técnico;
- 2,208 hours;
- titulada training;
- data processing, integration, visualization and analysis competencies.

**Visualización de datos usando Power BI**  
- complementary/special course;
- 48 hours;
- useful as focused supplemental training rather than a complete professional qualification.

**Analítica de datos para procesos logísticos**  
- complementary virtual training;
- 48 hours;
- domain-specific analytics content.

Program availability, city, modality, cohorts, seats, admission requirements and dates can change. Verify live Betowa listings before applying.

## Latin America and the Caribbean

ILO/Cinterfor provides a regional network and country-level vocational-training locator. It can help readers identify national training institutions and compare skills systems across Latin America and the Caribbean.

It is a locator and knowledge network, not a guarantee that a specific Data Analyst course, scholarship or funding award is available in every country.

Readers should verify the current catalogue, eligibility, cost, modality and employer recognition with the relevant national institution.

## Current income research — use carefully

### United States official quantitative benchmark

For **Statisticians (O*NET-SOC 15-2041.00)**, current BLS 2025 wage data surfaced through O*NET show:

| Percentile | Annual | Hourly |
|---|---:|---:|
| 10th | $54,680 | $26.29 |
| 25th | $70,710 | $33.99 |
| Median | $105,650 | $50.79 |
| 75th | $143,140 | $68.82 |
| 90th | $170,700 | $82.07 |

These are **Statisticians wages**, not a universal Data Analyst salary table.

### U.S. outlook for the Statisticians benchmark

O*NET/BLS data show:

- 2024 employment: about **32,200**;
- 2034 projected employment: about **34,900**;
- projected growth: **9%**;
- projected annual openings: about **2,000**.

Again, these figures belong to the Statisticians benchmark.

### Current non-government U.S. estimate

Indeed’s current U.S. **Data Analyst** salary page reports an average base salary of approximately **$85,108/year**, with a displayed range of approximately **$52,084–$139,074/year** and about **8.1k salary observations from job postings over the prior 36 months** on the reviewed 2026 page.

This is a **non-government, title-specific market estimate**, not an official wage statistic or guaranteed compensation. Market pages can change, so readers should verify the live page when making a compensation decision.

### Canada

Job Bank NOC 21223 national wages are approximately:

- C$25.00/hour low;
- C$40.87/hour median;
- C$61.03/hour high.

These belong to the database analyst/data administrator comparison and should not be treated as an exact universal Data Analyst rate.

### Colombia

Because official CUOC/OCUPACOL mappings are function-dependent and OCUPACOL itself cautions that displayed occupation-level market indicators lack statistical representativeness, this guide does not manufacture one official representative Colombian national Data Analyst salary.

For current compensation decisions in Colombia, compare multiple live employer postings and reputable market sources for the exact job scope, city, seniority, language requirements, technology stack and employment arrangement.

## A practical learning sequence

### Stage 1 — foundations

Learn:

- spreadsheet basics;
- percentages and rates;
- descriptive statistics;
- clean tables;
- basic charts;
- data privacy;
- documentation.

### Stage 2 — querying

Learn:

- relational concepts;
- keys;
- joins;
- SQL filtering and aggregation;
- data-quality checks;
- validation.

### Stage 3 — analysis

Learn:

- distributions;
- missing data;
- outliers;
- sampling;
- bias;
- correlation-versus-causation;
- accessible visualization;
- stakeholder communication.

### Stage 4 — automation

Add one scripting language such as Python or R for:

- reproducible cleaning;
- larger datasets;
- repeatable analysis;
- statistical workflows;
- automated validation.

### Stage 5 — domain depth

Choose a business or technical domain such as:

- finance;
- marketing;
- healthcare;
- cybersecurity;
- logistics;
- quality;
- public policy;
- operations;
- product analytics.

Domain understanding helps you ask better questions and detect implausible results.

## Portfolio projects without exposing private data

A portfolio can demonstrate ability without using confidential employer information.

Safe sources include:

- public government datasets;
- open-data portals;
- explicitly licensed datasets;
- synthetic data you create yourself;
- training datasets whose terms permit portfolio use.

A strong beginner project can include:

1. question;
2. source and license;
3. data dictionary;
4. cleaning steps;
5. SQL or code;
6. validation checks;
7. charts or dashboard;
8. findings;
9. limitations;
10. accessible summary;
11. README with reproduction steps.

Do not upload:

- employer datasets;
- customer records;
- employee information;
- screenshots of confidential systems;
- internal SQL containing sensitive identifiers;
- proprietary report definitions;
- credentials or tokens.

## Four-week starter action plan

### Week 1 — spreadsheet and data-quality basics

- choose one public or synthetic dataset;
- identify what one row represents;
- build a simple data dictionary;
- check missing values and duplicates;
- calculate basic counts, rates, mean and median;
- create one honest chart.

### Week 2 — SQL

- create or use a small practice database;
- write filtering and aggregation queries;
- practice joins;
- validate row counts before and after joins;
- document one query in plain language.

### Week 3 — analysis and communication

- write one clear business or research question;
- analyze it using your dataset;
- identify at least two limitations;
- create an accessible chart and short written summary;
- distinguish observation from interpretation.

### Week 4 — portfolio and job preparation

- clean your README;
- document data source and license;
- include reproducible steps;
- remove any sensitive information;
- write two résumé bullets describing the project accurately;
- search current roles using several related titles;
- compare actual requirements before deciding what to learn next.

## Job-search titles to consider

Depending on your skills, search for:

- Data Analyst;
- Junior Data Analyst;
- Reporting Analyst;
- Business Data Analyst;
- Operations Analyst;
- Marketing Analyst;
- Sales Analyst;
- Quality Analyst;
- Research Analyst;
- Data Quality Analyst;
- BI Analyst;
- Power BI Analyst;
- SQL Analyst;
- Analytics Specialist;
- Data Coordinator;
- Reporting Specialist.

Read the duties carefully. Two jobs with the same title may have very different technical and educational requirements.

## Questions to ask before accepting a role

Consider asking:

- What are the main data sources?
- Is SQL required daily?
- Which tools are used for dashboards and analysis?
- How are metric definitions governed?
- Who owns data quality?
- How are analysts expected to validate results?
- Is there a code-review or peer-review process?
- What data can be accessed remotely?
- What privacy/security training is required?
- Are overtime, on-call or deadline peaks common?
- Is this primarily reporting, statistical analysis, business analysis or database work?
- What skills distinguish a junior from a senior analyst here?
- Does the employer provide training or certification support?

## Sources and verification links

Verify current values and program availability before making a major decision.

### United States

- O*NET — Statisticians: https://www.onetonline.org/link/details/15-2041.00
- O*NET — Business Intelligence Analysts: https://www.onetonline.org/link/details/15-2051.01
- CareerOneStop WIOA training locator: https://www.careeronestop.org/LocalHelp/EmploymentAndTraining/find-WIOA-training-programs.aspx
- Apprenticeship.gov: https://www.apprenticeship.gov/
- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework

### Canada

- Job Bank — NOC 21223 occupational information: https://www.jobbank.gc.ca/
- Canada training gateway: https://www.canada.ca/en/services/jobs/training.html

### Colombia

- OCUPACOL: https://ocupacol.mintrabajo.gov.co/
- SENA Betowa: https://betowa.sena.edu.co/

### Latin America and Caribbean

- ILO/Cinterfor: https://www.oitcinterfor.org/

### Current non-government market context

- Indeed U.S. Data Analyst salary page: https://www.indeed.com/career/data-analyst/salaries

## Important notice

This guide provides general educational and career-planning information. It does not guarantee employment, income, admission, funding, apprenticeship placement, certification, promotion or any other result. Occupation mappings are comparisons and may not be exact equivalents across jurisdictions. Requirements, wages, technology expectations, training availability and employment conditions change over time.

No independent human certification, professional accreditation, legal review, statistical certification, accessibility certification or translation certification is claimed unless separately documented.

## Author and AI assistance

Created and directed by **Alberto “Al” Leiva**. ChatGPT supported research, organization, editing, translation support and document preparation under the author’s direction. The author remains responsible for editorial and publication decisions.

## License

Unless a file states otherwise, this material is licensed under **CC BY-NC-SA 4.0**.
