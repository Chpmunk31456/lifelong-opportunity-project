# Guide 17 — English v2 Editorial and Accessibility QA

**Guide:** 17 — Bank Teller and Member Services Representative  
**Date:** 2026-08-09  
**Artifact reviewed:** `references/english-v2-working-master.md`  
**Gate:** Editorial, readability, accessibility, structure, and encoding review  
**Decision:** **PASS**  

This QA record evaluates the English v2 working master as a controlled editorial artifact. It does not constitute independent human review, legal review, professional accessibility certification, regulator approval, accreditation, or publication approval. Claim-to-source traceability and link/freshness validation remain separate downstream gates.

## 1. Structure

**PASS.** The working master contains the required 19 substantive sections in the controlled order:

1. purpose and scope;
2. role definition and boundaries;
3. common job titles and employer settings;
4. daily work and responsibilities;
5. skills and tools;
6. entry requirements;
7. United States pathway;
8. Canada pathway;
9. Latin America and Colombia pathway;
10. free and low-cost learning;
11. funding, scholarships, and employer support;
12. apprenticeship and work-based learning;
13. income and labor-market research;
14. accessibility and accommodations;
15. privacy, cybersecurity, and fraud awareness;
16. responsible AI use;
17. job-search and interview preparation;
18. twelve-week entry plan and progression options;
19. verification checklist, sources, disclaimers, authorship, and license.

The heading hierarchy is descriptive and sequential. Country-specific material is clearly labeled.

## 2. Spelling, grammar, punctuation, and style

**PASS.** Review found no material spelling, grammar, or punctuation defect requiring correction before the next gate.

Editorial controls confirmed:

- complete sentences are used for explanatory prose;
- bullets are used where scanning is more useful than paragraphs;
- terminology is consistent with the occupational context;
- jargon is either avoided or explained in context;
- regulatory or compliance language is framed as boundaries and verification requirements rather than unsupported legal conclusions;
- the guide avoids hype, guarantees, artificial urgency, and training-provider marketing language;
- private salary estimates are not blended into official statistics;
- employer-dependent requirements are presented conditionally rather than universally.

## 3. Natural human readability

**PASS.** The text is written as practical career guidance rather than as a source dump or keyword list.

Controls confirmed:

- paragraphs are generally short;
- major decisions are introduced before details;
- warnings appear close to the action they govern;
- the guide explains why teller work can be an entry point while also stating the U.S. structural employment decline;
- the free-first strategy is expressed in concrete steps;
- the 12-week plan uses realistic sequential actions;
- interview preparation uses practical questions rather than generic motivational language;
- progression paths are clearly described as possibilities rather than promises.

## 4. Accessibility-oriented content design

**PASS at editorial-content level.** This is not a WCAG certification and does not evaluate final DOCX/PDF rendering.

Controls confirmed:

- no critical meaning depends on color;
- headings are descriptive rather than decorative;
- acronyms and formal program names are explained by surrounding text;
- checklists and numbered procedures are used for multi-step decisions;
- country and jurisdiction changes are visibly signposted;
- required, conditional, recommended, and optional concepts are distinguished in ordinary language;
- cost warnings appear before enrollment/payment decisions;
- sensitive-data warnings appear before AI and cybersecurity use cases;
- accessibility/accommodation content does not promise a specific accommodation outcome.

Final DOCX/PDF accessibility remains a downstream artifact-level gate.

## 5. Encoding and character review

**PASS for the Markdown working master.** The file was created as UTF-8 text through the repository contents API. Review found no intentional BOM requirement, mojibake, replacement characters, broken smart-quote substitutions, or malformed accent characters in Spanish proper names used inside the English guide.

Final generated DOCX/PDF encoding and extraction quality remain downstream checks.

## 6. Safety, privacy, cybersecurity, and responsible-AI framing

**PASS.** The guide:

- teaches escalation when authority is exceeded;
- does not authorize tellers to approve loans, originate regulated mortgages, provide investment/legal/tax advice, or override financial-crime, privacy, fraud, or authentication controls;
- instructs readers not to place real customer data or confidential institution information into public AI tools;
- limits AI examples to lower-risk learning uses using fictional or public information;
- states that AI does not replace employer policy, approved systems, compliance processes, human review, or authorized decision making;
- avoids describing suspicious-activity handling in a way that would instruct readers to circumvent controls.

## 7. Geographic coverage

**PASS at editorial level.** The guide contains substantive, separately labeled pathways for:

- United States;
- Canada;
- Latin America generally;
- Colombia specifically.

It does not present Latin America as a single regulatory or credentialing system. Colombia’s SENA examples are explicitly described as dynamic offerings requiring live verification.

## 8. Funding and training coverage

**PASS at editorial level.** The working master includes:

- employer onboarding and on-the-job training;
- free/low-cost learning;
- FAFSA when an eligible college/career-school program and learner qualify;
- scholarships without guarantee language;
- WIOA/American Job Center verification;
- employer educational assistance under Section 127 with plan/eligibility caveats;
- SENA as a Colombia free-first pathway where a relevant live offering exists;
- apprenticeship/work-based learning with an explicit teller-status discrepancy rather than an unsupported categorical claim.

## 9. Income-research presentation

**PASS at editorial level.** The master clearly separates:

- official U.S. BLS evidence;
- official Canada Job Bank evidence;
- current non-government U.S. estimates from Indeed, ZipRecruiter, and Salary.com.

The text does not average incompatible sources, represent private estimates as official data, or guarantee individual pay. It deliberately withholds a May 2025 BLS teller wage from the directly verified official box pending direct occupation-table capture.

Numerical verification remains part of claim-to-source traceability QA.

## 10. Versioning and publication status

**PASS.** The artifact is explicitly labeled as a **Controlled English v2 working master**, with revision date 2026-08-09. It expressly states that it is not yet source-frozen, localized, or publication-ready. The legacy English publication README has therefore not been silently overwritten at this gate.

## Gate conclusion

**Editorial/accessibility gate: PASS.**

The next controlled gate is **claim-to-source traceability**, including re-verification of all numerical, occupational, funding, apprenticeship, and jurisdiction-specific claims against the controlled source ledger and live authoritative sources where required. Link/freshness, terminology, structural, and source-freeze gates remain open after that review.
