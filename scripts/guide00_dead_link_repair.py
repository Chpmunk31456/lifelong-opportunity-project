#!/usr/bin/env python3
"""Controlled Guide 00 source repair for one confirmed dead Mexican program URL."""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

GUIDE = Path("project/revision-2026/guide-00")
QA = GUIDE / "qa"
STATUS = GUIDE / "GUIDE_00_HELPER_STATUS.json"
SOURCES = {
    "en": Path("00-foundation-guide/source/Lifelong_Opportunity_Foundation_Guide_English_v1.1_INTEGRATED_MASTER.md"),
    "es-419": Path("00-foundation-guide/source/Lifelong_Opportunity_Foundation_Guide_es-419_v1.1_INTEGRATED_MASTER.md"),
    "pt-BR": Path("00-foundation-guide/source/Lifelong_Opportunity_Foundation_Guide_pt-BR_v1.1_INTEGRATED_MASTER.md"),
}
DEAD = "https://programasparaelbienestar.gob.mx/jovenes-construyendo-el-futuro/"
REPLACEMENT = "https://www.jovenesconstruyendoelfuturo.stps.gob.mx/aprendiz"
EVIDENCE = QA / "GUIDE_00_DEAD_LINK_REPAIR_08C.md"
FREEZE_AMENDMENT = QA / "GUIDE_00_ENGLISH_SOURCE_FREEZE_AMENDMENT_08C.md"
TECH_QA = QA / "GUIDE_00_TRILINGUAL_TECHNICAL_QA_08.md"


def blob(path: Path) -> str:
    return subprocess.check_output(["git", "hash-object", str(path)], text=True).strip()


def urls(text: str) -> set[str]:
    return {u.rstrip(".,;:") for u in re.findall(r"https?://[^\s)<>\]`]+", text)}


def repair() -> None:
    records = []
    for locale, path in SOURCES.items():
        text = path.read_text(encoding="utf-8-sig")
        count = text.count(DEAD)
        new_count = text.count(REPLACEMENT)
        if count == 0:
            # Idempotent rerun is allowed only when the replacement is already present.
            if new_count == 0:
                raise SystemExit(f"{locale}: dead URL absent but replacement also absent")
            records.append((locale, blob(path), blob(path), 0))
            continue
        if count != 1:
            raise SystemExit(f"{locale}: expected exactly one dead URL occurrence, found {count}")
        if new_count:
            raise SystemExit(f"{locale}: replacement already exists before repair; refusing duplicate")
        before = blob(path)
        path.write_text(text.replace(DEAD, REPLACEMENT), encoding="utf-8")
        after = blob(path)
        records.append((locale, before, after, count))

    urlsets = [urls(path.read_text(encoding="utf-8-sig")) for path in SOURCES.values()]
    if not (urlsets[0] == urlsets[1] == urlsets[2]):
        raise SystemExit("post-repair trilingual URL sets are not identical")
    if DEAD in urlsets[0]:
        raise SystemExit("dead URL remains after repair")
    if REPLACEMENT not in urlsets[0]:
        raise SystemExit("replacement URL missing after repair")
    if len(urlsets[0]) != 27:
        raise SystemExit(f"expected 27 URLs after one-for-one replacement, found {len(urlsets[0])}")

    lines = [
        "# Guide 00 — Confirmed Dead-Link Repair 08C",
        "",
        "**Guide:** 00 — Lifelong Opportunity Foundation Guide",
        "**Branch:** `revision/guide-00-100-2026`",
        "**Repair date:** 2026-08-22",
        "**Status:** PASS",
        "",
        "## Defect",
        "",
        f"Publication live-link preflight returned HTTP **404** for `{DEAD}`.",
        "The guide already retained the official Jóvenes Construyendo el Futuro program homepage; the dead duplicate was replaced with the current official STPS apprentice information page rather than weakening the link gate.",
        "",
        "## Controlled replacement",
        "",
        f"- Removed: `{DEAD}`",
        f"- Added: `{REPLACEMENT}`",
        "- Replacement class: official Secretaría del Trabajo y Previsión Social / Jóvenes Construyendo el Futuro page",
        "- Claim text changed: **NO — URL-only maintenance**",
        "- Trilingual URL-set cardinality after repair: **27**",
        "- Trilingual URL-set parity after repair: **PASS**",
        "",
        "## Source blobs",
        "",
    ]
    for locale, before, after, changed in records:
        lines += [f"- **{locale}:** `{before}` -> `{after}` (replacement count {changed})"]
    lines += [
        "",
        "The English source changed only by this URL replacement. The prior English freeze is therefore amended below and final Trilingual Technical QA must rerun before Publication requalification resumes.",
    ]
    EVIDENCE.write_text("\n".join(lines) + "\n", encoding="utf-8")

    english_blob = blob(SOURCES["en"])
    FREEZE_AMENDMENT.write_text(
        "# Guide 00 — English Source Freeze Amendment 08C\n\n"
        "**Status:** PASS — URL-only maintenance amendment\n\n"
        f"Frozen English source: `{SOURCES['en'].as_posix()}`\n\n"
        f"Amended live Git blob: `{english_blob}`\n\n"
        f"Reason: the previously frozen source contained one URL that failed final publication live-link preflight with HTTP 404. The URL was replaced one-for-one with `{REPLACEMENT}`. No prose claim, structure, eligibility statement, funding classification, action step, safety/accessibility statement or version marker changed.\n\n"
        "The amended freeze is valid only together with `GUIDE_00_DEAD_LINK_REPAIR_08C.md` and a fresh Trilingual Technical QA PASS against the amended trilingual sources.\n",
        encoding="utf-8",
    )
    print(f"PASS: Guide 00 dead-link repair applied; 27 shared URLs; English blob {english_blob}")


def sync_status() -> None:
    if not EVIDENCE.is_file() or not FREEZE_AMENDMENT.is_file() or not TECH_QA.is_file():
        raise SystemExit("repair/freeze/technical evidence missing")
    tech = TECH_QA.read_text(encoding="utf-8-sig")
    if "**Trilingual Technical QA: PASS.**" not in tech:
        raise SystemExit("fresh technical QA is not PASS")
    if REPLACEMENT not in tech:
        raise SystemExit("fresh technical QA does not contain replacement URL")
    data = json.loads(STATUS.read_text(encoding="utf-8-sig"))
    if data["stages"]["publication"]["status"] != "PENDING":
        raise SystemExit("Publication is not PENDING")
    freeze_ev = data["stages"]["english_source_freeze"].setdefault("evidence", [])
    for p in (EVIDENCE.as_posix(), FREEZE_AMENDMENT.as_posix()):
        if p not in freeze_ev:
            freeze_ev.append(p)
    tech_ev = data["stages"]["technical_qa"].setdefault("evidence", [])
    if EVIDENCE.as_posix() not in tech_ev:
        tech_ev.append(EVIDENCE.as_posix())
    for stage in ("spanish_localization", "portuguese_localization"):
        ev = data["stages"][stage].setdefault("evidence", [])
        if EVIDENCE.as_posix() not in ev:
            ev.append(EVIDENCE.as_posix())
    data["updated"] = "2026-08-22"
    data["notes"] = "Guide 00 remains 8/10. Confirmed dead-link repaired one-for-one; English freeze amended; fresh Trilingual Technical QA PASS. First active gate: Publication."
    STATUS.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("PASS: Guide 00 helper synchronized after dead-link repair")


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "repair"
    if mode == "repair":
        repair()
    elif mode == "sync-status":
        sync_status()
    else:
        raise SystemExit("usage: guide00_dead_link_repair.py {repair|sync-status}")
