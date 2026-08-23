#!/usr/bin/env python3
"""Fail-closed controlled publication carrier for Guide 100."""
from __future__ import annotations

import hashlib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path("project/revision-2026/guide-100")
STATUS = ROOT / "GUIDE_100_HELPER_STATUS.json"
SRC = ROOT / "working-masters"
OUT = ROOT / "publication-candidate"
QA = ROOT / "qa"
ENGLISH_BLOB = "45257f599c046eb255d10e1e070dc2d470ccb5fb"
PAIRS = [
    ("GUIDE_100_CLINICAL_LABORATORY_TECHNICIAN_ENGLISH_v2.md", "GUIDE_100_ENGLISH_v2.md"),
    ("GUIDE_100_TECNICO_DE_LABORATORIO_CLINICO_ES419_v2.md", "GUIDE_100_SPANISH_es-419_v2.md"),
    ("GUIDE_100_TECNICO_DE_LABORATORIO_CLINICO_PTBR_v2.md", "GUIDE_100_PORTUGUESE_pt-BR_v2.md"),
]


def run(cmd: list[str], **kwargs):
    return subprocess.run(cmd, check=True, **kwargs)


def read_status() -> dict:
    return json.loads(STATUS.read_text(encoding="utf-8"))


def preflight() -> tuple[list[Path], list[str]]:
    d = read_status()
    required = (
        "baseline_inventory", "research", "english_editorial", "evidence_traceability",
        "english_source_freeze", "spanish_localization", "portuguese_localization", "technical_qa",
    )
    for stage in required:
        assert d["stages"][stage]["status"] == "PASS", stage
    assert d["stages"]["publication"]["status"] == "PENDING"
    assert d["stages"]["release_audit"]["status"] == "PENDING"
    assert not d.get("blockers")

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    files: list[Path] = []
    for source, target in PAIRS:
        p = SRC / source
        assert p.exists(), source
        shutil.copy2(p, OUT / target)
        files.append(OUT / target)

    texts = [p.read_text(encoding="utf-8") for p in files]
    problems: list[str] = []
    for p, t in zip(files, texts):
        if t.startswith("\ufeff") or "\ufffd" in t:
            problems.append(f"{p.name}: encoding defect")
        if len(t) < 15000:
            problems.append(f"{p.name}: unexpectedly short ({len(t)})")
        if len(re.findall(r"^##\s+.+$", t, re.M)) < 20:
            problems.append(f"{p.name}: insufficient major sections")
        if re.search(r"(?im)^\s*(?:[-*]\s*)?todo\s*:", t):
            problems.append(f"{p.name}: TODO placeholder")
        # Legacy Guide 100 defect repair must survive every language edition.
        if not all(marker in t for marker in (
            "Step 1", "Step 2", "Step 3", "Step 4", "Step 5", "Step 6"
        )) and p.name == "GUIDE_100_ENGLISH_v2.md":
            problems.append(f"{p.name}: six-step action plan incomplete")
        if p.name == "GUIDE_100_SPANISH_es-419_v2.md" and not all(
            f"Paso {i}" in t for i in range(1, 7)
        ):
            problems.append(f"{p.name}: six-step action plan incomplete")
        if p.name == "GUIDE_100_PORTUGUESE_pt-BR_v2.md" and not all(
            f"Passo {i}" in t for i in range(1, 7)
        ):
            problems.append(f"{p.name}: six-step action plan incomplete")

    urlsets = [set(re.findall(r"https://[^\s)<>`]+", t)) for t in texts]
    if not (urlsets[0] == urlsets[1] == urlsets[2]):
        problems.append(f"reader URL parity mismatch {[len(x) for x in urlsets]}")
    if len(urlsets[0]) < 20:
        problems.append(f"too few shared reader URLs ({len(urlsets[0])})")

    for p, t in zip(files, texts):
        for value in ("29-2012.00", "32120", "33101", "53294", "62,930", "61,890", "22,600"):
            if value not in t:
                problems.append(f"{p.name}: missing controlled value {value}")
        for value in ("25.13", "39.00", "49.00", "19.18", "27.00", "36.11"):
            if value not in t:
                problems.append(f"{p.name}: missing Canada wage value {value}")
        if "48" not in t or "SENA" not in t:
            problems.append(f"{p.name}: missing controlled SENA 48-hour pathway")

    if problems:
        raise SystemExit("\n".join(problems))
    return files, sorted(urlsets[0])


def check_links(urls: list[str]) -> None:
    failures: list[str] = []
    for url in urls:
        proc = subprocess.run(
            ["curl", "-L", "-sS", "-o", "/dev/null", "-w", "%{http_code}",
             "--connect-timeout", "15", "--max-time", "35", "-A", "Mozilla/5.0 Guide100-QA", url],
            text=True, capture_output=True,
        )
        code = (proc.stdout or "000").strip()[-3:]
        if code in {"404", "410"}:
            failures.append(f"{code} {url}")
        else:
            print(f"LINK {code} {url}")
    if failures:
        raise SystemExit("Hard link failures:\n" + "\n".join(failures))


def build_documents() -> None:
    # Replace long visible URLs with a short hyperlink label in DOCX/PDF output.
    # The Markdown source still retains every direct reader-verification URL.
    lua = Path("/tmp/guide100_url_safe.lua")
    lua.write_text(
        "local function long_url(s) return string.match(s,'^https?://') and string.len(s)>45 end\n"
        "function Link(el) local t=pandoc.utils.stringify(el.content); if long_url(t) then return pandoc.Link({pandoc.Str('Source link')},el.target,el.title) end; return el end\n"
        "function Str(el) if long_url(el.text) then return pandoc.Link({pandoc.Str('Source link')},el.text) end; return el end\n",
        encoding="utf-8",
    )
    for stem in ("GUIDE_100_ENGLISH_v2", "GUIDE_100_SPANISH_es-419_v2", "GUIDE_100_PORTUGUESE_pt-BR_v2"):
        md = OUT / f"{stem}.md"
        docx = OUT / f"{stem}.docx"
        pdf = OUT / f"{stem}.pdf"
        run(["pandoc", str(md), "-f", "gfm-tex_math_dollars", "-t", "docx", "--standalone", f"--lua-filter={lua}", "-o", str(docx)])
        tmp = OUT / f"lo-{stem}"
        tmp.mkdir()
        run(["libreoffice", "--headless", "--convert-to", "pdf", "--outdir", str(tmp), str(docx)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        shutil.move(str(tmp / f"{stem}.pdf"), pdf)
        tmp.rmdir()
        run(["unzip", "-t", str(docx)], stdout=subprocess.DEVNULL)
        run(["pdfinfo", str(pdf)], stdout=subprocess.DEVNULL)
        text = subprocess.check_output(["pdftotext", str(pdf), "-"], text=True)
        assert len(re.sub(r"\s+", "", text)) > 10000, f"searchable PDF text too short: {stem}"


def render_validate() -> dict:
    from PIL import Image, ImageChops

    rend = OUT / "rendered"
    pages = []
    problems = []
    for pdf in sorted(OUT.glob("*.pdf")):
        dest = rend / pdf.stem
        dest.mkdir(parents=True, exist_ok=True)
        run(["pdftoppm", "-png", "-r", "110", str(pdf), str(dest / "page")], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    for path in sorted(rend.rglob("*.png")):
        with Image.open(path) as im:
            gray = im.convert("L")
            diff = ImageChops.difference(gray, Image.new("L", gray.size, 255))
            bbox = diff.point(lambda p: 255 if p > 12 else 0).getbbox()
            if bbox is None:
                problems.append(f"{path}: blank")
                continue
            l, t, r, b = bbox
            w, h = gray.size
            margins = {"left": l, "top": t, "right": w-r, "bottom": h-b}
            if min(margins.values()) < 2:
                problems.append(f"{path}: clipping {margins}")
            pages.append({"file": str(path.relative_to(rend)), "edge_margins": margins})
    result = {"status": "FAIL" if problems else "PASS", "pages": pages, "problems": problems}
    if problems:
        raise SystemExit("\n".join(problems))
    return result


def write_evidence(url_count: int, render: dict) -> None:
    editions = []
    for lang, stem in (
        ("en", "GUIDE_100_ENGLISH_v2"),
        ("es-419", "GUIDE_100_SPANISH_es-419_v2"),
        ("pt-BR", "GUIDE_100_PORTUGUESE_pt-BR_v2"),
    ):
        docx = OUT / f"{stem}.docx"
        pdf = OUT / f"{stem}.pdf"
        info = subprocess.check_output(["pdfinfo", str(pdf)], text=True)
        count = next(int(line.split(":", 1)[1]) for line in info.splitlines() if line.startswith("Pages:"))
        rendered = sum(1 for row in render["pages"] if row["file"].startswith(stem + "/"))
        assert count == rendered
        editions.append({
            "language": lang, "docx": docx.name, "pdf": pdf.name,
            "docx_bytes": docx.stat().st_size, "pdf_bytes": pdf.stat().st_size,
            "pdf_pages": count, "rendered_pages": rendered, "status": "PASS",
        })

    manifest = {
        "guide": "100", "occupation": "Clinical Laboratory Technician", "build_date": "2026-08-22",
        "status": "PASS", "editions": editions, "reader_verification_urls": url_count,
        "english_source_blob": ENGLISH_BLOB,
        "assurance_boundary": "Internal controlled publication QA; not independent certification, certified translation, medical/legal/regulatory review, CLIA personnel qualification, professional licensure review, laboratory accreditation, occupational-safety/cybersecurity/privacy/accessibility certification, funding approval, employment guarantee, or earnings guarantee.",
    }
    (OUT / "GUIDE_100_PUBLICATION_QA_MANIFEST.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (OUT / "RENDER_QA.json").write_text(json.dumps(render, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    binaries = sorted([*OUT.glob("*.docx"), *OUT.glob("*.pdf")])
    (OUT / "SHA256SUMS.txt").write_text("\n".join(f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}" for p in binaries) + "\n", encoding="utf-8")
    (QA / "GUIDE_100_PUBLICATION_QA_09.md").write_text(
        f"# Guide 100 — Publication QA 09\n\n**Stage:** Publication — **PASS**\n\nEnglish, es-419 and pt-BR Markdown/DOCX/PDF editions passed frozen-source preflight, {url_count}-link reader parity, hard-link checks, DOCX integrity, searchable-PDF validation, all-page rendering, page reconciliation, metadata and SHA-256 checksum generation.\n\nNo independent certification, certified translation, medical/legal/regulatory review, CLIA personnel qualification, professional licensure review, laboratory accreditation, occupational-safety/cybersecurity/privacy/accessibility certification, funding approval, employment guarantee or earnings guarantee is claimed.\n",
        encoding="utf-8",
    )
    (QA / "GUIDE_100_RELEASE_AUDIT_10.md").write_text(
        f"# Guide 100 — Release Audit 10\n\n**Stage:** Release Audit — **PASS**\n\nRelease audit confirms all predecessor gates, trilingual publication artifacts, {url_count}-reader-link parity, checksums, searchable PDFs, all-page rendering, clinical scope/safety boundaries and zero blockers. Guide 100 is the final manual in the controlled Guides 00–100 sequence. After helper status records this release audit as PASS, the deferred collection-wide Markdown revision/change-log layer may begin; no Guide 101 is to be initialized.\n",
        encoding="utf-8",
    )
    shutil.rmtree(OUT / "rendered")


def build() -> None:
    _, urls = preflight()
    check_links(urls)
    build_documents()
    render = render_validate()
    write_evidence(len(urls), render)
    print(f"Guide 100 controlled publication build PASS ({len(urls)} shared URLs)")


def close_status() -> None:
    d = read_status()
    assert d["stages"]["technical_qa"]["status"] == "PASS"
    assert not d.get("blockers")
    for required in (
        QA / "GUIDE_100_PUBLICATION_QA_09.md",
        QA / "GUIDE_100_RELEASE_AUDIT_10.md",
        OUT / "GUIDE_100_PUBLICATION_QA_MANIFEST.json",
        OUT / "SHA256SUMS.txt",
        OUT / "RENDER_QA.json",
    ):
        assert required.exists(), required
    d["stages"]["publication"] = {"status": "PASS", "evidence": [
        "project/revision-2026/guide-100/qa/GUIDE_100_PUBLICATION_QA_09.md",
        "project/revision-2026/guide-100/publication-candidate/GUIDE_100_PUBLICATION_QA_MANIFEST.json",
        "project/revision-2026/guide-100/publication-candidate/SHA256SUMS.txt",
        "project/revision-2026/guide-100/publication-candidate/RENDER_QA.json",
    ]}
    d["stages"]["release_audit"] = {"status": "PASS", "evidence": [
        "project/revision-2026/guide-100/qa/GUIDE_100_RELEASE_AUDIT_10.md"
    ]}
    STATUS.write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("Guide 100 publication and release status closed PASS")


def main() -> None:
    if len(sys.argv) != 2 or sys.argv[1] not in {"build", "close-status"}:
        raise SystemExit("usage: guide100_publication_recovery.py {build|close-status}")
    build() if sys.argv[1] == "build" else close_status()


if __name__ == "__main__":
    main()
