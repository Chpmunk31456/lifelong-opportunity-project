# Lifelong Opportunity Guide 91 — Cloud Support Specialist

**Version:** 2.0 controlled working master  
**Language:** English  
**Primary U.S. benchmark:** O*NET-SOC 15-1231.00 — Computer Network Support Specialists  
**Canada comparisons:** NOC 22220 — Computer network and web technicians; NOC 22221 — User support technicians  
**Colombia comparisons:** CUOC 35130 — Técnicos en redes y tecnologías de la información; CUOC 35121 — Técnicos en asistencia y soporte de tecnologías de la información  
**Review date:** 2026-08-22

## What this career is

A Cloud Support Specialist helps keep cloud-hosted systems and services available, usable, secure and supportable. Depending on the employer, the work may involve identity and access, virtual networks, DNS, compute, storage, databases at a support level, monitoring, logs, incidents, backups, SaaS/application support, provider escalation and controlled production changes.

The title is broad. Some cloud-support roles are infrastructure-heavy and resemble network/system support. Others primarily support users and cloud applications. Some sit close to Cloud Administrator or Cloud Engineer work. Duties, permissions and escalation boundaries matter more than the title.

For the United States, the strongest current benchmark is **O*NET-SOC 15-1231.00 — Computer Network Support Specialists** because O*NET explicitly includes **cloud networks** and lists **Cloud Support Specialist** and **Junior Cloud Engineer (Nof)** as approved Registered Apprenticeship titles. Canada and Colombia require a two-scope model rather than one forced classification.

## Role scope by function

### Infrastructure/cloud-network support
Typical work may include virtual networks, routing, DNS, security groups/firewall rules, connectivity, compute/storage health, monitoring, backups and privileged platform support. This aligns more closely with **Canada NOC 22220** and **Colombia CUOC 35130**.

### User/application cloud support
Typical work may include SaaS access, application incidents, deployment/client issues, user configuration, communications software and first-line cloud-application troubleshooting. This aligns more closely with **Canada NOC 22221** and **Colombia CUOC 35121**.

### Adjacent roles
- **Help Desk/User Support:** broader first-line endpoint/application support.
- **Network Support:** connectivity, routing, DNS, network devices and cloud networks.
- **Cloud Administrator:** usually broader configuration/governance authority.
- **Cloud Engineer:** usually deeper design, build, automation and infrastructure-as-code responsibility.
- **SRE/DevOps:** generally broader reliability, automation and software-delivery engineering.

Do not assume that a Cloud Support Specialist owns architecture, security exceptions, budget, IAM policy design or production release authority unless the employer explicitly assigns those responsibilities.

## Start with impact and scope

Before troubleshooting, identify:
1. who or what is affected;
2. business/service impact;
3. account, tenant, subscription or project;
4. region/zone and environment;
5. resource or service involved;
6. timestamps;
7. recent changes;
8. authorization level;
9. available logs/metrics;
10. escalation path.

This prevents broad, risky changes made only to “see if it works.”

## Cloud account and resource hierarchy

Understand provider-specific versions of:
- organization/account/tenant;
- subscription/project/account;
- resource groups/folders/projects;
- regions and availability zones;
- resource names/IDs;
- tags/labels;
- quotas/service limits;
- billing/cost ownership.

Exact terminology differs across AWS, Azure, Google Cloud and other providers. Always verify the active target before a command or change.

## Shared responsibility

Cloud providers operate and secure portions of the platform; customers retain responsibilities that vary by service model and configuration. Managed service does **not** mean:
- the provider configures customer IAM correctly;
- customer data classification disappears;
- application vulnerabilities become the provider's responsibility;
- backups and recovery are automatically correct;
- network/firewall rules cannot be misconfigured;
- customer logging and monitoring requirements disappear.

Use the exact provider/service documentation rather than memorizing one generic responsibility chart.

## Identity, MFA and least privilege

Cloud support can involve powerful access. Required habits include:
- named identities;
- approved authentication methods;
- MFA where required;
- least privilege;
- temporary/elevated access where supported;
- careful handling of service accounts/workload identities;
- scope verification before changing roles or policies;
- escalation of suspicious access.

Never paste passwords, API keys, tokens, signing keys, certificates or other secrets into tickets, chat, public repositories or unapproved AI tools. Support access is not blanket authority to inspect all customer data or modify every resource.

## Compute foundations

Support-level concepts may include:
- virtual machines/instances;
- images/templates;
- instance size/type;
- startup/shutdown/restart behavior;
- disks/volumes;
- autoscaling concepts;
- containers and managed compute conceptually;
- health checks;
- quotas;
- operating-system access boundaries.

A restart may temporarily clear a symptom without establishing root cause. Capture evidence before destructive or state-changing actions when policy requires it.

## Storage foundations

Understand basic differences among:
- object storage;
- block storage;
- file storage;
- lifecycle/retention rules;
- encryption/access;
- redundancy options;
- snapshots/backups;
- versioning where available.

Do not change retention, encryption, public-access or replication settings without authority and impact review.

## Cloud networking foundations

A support specialist should understand:
- VPC/VNet/virtual networks;
- subnets;
- route tables;
- security groups/firewall rules;
- public/private IP addressing;
- NAT concepts;
- load balancers;
- DNS;
- VPN/private connectivity;
- ports/protocols;
- latency and packet path;
- certificates/TLS at a support level.

Troubleshoot the path layer by layer. A timeout can result from DNS, routing, firewall rules, service health, application behavior, certificate problems or dependency failure.

## DNS troubleshooting

Check:
- expected hostname;
- resolver path;
- record type/value;
- TTL/cache effects;
- private versus public zones;
- recent changes;
- certificate/hostname alignment;
- whether the destination service is actually healthy.

Avoid broad DNS changes when the evidence points to another layer.

## Logs, metrics, traces and alerts

Useful evidence can include:
- platform activity/audit logs;
- authentication logs;
- network-flow logs;
- system/application logs;
- metrics;
- traces;
- dashboards;
- alerts;
- provider service-health notices.

Logs may contain confidential or personal data. Follow approved access, retention, export and sharing requirements. Do not attach large protected log bundles to tickets when a minimal sanitized excerpt is sufficient.

## Repeatable troubleshooting workflow

1. Identify impact and urgency.
2. Confirm target account/resource/region/environment.
3. Confirm timestamps and recent changes.
4. Check provider and service health.
5. Review relevant logs, metrics and alerts.
6. Isolate identity, network, compute, storage, application or dependency layer.
7. Test one hypothesis at a time.
8. Use only authorized remediation.
9. Verify restoration from the user/service perspective.
10. Document evidence, actions, outcome and escalation.

Good support evidence is reproducible. “It works now” is weaker than documenting the actual symptom, evidence, change and validation.

## Incident and escalation discipline

Use organizational impact/urgency definitions. Escalate when:
- privileged change exceeds your authority;
- security/privacy impact is suspected;
- data loss or corruption may have occurred;
- provider-wide or cross-region failure is suspected;
- RPO/RTO or contractual objectives are at risk;
- the root cause is outside support scope;
- architecture redesign is required.

Do not promise a root cause or resolution time without evidence and authority.

## Backup, snapshot and recoverability

A successful backup job or snapshot does **not** prove recoverability. Understand:
- backup scope;
- retention;
- encryption/access;
- account/region separation where required;
- restore testing;
- RPO and RTO concepts;
- application consistency;
- dependency ordering;
- disaster-recovery ownership.

**Replication is not automatically a backup.** Deletion or corruption can replicate. Recovery claims should be based on tested recovery evidence, not only job-success indicators.

## Regions, zones and resilience

Regions and availability zones can reduce some failure risks, but resilience depends on architecture and service configuration. Multi-zone or multi-region design can add cost, consistency, latency and operational complexity.

A support specialist may gather evidence and execute approved runbooks, but should not redesign resilience architecture outside assigned authority.

## Change management and production authority

Cloud changes may affect IAM, firewall/security groups, compute, storage, DNS, routes, certificates, service parameters, monitoring, backups or deployments.

Before change, confirm:
- authorization;
- exact target and scope;
- expected impact;
- maintenance window if applicable;
- rollback or forward-fix plan;
- backup/recovery implications;
- validation plan;
- communication/escalation requirements.

Technical access does not equal production authority.

## CLI, scripting and infrastructure as code

Cloud CLIs, PowerShell, Bash, Python and infrastructure-as-code tools can make changes quickly and at scale. Use approved repositories/devices, avoid hard-coded secrets, peer-review changes where required, test lower-risk environments when feasible, verify target account/region before execution and capture version/plan/output evidence.

Do not paste destructive commands from forums or AI tools into production without understanding and reviewing them.

## Cost awareness

Support work can affect cost through instance size/count, storage, data transfer, snapshots, logging retention, managed services and abandoned resources. Cost optimization belongs within assigned authority; do not delete resources solely because they appear idle.

## Privacy and data residency

Cloud support can expose personal, customer, regulated or confidential data. Follow approved rules for access, retention, export, region/location, test data and incident handling. Do not invent legal requirements; escalate legal/privacy interpretation to the responsible function.

## Security support boundary

A support specialist may investigate suspicious logins, exposure, misconfiguration or connectivity issues, but security testing and incident response must remain within explicit authorization. Do not run intrusive scans, exploitation or destructive tests against cloud resources without permission.

Useful baseline references include NIST Cybersecurity Framework and CISA Secure Our World. Provider shared-responsibility documentation remains important for service-specific boundaries.

## Accessibility

Cloud support also includes the way users interact with portals, support documentation, dashboards and tickets. Provide clear headings, readable instructions, keyboard-friendly workflows, descriptive labels and accessible alternatives where practical. Automated checks can help identify issues but do not by themselves prove legal accessibility compliance.

## Responsible AI

Policy-approved AI can help explain error messages, draft runbooks, summarize sanitized logs, propose troubleshooting hypotheses, create synthetic practice scenarios or help review scripts.

Controls:
- do not submit secrets, credentials, customer data, proprietary architecture or protected logs to unapproved tools;
- verify generated commands against official documentation;
- review target account/region/resource before execution;
- validate generated code/scripts;
- treat AI explanations as hypotheses, not evidence;
- never let AI autonomously approve or execute privileged production changes outside governance.

## Technology signals

O*NET/Lightcast 2025 postings for the broader Computer Network Support Specialist occupation include Microsoft Office **13%**, Microsoft Active Directory **13%**, ServiceNow **9%**, Linux **7%**, macOS **6%**, Windows Server **6%**, Outlook **6%**, Excel **6%**, Windows **5%**, BGP **3%**, Azure **3%**, PowerShell **2%**, and SQL/Python/Splunk/Bash around **1%** each. O*NET's demand page also identifies firewall software at **10%**.

These are posting signals for the broader occupation, not universal requirements. Vendor-cloud skills should sit on top of identity, networking, operating-system, monitoring and troubleshooting fundamentals.

## United States education and pathways

O*NET places 15-1231.00 in **Job Zone Four — Considerable Preparation Needed**. Current education responses are approximately:
- **47%** bachelor's degree;
- **22%** associate degree;
- **14%** some college, no degree.

These describe occupation-level responses, not universal hiring rules.

O*NET lists approved Registered Apprenticeship titles **Cloud Support Specialist** and **Junior Cloud Engineer (Nof)**. Verify live openings through Apprenticeship.gov. CareerOneStop can help locate WIOA and other training resources; eligibility and funding vary.

## United States wages and outlook

Official 2025 wages for **Computer Network Support Specialists** are:

| Percentile | Annual | Hourly |
|---|---:|---:|
| 10th | $47,120 | $22.65 |
| 25th | $58,240 | $28.00 |
| Median | $76,220 | $36.64 |
| 75th | $98,750 | $47.48 |
| 90th | $127,780 | $61.43 |

2024–2034:
- employment 2024: **152,700**;
- projected employment 2034: **155,500**;
- projected growth: **2%**;
- projected annual openings: **9,600**.

These are occupation-level support statistics, not a pure title-only Cloud Support Specialist series.

### Adjacent non-government market context

Indeed's current **Cloud Engineer** page reports approximately **$135,392/year average**, **$88,667 low**, **$206,741 high**, around **4.5k observations**, over the prior **36 months**, updated **August 2, 2026**.

This is an engineering-heavy adjacent title and may be materially higher-paid than support work. It is not official data and must not be presented as an exact Cloud Support Specialist salary.

## Canada — infrastructure/cloud-network scope

For infrastructure-heavy cloud support, use **NOC 22220 — Computer network and web technicians**.

National wages:
- **C$21.00/hour** low;
- **C$36.00/hour** median;
- **C$55.00/hour** high.

Job Bank says related college/other training is usually required and some employers may require vendor training/certification. Job Bank currently indicates registration with a regulatory body is required in **Saskatchewan** for this NOC. Verify the exact occupation and current provincial rules before relying on that statement.

## Canada — user/application scope

For user-facing SaaS/application cloud support, use **NOC 22221 — User support technicians**.

National wages:
- **C$20.50/hour** low;
- **C$31.47/hour** median;
- **C$49.00/hour** high.

Typical requirements include relevant college/programming/network-administration education or courses; some employers may require vendor training/certification. Cloud-platform skills can improve prospects, but the actual role scope should determine which NOC comparison is more appropriate.

## Colombia

For infrastructure/cloud-network work, **CUOC 35130 — Técnicos en redes y tecnologías de la información** is the stronger comparison. It covers network/infrastructure operation, troubleshooting, installation/configuration, backups/recovery and documentation.

For application/user-facing support, **CUOC 35121 — Técnicos en asistencia y soporte de tecnologías de la información** covers software, hardware, networks, databases, internet, deployment and support.

OCUPACOL warns that displayed historical labor-market indicators are not statistically representative under its methodology. This guide therefore does not invent a national Cloud Support Specialist wage from those indicators.

## Colombia — SENA pathways

### Programación de Aplicaciones y Servicios para la Nube
Current SENA Betowa evidence identifies:
- **Técnico**;
- **2,256 hours**;
- formación titulada;
- current virtual listings;
- cloud-oriented application/service, database and technical foundations.

This is substantial cloud-oriented training but is development-oriented as well as support-oriented.

### Implementación de Servicios de Computación en la Nube
Current SENA Betowa evidence identifies:
- complementary virtual training;
- **48 hours**;
- cloud-service concepts and technological network-infrastructure administration competency.

This is supplemental training, not equivalent to the 2,256-hour Técnico. Cohorts, seats, modality and admissions change; verify the live listing.

## Vendor learning

Readers can investigate Microsoft Learn Azure, AWS Skill Builder and Google Cloud Skills Boost. Some material may be free; exams, labs or credentials can cost money. Verify current pricing, regional access and employer relevance before paying.

## Safe portfolio ideas

Use only personal, sandbox, training, open-source or explicitly authorized environments. Examples:
- synthetic cloud incident ticket and escalation;
- public sandbox architecture diagram;
- IAM least-privilege review of a self-owned lab;
- DNS/connectivity troubleshooting write-up;
- monitoring dashboard from synthetic telemetry;
- backup/restore test plan for a lab resource;
- provider-status correlation exercise;
- simple IaC lab with no real credentials.

Never publish employer/customer accounts, architecture, keys, tokens, logs, vulnerability details or proprietary runbooks.

## Four-week starter plan

### Week 1 — foundations
Learn account hierarchy, regions/zones, compute, storage, networking, DNS and IAM concepts. Build a personal lab within a small budget or free sandbox and set cost alerts where available.

### Week 2 — troubleshooting
Practice structured incident tickets, service-health checks, logs/metrics, network path analysis and one-hypothesis-at-a-time troubleshooting.

### Week 3 — security and recovery
Practice MFA, least privilege, secrets hygiene, backup/restore concepts, RPO/RTO, audit logs and controlled change/rollback planning.

### Week 4 — evidence and job readiness
Create a safe portfolio, map job descriptions to infrastructure versus user-support scope, verify training options, practice scenario interviews and document what you can safely do versus what must be escalated.

## Interview preparation

Be ready to explain:
- how you would isolate a cloud connectivity issue;
- authentication versus authorization;
- least privilege and MFA;
- why a snapshot is not proof of recoverability;
- why replication is not automatically a backup;
- provider service health versus customer configuration;
- DNS troubleshooting;
- how to verify a target account/region before a command;
- when you would escalate a privileged change;
- how you would handle a suspected secret exposure;
- how you validate AI-generated troubleshooting advice.

## Employer due diligence

Ask:
- Which providers/services are supported?
- Is this infrastructure, SaaS/user support, or both?
- What production privileges does the role have?
- Is there on-call work?
- What incident/severity process is used?
- Who owns IAM/security exceptions?
- Who owns architecture and recovery design?
- What change/release controls apply?
- Are scripts/IaC reviewed?
- What training/certification support is offered?
- How are privacy, data residency and customer access handled?

## Reader verification links

1. https://www.onetonline.org/link/details/15-1231.00
2. https://www.onetonline.org/link/localwages/15-1231.00
3. https://www.onetonline.org/link/localtrends/15-1231.00
4. https://www.onetonline.org/link/hot_tech/15-1231.00
5. https://www.onetonline.org/link/demand/15-1231.00
6. https://www.careeronestop.org/LocalHelp/EmploymentAndTraining/find-WIOA-training-programs.aspx
7. https://www.apprenticeship.gov/
8. https://www.indeed.com/career/cloud-engineer/salaries
9. https://learn.microsoft.com/en-us/training/azure/
10. https://skillbuilder.aws/
11. https://www.cloudskillsboost.google/
12. https://www.jobbank.gc.ca/marketreport/summary-occupation/24514/ca
13. https://www.jobbank.gc.ca/wagereport/occupation/3757
14. https://www.jobbank.gc.ca/marketreport/summary-occupation/3772/ca
15. https://www.jobbank.gc.ca/marketreport/wages-occupation/3772/ca
16. https://www.canada.ca/en/services/jobs/training.html
17. https://ocupacol.mintrabajo.gov.co/Profile/OccupationalProfile/35130
18. https://ocupacol.mintrabajo.gov.co/Profile/OccupationalProfile/35121
19. https://betowa.sena.edu.co/oferta/programacion-de-aplicaciones-y-servicios-para-la-nube?modality=V&programId=165934
20. https://betowa.sena.edu.co/oferta/implementacion-de-servicios-de-computacion-en-la-nube?modality=V&programId=229523
21. https://www.oitcinterfor.org/statsfp/paises
22. https://aws.amazon.com/compliance/shared-responsibility-model/
23. https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility
24. https://cloud.google.com/architecture/framework/security/shared-responsibility-shared-fate
25. https://www.nist.gov/cyberframework
26. https://www.nist.gov/privacy-framework
27. https://www.nist.gov/itl/ai-risk-management-framework
28. https://www.cisa.gov/secure-our-world
29. https://www.section508.gov/create/
30. https://www.w3.org/TR/WCAG22/

## Important limits

This guide provides career-planning and educational information. It does not guarantee employment, compensation, admission, funding, apprenticeship placement, certification, cloud-service availability or promotion. It does not provide legal, privacy, cybersecurity, architecture, recovery, vendor or accessibility certification. Language editions are controlled project localizations, not certified translations.
