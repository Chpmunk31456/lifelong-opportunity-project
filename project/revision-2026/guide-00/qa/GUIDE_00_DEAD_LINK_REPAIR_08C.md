# Guide 00 — Confirmed Dead-Link Repair 08C

**Guide:** 00 — Lifelong Opportunity Foundation Guide
**Branch:** `revision/guide-00-100-2026`
**Repair date:** 2026-08-22
**Status:** PASS

## Defect

Publication live-link preflight returned HTTP **404** for `https://programasparaelbienestar.gob.mx/jovenes-construyendo-el-futuro/`.
The guide already retained the official Jóvenes Construyendo el Futuro program homepage; the dead duplicate was replaced with the current official STPS apprentice information page rather than weakening the link gate.

## Controlled replacement

- Removed: `https://programasparaelbienestar.gob.mx/jovenes-construyendo-el-futuro/`
- Added: `https://www.jovenesconstruyendoelfuturo.stps.gob.mx/aprendiz`
- Replacement class: official Secretaría del Trabajo y Previsión Social / Jóvenes Construyendo el Futuro page
- Claim text changed: **NO — URL-only maintenance**
- Trilingual URL-set cardinality after repair: **27**
- Trilingual URL-set parity after repair: **PASS**

## Source blobs

- **en:** `1a2d9e709ee70e49d6fec75e45710782851f234b` -> `8244a3b104b20a0ffd54825d195b471f24fa474e` (replacement count 1)
- **es-419:** `ecb072697eb6faab41fc752fa6d8744c34e3bbfd` -> `2514e1c86b2e4908d58d5d9cf5527d04a64c0ab2` (replacement count 1)
- **pt-BR:** `5e42545073518337d29c95c04879aec08d6465db` -> `e21b0249cdd856f01ff109d8dcab45ba589152c9` (replacement count 1)

The English source changed only by this URL replacement. The prior English freeze is therefore amended below and final Trilingual Technical QA must rerun before Publication requalification resumes.
