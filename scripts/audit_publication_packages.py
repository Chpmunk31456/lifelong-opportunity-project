#!/usr/bin/env python3
"""Automated preflight for all published DOCX and PDF guide editions.

This script detects package corruption, missing searchable text, near-empty files,
obvious encoding problems, and basic guide/language metadata inconsistencies.
It cannot certify visual layout, accessibility semantics, factual currency, or
human translation quality.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
import unicodedata
import zipfile
from collections import Counter, defaultdict
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "QA_PUBLICATION_PREFLIGHT.md"
JSON_REPORT = ROOT / "QA_PUBLICATION_PREFLIGHT.json"
GUIDE_RE = re.compile(r"^(\d{2,3})-")
W_NS = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
LANGUAGE_BY_PATH = {
    "english": "English",
    "spanish": "Spanish (Latin America)",
    "portuguese": "Brazilian Portuguese",
}


def norm(text: str) -> str:
    text = unicodedata.normalize("NFKD", text)
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, text=True, capture_output=True, check=False)


def root_title(guide_dir: Path) -> str:
    readme = guide_dir / "README.md"
    if not readme.exists():
        return guide_dir.name
    lines = readme.read_text(encoding="utf-8-sig", errors="replace").splitlines()
    headings = [line.lstrip("#").strip() for line in lines if line.startswith("## ")]
    return headings[0] if headings else guide_dir.name


def language_for(path: Path) -> str:
    lowered = [part.lower() for part in path.parts]
    for key, label in LANGUAGE_BY_PATH.items():
        if key in lowered:
            return label
    return "Unknown"


def docx_text(path: Path) -> tuple[str, list[str]]:
    problems: list[str] = []
    try:
        with zipfile.ZipFile(path) as zf:
            bad = zf.testzip()
            if bad:
                problems.append(f"corrupt ZIP member: {bad}")
            required = {"[Content_Types].xml", "word/document.xml"}
            missing = required - set(zf.namelist())
            if missing:
                problems.append("missing required DOCX parts: " + ", ".join(sorted(missing)))
                return "", problems
            xml = zf.read("word/document.xml")
    except (zipfile.BadZipFile, OSError) as exc:
        return "", [f"cannot open DOCX package: {exc}"]
    try:
        root = ET.fromstring(xml)
        text = " ".join(node.text or "" for node in root.iter(W_NS + "t"))
    except ET.ParseError as exc:
        return "", [f"invalid word/document.xml: {exc}"]
    return re.sub(r"\s+", " ", text).strip(), problems


def pdf_text(path: Path) -> tuple[str, int | None, list[str]]:
    problems: list[str] = []
    info = run("pdfinfo", str(path))
    pages: int | None = None
    if info.returncode != 0:
        problems.append("pdfinfo failed: " + (info.stderr.strip() or "unknown error"))
    else:
        match = re.search(r"^Pages:\s+(\d+)", info.stdout, re.MULTILINE)
        if match:
            pages = int(match.group(1))
        if "Encrypted:       yes" in info.stdout:
            problems.append("PDF is encrypted")
    with tempfile.NamedTemporaryFile(suffix=".txt") as tmp:
        extract = run("pdftotext", "-enc", "UTF-8", str(path), tmp.name)
        if extract.returncode != 0:
            problems.append("pdftotext failed: " + (extract.stderr.strip() or "unknown error"))
            return "", pages, problems
        try:
            text = Path(tmp.name).read_text(encoding="utf-8", errors="replace")
        except OSError as exc:
            return "", pages, problems + [f"cannot read extracted PDF text: {exc}"]
    return re.sub(r"\s+", " ", text).strip(), pages, problems


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    records: list[dict[str, object]] = []
    counts = Counter()
    guide_files: dict[int, list[Path]] = defaultdict(list)

    guide_dirs: list[tuple[int, Path]] = []
    for path in ROOT.iterdir():
        if path.is_dir() and (match := GUIDE_RE.match(path.name)):
            number = int(match.group(1))
            if 0 <= number <= 100:
                guide_dirs.append((number, path))
    guide_dirs.sort()

    for number, guide_dir in guide_dirs:
        files = sorted(p for p in guide_dir.rglob("*") if p.suffix.lower() in {".docx", ".pdf"})
        guide_files[number] = files
        title = root_title(guide_dir)
        by_language = Counter(language_for(p) for p in files)
        for language in LANGUAGE_BY_PATH.values():
            expected = 2
            actual = by_language[language]
            if actual != expected:
                errors.append(f"Guide {number:02d} {language}: expected 2 package files, found {actual}")

        for path in files:
            rel = path.relative_to(ROOT).as_posix()
            language = language_for(path)
            kind = path.suffix.lower()[1:]
            counts[kind] += 1
            size = path.stat().st_size
            local_errors: list[str] = []
            local_warnings: list[str] = []
            pages: int | None = None

            if size < 1024:
                local_errors.append(f"file is unusually small ({size} bytes)")

            if kind == "docx":
                text, package_problems = docx_text(path)
                local_errors.extend(package_problems)
            else:
                text, pages, package_problems = pdf_text(path)
                local_errors.extend(package_problems)

            words = re.findall(r"\b\w+\b", text, flags=re.UNICODE)
            if len(words) < 100:
                local_errors.append(f"extracted text is near-empty ({len(words)} words)")
            if "�" in text:
                local_warnings.append("Unicode replacement character appears in extracted text")
            if re.search(r"\bfuture guide\b", text, re.IGNORECASE):
                local_errors.append("placeholder phrase 'future guide' appears in document text")
            if number != 49 and re.search(r"\b(?:guide|guia)\s*49\b", text, re.IGNORECASE):
                local_warnings.append("possible copied Guide 49 metadata in document text")

            filename_norm = norm(path.stem)
            if language == "English":
                key_terms = [term for term in norm(title).split() if len(term) >= 5][:4]
                if key_terms and sum(term in filename_norm for term in key_terms) < min(2, len(key_terms)):
                    local_warnings.append("English filename may not align with the root guide title")

            for item in local_errors:
                errors.append(f"{rel}: {item}")
            for item in local_warnings:
                warnings.append(f"{rel}: {item}")

            records.append({
                "guide": number,
                "title": title,
                "language": language,
                "format": kind.upper(),
                "path": rel,
                "size_bytes": size,
                "pages": pages,
                "word_count": len(words),
                "errors": local_errors,
                "warnings": local_warnings,
            })

    expected_total = 101 * 3
    if counts["docx"] != expected_total:
        errors.append(f"Expected {expected_total} DOCX files, found {counts['docx']}")
    if counts["pdf"] != expected_total:
        errors.append(f"Expected {expected_total} PDF files, found {counts['pdf']}")

    lines = [
        "# Publication Package Preflight",
        "",
        "Automated integrity and text-extraction review of all published DOCX and PDF guide editions.",
        "",
        "## Summary",
        "",
        f"- Guide directories reviewed: **{len(guide_dirs)}**",
        f"- DOCX files reviewed: **{counts['docx']}**",
        f"- PDF files reviewed: **{counts['pdf']}**",
        f"- Total package files reviewed: **{len(records)}**",
        f"- Blocking defects: **{len(errors)}**",
        f"- Warnings: **{len(warnings)}**",
        "",
        "## Blocking defects",
        "",
    ]
    lines.extend(f"- {item}" for item in errors) if errors else lines.append("- None detected.")
    lines.extend(["", "## Warnings", ""])
    lines.extend(f"- {item}" for item in warnings) if warnings else lines.append("- None detected.")
    lines.extend([
        "",
        "## Scope limitation",
        "",
        "This automated preflight checks file inventory, DOCX ZIP/XML integrity, PDF readability and text extraction, "
        "near-empty output, obvious placeholder metadata, and selected filename/title consistency signals. It does not "
        "certify visual layout, reading order, tagged-PDF accessibility, color contrast, factual currency, link destinations "
        "inside binary files, or human Spanish and Brazilian Portuguese translation quality. Those require separate review.",
        "",
    ])
    REPORT.write_text("\n".join(lines), encoding="utf-8")
    JSON_REPORT.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
    print("\n".join(lines))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
