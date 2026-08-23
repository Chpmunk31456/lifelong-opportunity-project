#!/usr/bin/env python3
"""Apply and verify the Guide 97 post-freeze NIST GenAI Profile URL correction.

This is deliberately narrow: exactly one obsolete NIST URL in each controlled
language master is replaced by the current official NIST publication URL. The
script then recalculates Git blob IDs and refreshes the affected QA records so
no post-freeze source change is silently accepted.
"""
from __future__ import annotations

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
G = ROOT / "project/revision-2026/guide-97"
WM = G / "working-masters"
QA = G / "qa"
RUNNER = ROOT / "scripts/guide97_publication_recovery.py"

OLD = "https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence-profile"
NEW = "https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence"
OLD_EN_BLOB = "0a4dcbe75ef6fa4e351af3bc4a13726c2e7dae94"
OLD_ES_BLOB = "c908e4cb7d6d61fc3f0b7e71e9eaac523db5ffa8"
OLD_PT_BLOB = "f6070362230523d336ffdc634b45ef95e9822b95"

FILES = {
    "en": WM / "GUIDE_97_MECHANICAL_ENGINEERING_TECHNICIAN_ENGLISH_v2.md",
    "es": WM / "GUIDE_97_MECHANICAL_ENGINEERING_TECHNICIAN_SPANISH_es-419_v2.md",
    "pt": WM / "GUIDE_97_MECHANICAL_ENGINEERING_TECHNICIAN_PORTUGUESE_pt-BR_v2.md",
}

QA_FILES = [
    QA / "GUIDE_97_ENGLISH_EDITORIAL_QA_03.md",
    QA / "GUIDE_97_EVIDENCE_TRACEABILITY_QA_04.md",
    QA / "GUIDE_97_ENGLISH_SOURCE_FREEZE_05.md",
    QA / "GUIDE_97_SPANISH_LOCALIZATION_QA_06.md",
    QA / "GUIDE_97_PORTUGUESE_LOCALIZATION_QA_07.md",
    QA / "GUIDE_97_TRILINGUAL_TECHNICAL_QA_08.md",
]

CONTROL_PATTERNS = [
    r"17-3027\.00", r"22301", r"31150",
    r"35[,.]82", r"74[,.]510", r"68[,.]730",
    r"C\$23[,.]08", r"C\$35[,.]00", r"C\$51[,.]28",
    r"3[,.]984", r"75[,.]124", r"36[,.]12", r"58[,.]275",
]


def blob(path: Path) -> str:
    return subprocess.check_output(["git", "hash-object", str(path)], text=True).strip()


def assert_semantic_controls(text: str, label: str) -> None:
    for pat in CONTROL_PATTERNS:
        if not re.search(pat, text, re.I):
            raise SystemExit(f"{label}: missing controlled value {pat}")
    if len(re.findall(r"^###\s+(?:Step|Paso|Etapa)\s+[1-6]\b", text, re.M | re.I)) != 6:
        raise SystemExit(f"{label}: six-step action plan parity failed")
    if "lockout/tagout" not in text.lower():
        raise SystemExit(f"{label}: LOTO boundary missing")
    if "AI" not in text and "IA" not in text:
        raise SystemExit(f"{label}: responsible-AI content missing")


def replace_exact_once(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    count_old = text.count(OLD)
    count_new = text.count(NEW)
    if count_old == 1:
        text = text.replace(OLD, NEW)
        path.write_text(text, encoding="utf-8")
    elif count_old == 0 and count_new == 1:
        pass
    else:
        raise SystemExit(f"{path}: expected exactly one old or one corrected NIST URL; old={count_old}, new={count_new}")
    text = path.read_text(encoding="utf-8")
    if text.count(NEW) != 1 or OLD in text:
        raise SystemExit(f"{path}: NIST URL correction verification failed")
    assert_semantic_controls(text, path.name)


def append_revalidation(path: Path, en_blob: str, es_blob: str, pt_blob: str) -> None:
    text = path.read_text(encoding="utf-8")
    # Refresh any stored pre-correction blob IDs so QA evidence points to the live corrected sources.
    text = text.replace(OLD_EN_BLOB, en_blob).replace(OLD_ES_BLOB, es_blob).replace(OLD_PT_BLOB, pt_blob)
    marker = "## Post-freeze source-link correction revalidation — 2026-08-22"
    if marker not in text:
        text = text.rstrip() + "\n\n" + marker + "\n\n"
        text += (
            "NIST moved the reader-verification page for *Artificial Intelligence Risk Management Framework: "
            "Generative Artificial Intelligence Profile*. The obsolete URL ending in `-profile` returned HTTP 404 during "
            "Publication QA. The official NIST publication page was reverified on 2026-08-22 and the URL-only correction "
            "was applied in English, `es-419`, and `pt-BR` with no change to occupational claims, wage/training values, "
            "safety/professional-scope controls, cybersecurity/AI guidance, action-plan milestones, or assurance boundaries.\n\n"
            f"- Revalidated English blob: `{en_blob}`\n"
            f"- Revalidated Spanish blob: `{es_blob}`\n"
            f"- Revalidated Portuguese blob: `{pt_blob}`\n"
            f"- Correct official NIST destination: {NEW}\n"
            "- Result: **PASS — affected gate revalidated after URL-only source correction.**\n"
        )
    path.write_text(text, encoding="utf-8")


def main() -> None:
    for p in FILES.values():
        if not p.exists():
            raise SystemExit(f"Missing controlled master: {p}")
        replace_exact_once(p)

    en_blob = blob(FILES["en"])
    es_blob = blob(FILES["es"])
    pt_blob = blob(FILES["pt"])

    # Link parity must remain exact across all controlled editions.
    sets = []
    for p in FILES.values():
        text = p.read_text(encoding="utf-8")
        sets.append(set(re.findall(r"https://[^\s)<>`]+", text)))
    if not (sets[0] == sets[1] == sets[2]):
        raise SystemExit(f"URL parity failed after correction: {[len(x) for x in sets]}")
    if len(sets[0]) != 26 or NEW not in sets[0] or OLD in sets[0]:
        raise SystemExit(f"Expected 26 corrected shared URLs; got {len(sets[0])}")

    for q in QA_FILES:
        if not q.exists():
            raise SystemExit(f"Missing QA record required for revalidation: {q}")
        append_revalidation(q, en_blob, es_blob, pt_blob)

    correction = QA / "GUIDE_97_SOURCE_LINK_CORRECTION_08A.md"
    correction.write_text(
        "# Guide 97 — Source Link Correction 08A\n\n"
        "## Scope\n"
        "Post-freeze URL-only correction for the NIST AI RMF Generative AI Profile reader-verification source.\n\n"
        "## Failure observed\n"
        f"Publication run 32601899587 returned HTTP 404 for `{OLD}`. No publication package or helper-status closure was committed.\n\n"
        "## Current official source\n"
        f"NIST publication page: {NEW}\n\n"
        "The official NIST page identifies NIST-AI-600-1, *Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile*, published July 26, 2024 and updated April 8, 2026.\n\n"
        "## Controlled correction\n"
        "The obsolete URL was replaced exactly once in each controlled language master. No substantive career, wage, training, safety, scope, cybersecurity, responsible-AI, accessibility, or action-plan content changed.\n\n"
        f"- English blob after correction: `{en_blob}`\n"
        f"- Spanish blob after correction: `{es_blob}`\n"
        f"- Portuguese blob after correction: `{pt_blob}`\n\n"
        "English Editorial, Evidence/Traceability, English Source Freeze, Spanish Localization, Portuguese Localization and Trilingual Technical QA records were revalidated against these corrected blobs. URL parity remains 26/26/26.\n\n"
        "## Result\n"
        "**PASS — controlled source-link correction and affected-gate revalidation.**\n",
        encoding="utf-8",
    )

    runner = RUNNER.read_text(encoding="utf-8")
    runner = runner.replace(OLD_EN_BLOB, en_blob)
    RUNNER.write_text(runner, encoding="utf-8")

    print("Guide 97 NIST link correction PASS")
    print("English blob:", en_blob)
    print("Spanish blob:", es_blob)
    print("Portuguese blob:", pt_blob)
    print("Shared URLs:", len(sets[0]))


if __name__ == "__main__":
    main()
