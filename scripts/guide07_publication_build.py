#!/usr/bin/env python3
"""Build and automated-QA Guide 07 trilingual publication candidates.

Automated controls only. This script does not claim independent human review,
professional translation certification, accessibility certification, accreditation,
legal, financial, HR, or publication approval. Rendered pages are generated for
separate visual inspection before the final release-audit gate.
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
SOURCE_DIR = ROOT / "project/revision-2026/guide-07/source"
OUT = ROOT / "project/revision-2026/guide-07/publication-candidate"
PDF_DIR = OUT / "pdf"
RENDER_DIR = OUT / "rendered"
EXPECTED_SHARED_URLS = 13

EDITIONS = {
    "English": (
        SOURCE_DIR / "GUIDE_07_ENGLISH_WORKING_MASTER_v2.md",
        "Lifelong Opportunity Guide 07",
        "en-US",
    ),
    "es-419": (
        SOURCE_DIR / "GUIDE_07_SPANISH_LATAM_WORKING_MASTER_v2.md",
        "Guía de Oportunidades para Toda la Vida 07",
        "es-419",
    ),
    "pt-BR": (
        SOURCE_DIR / "GUIDE_07_PORTUGUESE_BR_WORKING_MASTER_v2.md",
        "Guia de Oportunidades para Toda a Vida 07",
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


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    PDF_DIR.mkdir(parents=True, exist_ok=True)
    RENDER_DIR.mkdir(parents=True, exist_ok=True)

    sources = {}
    for locale, (source, title, lang_code) in EDITIONS.items():
        raw = source.read_bytes()
        if raw.startswith(b"\xef\xbb\xbf"):
            raise SystemExit(f"Unexpected UTF-8 BOM: {source}")
        text = raw.decode("utf-8", errors="strict")
        if "\ufffd" in text:
            raise SystemExit(f"Replacement character in source: {source}")
        sections = [int(m.group(1)) for m in re.finditer(r"^##\s+(\d{1,2})\.\s+", text, re.MULTILINE)]
        if sections != list(range(1, 20)):
            raise SystemExit(f"{locale}: expected sections 1-19, got {sections}")
        source_urls = urls(text)
        if len(source_urls) != EXPECTED_SHARED_URLS:
            raise SystemExit(f"{locale}: expected {EXPECTED_SHARED_URLS} source URLs, got {len(source_urls)}")
        sources[locale] = (source, title, lang_code, text, source_urls)

    canonical_urls = sources["English"][4]
    for locale in ("es-419", "pt-BR"):
        if sources[locale][4] != canonical_urls:
            raise SystemExit(f"{locale}: source URL set differs from English")

    stem = "Lifelong_Opportunity_Guide_07_Customer_Service_Specialist"
    generated_docx: list[Path] = []
    for locale, (source, _title, _lang_code, _text, _urls) in sources.items():
        docx = OUT / f"{stem}_{locale}_v2.0.docx"
        run(
            "pandoc", str(source), "--from=gfm", "--to=docx", "--standalone",
            "--metadata", f"lang={locale}", "--output", str(docx)
        )
        if docx.stat().st_size < 15000:
            raise SystemExit(f"DOCX unexpectedly small: {docx}")
        generated_docx.append(docx)

    subprocess.run(
        ["libreoffice", "--headless", "--convert-to", "pdf", "--outdir", str(PDF_DIR), *map(str, generated_docx)],
        check=True,
    )

    report = {
        "guide": "07",
        "occupation": "Customer Service Specialist / Customer Service Representative",
        "version": "2.0",
        "status": "publication candidate; automated QA plus rendered-page evidence pending visual review",
        "independent_human_certification": False,
        "professional_translation_certification": False,
        "accessibility_certification": False,
        "legal_financial_or_hr_review_certification": False,
        "verified_shared_source_url_count": EXPECTED_SHARED_URLS,
        "files": [],
        "renders": [],
    }

    for locale, (_source, title, lang_code, _text, source_urls) in sources.items():
        docx = OUT / f"{stem}_{locale}_v2.0.docx"
        pdf = PDF_DIR / f"{stem}_{locale}_v2.0.pdf"
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

        locale_render_dir = RENDER_DIR / locale
        locale_render_dir.mkdir(parents=True, exist_ok=True)
        prefix = locale_render_dir / "page"
        subprocess.run(["pdftoppm", "-png", "-r", "150", str(pdf), str(prefix)], check=True)
        pngs = sorted(locale_render_dir.glob("page-*.png"))
        if len(pngs) != pages:
            raise SystemExit(f"{locale}: rendered {len(pngs)} pages, expected {pages}")
        if any(p.stat().st_size < 5000 for p in pngs):
            raise SystemExit(f"{locale}: one or more rendered pages are unexpectedly small")

        for page_no, png in enumerate(pngs, start=1):
            report["renders"].append({
                "locale": locale,
                "page": page_no,
                "path": str(png.relative_to(ROOT)),
                "bytes": png.stat().st_size,
                "sha256": sha256(png),
            })

        for file in (docx, pdf):
            report["files"].append({
                "locale": locale,
                "language_code": lang_code,
                "path": str(file.relative_to(ROOT)),
                "bytes": file.stat().st_size,
                "sha256": sha256(file),
                "pages": pages if file.suffix == ".pdf" else None,
            })

    manifest = OUT / "GUIDE_07_PUBLICATION_QA_MANIFEST.json"
    manifest.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    checksums = OUT / "SHA256SUMS.txt"
    candidate_base = Path("project/revision-2026/guide-07/publication-candidate")
    checksum_items = report["files"] + report["renders"]
    checksums.write_text(
        "\n".join(
            f"{item['sha256']}  {Path(item['path']).relative_to(candidate_base)}"
            for item in checksum_items
        ) + "\n",
        encoding="utf-8",
    )

    print("Guide 07 trilingual publication candidate build and automated QA: PASS")
    for locale in EDITIONS:
        pages = next(i["pages"] for i in report["files"] if i["locale"] == locale and i["pages"] is not None)
        print(f"{locale}: {pages} PDF pages rendered")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
