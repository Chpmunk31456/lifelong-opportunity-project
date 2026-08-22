# Lifelong Opportunity Guide 86 — Database Administrator

**Version:** 2.0 controlled working master  
**Language:** English  
**Primary U.S. benchmark:** O*NET-SOC 15-1242.00 — Database Administrators  
**Canada comparison:** NOC 21223 — Database analysts and data administrators  
**Colombia comparison:** CUOC 25210 — Diseñadores y administradores de bases de datos  
**Review date:** 2026-08-22

## What this career is

A Database Administrator (DBA) helps keep organizational databases available, accurate, secure, recoverable and supportable. The work can include installing or configuring database-management systems, creating and maintaining databases, controlling access, testing changes, monitoring performance and capacity, applying approved upgrades, supporting backups and recovery, troubleshooting incidents, documenting configurations and helping teams use data systems safely.

This guide uses **O*NET-SOC 15-1242.00 — Database Administrators** as the primary United States benchmark. Canada maps closely to **NOC 21223 — Database analysts and data administrators**. Colombia has a direct match in **CUOC 25210 — Diseñadores y administradores de bases de datos**, which explicitly includes *Administrador de base de datos*.

A DBA may have powerful technical access. That does **not** mean the worker has unrestricted authority to read, copy, alter, export or delete any data. Production changes, privileged access, backups, security controls and recovery actions must remain inside employer authorization, change-management rules and applicable privacy/security obligations.

## Why this career still matters

Organizations depend on databases for transactions, customer records, finance, operations, logistics, healthcare, government services, analytics, identity, applications and internal systems. Cloud platforms and managed database services automate some infrastructure tasks, but they do not eliminate the need for people who can:

- understand data structures and dependencies;
- control access;
- detect performance or capacity problems;
- protect integrity and availability;
- verify backups and recoverability;
- plan and validate changes;
- investigate incidents;
- document systems;
- coordinate with application, cloud, security and business teams.

The occupation is evolving rather than simply disappearing. Current U.S. projections show a slight decline in total DBA employment, while replacement and turnover still create thousands of openings each year. That means learners should build skills that transfer across traditional databases, cloud-managed services, automation, data platforms and security-aware operations.

## What Database Administrators actually do

Current O*NET tasks include:

- modifying existing databases and DBMS platforms or directing approved changes;
- planning and implementing database security measures;
- installing approved DBMS upgrades;
- specifying users and access levels;
- testing database and application changes;
- correcting errors and making necessary modifications;
- supporting and training users or junior technical staff;
- planning and supervising installation/testing of new database systems where assigned;
- assessing database performance;
- developing database parameters, specifications and data models.

A job may emphasize only part of this list. Some DBAs focus on Oracle or SQL Server. Others work heavily with PostgreSQL, MySQL, cloud databases, data warehouses, NoSQL systems, high availability, automation or application support.

## DBA is not the same as every adjacent data role

### Database Administrator

Usually emphasizes:

- operational databases;
- security/access;
- backup/recovery;
- patching/upgrades;
- performance;
- capacity;
- availability;
- incidents;
- controlled changes.

### Database Developer

Often emphasizes:

- schema objects;
- stored procedures;
- functions;
- query development;
- application-facing database logic.

### Database Architect

Usually operates at a broader design level involving:

- platform selection;
- data architecture;
- integration patterns;
- resilience patterns;
- standards and long-term design.

### Data Engineer

Often focuses more on:

- pipelines;
- data movement;
- transformation;
- warehouses/lakes;
- orchestration;
- analytics platforms.

### Data Analyst / BI Analyst

Usually focuses more on querying, analysis, metrics, visualization and business interpretation than production database administration.

Actual employers may combine these responsibilities. Read the job description rather than relying on the title alone.

## The first operating rule: know your authority before you act

Before making a production change, confirm:

1. What system and environment are in scope?
2. Is the action authorized?
3. Is a change ticket, approval or maintenance window required?
4. What is the business impact if the action fails?
5. Is a backup, snapshot, restore point or rollback path required?
6. Has the script/change been tested in an appropriate non-production environment?
7. Who must be notified?
8. What validation proves success?
9. What condition requires stopping and escalating?
10. What evidence must be retained for audit or incident review?

Technical capability is not the same as organizational authority.

## Database fundamentals

A strong DBA should understand:

- relational database concepts;
- tables, rows and columns;
- primary and foreign keys;
- constraints;
- indexes;
- views;
- schemas;
- transactions;
- isolation and concurrency;
- normalization and denormalization tradeoffs;
- data types;
- stored procedures/functions where used;
- database files/storage structures;
- logs/journals;
- replication concepts;
- backup types;
- recovery concepts;
- high-availability patterns.

The exact implementation varies by platform, but the underlying principles transfer.

## SQL

SQL is the leading current employer-posting technology signal for this occupation.

A DBA should usually understand:

- `SELECT` and filtering;
- joins;
- aggregation;
- data definition language (DDL);
- data manipulation language (DML);
- transactions;
- permissions;
- indexes;
- execution plans;
- locking/blocking;
- stored procedures/functions where relevant;
- administrative catalog/system views;
- safe scripting and change validation.

A query or script is not safe merely because it executes successfully.

Before a consequential SQL action, verify:

- the target environment;
- object names;
- row scope;
- transaction behavior;
- permissions;
- expected row counts;
- backup/rollback readiness;
- performance impact;
- post-change validation.

## Current technology signals

O*NET's 2025 employer-posting data for Database Administrators show current demand signals including:

- SQL — **62%**;
- Python — **42%**;
- AWS — **29%**;
- Microsoft Azure — **25%**;
- Snowflake — **16%**;
- Apache Spark — **13%**;
- Microsoft Power BI — **12%**;
- Java — **12%**;
- PostgreSQL — **11%**;
- Apache Kafka — **10%**;
- Apache Airflow — **9%**;
- Microsoft SQL Server — **9%**;
- Tableau — **9%**;
- NoSQL — **9%**;
- Amazon Redshift — **9%**;
- Git — **8%**;
- Linux — **8%**;
- MySQL — **8%**;
- Oracle PL/SQL — **7%**;
- Oracle Database — **7%**;
- UNIX — **6%**;
- Terraform — **5%**;
- PowerShell — **5%**;
- MongoDB — **5%**.

These are posting signals, not a checklist that every DBA must satisfy. Choose depth based on the target employer/platform.

## Identity, access and privileged administration

Database access should follow approved organizational controls.

Good practices include:

- least privilege;
- role-based access where supported;
- separate normal and privileged accounts where policy requires;
- MFA for supported administrative access;
- approved credential/secrets storage;
- no passwords or connection strings in chat, tickets, public repositories or personal notes;
- no shared administrator accounts unless an approved legacy/emergency process explicitly requires them;
- periodic access review;
- timely removal of unneeded privileges;
- logging/auditability of privileged actions where supported;
- separation of duties for sensitive operations where required.

Never use database access for curiosity browsing.

## Security and database integrity

O*NET explicitly includes database security as a core DBA responsibility.

A DBA may help with:

- access control;
- configuration hardening;
- encryption configuration where assigned;
- patching/upgrades;
- vulnerability remediation;
- audit logging;
- secure network exposure;
- backup protection;
- secrets management;
- monitoring suspicious or failed access;
- incident evidence preservation;
- recovery from integrity or availability incidents.

Security architecture and legal interpretation may belong to other teams. Know when to escalate.

## Backup is not the same as recoverability

A job log saying “backup completed” is useful but insufficient evidence that the organization can recover what it needs.

A mature backup/recovery process may include:

- approved backup schedules;
- retention rules;
- encryption/protection of backup media or repositories;
- offsite or separate-failure-domain copies where required;
- restore testing;
- point-in-time recovery where supported;
- documented recovery runbooks;
- monitoring failed or delayed backups;
- verification of backup scope;
- disaster-recovery exercises;
- tested application/database dependencies.

Organizations may define **RPO** (Recovery Point Objective) and **RTO** (Recovery Time Objective). A DBA should understand the organization's targets and avoid inventing them independently.

## Restore testing

A restore test should answer questions such as:

- Can the backup actually be read?
- Is the expected database/version present?
- Can it restore in the required environment?
- Are encryption keys/secrets available through approved recovery processes?
- Does the restored database pass integrity checks?
- Can applications reconnect correctly?
- Are recovery steps documented and current?
- Did the test meet the organization's recovery objectives?

Never perform a destructive restore over a production system without explicit authorization and a controlled plan.

## High availability, replication and failover

Depending on the platform, a DBA may support:

- replicas;
- clusters;
- availability groups;
- standby databases;
- managed cloud replicas;
- multi-zone or regional configurations;
- failover procedures;
- replication-lag monitoring.

High availability does not replace backups. Replication can faithfully reproduce corruption, deletion or malicious changes.

Failover should be tested under approved procedures rather than assumed to work because components appear healthy.

## Performance and capacity

DBAs may investigate:

- slow queries;
- inefficient execution plans;
- missing or excessive indexes;
- locks/blocking/deadlocks;
- CPU/memory pressure;
- disk/storage pressure;
- I/O latency;
- connection exhaustion;
- transaction-log growth;
- replication lag;
- table/index growth;
- maintenance overhead;
- workload changes.

Use evidence before tuning. A change that improves one query can degrade another workload.

Document:

- baseline condition;
- observed metric;
- hypothesis;
- change;
- validation;
- rollback plan;
- result.

## Change management

Production database changes can affect many applications and users. A disciplined change may require:

- documented purpose;
- approved request/ticket;
- dependency review;
- tested script/package;
- peer review;
- backup or restore point;
- maintenance window;
- communication plan;
- execution steps;
- validation checks;
- rollback steps;
- post-change monitoring;
- evidence of completion.

Do not silently “fix” production outside approved controls merely because the technical change appears small.

## Schema changes and migrations

Before a schema or data migration, consider:

- table size;
- lock duration;
- transaction-log impact;
- application compatibility;
- index impact;
- replication impact;
- rollback feasibility;
- data-type conversion risk;
- null/default behavior;
- time-zone/encoding issues;
- required downtime;
- validation counts/checksums;
- privacy/security impact.

For large or high-risk changes, use the organization's tested migration pattern rather than improvising in production.

## Patching and upgrades

Database platforms require security and lifecycle maintenance.

A controlled patch/upgrade plan can include:

- vendor support/lifecycle review;
- compatibility assessment;
- application-driver/client compatibility;
- backup/recovery readiness;
- non-production testing;
- high-availability/failover sequence;
- maintenance-window approval;
- rollback or fallback plan;
- post-upgrade integrity/performance validation;
- documentation of version/configuration changes.

Never promise “zero downtime” unless the architecture and tested procedure actually support it.

## Monitoring and alerting

Useful monitoring domains include:

- availability;
- failed connections;
- authentication failures;
- database errors;
- CPU/memory/storage;
- I/O latency;
- query duration;
- blocking/deadlocks;
- backup success/failure;
- replication status;
- transaction-log growth;
- capacity thresholds;
- certificate or credential expiry where applicable;
- cloud service health/cost anomalies.

Alerts should have ownership, severity and an expected response. Too many low-quality alerts create noise and can hide real incidents.

## Incident response and escalation

A DBA may be involved when there is:

- database outage;
- corruption;
- suspected unauthorized access;
- credential compromise;
- ransomware or destructive activity;
- accidental deletion;
- replication failure;
- failed recovery;
- severe performance degradation;
- data-integrity concern;
- unexpected data exposure.

Follow the organization's incident process. Preserve evidence and timestamps. Do not destroy logs or “clean up” before the incident/security team determines what must be retained.

## Privacy, retention and data governance

DBAs may be able to see highly sensitive information. That access must be treated as a responsibility, not a benefit of the job.

Follow approved rules for:

- authorized purpose;
- minimum necessary access;
- data classification;
- retention and deletion;
- legal holds where applicable;
- masking/tokenization where required;
- secure extracts;
- test-data handling;
- recipient verification;
- export controls;
- audit logging;
- incident reporting.

Do not copy production datasets into personal or uncontrolled development environments.

## Development, test and production separation

Good environments reduce risk.

Where the organization supports it:

- develop and test changes outside production;
- use synthetic, masked or approved test data;
- restrict production credentials;
- separate deployment approval from development where required;
- keep environment-specific connection strings/secrets controlled;
- validate the target before running scripts.

A common high-impact mistake is executing the right script against the wrong environment.

## Cloud and managed database services

Managed services can automate tasks such as hardware management, patching options, snapshots or replication. They do not remove customer responsibilities.

A DBA or cloud-data operator may still need to manage:

- identity and access;
- network exposure;
- security groups/firewalls;
- database users/roles;
- encryption/key settings where configurable;
- backup retention;
- logging/audit configuration;
- maintenance settings;
- instance/service sizing;
- query performance;
- resilience architecture;
- application credentials;
- cost/capacity;
- change governance.

Understand the specific provider's shared-responsibility model rather than assuming “cloud means the provider handles security.”

## Automation, scripting and infrastructure as code

Automation can reduce repetitive work but can also multiply mistakes.

Common tools may include:

- Python;
- PowerShell;
- shell scripts;
- SQL scripts;
- Terraform;
- configuration-management tools;
- CI/CD pipelines;
- cloud automation.

Controls should include:

- version control;
- peer review where required;
- parameter validation;
- environment safeguards;
- secrets management;
- dry-run/test capability where available;
- logging;
- rollback;
- limited permissions for automation identities.

## Responsible AI for DBA work

AI may help with low-risk tasks when organizational policy permits, such as:

- drafting SQL or administrative scripts;
- explaining an execution plan;
- drafting runbooks;
- proposing test cases;
- generating synthetic data;
- summarizing public documentation;
- suggesting monitoring queries;
- explaining an error message.

Human validation remains mandatory.

Do **not**:

- upload production data, credentials, private schemas, connection strings or protected logs to an unapproved AI service;
- execute AI-generated SQL in production without review/testing/authorization;
- accept invented object names, syntax, metrics or vendor behavior;
- let an AI agent make autonomous production changes outside approved governance;
- treat AI output as incident evidence or vendor documentation;
- skip rollback planning because an AI-generated recommendation looks plausible.

For consequential changes, verify against authoritative platform documentation and organizational controls.

NIST AI RMF and the Generative AI Profile are voluntary risk-management guidance, not substitutes for database/security governance.

## Accessibility and usable documentation

Database documentation should be usable by the people who need it, including under incident pressure.

Helpful practices include:

- meaningful headings;
- clear step order;
- readable fonts/contrast;
- tables with proper headers;
- text descriptions for architecture diagrams;
- not relying on color alone;
- keyboard-accessible documentation/tools where supported;
- clear error/decision branches;
- plain-language explanations of high-impact steps;
- commands/scripts formatted distinctly from explanatory text.

An automated accessibility checker does not prove legal compliance.

## Education and entry pathways — United States

O*NET places Database Administrators in **Job Zone Four — Considerable Preparation Needed**.

Current education responses indicate:

- **89%** bachelor's degree;
- **4%** post-baccalaureate certificate;
- **3%** associate degree.

These are occupation-level survey responses, not an absolute rule for every posting.

People may build toward DBA work through:

- IT support;
- application support;
- systems administration;
- database development;
- data operations;
- software development;
- cloud support;
- reporting/BI work;
- formal computer science/information systems programs;
- employer training;
- apprenticeships or technician pathways.

### U.S. training and funding locators

CareerOneStop and American Job Centers can help investigate local training, WIOA-approved providers and support services. Eligibility and funding vary; no funding is guaranteed.

O*NET lists approved apprenticeship titles:

- **Database Administrator (Nof)**;
- **Database Technician**.

Use Apprenticeship.gov to verify whether an active opportunity exists in your location.

## Canada

Canada Job Bank maps Database Administrator (DBA) to **NOC 21223 — Database analysts and data administrators**.

Typical requirements currently include:

- a bachelor's degree or college program, usually in computer science, computer engineering or mathematics;
- programming and related experience.

Job Bank currently states that this occupation is **not regulated in Canada**. Employer requirements can still be substantial.

### Canada wages

Current Job Bank national wages are:

- **C$25.00/hour — low**;
- **C$40.87/hour — median**;
- **C$61.03/hour — high**.

They apply to NOC 21223 and should not be presented as guaranteed pay for every DBA job.

Canada.ca provides national links for student aid, skills training, employment services and provincial/territorial programs. Eligibility and availability vary.

## Colombia

Colombia's direct mapping is **CUOC 25210 — Diseñadores y administradores de bases de datos**, competency level 4.

Official titles include:

- Administrador de base de datos;
- Administrador de datos;
- Analista de base de datos;
- Arquitecto de bases de datos;
- Data manager;
- Desarrollador de base de datos;
- Diseñador de bases de datos;
- Gerente de base de datos;
- Programador de base de datos.

Official functions cover architecture, DBMS implementation/testing, tool selection, access/use policy, backup/recovery, security/integrity, risk management and technical coordination.

OCUPACOL currently does not provide an available occupied-worker count for this profile. This guide does not fabricate a representative national Colombian DBA salary.

### SENA — long-form pathway

**Implementación y gestión de bases de datos**

- Tecnólogo;
- **3,984 hours**;
- titulada training;
- current Betowa listing;
- admission/selection and state-exam requirements apply;
- location, modality, cohort, seats and dates must be verified live.

### SENA — supplemental pathways

**Bases de datos: generalidades y sistemas de gestión**

- virtual complementary training;
- **40 hours**;
- relational database, normalization, entity-relationship and design fundamentals.

**Construcción de bases de datos con MySQL**

- complementary training;
- **48 hours**;
- focused MySQL database construction.

Short courses supplement rather than replace the long-form Tecnólogo or employer experience requirements.

## Latin America and Caribbean

OIT/Cinterfor can help locate national vocational-training institutions and systems across Latin America and the Caribbean. It is a locator, not a guarantee of a current DBA course, scholarship, admission or funding.

## U.S. official wages

BLS 2025 wage data surfaced through O*NET show:

| Percentile | Annual | Hourly |
|---|---:|---:|
| 10th | $60,230 | $28.96 |
| 25th | $79,610 | $38.28 |
| Median | $104,620 | $50.30 |
| 75th | $135,460 | $65.13 |
| 90th | $163,320 | $78.52 |

These values belong to O*NET-SOC 15-1242.00 Database Administrators.

## U.S. employment outlook

O*NET/BLS projections show:

- employment 2024: **78,000**;
- projected employment 2034: **77,500**;
- projected growth: **-1%**;
- projected annual openings: **3,800**.

This is a slight projected decline in total employment, not growth. Annual openings include replacement/turnover.

## Current non-government U.S. market estimate

Indeed's current U.S. Database Administrator page reviewed in August 2026 reports approximately:

- average base salary: **$110,414/year**;
- low: **$73,876/year**;
- high: **$165,024/year**;
- **2.1k** salaries taken from job postings over the prior **36 months**;
- updated **August 10, 2026**.

This is a title-specific non-government estimate, not an official wage series and not guaranteed compensation.

## A practical learning sequence

### Stage 1 — database foundations

Learn:

- relational models;
- keys/constraints;
- normalization;
- SQL;
- transactions;
- basic security;
- backup concepts.

### Stage 2 — one database platform deeply

Choose one environment such as:

- PostgreSQL;
- Microsoft SQL Server;
- MySQL;
- Oracle Database.

Practice installation/configuration, users/roles, backup/restore, monitoring and safe changes.

### Stage 3 — operations

Add:

- performance analysis;
- indexing;
- monitoring;
- maintenance;
- patching;
- recovery testing;
- incident troubleshooting;
- automation.

### Stage 4 — cloud and resilience

Learn:

- one cloud platform;
- managed database concepts;
- identity/network controls;
- replication/high availability;
- backup/retention settings;
- infrastructure automation;
- shared responsibility.

### Stage 5 — specialization

Possible directions include:

- cloud DBA/data platform engineer;
- database reliability;
- database security;
- performance engineering;
- data engineering;
- architecture;
- platform automation.

## Safe portfolio projects

Use synthetic, public or explicitly licensed data.

Possible projects:

1. create a small relational schema with constraints;
2. document an entity-relationship model;
3. create least-privilege roles;
4. back up and restore a practice database;
5. demonstrate point-in-time recovery in a lab if the platform supports it;
6. create a performance baseline and index-tuning exercise;
7. simulate replication/failover in a lab;
8. write a migration with validation and rollback steps;
9. create a monitoring dashboard using synthetic workload;
10. write a recovery runbook and test report.

Never publish:

- employer/customer data;
- credentials or connection strings;
- production schemas or screenshots;
- private IPs/hostnames;
- proprietary configuration;
- real backup files;
- access tokens/keys;
- vulnerability details for systems you do not own or have authorization to test.

## A four-week starter plan

### Week 1 — SQL and schema basics

- install a local practice database;
- create tables/keys/constraints;
- practice SQL safely;
- document the schema;
- create non-privileged users.

### Week 2 — backup and recovery

- create an approved lab backup;
- restore it to a separate lab instance;
- record time/steps;
- verify row/object counts;
- document what failed and what you corrected.

### Week 3 — monitoring and performance

- create a synthetic workload;
- capture a baseline;
- identify one slow query;
- review its execution plan;
- test an improvement;
- compare before/after evidence.

### Week 4 — change control and portfolio

- create a small schema migration;
- write pre-checks, execution, validation and rollback steps;
- remove secrets/private data;
- write a README;
- search current DBA/database technician/cloud database postings;
- compare actual requirements with your next learning goal.

## Job titles to search

Depending on experience and platform, search for:

- Database Administrator;
- DBA;
- Junior Database Administrator;
- Database Technician;
- SQL Server DBA;
- Oracle DBA;
- PostgreSQL DBA;
- MySQL DBA;
- Cloud Database Administrator;
- Database Support Engineer;
- Database Operations Engineer;
- Database Reliability Engineer;
- Data Platform Administrator;
- Database Analyst.

## Questions to ask an employer

Before accepting a role, consider asking:

- Which database platforms and versions are in scope?
- What percentage is on-premises versus cloud-managed?
- What are the on-call expectations?
- How are privileged accounts managed?
- Is MFA required for administration?
- How often are restores tested?
- Are RPO/RTO targets documented?
- Who owns database security configuration?
- How are patches and schema changes approved?
- Is there a defined maintenance window?
- What monitoring/alerting platform is used?
- How are secrets stored?
- Is infrastructure/database automation version controlled and reviewed?
- What separates junior from senior DBA responsibility?
- What training or certification support is available?

## Verification links

Check current values and program availability before making an important decision.

### United States

- O*NET Database Administrators: https://www.onetonline.org/link/details/15-1242.00
- O*NET national wages: https://www.onetonline.org/link/localwages/15-1242.00
- O*NET national trends: https://www.onetonline.org/link/localtrends/15-1242.00
- O*NET hot technologies: https://www.onetonline.org/link/hot_tech/15-1242.00
- CareerOneStop WIOA locator: https://www.careeronestop.org/LocalHelp/EmploymentAndTraining/find-WIOA-training-programs.aspx
- Apprenticeship.gov: https://www.apprenticeship.gov/
- Indeed U.S. DBA salary context: https://www.indeed.com/career/database-administrator/salaries

### Canada

- Job Bank DBA summary: https://www.jobbank.gc.ca/marketreport/summary-occupation/17875/ca
- Job Bank DBA requirements: https://www.jobbank.gc.ca/marketreport/requirements/17875/ca
- Job Bank DBA wages: https://www.jobbank.gc.ca/marketreport/wages-occupation/17875/ca
- Canada training gateway: https://www.canada.ca/en/services/jobs/training.html

### Colombia

- OCUPACOL CUOC 25210: https://ocupacol.mintrabajo.gov.co/Profile/OccupationalProfile/25210
- SENA Implementación y gestión de bases de datos: https://betowa.sena.edu.co/oferta/implementacion-y-gestion-de-bases-de-datos?modality=P&offertype=open&programId=178214
- SENA Bases de datos: generalidades y sistemas de gestión: https://betowa.sena.edu.co/oferta/bases-de-datos-generalidades-y-sistemas-de-gestion?modality=V&offertype=open&programId=73885

### Regional, security, AI and accessibility

- OIT/Cinterfor training locator: https://www.oitcinterfor.org/statsfp/paises
- CISA Secure Our World: https://www.cisa.gov/secure-our-world
- NIST Cybersecurity Framework: https://www.nist.gov/cyberframework
- NIST Privacy Framework: https://www.nist.gov/privacy-framework
- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework
- Section 508 document guidance: https://www.section508.gov/create/
- WCAG 2.2: https://www.w3.org/TR/WCAG22/

## Important notice

This guide provides general education and career-planning information. It does not guarantee employment, income, admission, funding, apprenticeship placement, certification, promotion or any other outcome. Occupational mappings are comparisons and requirements vary by employer and jurisdiction. Wages, technologies, programs and job conditions change over time.

This guide does not provide legal, privacy, cybersecurity, accounting or vendor-specific professional advice and does not independently certify any system as secure, recoverable, compliant or accessible.

## Author and AI assistance

Created and directed by **Alberto “Al” Leiva**. ChatGPT supported research, organization, editing, translation support and document preparation under the author's direction. The author remains responsible for editorial and publication decisions.

## License

Unless a file states otherwise, this material is licensed under **CC BY-NC-SA 4.0**.
