# Guide Helper Status Manifest Contract

This contract provides a machine-readable handoff between the controlled helper roles in `project/helpers/`.

## Required file

Each active revision guide should maintain:

`project/revision-2026/guide-NN/GUIDE_NN_HELPER_STATUS.json`

## Required fields

```json
{
  "guide": "NN",
  "occupation": "Occupation title",
  "branch": "revision/guide-00-100-2026",
  "updated": "YYYY-MM-DD",
  "stages": {
    "research": {"status": "PENDING", "evidence": []},
    "english_editorial": {"status": "PENDING", "evidence": []},
    "evidence_traceability": {"status": "PENDING", "evidence": []},
    "english_source_freeze": {"status": "PENDING", "evidence": []},
    "spanish_localization": {"status": "PENDING", "evidence": []},
    "portuguese_localization": {"status": "PENDING", "evidence": []},
    "technical_qa": {"status": "PENDING", "evidence": []},
    "publication": {"status": "PENDING", "evidence": []},
    "release_audit": {"status": "PENDING", "evidence": []}
  },
  "blockers": []
}
```

Allowed stage statuses are `PENDING`, `PASS`, `FAIL`, and `BLOCKED`.

## Gate dependencies

- `english_editorial` requires `research=PASS`.
- `evidence_traceability` requires `research=PASS` and `english_editorial=PASS`.
- `english_source_freeze` requires `research`, `english_editorial`, and `evidence_traceability` all `PASS`.
- Spanish and Portuguese localization require `english_source_freeze=PASS`.
- `technical_qa` requires both localization stages `PASS`.
- `publication` requires `technical_qa=PASS`.
- `release_audit` requires `publication=PASS` and must independently confirm all required evidence.

## Evidence rules

Every `PASS` stage must cite at least one repository-relative evidence path. Evidence paths must exist on the controlled revision branch. A status entry may not claim independent human certification unless such evidence actually exists.

The manifest is a coordination record, not proof by itself. The Release Auditor must inspect the underlying evidence.
