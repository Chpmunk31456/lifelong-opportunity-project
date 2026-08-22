# Lifelong Opportunity Guide 87 — Software Quality Assurance Analyst and Tester

**Version:** 2.0 controlled working master  
**Language:** English  
**Primary U.S. benchmark:** O*NET-SOC 15-1253.00 — Software Quality Assurance Analysts and Testers  
**Canada comparisons:** NOC 21222 — Information systems specialists; NOC 22222 — Information systems testing technicians  
**Colombia comparison:** CUOC 25190 — Desarrolladores y analistas de software y multimedia no clasificados en otras ocupaciones  
**Review date:** 2026-08-22

## What this career is

Software quality assurance (QA) analysts and testers help teams determine whether software behaves as intended, satisfies defined requirements, handles errors safely, and can be released with an understood level of risk. The work can include reviewing requirements, designing test cases, preparing test data, executing manual or automated checks, documenting defects, retesting fixes, supporting regression testing, evaluating usability and accessibility, and helping teams understand evidence about software quality.

This is not simply “trying to break software.” Strong QA work is disciplined evidence work. A tester must know what is being verified, what environment and build were used, what data and preconditions applied, what result was expected, what actually happened, and how another person can reproduce the observation.

The United States has a direct occupational match in **O*NET-SOC 15-1253.00 — Software Quality Assurance Analysts and Testers**. Canada separates the scope more clearly: analyst-level QA work maps usefully to **NOC 21222 — Information systems specialists**, while execution-oriented software testing maps to **NOC 22222 — Information systems testing technicians**. Colombia has a strong direct QA/testing comparison in **CUOC 25190**.

## Why this career remains important

Software now affects banking, healthcare, government, transportation, education, commerce, communications, manufacturing, cybersecurity and everyday consumer services. Defects can cause:

- incorrect calculations;
- unavailable services;
- failed transactions;
- confusing workflows;
- inaccessible interfaces;
- data loss;
- privacy exposure;
- security weaknesses;
- expensive rework;
- regulatory or contractual problems;
- customer harm or loss of trust.

Automation and AI can expand testing capacity, but they do not remove the need for people who can define trustworthy checks, interpret failures, recognize weak test evidence, investigate edge cases, communicate risk and understand when a test result is not enough to justify a release decision.

## Common job titles

Depending on employer and seniority, search for titles such as:

- Software QA Analyst;
- Software Quality Assurance Analyst;
- QA Tester;
- Software Tester;
- Manual Tester;
- QA Engineer;
- Test Engineer;
- Automation Tester;
- Test Automation Engineer;
- Quality Engineer;
- SDET / Software Development Engineer in Test;
- API Tester;
- Mobile QA Tester;
- Accessibility Tester;
- Performance Tester;
- UAT Analyst;
- Regression Tester.

Titles overlap. Read the actual duties, required coding depth, test ownership, environment responsibility and release authority.

## Core work: test basis and traceability

Testing should begin from a defined **test basis**. Depending on the organization, that can include:

- approved requirements;
- acceptance criteria;
- user stories;
- interface or API contracts;
- designs or specifications;
- documented user workflows;
- defect fixes;
- risk controls;
- approved policy or regulatory requirements where assigned.

A tester should be able to explain what each important test is intended to verify. QA should not silently invent a requirement simply to make a test pass or fail.

Traceability can connect:

**requirement or risk → test case → test execution → evidence → defect or result → retest / release decision input.**

The exact tooling varies, but the evidence chain matters.

## Test-case design

A defensible test case can include:

- objective;
- requirement or risk being tested;
- preconditions;
- environment;
- build/version;
- test data;
- steps;
- expected result;
- actual result;
- pass/fail/blocked status;
- evidence;
- cleanup or reset steps where needed;
- linked defect or requirement.

Expected behavior should come from authoritative product information or approved team decisions. When the requirement is unclear or contradictory, raise the ambiguity rather than choosing an expected result after seeing what the product does.

## Reproducible defect reports

A useful defect report should help another qualified person reproduce and investigate the issue.

Include, where relevant:

- concise title;
- environment, browser/device or platform;
- build/version;
- preconditions;
- repeatable steps;
- expected result;
- actual result;
- frequency or reproducibility;
- evidence such as safe screenshots, logs or video;
- severity or impact;
- linked requirement or test;
- test-data identifier without exposing protected data.

Describe what was observed. Avoid blaming a developer or claiming a root cause that has not been established.

## Severity versus priority

These terms are related but not identical.

- **Severity** describes how strongly a defect affects users, system behavior, safety, data, security or business operation.
- **Priority** describes how urgently or in what order the organization chooses to address the defect.

A severe defect can sometimes have lower immediate priority because it affects an obsolete or disabled feature. A lower-severity defect can have high priority because it blocks a major release, customer commitment or legal requirement. Teams define scales differently; use the organization’s definitions and escalation rules.

## Test levels and test types

Relevant testing can include:

- unit testing;
- integration testing;
- system testing;
- end-to-end testing;
- acceptance testing;
- functional testing;
- regression testing;
- negative/error testing;
- boundary-value testing;
- compatibility testing;
- API testing;
- database/data validation;
- usability testing;
- accessibility testing;
- performance/load/stress testing;
- recovery/resilience testing where assigned;
- security testing within explicit authorization.

No single tester necessarily owns every test type. Unit testing is often primarily developer-owned. Release authorization may belong to product, engineering, risk, change management or another accountable role. QA provides evidence and risk information within the organization’s decision process.

## Exploratory and scripted testing

Scripted testing supports repeatability, regression coverage and traceability. Exploratory testing uses tester judgment to investigate behavior, state transitions and unexpected interactions.

They are complementary. Good exploratory testing still has:

- defined scope;
- appropriate environment;
- authorized data;
- notes or evidence;
- a clear explanation of what was tried and what was observed.

## Test data

Test data should support realistic scenarios without creating unnecessary privacy or security risk.

Prefer:

- synthetic data;
- approved masked data;
- purpose-built test accounts;
- controlled datasets with known expected outcomes.

Avoid casually copying production customer or employee data into test environments. Protect credentials, API tokens and private keys. Do not attach protected information to a defect ticket unless it is authorized and necessary. Sanitize screenshots and logs when needed.

## Test environments and configuration

A result is meaningful only if the environment is understood.

Record important information such as:

- application version/build;
- operating system;
- browser/device;
- service or API version;
- feature flags;
- database version or seed state;
- test account role;
- dependent service state;
- environment-specific configuration.

When environments drift, a test may pass in one place and fail in another. Avoid claiming a defect is “fixed” until the relevant retest occurs in the intended environment/build.

## Regression testing

Regression testing checks whether a new change has damaged previously working behavior.

Useful regression strategy considers:

- changed components;
- dependency impact;
- high-value user paths;
- prior defect history;
- business criticality;
- security/privacy impact;
- integration points;
- time available;
- automation reliability.

A huge regression suite that nobody trusts is not automatically better than a smaller, risk-focused suite with reliable evidence.

## Test automation

Automation is valuable when a check is repeatable, stable and worth running frequently. It is not a goal by itself.

Common technologies in current U.S. postings for the occupation include **Python, Selenium, Atlassian JIRA, SQL, Java, Jenkins CI, JavaScript, Postman, AWS, Git, Linux, Microsoft Azure, Apache JMeter, C#, GitHub, C++, Microsoft Playwright, Azure DevOps Services, TestNG, RESTful API, Appium and REST Assured**.

Automation requires:

- maintainable code;
- stable interfaces or selectors;
- meaningful assertions;
- version control;
- code review where required;
- controlled test data;
- environment assumptions;
- failure diagnostics;
- management of flaky tests;
- maintenance as the product changes.

Automated tests can also be wrong. A passing suite does not prove that the product is defect-free.

## Flaky tests

A flaky test produces inconsistent results without a meaningful product change.

Common causes include:

- timing assumptions;
- unstable test data;
- shared state;
- unreliable dependencies;
- race conditions;
- brittle UI selectors;
- environment capacity;
- network instability.

Do not normalize unexplained flakiness. Track it, investigate it and decide whether the test should be repaired, quarantined or replaced according to team policy.

## API testing

API tests can verify:

- status codes;
- response schemas;
- required fields;
- authorization behavior;
- validation errors;
- business rules;
- idempotency where relevant;
- pagination;
- boundary cases;
- error handling;
- performance under approved conditions.

Tools such as Postman or automated libraries can help, but a tool does not determine what the correct business behavior should be.

## Database and data validation

QA may need to verify that:

- transactions create the expected records;
- updates affect the intended rows;
- data types and constraints work correctly;
- calculations reconcile;
- migrations preserve required information;
- duplicate handling follows requirements;
- audit or history records are created where required.

Use read/write database access only within authorization. Never use production queries or data modifications simply because credentials are technically available.

## CI/CD and release pipelines

QA often works with continuous integration and delivery pipelines. A reliable quality gate should make clear:

- which build/version was tested;
- which suites ran;
- which tests failed or were skipped;
- whether results are trustworthy;
- what evidence is retained;
- what threshold or release criterion applies;
- who may override or waive a gate.

Passing automated tests is evidence. It is not automatically permission to release unless the organization explicitly defines it that way.

## Security-testing boundary

Functional QA is not automatically penetration testing.

Approved QA checks may include safe validation of:

- role-based access;
- authorization errors;
- session behavior;
- input validation;
- secure defaults;
- privacy controls;
- expected audit behavior.

Intrusive scanning, exploit attempts, credential attacks, destructive payloads, penetration tests or tests against systems outside scope require explicit authorization and defined rules of engagement.

NIST’s Secure Software Development Framework (SSDF) can support secure-development practices. The OWASP Web Security Testing Guide can provide useful technical testing ideas for authorized web applications and services. Neither gives a tester permission to attack a system.

## Accessibility testing

QA can contribute significantly to accessibility by checking:

- keyboard operation;
- visible focus;
- form labels;
- error messages;
- heading structure;
- contrast;
- zoom/reflow;
- screen-reader behavior;
- non-color-only communication;
- captions or alternatives where relevant.

Automated accessibility scanners detect only part of the problem space. Passing an automated scan does not establish legal accessibility compliance. Manual and assistive-technology testing may be necessary, and the organization remains responsible for its accessibility obligations.

## Performance testing

Performance testing may measure:

- response time;
- throughput;
- concurrency;
- resource use;
- stability under load;
- recovery after load.

Load or stress tests can disrupt systems. Use approved environments, limits, data and schedules. Do not run stress tests against production or third-party services without explicit authorization.

## Privacy and security in QA evidence

Bug trackers, screenshots, videos, logs and test exports can contain sensitive information.

Practical controls include:

- least-privilege access;
- approved repositories and ticketing systems;
- MFA and approved credential practices;
- removal/masking of unnecessary sensitive values;
- recipient verification;
- controlled retention and deletion;
- no personal email or storage for protected artifacts;
- no credentials or secrets in screenshots/code snippets;
- incident escalation for suspected exposure.

Having access to a test environment does not mean every dataset or field may be copied elsewhere.

## Responsible AI in QA/testing

AI can help with low-risk work when organizational policy permits, for example:

- drafting test ideas;
- drafting test cases;
- generating synthetic test data;
- explaining a stack trace;
- drafting automation code;
- summarizing non-sensitive defect history;
- suggesting edge cases;
- drafting test documentation.

Human verification remains necessary.

Do not:

- upload protected source code, credentials, customer data, private logs or unreleased product details to an unapproved AI tool;
- accept AI-invented requirements or expected behavior;
- assume AI-generated tests have valid assertions;
- let AI autonomously close defects;
- let AI approve releases outside governance;
- treat generated explanations as proven root cause;
- expose confidential vulnerabilities to public AI systems;
- present AI output as test evidence without independent execution and verification.

NIST AI RMF and the Generative AI Profile provide voluntary risk-management guidance. They do not replace product requirements, organizational governance or accountable human review.

## Ethical and professional boundaries

A QA analyst or tester should not:

- fabricate test results;
- mark a test passed without evidence;
- hide known failures to meet a deadline;
- alter expected results after execution merely to create a pass;
- delete defects without authorized disposition;
- use production data outside authorization;
- exploit systems outside the approved scope;
- disclose confidential defects or vulnerabilities improperly;
- claim a product is “bug free” because a suite passed;
- claim legal, security or accessibility certification without authority.

Strong QA communicates uncertainty. “No defect observed in this test scope” is different from “the feature cannot fail.”

## Education and entry pathways — United States

O*NET places 15-1253.00 in **Job Zone Four — Considerable Preparation Needed**. Current education responses for new hires include approximately:

- **50% bachelor’s degree**;
- **26% associate degree**;
- **9% post-secondary certificate**.

These are occupation-level responses, not absolute requirements for every vacancy. Employers may accept combinations of degree, technical education, coding skill, domain experience, portfolio evidence, internships, apprenticeship or prior support/development experience.

Useful study areas include:

- software testing;
- computer science;
- software development;
- information systems;
- databases and SQL;
- web technologies;
- APIs;
- automation;
- cybersecurity fundamentals;
- accessibility;
- technical communication.

### U.S. workforce and apprenticeship locators

CareerOneStop and American Job Centers can help readers investigate local training and WIOA-eligible programs. Eligibility, provider approval and funding vary locally.

O*NET lists the approved Registered Apprenticeship title **Software Quality Assurance Tester (Nof)**. Verify actual current openings through Apprenticeship.gov; an approved title does not guarantee an available apprenticeship.

## Canada

Canada requires a two-anchor interpretation for this guide.

### Analyst-level QA — NOC 21222

The Job Bank title **Software QA (Quality Assurance) Analyst** maps to **NOC 21222 — Information systems specialists**. National wages currently show approximately:

- **C$28.85/hour low**;
- **C$46.15/hour median**;
- **C$68.68/hour high**.

A bachelor’s degree in computer science, computer systems engineering, software engineering, business administration or a related discipline, or a college computer-science program, is usually required according to current Job Bank information.

### Testing-technician — NOC 22222

The Job Bank title **Software Tester** maps to **NOC 22222 — Information systems testing technicians**. National wages currently show approximately:

- **C$17.50/hour low**;
- **C$35.00/hour median**;
- **C$51.28/hour high**.

Current Job Bank requirements commonly include a college program or courses in computer science, programming or network administration; vendor training/certification may be required by some employers.

Regulation is not uniform nationally. Job Bank currently identifies the testing-technician occupation as regulated in Manitoba through the Certified Technicians and Technologists Association of Manitoba. Check the current province or territory for the role you are considering.

## Colombia

**CUOC 25190** is a strong direct comparison for software QA/testing and includes titles such as:

- Analista de prueba de software;
- Analista de pruebas - tester;
- Analista de software de pruebas;
- Analista de aseguramiento de la calidad informática;
- Probador de sistemas;
- Probador de software;
- Coordinador de prueba de software;
- Líder de pruebas testing.

Official functions include developing, executing, analyzing and documenting test plans/results, verifying software against user needs and reference models, implementing test procedures, preparing systems for testing, managing technology-solution risk, and controlling software quality against technical parameters.

No representative national Colombian QA/tester salary is created here because the current official profile does not provide statistically representative occupied-worker wage evidence suitable for that claim.

### SENA pathways

Current SENA Betowa pathways include:

**Procesamiento de pruebas de software**  
- Técnico;
- **2,208 hours**;
- long-form titulada training;
- software testing plus related software-development/database competencies.

**Manejo de pruebas de software**  
- complementary virtual training;
- **40 hours**.

**Modelos de calidad de software**  
- complementary virtual training;
- **40 hours**.

**Procesos para software de calidad**  
- complementary virtual training;
- **40 hours**.

The 40-hour courses are supplemental and are not equivalent to the 2,208-hour Técnico. Program availability, cohorts, seats, modality and admission requirements must be checked live.

## Latin America and Caribbean

ILO/Cinterfor can help readers locate national vocational-training institutions across Latin America and the Caribbean. It is a training-system locator, not a guarantee of a current software-testing course, scholarship, seat or funding award.

## Current wages and outlook — use the correct population

### United States official occupation

BLS 2025 wage data surfaced through O*NET for **15-1253.00** show:

| Percentile | Annual | Hourly |
|---|---:|---:|
| 10th | $61,440 | $29.54 |
| 25th | $80,310 | $38.61 |
| Median | $104,300 | $50.14 |
| 75th | $133,180 | $64.03 |
| 90th | $167,010 | $80.29 |

O*NET/BLS 2024–2034 projections show:

- 2024 employment: **201,700**;
- projected 2034 employment: **221,900**;
- projected growth: **10%**;
- projected annual openings: **14,000**.

Annual openings include growth and replacement openings.

### Current non-government U.S. market context

Indeed’s U.S. **Software Quality Assurance Analyst** page, reviewed in August 2026, reported approximately:

- average base salary **$87,641/year**;
- low **$56,161/year**;
- high **$136,766/year**;
- **208** salary observations from postings over the prior **36 months**;
- updated **August 2, 2026**.

This is a title-specific non-government estimate and does not replace official BLS/O*NET statistics. Verify the live page before a compensation decision.

## A practical learning sequence

### Stage 1 — testing foundations

Learn:

- requirements and acceptance criteria;
- test cases;
- expected versus actual results;
- defect reporting;
- severity versus priority;
- regression concepts;
- basic accessibility and privacy awareness.

### Stage 2 — technical foundations

Add:

- HTML/CSS/JavaScript basics;
- SQL;
- HTTP and APIs;
- browser developer tools;
- Git/version control;
- logs;
- command-line basics.

### Stage 3 — automation

Choose one stack and learn:

- automation framework basics;
- stable selectors;
- assertions;
- test data;
- setup/teardown;
- debugging;
- CI integration;
- flaky-test diagnosis.

### Stage 4 — specialization

Develop deeper skill in one or more areas:

- API testing;
- mobile testing;
- performance testing;
- accessibility testing;
- database/data validation;
- security-focused QA within authorization;
- domain-specific quality work.

## Safe portfolio projects

Use public, licensed, open-source or self-built software and synthetic data.

Useful projects include:

1. a test plan for a demo application;
2. a requirement-to-test traceability matrix;
3. several high-quality defect reports;
4. an API test collection against a local/public demo API;
5. an automation suite for a self-built or open-source application;
6. an accessibility review combining automated and manual checks;
7. a controlled performance test against a local demo environment;
8. a CI workflow that executes tests and preserves results.

Do not publish employer source code, proprietary requirements, real customer records, credentials, private logs, unauthorized vulnerability details or screenshots containing protected data.

## Four-week starter plan

### Week 1 — manual testing discipline

- choose a public or self-built demo app;
- write ten test cases;
- define expected results before execution;
- record actual results;
- write two reproducible defect reports;
- practice severity versus priority.

### Week 2 — API and SQL

- learn basic HTTP methods/status codes;
- use a demo API;
- create positive and negative API checks;
- practice basic SQL queries against a local sample database;
- document test data and cleanup.

### Week 3 — automation

- choose Playwright, Selenium or another appropriate framework;
- automate a small stable user flow;
- add assertions;
- run locally and through version control;
- investigate one intentionally failing test.

### Week 4 — evidence and job preparation

- create a clean README;
- include requirements, test cases, results and limitations;
- remove sensitive information;
- add a simple CI test run if appropriate;
- write accurate résumé bullets;
- compare current job descriptions before deciding which tools to learn next.

## Questions to ask before accepting a QA/testing role

Consider asking:

- Is the role primarily manual, automation, analyst-level QA or test execution?
- Which product areas and test types are owned by this team?
- Who defines severity and priority?
- Who has final release authority?
- Which automation frameworks are used?
- How are flaky tests handled?
- How is test data created and protected?
- Are production datasets ever used in non-production environments?
- What security testing is within QA scope?
- How are accessibility requirements tested?
- How are defects and test results retained?
- Is there on-call, weekend release or after-hours testing?
- What distinguishes junior from senior performance?
- Does the employer fund training or certification?

## Sources and verification links

Verify current values, requirements and program availability before a major decision.

### United States

- O*NET — Software Quality Assurance Analysts and Testers: https://www.onetonline.org/link/details/15-1253.00
- O*NET summary: https://www.onetonline.org/link/summary/15-1253.00
- O*NET wages: https://www.onetonline.org/link/localwages/15-1253.00
- O*NET outlook: https://www.onetonline.org/link/localtrends/15-1253.00
- CareerOneStop WIOA locator: https://www.careeronestop.org/LocalHelp/EmploymentAndTraining/find-WIOA-training-programs.aspx
- Apprenticeship.gov: https://www.apprenticeship.gov/
- Indeed market context: https://www.indeed.com/career/software-quality-assurance-analyst/salaries

### Canada

- Job Bank QA Analyst: https://www.jobbank.gc.ca/marketreport/summary-occupation/22511/ca
- Job Bank QA Analyst requirements: https://www.jobbank.gc.ca/marketreport/requirements/22511/ca
- Job Bank QA Analyst wages: https://www.jobbank.gc.ca/marketreport/wages-occupation/22511/ca
- Job Bank Software Tester: https://www.jobbank.gc.ca/marketreport/summary-occupation/3950/ca
- Job Bank Software Tester requirements: https://www.jobbank.gc.ca/marketreport/requirements/3950/ca
- Job Bank Software Tester wages: https://www.jobbank.gc.ca/wagereport/occupation/3950
- Canada training gateway: https://www.canada.ca/en/services/jobs/training.html

### Colombia

- OCUPACOL CUOC 25190: https://ocupacol.mintrabajo.gov.co/Profile/OccupationalProfile/25190
- SENA — Procesamiento de pruebas de software: https://betowa.sena.edu.co/oferta/procesamiento-de-pruebas-de-software?level=2&modality=V&programId=171614
- SENA — Manejo de pruebas de software: https://betowa.sena.edu.co/oferta/manejo-de-pruebas-de-software?programId=103412
- SENA — Modelos de calidad de software: https://betowa.sena.edu.co/oferta/modelos-de-calidad-de-software?modality=V&offertype=open&programId=73282&technology=1
- SENA — Procesos para software de calidad: https://betowa.sena.edu.co/oferta/procesos-para-software-de-calidad?programId=68240

### Secure development, AI and accessibility

- NIST SSDF: https://csrc.nist.gov/pubs/sp/800/218/final
- OWASP Web Security Testing Guide: https://owasp.org/www-project-web-security-testing-guide/
- NIST AI RMF: https://www.nist.gov/itl/ai-risk-management-framework
- Section 508 authoring guidance: https://www.section508.gov/create/
- WCAG 2.2: https://www.w3.org/TR/WCAG22/
- ILO/Cinterfor regional locator: https://www.oitcinterfor.org/statsfp/paises

## Important notice

This guide provides general educational and career-planning information. It does not guarantee employment, income, admission, funding, apprenticeship placement, certification, promotion or any other result. Occupation mappings are comparisons and may not be exact equivalents across jurisdictions. Requirements, wages, technology expectations, training availability and employment conditions change over time.

No independent human certification, professional accreditation, legal review, security assessment, accessibility certification, software-release certification or translation certification is claimed unless separately documented.

## Author and AI assistance

Created and directed by **Alberto “Al” Leiva**. ChatGPT supported research, organization, editing, translation support and document preparation under the author’s direction. The author remains responsible for editorial and publication decisions.

## License

Unless a file states otherwise, this material is licensed under **CC BY-NC-SA 4.0**.
