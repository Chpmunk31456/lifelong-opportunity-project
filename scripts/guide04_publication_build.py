#!/usr/bin/env python3
"""Build and QA Guide 04 trilingual publication candidates.

Automated controls only. This script does not claim independent human review,
professional translation certification, accessibility certification, accreditation,
legal review, or publication approval.
"""
from __future__ import annotations

from html import unescape
import hashlib
import json
from pathlib import Path
import re
import subprocess
import unicodedata
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "project/revision-2026/guide-04/working"
OUT = ROOT / "project/revision-2026/guide-04/publication-candidate"
PDF_DIR = OUT / "pdf"
RENDER_DIR = OUT / "rendered"
EXPECTED_SHARED_URLS = 12

EDITIONS = {
    "English": (
        SOURCE_DIR / "GUIDE_04_ENGLISH_WORKING_MASTER_06.md",
        "LIFELONG OPPORTUNITY — PROJECT COORDINATOR",
        "en-US",
    ),
    "es-419": (
        SOURCE_DIR / "GUIDE_04_ES_419_WORKING_MASTER_08.md",
        "OPORTUNIDAD PARA TODA LA VIDA — COORDINADOR/A DE PROYECTOS",
        "es-419",
    ),
    "pt-BR": (
        SOURCE_DIR / "GUIDE_04_PT_BR_WORKING_MASTER_10.md",
        "OPORTUNIDADE PARA TODA A VIDA — COORDENADOR/A DE PROJETOS",
        "pt-BR",
    ),
}


def normalize(value: str) -> str:
    value = unicodedata.normalize("NFKD", value)
    value = "".join(ch for ch in value if not unicodedata.combining(ch))
    return " ".join(value.casefold().split())


def urls(text: str) -> set[str]:
    return set(re.findall(r"https?://[^\s)>\]]+", text))


def run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, check=True, text=True, capture_output=True)


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    PDF_DIR.mkdir(parents=True, exist_ok=True)
    RENDER_DIR.mkdir(parents=True, exist_ok=True)

    sources: dict[str, tuple[Path, str, str, str, set[str]]] = {}
    for locale, (source, title, lang_code) in EDITIONS.items():
        raw = source.read_bytes()
        if raw.startswith(b"\xef\xbb\xbf"):
            raise SystemExit(f"Unexpected UTF-8 BOM: {source}")
        text = raw.decode("utf-8", errors="strict")
        if "\ufffd" in text:
            raise SystemExit(f"Replacement character in source: {source}")
        sections = [int(m.group(1)) for m in re.finditer(r"^#\s+(\d{1,2})\.\s+", text, re.MULTILINE)]
        if sections != list(range(1, 23)):
            raise SystemExit(f"{locale}: expected sections 1-22, got {sections}")
        source_urls = urls(text)
        if len(source_urls) != EXPECTED_SHARED_URLS:
            raise SystemExit(
                f"{locale}: expected {EXPECTED_SHARED_URLS} verified source URLs, got {len(source_urls)}"
            )
        for anchor in ("BLS", "WIOA", "Registered Apprenticeship", "NOC", "SENA", "Servicio Público de Empleo"):
            if anchor not in text:
                raise SystemExit(f"{locale}: missing control anchor {anchor}")
        sources[locale] = (source, title, lang_code, text, source_urls)

    canonical_urls = sources["English"][4]
    for locale in ("es-419", "pt-BR"):
        if sources[locale][4] != canonical_urls:
            raise SystemExit(f"{locale}: source URL set differs from English")

    for locale, (source, _title, _lang_code, _text, _urls) in sources.items():
        docx = OUT / f"Lifelong_Opportunity_Guide_04_Project_Coordinator_{locale}_v2.0.docx"
        run(
            "pandoc", str(source), "--from=gfm", "--to=docx", "--standalone",
            "--metadata", f"lang={locale}", "--output", str(docx),
        )
        if docx.stat().st_size < 15000:
            raise SystemExit(f"DOCX unexpectedly small: {docx}")

    subprocess.run(
        [
            "libreoffice", "--headless", "--convert-to", "pdf", "--outdir", str(PDF_DIR),
            *[str(OUT / f"Lifelong_Opportunity_Guide_04_Project_Coordinator_{locale}_v2.0.docx") for locale in EDITIONS],
        ],
        check=True,
    )

    report = {
        "guide": "04",
        "occupation": "Project Coordinator",
        "version": "2.0",
        "status": "publication candidate; automated QA only",
        "independent_human_certification": False,
        "professional_translation_certification": False,
        "accessibility_certification": False,
        "verified_shared_source_url_count": EXPECTED_SHARED_URLS,
        "files": [],
    }

    for locale, (_source, title, lang_code, _text, source_urls) in sources.items():
        docx = OUT / f"Lifelong_Opportunity_Guide_04_Project_Coordinator_{locale}_v2.0.docx"
        pdf = PDF_DIR / f"Lifelong_Opportunity_Guide_04_Project_Coordinator_{locale}_v2.0.pdf"
        if not docx.is_file() or not pdf.is_file():
            raise SystemExit(f"Missing generated pair for {locale}")

        with ZipFile(docx) as zf:
            names = set(zf.namelist())
            required = {"word/document.xml", "word/_rels/document.xml.rels", "docProps/core.xml"}
            missing = required - names
            if missing:
                raise SystemExit(f"{docx}: missing OOXML parts {sorted(missing)}")
            document_xml = zf.read("word/document.xml").decode("utf-8", errors="strict")
            relationships = zf.read("word/_rels/document.xml.rels").decode("utf-8", errors="strict")
            core_xml = zf.read("docProps/core.xml").decode("utf-8", errors="strict")
            if "\ufffd" in document_xml + relationships + core_xml:
                raise SystemExit(f"{docx}: encoding replacement character detected")
            targets = unescape(relationships)
            missing_links = sorted(url for url in source_urls if url not in targets)
            if missing_links:
                raise SystemExit(f"{docx}: hyperlinks missing from relationships: {missing_links}")

        pdfinfo = run("pdfinfo", str(pdf)).stdout
        match = re.search(r"^Pages:\s+(\d+)$", pdfinfo, re.MULTILINE)
        pages = int(match.group(1)) if match else 0
        if pages < 8:
            raise SystemExit(f"{pdf}: unexpectedly low page count {pages}")

        txt = pdf.with_suffix(".txt")
        subprocess.run(["pdftotext", "-layout", str(pdf), str(txt)], check=True)
        extracted = txt.read_text(encoding="utf-8", errors="replace")
        txt.unlink()
        if len(extracted.strip()) < 10000:
            raise SystemExit(f"{pdf}: insufficient extractable text")
        if normalize(title) not in normalize(extracted):
            raise SystemExit(f"{pdf}: expected title not found")
        if "\ufffd" in extracted:
            raise SystemExit(f"{pdf}: replacement-character encoding defect detected")

        render = RENDER_DIR / f"{pdf.stem}_page_001"
        subprocess.run(["pdftoppm", "-f", "1", "-singlefile", "-png", "-r", "130", str(pdf), str(render)], check=True)
        png = Path(str(render) + ".png")
        if not png.is_file() or png.stat().st_size < 5000:
            raise SystemExit(f"Missing or unexpectedly small first-page render: {png}")

        for file in (docx, pdf):
            report["files"].append({
                "locale": locale,
                "language_code": lang_code,
                "path": str(file.relative_to(ROOT)),
                "bytes": file.stat().st_size,
                "sha256": hashlib.sha256(file.read_bytes()).hexdigest(),
                "pages": pages if file.suffix == ".pdf" else None,
            })

    expected_renders = {
        RENDER_DIR / f"Lifelong_Opportunity_Guide_04_Project_Coordinator_{locale}_v2.0_page_001.png"
        for locale in EDITIONS
    }
    if not all(path.is_file() and path.stat().st_size >= 5000 for path in expected_renders):
        raise SystemExit("Expected three valid Guide 04 first-page renders")

    manifest = OUT / "GUIDE_04_PUBLICATION_QA_MANIFEST.json"
    manifest.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    checksums = OUT / "SHA256SUMS.txt"
    candidate_base = Path("project/revision-2026/guide-04/publication-candidate")
    checksums.write_text(
        "\n".join(
            f"{item['sha256']}  {Path(item['path']).relative_to(candidate_base)}"
            for item in report["files"]
        ) + "\n",
        encoding="utf-8",
    )

    print("Guide 04 trilingual publication candidate build and automated QA: PASS")
    print("DOCX/PDF pairs: 3")
    print("First-page renders: 3")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
