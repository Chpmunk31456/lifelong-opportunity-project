#!/usr/bin/env python3
"""Fail-closed release auditor for Guide 07.

This auditor requires all prerequisite helper stages to be PASS, validates the
publication manifest/checksums, and requires an explicit full-page visual-review
record before it can write a final PASS gate.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GUIDE = ROOT / "project/revision-2026/guide-07"
STATUS = GUIDE / "GUIDE_07_HELPER_STATUS.json"
PUB = GUIDE / "publication-candidate"
MANIFEST = PUB / "GUIDE_07_PUBLICATION_QA_MANIFEST.json"
CHECKSUMS = PUB / "SHA256SUMS.txt"
VISUAL = GUIDE / "qa/GUIDE_07_FULL_PAGE_VISUAL_REVIEW_10.md"
FINAL = GUIDE / "qa/GUIDE_07_FINAL_PUBLICATION_CANDIDATE_GATE_11.md"

REQUIRED_PRIOR = [
    "research",
    "english_editorial",
    "evidence_traceability",
    "english_source_freeze",
    "spanish_localization",
    "portuguese_localization",
    "technical_qa",
    "publication",
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    if not STATUS.is_file():
        raise SystemExit("Missing helper status manifest")
    status = json.loads(STATUS.read_text(encoding="utf-8"))
    blockers = status.get("blockers", [])
    if blockers:
        raise SystemExit(f"Open blockers: {blockers}")

    stages = status.get("stages", {})
    for stage in REQUIRED_PRIOR:
        if stages.get(stage, {}).get("status") != "PASS":
            raise SystemExit(f"Required prior stage is not PASS: {stage}")

    if not MANIFEST.is_file() or not CHECKSUMS.is_file():
        raise SystemExit("Publication manifest/checksums missing")
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    files = manifest.get("files", [])
    renders = manifest.get("renders", [])
    if len(files) != 6:
        raise SystemExit(f"Expected 6 publication files, got {len(files)}")
    if not renders:
        raise SystemExit("No rendered-page evidence recorded")

    expected_render_count = sum(
        int(item["pages"]) for item in files if item.get("pages") is not None
    )
    if len(renders) != expected_render_count:
        raise SystemExit(
            f"Render count mismatch: expected {expected_render_count}, got {len(renders)}"
        )

    for item in files + renders:
        path = ROOT / item["path"]
        if not path.is_file():
            raise SystemExit(f"Manifest file missing: {item['path']}")
        if sha256(path) != item["sha256"]:
            raise SystemExit(f"SHA-256 mismatch: {item['path']}")

    if not VISUAL.is_file():
        raise SystemExit(
            "Full-page visual review record is missing; release audit remains blocked"
        )
    visual = VISUAL.read_text(encoding="utf-8")
    required_visual_phrases = [
        "Status: PASS",
        "English",
        "es-419",
        "pt-BR",
        "all rendered pages",
        "no clipping",
        "no overlap",
        "no broken glyphs",
    ]
    missing = [p for p in required_visual_phrases if p.casefold() not in visual.casefold()]
    if missing:
        raise SystemExit(f"Visual-review record incomplete: {missing}")

    FINAL.write_text(
        "# Guide 07 — Final publication-candidate gate 11\n\n"
        "**Status:** PASS — controlled publication candidate\n\n"
        "## Evidence reviewed\n\n"
        "- Research, English editorial, claim traceability, and English source-freeze gates: PASS.\n"
        "- es-419 and pt-BR localization with trilingual source parity: PASS.\n"
        "- Automated technical QA: PASS.\n"
        "- Three DOCX and three searchable PDF publication candidates: PASS.\n"
        "- OOXML hyperlink/encoding checks and SHA-256 reconciliation: PASS.\n"
        f"- Full rendered-page set: {len(renders)} pages across all language editions.\n"
        "- Full-page visual review record: PASS.\n\n"
        "## Assurance boundary\n\n"
        "This gate does not claim independent human certification, professional translation certification, accessibility certification, accreditation, legal review, financial advice, or guaranteed employment/training outcomes.\n",
        encoding="utf-8",
    )
    print("Guide 07 final release audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
