#!/usr/bin/env python3
"""Build and audit Guide 53 trilingual publication candidates.

Automated controls only. This script does not claim independent human review,
professional translation certification, accessibility certification, accreditation,
clinical review, legal review, or publication approval.
"""
from __future__ import annotations

from html import unescape
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import unicodedata
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "project/revision-2026/guide-53/working-masters"
OUT = ROOT / "project/revision-2026/guide-53/publication-candidate"
RENDER_DIR = OUT / "rendered"

EDITIONS = {
    "English": {
        "source": SOURCE_DIR / "GUIDE_53_PHYSICAL_THERAPIST_ASSISTANT_ENGLISH_v2.md",
        "stem": "GUIDE_53_ENGLISH_v2",
        "title": "Guide 53 — Physical Therapist Assistant",
        "lang": "en-US",
    },
    "Spanish": {
        "source": SOURCE_DIR / "GUIDE_53_PHYSICAL_THERAPIST_ASSISTANT_SPANISH_es-419_v1.md",
        "stem": "GUIDE_53_SPANISH_es-419_v1",
        "title": "Guía 53 — Asistente de fisioterapia (Physical Therapist Assistant)",
        "lang": "es-419",
    },
    "Portuguese": {
        "source": SOURCE_DIR / "GUIDE_53_PHYSICAL_THERAPIST_ASSISTANT_PORTUGUESE_pt-BR_v1.md",
        "stem": "GUIDE_53_PORTUGUESE_pt-BR_v1",
        "title": "Guia 53 — Assistente de fisioterapia (Physical Therapist Assistant)",
        "lang": "pt-BR",
    },
}

AUTHOR = "Alberto (Al) Leiva"
SUBJECT = "Lifelong Opportunity career and education guide"


def normalize(value: str) -> str:
    value = unicodedata.normalize("NFKD", value)
    value = "".join(ch for ch in value if not unicodedata.combining(ch))
    return " ".join(value.casefold().split())


def urls(text: str) -> list[str]:
    return re.findall(r"https?://[^\s)>\]]+", text)


def run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, check=True, text=True, capture_output=True)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    if RENDER_DIR.exists():
        shutil.rmtree(RENDER_DIR)
    RENDER_DIR.mkdir(parents=True, exist_ok=True)

    source_data: dict[str, dict[str, object]] = {}
    canonical_url_sequence: list[str] | None = None
    canonical_h2_count: int | None = None

    required_anchors = (
        "CAPTE", "FSBPT", "NPTE", "BLS", "WIOA", "FAFSA",
        "NOC 32109", "Ley 528 de 1999", "SENA", "OIT/Cinterfor",
        "Salary.com", "USD $65", "CAD $26", "22%",
    )

    for edition, meta in EDITIONS.items():
        source = meta["source"]
        assert isinstance(source, Path)
        raw = source.read_bytes()
        if raw.startswith(b"\xef\xbb\xbf"):
            raise SystemExit(f"Unexpected UTF-8 BOM: {source}")
        text = raw.decode("utf-8", errors="strict")
        if "\ufffd" in text:
            raise SystemExit(f"Replacement character in source: {source}")
        if any(ch in text for ch in ("\u200b", "\ufeff")):
            raise SystemExit(f"Zero-width/BOM character in source: {source}")

        h2_count = len(re.findall(r"^##\s+", text, re.MULTILINE))
        if h2_count < 20:
            raise SystemExit(f"{edition}: unexpectedly low H2 section count {h2_count}")
        if canonical_h2_count is None:
            canonical_h2_count = h2_count
        elif h2_count != canonical_h2_count:
            raise SystemExit(f"{edition}: H2 count {h2_count} differs from English {canonical_h2_count}")

        source_urls = urls(text)
        if len(source_urls) < 20:
            raise SystemExit(f"{edition}: unexpectedly low source URL count {len(source_urls)}")
        if canonical_url_sequence is None:
            canonical_url_sequence = source_urls
        elif source_urls != canonical_url_sequence:
            raise SystemExit(f"{edition}: source URL sequence differs from English")

        for anchor in required_anchors:
            if anchor not in text:
                raise SystemExit(f"{edition}: missing controlled anchor {anchor!r}")

        source_data[edition] = {
            "text": text,
            "urls": source_urls,
            "h2_count": h2_count,
        }

    report: dict[str, object] = {
        "guide": "53",
        "occupation": "Physical Therapist Assistant",
        "build_date": "2026-08-19",
        "status": "publication candidate; automated QA only",
        "independent_human_certification": False,
        "professional_translation_certification": False,
        "accessibility_certification": False,
        "clinical_review_certification": False,
        "shared_source_url_count": len(canonical_url_sequence or []),
        "h2_section_count": canonical_h2_count,
        "files": [],
        "rendered_pages": {},
    }

    content_files: list[Path] = []

    for edition, meta in EDITIONS.items():
        source = meta["source"]
        assert isinstance(source, Path)
        stem = str(meta["stem"])
        title = str(meta["title"])
        lang = str(meta["lang"])

        md = OUT / f"{stem}.md"
        docx = OUT / f"{stem}.docx"
        pdf = OUT / f"{stem}.pdf"

        shutil.copyfile(source, md)
        if md.read_bytes() != source.read_bytes():
            raise SystemExit(f"{edition}: publication Markdown is not byte-identical to frozen master")

        run(
            "pandoc", str(source),
            "--from=gfm-tex_math_dollars", "--to=docx", "--standalone",
            "--metadata", f"title={title}",
            "--metadata", f"author={AUTHOR}",
            "--metadata", f"subject={SUBJECT}",
            "--metadata", f"lang={lang}",
            "--output", str(docx),
        )
        if docx.stat().st_size < 20000:
            raise SystemExit(f"{edition}: DOCX unexpectedly small: {docx.stat().st_size}")

        subprocess.run(
            ["libreoffice", "--headless", "--convert-to", "pdf", "--outdir", str(OUT), str(docx)],
            check=True,
        )
        if not pdf.is_file() or pdf.stat().st_size < 50000:
            raise SystemExit(f"{edition}: missing or unexpectedly small PDF")

        source_urls = source_data[edition]["urls"]
        assert isinstance(source_urls, list)
        with ZipFile(docx) as zf:
            names = set(zf.namelist())
            required_parts = {"word/document.xml", "word/_rels/document.xml.rels", "docProps/core.xml"}
            missing = required_parts - names
            if missing:
                raise SystemExit(f"{edition}: DOCX missing OOXML parts {sorted(missing)}")
            document_xml = zf.read("word/document.xml").decode("utf-8", errors="strict")
            rels = zf.read("word/_rels/document.xml.rels").decode("utf-8", errors="strict")
            core_xml = zf.read("docProps/core.xml").decode("utf-8", errors="strict")
            if "\ufffd" in document_xml + rels + core_xml:
                raise SystemExit(f"{edition}: replacement character in DOCX XML")
            targets = unescape(rels)
            missing_links = [u for u in source_urls if u not in targets]
            if missing_links:
                raise SystemExit(f"{edition}: missing hyperlinks from DOCX relationships: {missing_links}")
            if AUTHOR not in core_xml:
                raise SystemExit(f"{edition}: author metadata missing from DOCX")

        pdfinfo = run("pdfinfo", str(pdf)).stdout
        page_match = re.search(r"^Pages:\s+(\d+)$", pdfinfo, re.MULTILINE)
        pages = int(page_match.group(1)) if page_match else 0
        if pages < 8 or pages > 30:
            raise SystemExit(f"{edition}: implausible PDF page count {pages}")

        txt = OUT / f"{stem}.txt"
        subprocess.run(["pdftotext", "-layout", str(pdf), str(txt)], check=True)
        extracted = txt.read_text(encoding="utf-8", errors="replace")
        txt.unlink()
        if len(extracted.strip()) < 15000:
            raise SystemExit(f"{edition}: insufficient extractable PDF text")
        if "\ufffd" in extracted:
            raise SystemExit(f"{edition}: replacement character in PDF text extraction")
        # Title wording can wrap or normalize differently; require the stable occupation identity.
        if normalize("Physical Therapist Assistant") not in normalize(extracted):
            raise SystemExit(f"{edition}: occupation identity missing from PDF extraction")

        edition_render_dir = RENDER_DIR / lang
        edition_render_dir.mkdir(parents=True, exist_ok=True)
        subprocess.run(
            ["pdftoppm", "-png", "-r", "120", str(pdf), str(edition_render_dir / "page")],
            check=True,
        )
        rendered = sorted(edition_render_dir.glob("page-*.png"))
        if len(rendered) != pages:
            raise SystemExit(f"{edition}: rendered page count {len(rendered)} != PDF page count {pages}")
        if any(p.stat().st_size < 5000 for p in rendered):
            raise SystemExit(f"{edition}: unexpectedly small rendered page")

        report["rendered_pages"][lang] = pages
        for file in (md, docx, pdf):
            content_files.append(file)
            report["files"].append({
                "edition": edition,
                "language_code": lang,
                "path": str(file.relative_to(ROOT)),
                "bytes": file.stat().st_size,
                "sha256": sha256(file),
                "pages": pages if file.suffix == ".pdf" else None,
            })

    manifest = OUT / "GUIDE_53_PUBLICATION_QA_MANIFEST.json"
    manifest.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    checksums = OUT / "SHA256SUMS.txt"
    checksums.write_text(
        "\n".join(f"{sha256(p)}  {p.name}" for p in content_files) + "\n",
        encoding="utf-8",
    )

    # Revalidate the sealed content hashes immediately.
    for p in content_files:
        expected = next(
            line.split()[0] for line in checksums.read_text(encoding="utf-8").splitlines()
            if line.endswith(f"  {p.name}")
        )
        if sha256(p) != expected:
            raise SystemExit(f"Checksum revalidation failed: {p.name}")

    print("Guide 53 trilingual publication build and automated QA: PASS")
    print(f"Content artifacts: {len(content_files)}")
    print(f"Rendered pages: {sum(report['rendered_pages'].values())}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
