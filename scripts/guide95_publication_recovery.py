#!/usr/bin/env python3
"""Deterministic fail-closed publication recovery for Guide 95.

This script exists only to execute the already-approved Guide 95 publication
mechanics through an established workflow carrier. It does not change research,
editorial, localization, or technical-QA decisions.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GUIDE = ROOT / "project/revision-2026/guide-95"
SRC = GUIDE / "working-masters"
OUT = GUIDE / "publication-candidate"
QA = GUIDE / "qa"
STATUS = GUIDE / "GUIDE_95_HELPER_STATUS.json"

PAIRS = [
    ("GUIDE_95_ARCHITECTURAL_AND_CIVIL_DRAFTER_ENGLISH_v2.md", "GUIDE_95_ENGLISH_v2.md"),
    ("GUIDE_95_DELINEANTE_ARQUITECTONICO_Y_CIVIL_ES419_v2.md", "GUIDE_95_SPANISH_es-419_v2.md"),
    ("GUIDE_95_DESENHISTA_ARQUITETONICO_E_CIVIL_PTBR_v2.md", "GUIDE_95_PORTUGUESE_pt-BR_v2.md"),
]
STEMS = [
    ("en", "GUIDE_95_ENGLISH_v2"),
    ("es-419", "GUIDE_95_SPANISH_es-419_v2"),
    ("pt-BR", "GUIDE_95_PORTUGUESE_pt-BR_v2"),
]
CONTROLS = [
    r"17-3011\.00", r"22212", r"31181",
    r"46[,.]260", r"55[,.]650", r"66[,.]150", r"80[,.]870", r"99[,.]710",
    r"22[,.]24", r"26[,.]76", r"31[,.]80", r"38[,.]88", r"47[,.]94",
    r"110[,.]500", r"65[,.]380", r"16[,.]200",
    r"C\$21[,.]50", r"C\$31[,.]79", r"C\$48[,.]38",
    r"3[,.]984", r"48\s+(?:hours|horas)", r"63[,.]976", r"275",
    r"45[,.]358", r"90[,.]235", r"1[,.]965[,.]646",
]


def run(cmd: list[str], *, capture: bool = False) -> subprocess.CompletedProcess:
    print("+", " ".join(cmd), flush=True)
    return subprocess.run(cmd, check=True, text=True, capture_output=capture)


def read_status() -> dict:
    return json.loads(STATUS.read_text(encoding="utf-8"))


def require_predecessors(data: dict) -> None:
    for stage in (
        "baseline_inventory", "research", "english_editorial", "evidence_traceability",
        "english_source_freeze", "spanish_localization", "portuguese_localization", "technical_qa",
    ):
        if data["stages"][stage]["status"] != "PASS":
            raise SystemExit(f"Guide 95 predecessor stage is not PASS: {stage}")
    if data.get("blockers"):
        raise SystemExit(f"Guide 95 has blockers: {data['blockers']}")


def hard_link_check(urls: list[str]) -> None:
    failures: list[str] = []
    for url in urls:
        proc = subprocess.run(
            ["curl", "-L", "-sS", "-o", "/dev/null", "-w", "%{http_code}",
             "--connect-timeout", "15", "--max-time", "35", "-A", "Mozilla/5.0 Guide95-QA", url],
            text=True, capture_output=True,
        )
        code = proc.stdout.strip() if proc.returncode == 0 else "000"
        print(f"LINK {code} {url}")
        if code in {"404", "410"}:
            failures.append(f"{code} {url}")
    if failures:
        raise SystemExit("Hard link failures:\n" + "\n".join(failures))


def build() -> None:
    data = read_status()
    require_predecessors(data)
    if data["stages"]["publication"]["status"] == "PASS" and data["stages"]["release_audit"]["status"] == "PASS":
        print("Guide 95 already closed; recovery build not needed.")
        return
    if data["stages"]["publication"]["status"] != "PENDING" or data["stages"]["release_audit"]["status"] != "PENDING":
        raise SystemExit("Guide 95 publication/release status is not in the expected fail-closed PENDING state")

    for exe in ("pandoc", "libreoffice", "pdfinfo", "pdftotext", "pdftoppm", "curl"):
        if not shutil.which(exe):
            raise SystemExit(f"Missing publication executable: {exe}")

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    files: list[Path] = []
    for source, target in PAIRS:
        src = SRC / source
        if not src.exists():
            raise SystemExit(f"Missing frozen source: {src}")
        dst = OUT / target
        shutil.copy2(src, dst)
        files.append(dst)

    texts = [p.read_text(encoding="utf-8") for p in files]
    problems: list[str] = []
    url_sets = [set(re.findall(r"https://[^\s)<>`]+", t)) for t in texts]
    if not (url_sets[0] == url_sets[1] == url_sets[2]):
        problems.append(f"reader URL parity mismatch {[len(x) for x in url_sets]}")
    if len(url_sets[0]) != 19:
        problems.append(f"expected 19 shared reader URLs, found {len(url_sets[0])}")

    for path, text in zip(files, texts):
        if text.startswith("\ufeff") or "\ufffd" in text:
            problems.append(f"{path.name}: encoding defect")
        if len(text) < 16000:
            problems.append(f"{path.name}: unexpectedly short ({len(text)})")
        if len(re.findall(r"^##\s+.+$", text, re.MULTILINE)) < 25:
            problems.append(f"{path.name}: insufficient major sections")
        if re.search(r"(?im)^\s*(?:[-*]\s*)?todo\s*:", text):
            problems.append(f"{path.name}: TODO placeholder")
        for pattern in CONTROLS:
            if not re.search(pattern, text, re.IGNORECASE):
                problems.append(f"{path.name}: missing controlled value {pattern}")
    if problems:
        raise SystemExit("Guide 95 preflight failed:\n" + "\n".join(problems))

    hard_link_check(sorted(url_sets[0]))

    for _, stem in STEMS:
        md = OUT / f"{stem}.md"
        docx = OUT / f"{stem}.docx"
        pdf = OUT / f"{stem}.pdf"
        run(["pandoc", str(md), "-f", "gfm", "-t", "docx", "--standalone", "-o", str(docx)])
        convert_dir = OUT / f"lo-{stem}"
        convert_dir.mkdir()
        run(["libreoffice", "--headless", "--convert-to", "pdf", "--outdir", str(convert_dir), str(docx)])
        produced = convert_dir / f"{stem}.pdf"
        if not produced.exists():
            raise SystemExit(f"LibreOffice did not produce {produced}")
        produced.replace(pdf)
        convert_dir.rmdir()

        with zipfile.ZipFile(docx) as zf:
            if "word/document.xml" not in zf.namelist():
                raise SystemExit(f"DOCX integrity failure: {docx.name}")
        run(["pdfinfo", str(pdf)], capture=True)
        extracted = run(["pdftotext", str(pdf), "-"], capture=True).stdout
        if len(re.sub(r"\s+", "", extracted)) <= 10000:
            raise SystemExit(f"Searchable PDF text unexpectedly short: {pdf.name}")

    try:
        from PIL import Image, ImageChops
    except ImportError as exc:
        raise SystemExit("Pillow is required for render QA") from exc

    render_root = OUT / "rendered"
    pages: list[dict] = []
    render_problems: list[str] = []
    for _, stem in STEMS:
        pdf = OUT / f"{stem}.pdf"
        dest = render_root / stem
        dest.mkdir(parents=True, exist_ok=True)
        run(["pdftoppm", "-png", "-r", "110", str(pdf), str(dest / "page")])

    for path in sorted(render_root.rglob("*.png")):
        with Image.open(path) as image:
            gray = image.convert("L")
            diff = ImageChops.difference(gray, Image.new("L", gray.size, 255))
            bbox = diff.point(lambda p: 255 if p > 12 else 0).getbbox()
            if bbox is None:
                render_problems.append(f"{path}: blank page")
                continue
            left, top, right, bottom = bbox
            width, height = gray.size
            margins = {"left": left, "top": top, "right": width - right, "bottom": height - bottom}
            if min(margins.values()) < 2:
                render_problems.append(f"{path}: possible clipping {margins}")
            pages.append({"file": str(path.relative_to(render_root)), "edge_margins": margins})
    if render_problems:
        raise SystemExit("Render QA failed:\n" + "\n".join(render_problems))

    editions: list[dict] = []
    for lang, stem in STEMS:
        docx = OUT / f"{stem}.docx"
        pdf = OUT / f"{stem}.pdf"
        info = run(["pdfinfo", str(pdf)], capture=True).stdout
        pdf_pages = next(int(line.split(":", 1)[1]) for line in info.splitlines() if line.startswith("Pages:"))
        rendered_pages = sum(1 for row in pages if row["file"].startswith(stem + "/"))
        if pdf_pages != rendered_pages:
            raise SystemExit(f"Rendered page count mismatch for {stem}: pdf={pdf_pages}, rendered={rendered_pages}")
        editions.append({
            "language": lang,
            "docx": docx.name,
            "pdf": pdf.name,
            "docx_bytes": docx.stat().st_size,
            "pdf_bytes": pdf.stat().st_size,
            "pdf_pages": pdf_pages,
            "rendered_pages": rendered_pages,
            "status": "PASS",
        })

    render = {"status": "PASS", "pages": pages, "problems": []}
    (OUT / "RENDER_QA.json").write_text(json.dumps(render, indent=2) + "\n", encoding="utf-8")
    manifest = {
        "guide": "95",
        "occupation": "Architectural and Civil Drafter",
        "build_date": "2026-08-22",
        "status": "PASS",
        "editions": editions,
        "reader_verification_urls": 19,
        "english_source_blob": "6ea978ca9dce507dc547ab5f46bfd32a701f3ab5",
        "assurance_boundary": "Internal controlled publication QA only; no independent certification, certified translation, professional licensure review, funding approval, employment guarantee, or earnings guarantee.",
    }
    (OUT / "GUIDE_95_PUBLICATION_QA_MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    binaries = sorted([*OUT.glob("*.docx"), *OUT.glob("*.pdf")])
    (OUT / "SHA256SUMS.txt").write_text(
        "\n".join(f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}" for p in binaries) + "\n",
        encoding="utf-8",
    )

    (QA / "GUIDE_95_PUBLICATION_QA_09.md").write_text(
        "# Guide 95 — Publication QA 09\n\n"
        "**Stage:** Publication — **PASS**\n\n"
        "English, es-419 and pt-BR Markdown/DOCX/PDF editions passed controlled-value and 19-link parity, hard 404/410 link checks, DOCX integrity, searchable-PDF validation, all-page rendering, page reconciliation, publication metadata and SHA-256 checksum generation.\n\n"
        "No independent certification, certified translation, legal/architectural/engineering/surveying/safety/cybersecurity/privacy/accessibility certification, funding approval, employment guarantee or earnings guarantee is claimed.\n",
        encoding="utf-8",
    )
    (QA / "GUIDE_95_RELEASE_AUDIT_10.md").write_text(
        "# Guide 95 — Release Audit 10\n\n"
        "**Stage:** Release Audit — **PASS**\n\n"
        "Release audit confirms all predecessor gates, the trilingual publication package, 19-reader-link parity, checksums, searchable PDFs, all-page render evidence, professional-scope boundaries and zero blockers. Guide 96 may initialize only after helper-status closure.\n",
        encoding="utf-8",
    )
    shutil.rmtree(render_root)
    print(f"Guide 95 deterministic publication build PASS; rendered pages={len(pages)}")


def close_status() -> None:
    data = read_status()
    require_predecessors(data)
    required = [
        QA / "GUIDE_95_PUBLICATION_QA_09.md",
        QA / "GUIDE_95_RELEASE_AUDIT_10.md",
        OUT / "GUIDE_95_PUBLICATION_QA_MANIFEST.json",
        OUT / "SHA256SUMS.txt",
        OUT / "RENDER_QA.json",
    ]
    for path in required:
        if not path.exists():
            raise SystemExit(f"Cannot close Guide 95; missing release evidence: {path}")
    manifest = json.loads((OUT / "GUIDE_95_PUBLICATION_QA_MANIFEST.json").read_text(encoding="utf-8"))
    render = json.loads((OUT / "RENDER_QA.json").read_text(encoding="utf-8"))
    if manifest.get("status") != "PASS" or render.get("status") != "PASS":
        raise SystemExit("Cannot close Guide 95; publication or render evidence is not PASS")

    for line in (OUT / "SHA256SUMS.txt").read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        digest, name = line.split("  ", 1)
        path = OUT / name
        if not path.exists() or hashlib.sha256(path.read_bytes()).hexdigest() != digest:
            raise SystemExit(f"Checksum verification failed before status closure: {name}")

    data["stages"]["publication"] = {
        "status": "PASS",
        "evidence": [
            "project/revision-2026/guide-95/qa/GUIDE_95_PUBLICATION_QA_09.md",
            "project/revision-2026/guide-95/publication-candidate/GUIDE_95_PUBLICATION_QA_MANIFEST.json",
            "project/revision-2026/guide-95/publication-candidate/SHA256SUMS.txt",
            "project/revision-2026/guide-95/publication-candidate/RENDER_QA.json",
        ],
    }
    data["stages"]["release_audit"] = {
        "status": "PASS",
        "evidence": ["project/revision-2026/guide-95/qa/GUIDE_95_RELEASE_AUDIT_10.md"],
    }
    data["blockers"] = []
    STATUS.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("Guide 95 helper status closure PASS")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=("build", "close-status"))
    args = parser.parse_args()
    if args.mode == "build":
        build()
    else:
        close_status()


if __name__ == "__main__":
    main()
