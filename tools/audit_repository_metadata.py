#!/usr/bin/env python3
"""Audit guide metadata, linked packages, and local Markdown links."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "QA_METADATA_AUDIT.md"
GUIDE_DIR_RE = re.compile(r"^(\d{2,3})-")
GUIDE_HEADING_RE = re.compile(r"^#\s+Lifelong Opportunity Guide\s+(\d{1,3})\s*$", re.MULTILINE | re.IGNORECASE)
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
LANGUAGE_ROWS = {
    "english": re.compile(r"^\|\s*English\s*\|(.+)$", re.MULTILINE | re.IGNORECASE),
    "spanish": re.compile(r"^\|\s*Spanish(?:\s*\(Latin America\))?\s*\|(.+)$", re.MULTILINE | re.IGNORECASE),
    "portuguese": re.compile(r"^\|\s*(?:Brazilian Portuguese|Portuguese(?:\s*\(Brazil\))?)\s*\|(.+)$", re.MULTILINE | re.IGNORECASE),
}
LANGUAGE_NAMES = {"english": "English", "spanish": "Spanish", "portuguese": "Portuguese"}


def guide_directories() -> list[tuple[int, Path]]:
    found: list[tuple[int, Path]] = []
    for path in ROOT.iterdir():
        if path.is_dir() and (match := GUIDE_DIR_RE.match(path.name)):
            found.append((int(match.group(1)), path))
    return sorted(found)


def local_target(source: Path, raw_target: str) -> Path | None:
    target = raw_target.strip().split("#", 1)[0].strip()
    if not target or target.startswith(("http://", "https://", "mailto:", "tel:", "#")):
        return None
    return (source.parent / unquote(target)).resolve()


def display(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def row_links(text: str, language: str) -> list[str]:
    match = LANGUAGE_ROWS[language].search(text)
    return MARKDOWN_LINK_RE.findall(match.group(1)) if match else []


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    checks: list[str] = []
    broken_links: list[str] = []

    guides = guide_directories()
    numbers = [number for number, _ in guides]
    expected = set(range(101))

    missing = sorted(expected - set(numbers))
    duplicates = sorted({n for n in numbers if numbers.count(n) > 1})
    if missing:
        errors.append(f"Missing guide directories: {', '.join(f'{n:02d}' for n in missing)}")
    if duplicates:
        errors.append(f"Duplicate guide numbers: {duplicates}")
    checks.append(f"Found {len(guides)} numbered guide directories.")

    for number, guide_dir in guides:
        root_readme = guide_dir / "README.md"
        if not root_readme.exists():
            errors.append(f"{display(guide_dir)}: missing root README.md")
            continue

        text = root_readme.read_text(encoding="utf-8-sig", errors="replace")
        heading = GUIDE_HEADING_RE.search(text)
        if not heading:
            errors.append(f"{display(root_readme)}: missing canonical guide-number heading")
        elif int(heading.group(1)) != number:
            errors.append(f"{display(root_readme)}: heading says Guide {heading.group(1)}, folder is Guide {number:02d}")

        if number != 49 and re.search(r"Lifelong Opportunity Guide\s+49\b", text, re.IGNORECASE):
            errors.append(f"{display(root_readme)}: copied Guide 49 metadata detected")
        if re.search(r"\bfuture guide\b", text, re.IGNORECASE):
            errors.append(f"{display(root_readme)}: placeholder phrase 'future guide' detected")

        for language, language_name in LANGUAGE_NAMES.items():
            edition_dir = guide_dir / language
            edition_readme = edition_dir / "README.md"
            if not edition_dir.exists():
                errors.append(f"{display(guide_dir)}: missing {language}/ directory")
            elif not edition_readme.exists():
                errors.append(f"{display(edition_dir)}: missing README.md")
            else:
                edition_text = edition_readme.read_text(encoding="utf-8-sig", errors="replace")
                if number != 49 and re.search(r"\bGuide:?\s*49\b", edition_text, re.IGNORECASE):
                    errors.append(f"{display(edition_readme)}: copied Guide 49 metadata detected")
                if re.search(r"\bfuture guide\b", edition_text, re.IGNORECASE):
                    errors.append(f"{display(edition_readme)}: placeholder phrase 'future guide' detected")
                if language_name.lower() not in edition_text.lower():
                    warnings.append(f"{display(edition_readme)}: language name '{language_name}' not found")

            links = row_links(text, language)
            docx_links = [link for link in links if link.lower().split("#", 1)[0].endswith(".docx")]
            pdf_links = [link for link in links if link.lower().split("#", 1)[0].endswith(".pdf")]
            if not docx_links:
                errors.append(f"{display(root_readme)}: {language} row has no DOCX link")
            if not pdf_links:
                errors.append(f"{display(root_readme)}: {language} row has no PDF link")
            for link in docx_links + pdf_links:
                target = local_target(root_readme, link)
                if target is not None and not target.exists():
                    errors.append(f"{display(root_readme)}: linked package missing → {link}")

    all_markdown = sorted(ROOT.rglob("*.md"))
    for md_file in all_markdown:
        text = md_file.read_text(encoding="utf-8-sig", errors="replace")
        if "�" in text:
            warnings.append(f"{display(md_file)}: Unicode replacement character detected")
        for raw_target in MARKDOWN_LINK_RE.findall(text):
            target = local_target(md_file, raw_target)
            if target is not None and not target.exists():
                broken_links.append(f"{display(md_file)} → {raw_target}")

    if broken_links:
        errors.append(f"Broken local Markdown links: {len(broken_links)}")
    checks.append(f"Checked {len(all_markdown)} Markdown files for local-link integrity.")

    lines = [
        "# Repository Metadata Audit", "", "Automated structural audit of Guides 00–100.", "",
        "## Summary", "",
        f"- Numbered guide directories: **{len(guides)}**",
        f"- Markdown files checked: **{len(all_markdown)}**",
        f"- Blocking defects: **{len(errors)}**",
        f"- Warnings: **{len(warnings)}**",
        f"- Broken local links: **{len(broken_links)}**", "",
        "## Checks performed", "",
    ]
    lines.extend(f"- {item}" for item in checks)
    lines.extend(["", "## Blocking defects", ""])
    lines.extend(f"- {item}" for item in errors) if errors else lines.append("- None detected.")
    if broken_links:
        lines.extend(["", "### Broken-link details", ""])
        lines.extend(f"- `{item}`" for item in broken_links)
    lines.extend(["", "## Warnings", ""])
    lines.extend(f"- {item}" for item in warnings) if warnings else lines.append("- None detected.")
    lines.extend([
        "", "## Scope limitation", "",
        "This audit validates repository structure, metadata patterns, linked package presence, and local Markdown links. "
        "It does not replace visual inspection of DOCX/PDF rendering, PDF searchability testing, accessibility review, "
        "factual currency review, or human Spanish/Portuguese linguistic review.", "",
    ])

    REPORT.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
