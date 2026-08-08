"""Build the missing Spanish guide editions from their English DOCX sources.

The translator preserves each source DOCX package and paragraph formatting.
Translations are cached so interrupted runs can resume without repeating work.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import tempfile
import threading
import time
import urllib.parse
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree

from document_safety import parse_xml_part, resolve_repository_path, validate_docx


ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / "project"
SOURCE_JSON = PROJECT / "spanish-source-paragraphs.json"
CACHE_JSON = PROJECT / "spanish-translation-cache.json"
FAILURES_JSON = PROJECT / "spanish-translation-failures.json"
NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
TEXT_PARTS = re.compile(
    r"^word/(document|header\d+|footer\d+|footnotes|endnotes|comments)\.xml$"
)
GUIDE_NUMBERS = {"06", *[f"{n:02d}" for n in range(11, 20)], "25", "34", "43", "64"}
NOTICE = (
    "Traducción asistida por máquina. Antes de tomar decisiones importantes "
    "basadas en esta guía, solicite la revisión de una persona con dominio del "
    "español y con los conocimientos técnicos pertinentes."
)
LOCK = threading.Lock()


def guide_folders() -> list[Path]:
    return sorted(
        folder
        for folder in ROOT.iterdir()
        if folder.is_dir() and folder.name[:2] in GUIDE_NUMBERS
    )


def source_docx(folder: Path) -> Path:
    candidates = list((folder / "english" / "docx").glob("*.docx"))
    if len(candidates) != 1:
        raise RuntimeError(f"Expected one English DOCX in {folder.name}, found {len(candidates)}")
    return candidates[0]


def should_translate(text: str) -> bool:
    text = text.strip()
    return bool(
        text
        and re.search(r"[A-Za-z]", text)
        and not re.fullmatch(r"https?://\S+|[\w.+-]+@[\w.-]+\.\w+", text)
    )


def collect_paragraphs(docx: Path):
    docx = resolve_repository_path(docx, ROOT, allowed_extensions={".docx"})
    validate_docx(docx)
    parts: dict[str, bytes] = {}
    records: list[tuple[str, int, str]] = []
    with ZipFile(docx) as archive:
        for name in archive.namelist():
            if not TEXT_PARTS.match(name):
                continue
            data = archive.read(name)
            parts[name] = data
            root = parse_xml_part(data, name)
            for index, paragraph in enumerate(root.xpath(".//w:p", namespaces=NS)):
                nodes = paragraph.xpath(".//w:t", namespaces=NS)
                text = "".join(node.text or "" for node in nodes).strip()
                if nodes and should_translate(text):
                    records.append((name, index, text))
    return parts, records


def translate(text: str) -> str:
    query = urllib.parse.urlencode(
        {"client": "gtx", "sl": "en", "tl": "es", "dt": "t", "q": text}
    )
    url = "https://translate.googleapis.com/translate_a/single?" + query
    last_error: Exception | None = None
    for attempt in range(3):
        try:
            completed = subprocess.run(
                [
                    "curl.exe", "--ssl-no-revoke", "--fail", "--silent",
                    "--show-error", "--connect-timeout", "8", "--max-time", "20", url,
                ],
                check=True, capture_output=True, text=True, encoding="utf-8",
            )
            payload = json.loads(completed.stdout)
            result = "".join(piece[0] for piece in payload[0] if piece[0]).strip()
            return result or text
        except Exception as exc:
            last_error = exc
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"Translation failed after retries: {last_error}")


def save_cache(data: dict[str, str]) -> None:
    CACHE_JSON.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def extract() -> None:
    texts: dict[str, None] = {}
    for folder in guide_folders():
        _, records = collect_paragraphs(source_docx(folder))
        for _, _, text in records:
            texts.setdefault(text, None)
    SOURCE_JSON.write_text(
        json.dumps(list(texts), ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"Extracted {len(texts)} unique paragraphs from {len(guide_folders())} guides.")


def translate_all() -> None:
    texts = json.loads(SOURCE_JSON.read_text(encoding="utf-8"))
    translations = (
        json.loads(CACHE_JSON.read_text(encoding="utf-8")) if CACHE_JSON.exists() else {}
    )
    pending = [text for text in texts if text not in translations]
    failures = []
    print(f"Cached {len(translations)}; translating {len(pending)} paragraphs.")
    with ThreadPoolExecutor(max_workers=4) as pool:
        futures = {pool.submit(translate, text): text for text in pending}
        for count, future in enumerate(as_completed(futures), 1):
            source = futures[future]
            try:
                result = future.result()
                with LOCK:
                    translations[source] = result
            except Exception as exc:
                failures.append({"text": source, "error": str(exc)})
            if count % 25 == 0:
                save_cache(translations)
                print(f"Processed {count}/{len(pending)}.")
    save_cache(translations)
    if failures:
        FAILURES_JSON.write_text(
            json.dumps(failures, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        raise SystemExit(f"{len(failures)} paragraphs failed; rerun to retry.")
    if FAILURES_JSON.exists():
        FAILURES_JSON.unlink()
    print("Translation complete.")


def write_docx(source: Path, destination: Path, translations: dict[str, str]) -> None:
    source = resolve_repository_path(source, ROOT, allowed_extensions={".docx"})
    destination = resolve_repository_path(
        destination, ROOT, allowed_extensions={".docx"}, must_exist=False
    )
    part_bytes, records = collect_paragraphs(source)
    grouped: dict[str, dict[int, str]] = {}
    for part, index, text in records:
        grouped.setdefault(part, {})[index] = translations[text]
    updated: dict[str, bytes] = {}
    for part, data in part_bytes.items():
        root = parse_xml_part(data, part)
        for index, paragraph in enumerate(root.xpath(".//w:p", namespaces=NS)):
            replacement = grouped.get(part, {}).get(index)
            if replacement is None:
                continue
            nodes = paragraph.xpath(".//w:t", namespaces=NS)
            nodes[0].text = replacement
            nodes[0].set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
            for node in nodes[1:]:
                node.text = ""
        updated[part] = etree.tostring(
            root, xml_declaration=True, encoding="UTF-8", standalone=True
        )
    destination.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=f".{destination.stem}-", suffix=".tmp.docx", dir=destination.parent
    )
    os.close(descriptor)
    temporary = Path(temporary_name)
    try:
        with ZipFile(source) as original, ZipFile(temporary, "w", ZIP_DEFLATED) as output:
            for item in original.infolist():
                output.writestr(item, updated.get(item.filename, original.read(item.filename)))
        validate_docx(temporary)
        os.replace(temporary, destination)
    finally:
        temporary.unlink(missing_ok=True)


def build() -> None:
    translations = json.loads(CACHE_JSON.read_text(encoding="utf-8"))
    for folder in guide_folders():
        number = folder.name[:2]
        stem = f"Guia_{number}_{folder.name[3:].replace('-', '_')}"
        destination = folder / "spanish" / "docx" / f"{stem}.docx"
        write_docx(source_docx(folder), destination, translations)
        spanish = folder / "spanish"
        (spanish / "README.md").write_text(
            f"# Guía {number}\n\n"
            f"- [Documento editable de Microsoft Word](./docx/{stem}.docx)\n"
            f"- [PDF con texto seleccionable](./pdf/{stem}.pdf)\n\n"
            f"> **Aviso de traducción:** {NOTICE}\n",
            encoding="utf-8",
        )
        (spanish / "QC.md").write_text(
            f"# Registro de control de calidad — Guía {number}\n\n"
            "- Idioma: español\n"
            "- Origen: edición inglesa del mismo directorio\n"
            "- Método: traducción asistida por máquina con estructura DOCX preservada\n"
            "- Formatos: DOCX editable y PDF con texto seleccionable\n"
            "- Estado: se recomienda revisión lingüística y técnica humana\n\n"
            f"**Aviso:** {NOTICE}\n",
            encoding="utf-8",
        )
        print(destination.relative_to(ROOT))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=("extract", "translate", "build"))
    args = parser.parse_args()
    {"extract": extract, "translate": translate_all, "build": build}[args.mode]()
