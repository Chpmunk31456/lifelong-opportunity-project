#!/usr/bin/env python3
"""Audit Lifelong Opportunity guide metadata and local Markdown links.

The script is intentionally dependency-free so it can run locally or in GitHub Actions.
It writes QA_METADATA_AUDIT.md and returns a non-zero exit code when blocking defects exist.
"""

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
LANGUAGES = {
    "english": "English",
    "spanish": "Spanish",
    "portuguese": "Portuguese",
}


def guide_directories() -> list[tuple[int, Path]]:
    found: list[tuple[int, Path]] = []
    for path in ROOT.iterdir():
        if not path.is_dir():
            continue
        match = GUIDE_DIR_RE.match(path.name)
        if match:
            found.append((int(match.group(1)), path))
    return sorted(found)


def local_target(source: Path, raw_target: str) -> Path | None:
    target = raw_target.strip().split("#", 1)[0].strip()
    if not target or target.startswith(("http://", "https://", "mailto:", "tel:", "#")):
        return None
    target = unquote(target)
    return (source.parent / target).resolve()


def display(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    checks: list[str] = []

    guides = guide_directories()
    numbers = [number for number, _ in guides]
    expected = list(range(0, 101))

    missing_dirs = sorted(set(expected) - set(numbers))
    duplicate_numbers = sorted({n for n in numbers if numbers.count(n) > 1})
    unexpected_numbers = sorted(set(numbers) - set(expected))

    if missing_dirs:
        errors.append(f"Missing guide directories: {', '.join(f'{n:02d}' for n in missing_dirs)}")
    if duplicate_numbers:
        errors.append(f"Duplicate guide numbers: {duplicate_numbers}")
    if unexpected_numbers:
        warnings.append(f"Unexpected guide numbers outside 00–100: {unexpected_numbers}")
    checks.append(f"Found {len(guides)} numbered guide directories.")

    all_markdown = sorted(ROOT.rglob("*.md"))
    broken_links: list[str] = []

    for number, guide_dir in guides:
        root_readme = guide_dir / "README.md"
        if not root_readme.exists():
            errors.append(f"{display(guide_dir)}: missing root README.md")
            continue

        text = root_readme.read_text(encoding="utf-8-sig", errors="replace")
        match = GUIDE_HEADING_RE.search(text)
        if not match:
            errors.append(f"{display(root_readme)}: missing canonical guide-number heading")
        elif int(match.group(1)) != number:
            errors.append(
                f"{display(root_readme)}: heading says Guide {match.group(1)}, folder is Guide {number:02d}"
            )

        if number != 49 and re.search(r"Lifelong Opportunity Guide\s+49\b", text, re.IGNORECASE):
            errors.append(f"{display(root_readme)}: copied Guide 49 metadata detected")
        if re.search(r"\bfuture guide\b", text, re.IGNORECASE):
            errors.append(f"{display(root_readme)}: placeholder phrase 'future guide' detected")

        for language_dir, language_name in LANGUAGES.items():
            edition_dir = guide_dir / language_dir
            edition_readme = edition_dir / "README.md"
            if not edition_dir.exists():
                errors.append(f"{display(guide_dir)}: missing {language_dir}/ directory")
                continue
            if not edition_readme.exists():
                errors.append(f"{display(edition_dir)}: missing README.md")
                continue

            edition_text = edition_readme.read_text(encoding="utf-8-sig", errors="replace")
            if number != 49 and re.search(r"\bGuide:?\s*49\b", edition_text, re.IGNORECASE):
                errors.append(f"{display(edition_readme)}: copied Guide 49 metadata detected")
            if re.search(r"\bfuture guide\b", edition_text, re.IGNORECASE):
                errors.append(f"{display(edition_readme)}: placeholder phrase 'future guide' detected")
            if language_name.lower() not in edition_text.lower():
                warnings.append(f"{display(edition_readme)}: language name '{language_name}' not found")

            docx_files = list((edition_dir / "docx").glob("*.docx")) if (edition_dir / "docx").exists() else []
            pdf_files = list((edition_dir / "pdf").glob("*.pdf")) if (edition_dir / "pdf").exists() else []
            if not docx_files:
                errors.append(f"{display(edition_dir)}: no DOCX file found")
            if not pdf_files:
                errors.append(f"{display(edition_dir)}: no PDF file found")
            if len(docx_files) > 1:
                warnings.append(f"{display(edition_dir)}: multiple DOCX files ({len(docx_files)})")
            if len(pdf_files) > 1:
                warnings.append(f"{display(edition_dir)}: multiple PDF files ({len(pdf_files)})")

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
        "# Repository Metadata Audit",
        "",
        "Automated structural audit of Guides 00–100.",
        "",
        "## Summary",
        "",
        f"- Numbered guide directories: **{len(guides)}**",
        f"- Markdown files checked: **{len(all_markdown)}**",
        f"- Blocking defects: **{len(errors)}**",
        f"- Warnings: **{len(warnings)}**",
        f"- Broken local links: **{len(broken_links)}**",
        "",
        "## Checks performed",
        "",
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
        "",
        "## Scope limitation",
        "",
        "This audit validates repository structure, metadata patterns, package presence, and local Markdown links. "
        "It does not replace visual inspection of DOCX/PDF rendering, PDF searchability testing, accessibility review, "
        "factual currency review, or human Spanish/Portuguese linguistic review.",
        "",
    ])

    REPORT.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
