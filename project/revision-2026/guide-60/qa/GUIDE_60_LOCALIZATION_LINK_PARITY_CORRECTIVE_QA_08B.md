# Guide 60 — Localization Link Parity Corrective QA 08B

**Stage:** Corrective Localization / Technical QA — **PASS**

The controlled Spanish (`es-419`) and Brazilian Portuguese (`pt-BR`) masters were corrected to restore exact source-link parity with the frozen English master. No occupational facts, controlled wage values, jurisdiction mappings, role-scope boundaries, safeguarding language, privacy controls, cybersecurity controls, AI-use boundaries, or substantive localization prose were changed.

Corrected parity items:

- Government of Canada Job Bank NOC 42201 requirements URL restored to `https://www.jobbank.gc.ca/marketreport/requirements/5112/ca`.
- Government of Canada Job Bank NOC 42201 wages URL restored to `https://www.jobbank.gc.ca/wagereport/occupation/5121`.
- SENA Betowa URL restored to the frozen English query string including `modality=V`, `offertype=open`, and `programId=144936`.

Post-correction review confirms the Spanish and Portuguese source sections now use the same controlled Canada and SENA URLs as the frozen English source.

This corrective QA preserves the existing Spanish Localization, Portuguese Localization, and Technical QA PASS decisions. Publication and Release Audit remain fail-closed until the trilingual DOCX/PDF build, searchable-text checks, all-page rendering, clipping checks, metadata, manifest, and SHA-256 checksum gates pass.
