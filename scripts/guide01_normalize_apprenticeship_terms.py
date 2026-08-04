#!/usr/bin/env python3
"""Normalize Guide 01's first apprenticeship definitions in es-419 and pt-BR.

This controlled edit closes the two wording findings recorded in
project/revision-2026/guide-01/TRILINGUAL_TERMINOLOGY_QA_02.md.

The script is intentionally idempotent and fails closed when a source file is
missing, an expected phrase appears an unexpected number of times, or the
post-edit validation does not establish the controlled terminology.
"""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

EDITS = {
    ROOT
    / "project/revision-2026/guide-01/working-masters/"
    "GUIDE_01_TRABAJADOR_COMUNITARIO_DE_SALUD_ES419_WORKING_MASTER.md": (
        "- **aprendizaje formal:** trabajo remunerado estructurado y formación relacionada cuando existe un programa formalmente establecido;",
        "- **aprendizaje formal remunerado:** trabajo remunerado estructurado y formación relacionada cuando existe un programa formalmente establecido;",
        "aprendizaje formal remunerado",
    ),
    ROOT
    / "project/revision-2026/guide-01/working-masters/"
    "GUIDE_01_AGENTE_COMUNITARIO_DE_SAUDE_PTBR_WORKING_MASTER.md": (
        "- **aprendizagem formal:** trabalho remunerado estruturado e instrução relacionada quando há programa formalmente estabelecido;",
        "- **aprendizagem profissional formal remunerada:** trabalho remunerado estruturado e instrução relacionada quando há programa formalmente estabelecido;",
        "aprendizagem profissional formal remunerada",
    ),
}


def normalize(path: Path, old: str, new: str, required_term: str) -> bool:
    if not path.is_file():
        raise SystemExit(f"Missing controlled working master: {path.relative_to(ROOT)}")

    raw = path.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"):
        raise SystemExit(f"Unexpected UTF-8 BOM: {path.relative_to(ROOT)}")

    text = raw.decode("utf-8")
    old_count = text.count(old)
    new_count = text.count(new)

    if old_count == 1 and new_count == 0:
        updated = text.replace(old, new, 1)
        path.write_text(updated, encoding="utf-8", newline="\n")
        changed = True
    elif old_count == 0 and new_count == 1:
        changed = False
    else:
        raise SystemExit(
            f"Unexpected terminology state in {path.relative_to(ROOT)}: "
            f"old={old_count}, controlled={new_count}"
        )

    final = path.read_text(encoding="utf-8")
    if final.count(old) != 0 or final.count(new) != 1:
        raise SystemExit(f"Post-edit phrase validation failed: {path.relative_to(ROOT)}")
    if required_term not in final:
        raise SystemExit(f"Controlled term missing after edit: {path.relative_to(ROOT)}")
    if "\ufffd" in final:
        raise SystemExit(f"Replacement-character encoding defect: {path.relative_to(ROOT)}")

    action = "normalized" if changed else "already normalized"
    print(f"{action}: {path.relative_to(ROOT)}")
    return changed


def main() -> None:
    changed = 0
    for path, (old, new, required_term) in EDITS.items():
        changed += int(normalize(path, old, new, required_term))

    print(f"Guide 01 apprenticeship terminology validation passed; files changed: {changed}")


if __name__ == "__main__":
    main()
