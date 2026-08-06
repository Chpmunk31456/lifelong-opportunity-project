#!/usr/bin/env python3
"""Extract and compare Guide 02 English DOCX/PDF artifacts.

Automated technical intake only. This script does not certify factual currency,
accessibility conformance, editorial quality, accreditation, or publication readiness.
"""
from __future__ import annotations

import hashlib
import json
import re
import zipfile
from difflib import SequenceMatcher
from pathlib import Path
from xml.etree import ElementTree as ET

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
DOCX = ROOT / "02-peer-support-specialist/english/docx/Lifelong_Opportunity_Peer_Support_Specialist_Guide_English_v1.0.docx"
PDF = ROOT / "02-peer-support-specialist/english/pdf/Lifelong_Opportunity_Peer_Support_Specialist_Guide_English_v1.0.pdf"
OUT = ROOT / "project/revision-2026/guide-02"
SOURCE = OUT / "source"
QA = OUT / "qa"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().casefold()


def main() -> int:
    if not DOCX.is_file() or not PDF.is_file():
        raise SystemExit("Missing Guide 02 English DOCX or PDF artifact")

    SOURCE.mkdir(parents=True, exist_ok=True)
    QA.mkdir(parents=True, exist_ok=True)

    ns = {
        "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
        "dc": "http://purl.org/dc/elements/1.1/",
        "dcterms": "http://purl.org/dc/terms/",
    }
    with zipfile.ZipFile(DOCX) as archive:
        names = set(archive.namelist())
        required = {
            "[Content_Types].xml",
            "word/document.xml",
            "word/_rels/document.xml.rels",
            "docProps/core.xml",
        }
        missing = sorted(required - names)
        if missing:
            raise SystemExit(f"Missing required OOXML parts: {missing}")

        document_root = ET.fromstring(archive.read("word/document.xml"))
        paragraphs: list[str] = []
        for paragraph in document_root.findall(".//w:p", ns):
            text = "".join(node.text or "" for node in paragraph.findall(".//w:t", ns)).strip()
            if text:
                paragraphs.append(text)
        docx_text = "\n\n".join(paragraphs) + "\n"

        relationships_root = ET.fromstring(archive.read("word/_rels/document.xml.rels"))
        links = sorted(
            {
                relationship.attrib.get("Target", "")
                for relationship in relationships_root
                if relationship.attrib.get("TargetMode") == "External"
            }
        )

        core = ET.fromstring(archive.read("docProps/core.xml"))

        def value(tag: str) -> str:
            element = core.find(tag, ns)
            return (element.text or "").strip() if element is not None else ""

        metadata = {
            "title": value("dc:title"),
            "subject": value("dc:subject"),
            "creator": value("dc:creator"),
            "description": value("dc:description"),
            "created": value("dcterms:created"),
            "modified": value("dcterms:modified"),
        }

    docx_extract = SOURCE / "GUIDE_02_ENGLISH_DOCX_EXTRACTED_BASELINE.md"
    docx_extract.write_text(
        "# Guide 02 English DOCX extracted baseline\n\n" + docx_text,
        encoding="utf-8",
        newline="\n",
    )

    reader = PdfReader(str(PDF), strict=True)
    if reader.is_encrypted:
        raise SystemExit("Guide 02 PDF is encrypted")
    pdf_pages = [(page.extract_text() or "").strip() for page in reader.pages]
    pdf_text = "\n\n".join(text for text in pdf_pages if text) + "\n"
    if "\ufffd" in pdf_text:
        raise SystemExit("Replacement-character encoding defect in PDF extraction")
    pdf_text_path = SOURCE / "GUIDE_02_ENGLISH_PDF_EXTRACTED_BASELINE.txt"
    pdf_text_path.write_text(pdf_text, encoding="utf-8", newline="\n")

    pdf_metadata = {str(key): str(value) for key, value in (reader.metadata or {}).items()}
    pdf_technical = {
        "pages": len(reader.pages),
        "encrypted": reader.is_encrypted,
        "metadata": pdf_metadata,
        "extracted_characters": len(pdf_text),
        "parser": "pypdf strict mode",
    }
    (QA / "pdf-technical-results.json").write_text(
        json.dumps(pdf_technical, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )

    normalized_docx = normalize(docx_text)
    normalized_pdf = normalize(pdf_text)
    ratio = SequenceMatcher(None, normalized_docx, normalized_pdf).ratio()
    containment = normalized_docx in normalized_pdf or normalized_pdf in normalized_docx

    decision = (
        "**PASS for technical source-equivalence intake:** the artifacts are structurally readable and their normalized text is highly consistent."
        if ratio >= 0.97
        else "**HOLD:** normalized text similarity is below 0.97; inspect extraction differences before using either artifact as the revision baseline."
    )

    report_lines = [
        "# Guide 02 English artifact extraction and equivalence QA 01",
        "",
        "- **Guide:** 02 - Peer Support Specialist",
        "- **Scope:** Existing English v1.0 DOCX and PDF only",
        "- **Control:** Automated technical extraction; not independent human certification, accreditation, professional translation certification, accessibility certification, legal review, or factual validation",
        "",
        "## Inventory",
        "",
        "| Artifact | Bytes | SHA-256 |",
        "|---|---:|---|",
        f"| `{DOCX.relative_to(ROOT).as_posix()}` | {DOCX.stat().st_size} | `{digest(DOCX)}` |",
        f"| `{PDF.relative_to(ROOT).as_posix()}` | {PDF.stat().st_size} | `{digest(PDF)}` |",
        "",
        "## DOCX package and metadata",
        "",
        "- Missing required OOXML parts: None",
        f"- Extracted non-empty paragraphs: {len(paragraphs)}",
        f"- External relationships: {len(links)}",
        f"- Core metadata: `{json.dumps(metadata, ensure_ascii=False)}`",
        "",
        "## PDF technical results",
        "",
        f"- Pages: {len(reader.pages)}",
        f"- Encrypted: {reader.is_encrypted}",
        f"- Extracted characters: {len(pdf_text)}",
        "- Structural parser: pypdf strict mode passed",
        f"- Metadata: `{json.dumps(pdf_metadata, ensure_ascii=False)}`",
        "",
        "## DOCX-to-PDF text comparison",
        "",
        f"- Normalized similarity ratio: **{ratio:.6f}**",
        f"- Full normalized containment: **{containment}**",
        f"- DOCX normalized characters: {len(normalized_docx)}",
        f"- PDF normalized characters: {len(normalized_pdf)}",
        "",
        "## Gate decision",
        "",
        decision,
        "",
        "This result does not validate factual currency, link destinations, accessibility conformance, editorial quality, or publication readiness. Those remain separate controlled gates.",
        "",
    ]
    report = QA / "GUIDE_02_ENGLISH_ARTIFACT_EXTRACTION_QA_01.md"
    report.write_text("\n".join(report_lines), encoding="utf-8", newline="\n")
    (QA / "GUIDE_02_ENGLISH_EXTERNAL_LINKS_01.txt").write_text(
        "\n".join(links) + "\n", encoding="utf-8", newline="\n"
    )

    if ratio < 0.97 or len(pdf_text.strip()) < 1000:
        raise SystemExit("Fail-closed Guide 02 artifact QA gate")

    print(f"Guide 02 artifact QA passed with similarity {ratio:.6f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
