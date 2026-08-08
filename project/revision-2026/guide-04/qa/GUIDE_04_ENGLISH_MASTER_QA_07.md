# Guide 04 — English Working Master QA 07

Date: 2026-08-08  
Branch: `revision/guide-00-100-2026`  
Guide: 04 — Project Coordinator  
English input: `project/revision-2026/guide-04/working/GUIDE_04_ENGLISH_WORKING_MASTER_06.md`  
English master commit: `5146accdffe359465d326bf71e75336fc8817294`

## Purpose

Run the controlled factual, editorial, terminology, accessibility, encoding, link, source-labeling, and structural review required before the English meaning is frozen for translation. This is an internal QA decision. It is not independent human certification, accreditation, legal advice, accessibility certification, endorsement by any source organization, or final publication approval.

## Controlled inputs

- Current-source evidence intake: `GUIDE_04_CURRENT_SOURCE_EVIDENCE_INTAKE_02.md`, commit `f0aba4e7bb1c52a5e951d38ba946c754f2bb392b`.
- Deterministic legacy extraction/reconciliation evidence: commit `471cbead5bdc324d2520acab34dcbf4c13035942`, workflow run `31243218561`.
- Composite-source decision: `GUIDE_04_COMPOSITE_SOURCE_DECISION_05.md`, commit `e428eac87d55efcb28255493826eb6b50abdba25`.
- Revised English working master: `GUIDE_04_ENGLISH_WORKING_MASTER_06.md`, commit `5146accdffe359465d326bf71e75336fc8817294`.

## Factual and source-control review

**PASS.** High-impact factual claims in the English master are constrained to the current evidence gate or explicitly framed as variable guidance.

Verified controls:

- The U.S. Bureau of Labor Statistics Project Management Specialists series is labeled a **broader occupational anchor/proxy**, not an exact-title Project Coordinator wage.
- The BLS values carried into the master are the controlled evidence values: **US$100,750 median annual wage in May 2024**, **6% projected growth from 2024 to 2034**, and approximately **78,200 openings per year on average** for the broader occupation.
- The exact-title Project Coordinator figure is separately labeled **non-government market evidence**: ZipRecruiter displayed **US$59,915/year (US$28.81/hour), “As of Jul 20, 2026,”** when checked for the August 8, 2026 evidence intake.
- The guide does not extrapolate U.S. or Canadian wages to Colombia or Latin America.
- Canadian wage use is conditioned on matching duties, industry, location, and NOC rather than title alone.
- SENA program examples and the February 2026 free-place statement are attributed to the current controlled evidence; the master warns that intake, modality, location, prerequisites, dates, and admission vary.
- American Job Center/WIOA assistance is described as eligibility- and program-dependent, not guaranteed.
- Federal student aid and scholarships are described as eligibility- and school/program-participation dependent, not guaranteed.
- Registered Apprenticeship is accurately framed as a paid, employer-driven pathway while explicitly avoiding any claim that a generic Project Coordinator apprenticeship is universally available.
- Employer tuition, reimbursement, paid learning, and professional-development benefits are described as employer-specific rather than entitlements.
- The unsupported legacy statement that an employer education service period “may last up to two years” was removed. The revised master states that any required employment period and repayment terms are employer-, contract-, and jurisdiction-specific.
- The legacy healthcare-specific work-based-learning spillover was removed rather than being generalized to Project Coordinator work.
- No credential is presented as a universal legal requirement for Project Coordinator work.
- CAPM, PMP, Scrum, Agile, platform, and tool credentials are described as optional or employer-dependent unless a specific vacancy or progression path requires them.
- The guide does not claim that remote work, employment, promotion, funding, salary, credential recognition, or apprenticeship placement is guaranteed.

## Editorial and natural-readability review

**PASS.** The master was rewritten as a coherent career guide rather than a mechanical patch of the legacy edition.

Controls checked:

- plain-English explanations precede specialized terms;
- long or ambiguous legacy sentences were rewritten;
- repetitive healthcare/licensing template language that did not fit this occupation was removed;
- duties, authority, and escalation boundaries are stated in occupation-appropriate language;
- headings follow a logical reader journey from role understanding through pay, learning, funding, geography, accessibility, security, portfolio evidence, interviews, entry, advancement, decision-making, and maintenance;
- lists are used for comparisons/checklists and numbered sequences are used only where order matters;
- unsupported certainty and promotional language were removed;
- U.S., Canada, Colombia, and broader Latin America sections are clearly distinguished;
- non-government income research is visibly separated from official occupational evidence; and
- the AI-assistance disclosure preserves human accountability and avoids any claim of independent human certification.

## Terminology review

**PASS.** Controlled terminology is internally consistent.

- `Project Coordinator` refers to the broad job title being discussed.
- `Project Management Specialists (SOC 13-1082)` refers specifically to the BLS occupational proxy.
- `Registered Apprenticeship` is not used as a synonym for internship, ordinary training, pre-apprenticeship, co-op, practicum, or trainee work.
- `National Occupational Classification (NOC)` is introduced before the abbreviation is relied upon in the Canada section.
- `Workforce Innovation and Opportunity Act (WIOA)` is expanded on first substantive use.
- `Free Application for Federal Student Aid (FAFSA)` is expanded on first use.
- `Servicio Público de Empleo (SPE)` is expanded before abbreviation.
- Credential names are examples, not implied mandates.

## Accessibility and inclusive-design review

**PASS for source-format controls; final rendered accessibility remains a later publication gate.**

The Markdown source:

- uses descriptive hierarchical headings;
- uses descriptive link text rather than bare URLs for reader-facing navigation except where source identity itself is useful;
- does not rely on color to communicate meaning;
- uses text tables with explicit headers for worksheets;
- provides prose equivalents for all substantive concepts rather than relying on visual diagrams;
- includes accommodation considerations across education, testing, apprenticeship/work-based learning, and employment;
- explicitly asks readers to evaluate accessibility across the full pathway;
- includes accessible-document and inclusive-meeting practices; and
- avoids claiming that this internal review is an accessibility certification.

DOCX/PDF semantic structure, tagged output where supported, reading order, table rendering, hyperlink rendering, page breaks, and visual contrast remain publication-artifact QA items.

## Privacy, cybersecurity, and ethical-AI review

**PASS.** The revised master includes occupation-appropriate controls for:

- approved systems and accounts;
- multifactor authentication where required or available;
- least-privilege/role-based access;
- project repositories and personal-storage boundaries;
- confidential customer, employee, financial, health, security, procurement, and proprietary information;
- meeting notes and recordings;
- retention, legal-hold, records-management, and deletion rules;
- public versus approved enterprise AI tools;
- verification of AI-generated facts, calculations, citations, status, dates, actions, and summaries; and
- human accountability for project records and communications.

## Encoding and structural review

**PASS at Markdown source stage.** The controlled master is stored as UTF-8 text through GitHub’s contents API and uses standard Markdown structure. No visible UTF-8 BOM, mojibake substitution, or legacy encoding artifact was introduced in the controlled master.

The source contains:

- version and controlled status;
- license statement;
- authorship/AI-assistance disclosure;
- ethical limits;
- role definition and boundaries;
- duties/tools/work cycle;
- fit/sustainability;
- income/outlook with source labels;
- education/credentials;
- funding/scholarships/employer support/apprenticeship controls;
- U.S., Canada, Colombia, and Latin America coverage;
- accessibility;
- privacy/cybersecurity/ethical AI;
- portfolio and résumé evidence;
- interview preparation;
- 30/60/90-day plan;
- advancement/exit planning;
- verification checklist;
- twelve-week plan;
- worksheets;
- sources; and
- versioning/maintenance controls.

## Link review

**PASS for controlled-source inclusion; repeat HTTP/link integrity testing at publication-candidate QA.**

The reader-facing links are limited primarily to official public sources plus the clearly labeled ZipRecruiter non-government salary source already captured in the current-source evidence intake. Source identity and intended use are stated near the links. Mutable salary data and live training availability are explicitly marked for recheck before publication.

This gate does not substitute for the later automated external-link validation required before publication-candidate status.

## Translation-control decision

**PASS — freeze English Working Master 06 for semantic translation.**

The English meaning may now be used as the controlled source for:

1. neutral Latin American Spanish; and
2. Brazilian Portuguese.

Translation rules:

- preserve the distinction between official occupational proxy data and exact-title non-government market evidence;
- preserve all uncertainty, eligibility, variability, and no-guarantee language;
- do not localize U.S. or Canadian salary numbers into Latin American salary claims;
- retain Colombia-specific public pathways accurately;
- translate organization/program names conservatively and preserve official names where changing them would impede verification;
- keep `Registered Apprenticeship` conceptually distinct from generic apprenticeship/internship terminology;
- preserve privacy, cybersecurity, accessibility, ethical-AI, repayment, and scope-of-authority controls;
- do not introduce credentials, legal requirements, pay claims, scholarships, or pathways that are absent from the controlled English source without a new evidence gate; and
- record any necessary translator note or jurisdictional adaptation rather than silently changing meaning.

## Current QA gate

English factual/editorial/source/accessibility-source QA is closed. The next sequential gate is **neutral Latin American Spanish translation from frozen English Working Master 06**, followed by Spanish terminology/structure/link/source-parity QA. Brazilian Portuguese must follow from the same frozen English meaning after Spanish is controlled; neither translation is a publication candidate until its QA passes.

## Controlled decision

**PASS — English master frozen for translation.**  
**HOLD — final publication status remains prohibited until trilingual parity, DOCX, PDF, metadata, rendering, link, checksum, and publication QA are complete.**
