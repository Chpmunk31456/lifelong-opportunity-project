# Guide 17 — English v2 source freeze

**Guide:** 17 — Bank Teller and Member Services Representative  
**Freeze date:** 2026-08-09  
**Frozen artifact:** `references/english-v2-working-master.md`  
**Frozen master blob SHA:** `c6719ff7e5d848c557d173ef64934548af87ba33`  
**Corrected branch head reviewed before this freeze:** `5403664434e561a314463e7d3b1207a583def35b`  
**Gate:** English localization source freeze  
**Decision:** **PASS — frozen for localization**

## Evidence used for this decision

1. `english-v2-reconciliation.md` — controlled legacy-to-v2 reconciliation completed before construction of the working master.
2. `english-v2-editorial-accessibility-qa.md` — **PASS** for structure, spelling, grammar, style, natural readability, accessibility-oriented content design, and encoding at the editorial-content level.
3. `english-v2-traceability-qa-recheck.md` — **PASS** for claim-to-source traceability and freshness after the earlier controlled correction cycle.
4. `english-v2-link-terminology-structure-encoding-qa.md` — preserved historical **FAIL CLOSED** because private-market salary snapshots had changed. The same record states that terminology, structure, encoding, country labeling, occupational boundaries, apprenticeship caution, disclaimers, and principal official-reference reachability passed subject to those freshness corrections.
5. `english-v2-private-income-recheck-2026-08-09.md` — **PASS** for the affected private-income source-state and traceability correction. It confirms that the corrected working master keeps private estimates separate from official BLS statistics and removes the defect that blocked the prior technical pre-freeze gate.

The historical FAIL record is intentionally retained. This source-freeze decision does not rewrite it or claim that the earlier snapshot was correct; it documents that the specific blocking freshness defect was subsequently corrected and rechecked while the unaffected technical controls had already passed.

## Frozen-source controls

The English v2 localization source is frozen with the following controlled characteristics:

- 19 required substantive sections in the approved order;
- practical, natural English with no material editorial defect identified by the controlled editorial gate;
- explicit United States, Canada, Latin America, and Colombia pathways where relevant;
- funding, scholarships, employer support, free/low-cost learning, and work-based-learning guidance with verification boundaries;
- official labor-market and income evidence kept distinct from clearly labeled non-government estimates;
- cautious treatment of Registered Apprenticeship where source pages conflict;
- privacy, cybersecurity, fraud-escalation, accessibility, and responsible-AI boundaries;
- no employment, income, credential, accreditation, regulator-approval, or independent-human-review guarantee;
- UTF-8 source content with the prior technical gate reporting no obvious mojibake, replacement-character artifact, or leading BOM artifact.

## What this PASS authorizes

This PASS authorizes creation of the neutral Latin American Spanish (`es-419`) and Brazilian Portuguese (`pt-BR`) editions from this exact frozen English source.

It does **not** authorize final publication or release. The localized editions must still pass their own terminology, structural, semantic-parity, link, encoding, accessibility-oriented, and source-reference checks. DOCX/PDF generation, metadata, checksums where required, rendering/package QA, publication QA, and release audit also remain downstream.

If the English master changes after this freeze, this record becomes stale and a new controlled freeze must be created before localization continues.

## Certification boundary

This is an internal controlled source-freeze record. It is not independent human review, professional translation certification, accessibility certification, accreditation, legal review, regulator approval, financial advice, employment advice certification, or publication approval.
