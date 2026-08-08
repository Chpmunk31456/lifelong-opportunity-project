# Evidence / Traceability Helper

## Mission
Demonstrate that material factual claims in the English working master are supported by current evidence before source freeze.

## Required inputs
- English working master.
- Research Helper evidence register.
- Existing guide QA records.

## Required checks
For each material claim, classify it as:
- supported by cited/recorded source;
- reasonable general guidance not requiring an external factual citation;
- qualified estimate/opinion;
- unsupported;
- contradicted;
- stale/needs refresh.

Verify numbers, dates, wage units, percentages, jurisdiction, credential names, regulator names, training duration, costs, and availability language against the evidence register.

## Required output
Create a claim-to-source traceability matrix in the guide QA directory. Record the claim or section, source, support status, any caveat, and disposition. Record all unsupported or contradicted claims explicitly.

## PASS conditions
PASS only when every material claim is supported, qualified, removed, or explicitly blocked and no contradicted claim remains in the proposed frozen English source.

## Blocking conditions
- Unsupported material wage, licensing, safety, legal, education, funding, or credential claim.
- Numeric/date mismatch that changes meaning.
- Source does not actually support the attributed statement.
