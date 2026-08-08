#!/usr/bin/env python3
"""Validate controlled helper status manifests for Lifelong Opportunity Guides.

This is a coordination and evidence-presence gate. It does not certify factual
accuracy, translation quality, accessibility, legal compliance, or human review.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ALLOWED = {"PENDING", "PASS", "FAIL", "BLOCKED"}
ORDER = [
    "research",
    "english_editorial",
    "evidence_traceability",
    "english_source_freeze",
    "spanish_localization",
    "portuguese_localization",
    "technical_qa",
    "publication",
    "release_audit",
]
DEPENDENCIES = {
    "english_editorial": ["research"],
    "evidence_traceability": ["research", "english_editorial"],
    "english_source_freeze": ["research", "english_editorial", "evidence_traceability"],
    "spanish_localization": ["english_source_freeze"],
    "portuguese_localization": ["english_source_freeze"],
    "technical_qa": ["spanish_localization", "portuguese_localization"],
    "publication": ["technical_qa"],
    "release_audit": ["publication"],
}


def manifest_path(guide: str) -> Path:
    return ROOT / f"project/revision-2026/guide-{guide}/GUIDE_{guide}_HELPER_STATUS.json"


def validate(guide: str, target: str | None) -> int:
    path = manifest_path(guide)
    if not path.is_file():
        raise SystemExit(f"Missing helper status manifest: {path.relative_to(ROOT)}")
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("guide") != guide:
        raise SystemExit(f"Manifest guide mismatch: expected {guide!r}, got {data.get('guide')!r}")
    if data.get("branch") != "revision/guide-00-100-2026":
        raise SystemExit("Manifest branch must be revision/guide-00-100-2026")
    stages = data.get("stages")
    if not isinstance(stages, dict):
        raise SystemExit("Manifest stages must be an object")

    for name in ORDER:
        if name not in stages:
            raise SystemExit(f"Missing stage: {name}")
        entry = stages[name]
        status = entry.get("status")
        evidence = entry.get("evidence")
        if status not in ALLOWED:
            raise SystemExit(f"{name}: invalid status {status!r}")
        if not isinstance(evidence, list):
            raise SystemExit(f"{name}: evidence must be a list")
        if status == "PASS" and not evidence:
            raise SystemExit(f"{name}: PASS requires at least one evidence path")
        for raw in evidence:
            p = ROOT / raw
            if not p.exists():
                raise SystemExit(f"{name}: missing evidence path: {raw}")
        if status == "PASS":
            for dependency in DEPENDENCIES.get(name, []):
                if stages[dependency].get("status") != "PASS":
                    raise SystemExit(f"{name}: PASS is invalid because dependency {dependency} is not PASS")

    blockers = data.get("blockers", [])
    if not isinstance(blockers, list):
        raise SystemExit("blockers must be a list")

    if target:
        if target not in ORDER:
            raise SystemExit(f"Unknown target stage: {target}")
        if stages[target]["status"] != "PASS":
            raise SystemExit(f"Target stage {target} is {stages[target]['status']}, not PASS")
        if target == "release_audit" and blockers:
            raise SystemExit(f"Release audit cannot pass with unresolved blockers: {blockers}")

    print(f"Guide {guide} helper manifest validation: PASS")
    for name in ORDER:
        print(f"{name}: {stages[name]['status']}")
    if blockers:
        print(f"Blockers recorded: {len(blockers)}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--guide", required=True, help="Two-digit guide number, e.g. 07")
    parser.add_argument("--target", choices=ORDER)
    args = parser.parse_args()
    guide = args.guide.zfill(2)
    return validate(guide, args.target)


if __name__ == "__main__":
    raise SystemExit(main())
