#!/usr/bin/env python3
"""Configuration-driven deterministic pipeline for Lifelong Opportunity Guides.

This controller deliberately does not perform or certify subjective research,
editorial review, translation quality, legal review, accessibility certification,
or independent human review. It verifies explicit evidence and automates only
repeatable deterministic checks and publication mechanics.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG_DIR = ROOT / "project" / "pipeline" / "configs"
URL_RE = re.compile(r"https?://[^\s)>\]}]+")
SECTION_RE = re.compile(r"^##\s+(\d+)\.\s+", re.MULTILINE)


def die(message: str) -> None:
    raise SystemExit(message)


def run(cmd: list[str], cwd: Path | None = None) -> subprocess.CompletedProcess:
    print("+", " ".join(cmd))
    return subprocess.run(cmd, cwd=cwd or ROOT, check=True, text=True, capture_output=False)


def load_config(guide: str) -> dict:
    guide = f"{int(guide):02d}"
    path = CONFIG_DIR / f"GUIDE_{guide}.json"
    if not path.exists():
        die(f"Missing guide config: {path.relative_to(ROOT)}")
    try:
        cfg = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        die(f"Invalid JSON in {path.relative_to(ROOT)}: {exc}")
    if cfg.get("guide") != guide:
        die(f"Config guide mismatch: expected {guide}, got {cfg.get('guide')!r}")
    return cfg


def read_utf8(path: Path) -> str:
    try:
        raw = path.read_bytes()
        if raw.startswith(b"\xef\xbb\xbf"):
            die(f"UTF-8 BOM not allowed: {path.relative_to(ROOT)}")
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        die(f"Invalid UTF-8 in {path.relative_to(ROOT)}: {exc}")
    if "\ufffd" in text:
        die(f"Replacement character found in {path.relative_to(ROOT)}")
    return text


def source_paths(cfg: dict) -> dict[str, Path]:
    return {lang: ROOT / rel for lang, rel in cfg["source"].items()}


def require_path(path: Path, label: str) -> None:
    if not path.exists():
        die(f"Missing {label}: {path.relative_to(ROOT)}")


def section_numbers(text: str) -> list[int]:
    return [int(x) for x in SECTION_RE.findall(text)]


def urls(text: str) -> set[str]:
    return {u.rstrip(".,;") for u in URL_RE.findall(text)}


def validate_config(cfg: dict, require_localizations: bool = False) -> None:
    required = [
        "guide", "occupation", "source", "status_manifest", "publication_dir",
        "visual_review_evidence", "expected_sections", "output_stem"
    ]
    for key in required:
        if key not in cfg:
            die(f"Config missing required key: {key}")
    for lang in ("en", "es-419", "pt-BR"):
        if lang not in cfg["source"]:
            die(f"Config source missing language: {lang}")
    en = source_paths(cfg)["en"]
    require_path(en, "English source")
    read_utf8(en)
    if require_localizations:
        for lang, path in source_paths(cfg).items():
            require_path(path, f"{lang} source")
            read_utf8(path)
    first = int(cfg["expected_sections"]["first"])
    last = int(cfg["expected_sections"]["last"])
    if first < 1 or last < first:
        die("Invalid expected_sections range")
    print(f"PASS config Guide {cfg['guide']} — {cfg['occupation']}")


def load_status(cfg: dict) -> dict:
    path = ROOT / cfg["status_manifest"]
    require_path(path, "helper status manifest")
    data = json.loads(read_utf8(path))
    if data.get("guide") != cfg["guide"]:
        die("Helper status manifest guide mismatch")
    if data.get("blockers"):
        die(f"Helper status manifest has blockers: {data['blockers']}")
    return data


def require_stage(status: dict, name: str) -> None:
    stage = status.get("stages", {}).get(name)
    if not stage:
        die(f"Missing helper stage in status manifest: {name}")
    if stage.get("status") != "PASS":
        die(f"Stage {name} is not PASS: {stage.get('status')}")
    evidence = stage.get("evidence") or []
    if not evidence:
        die(f"Stage {name} has PASS but no evidence paths")
    for rel in evidence:
        require_path(ROOT / rel, f"evidence for {name}")


def parity(cfg: dict) -> dict:
    validate_config(cfg, require_localizations=True)
    status = load_status(cfg)
    for stage in ("research", "english_editorial", "evidence_traceability", "english_source_freeze"):
        require_stage(status, stage)

    texts = {lang: read_utf8(path) for lang, path in source_paths(cfg).items()}
    first = int(cfg["expected_sections"]["first"])
    last = int(cfg["expected_sections"]["last"])
    expected = list(range(first, last + 1))
    for lang, text in texts.items():
        found = section_numbers(text)
        if found != expected:
            die(f"{lang}: numbered sections mismatch. Expected {expected}, found {found}")

    en_urls = urls(texts["en"])
    required_urls = set(cfg.get("required_urls", []))
    missing_required = sorted(required_urls - en_urls)
    if missing_required:
        die(f"English source missing configured required URLs: {missing_required}")
    for lang in ("es-419", "pt-BR"):
        lang_urls = urls(texts[lang])
        if lang_urls != en_urls:
            die(f"{lang}: URL-set mismatch: missing={sorted(en_urls-lang_urls)}, extra={sorted(lang_urls-en_urls)}")

    for token in cfg.get("critical_tokens", []):
        missing = [lang for lang, text in texts.items() if token not in text]
        if missing:
            die(f"Critical token {token!r} missing from: {', '.join(missing)}")

    result = {
        "guide": cfg["guide"],
        "sections": len(expected),
        "urls": len(en_urls),
        "critical_tokens": len(cfg.get("critical_tokens", [])),
        "status": "PASS",
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return result


def publication_names(cfg: dict) -> dict[str, tuple[str, str]]:
    stem = cfg["output_stem"]
    return {
        "en": (f"{stem}_English_v2.0.docx", f"{stem}_English_v2.0.pdf"),
        "es-419": (f"{stem}_es-419_v2.0.docx", f"{stem}_es-419_v2.0.pdf"),
        "pt-BR": (f"{stem}_pt-BR_v2.0.docx", f"{stem}_pt-BR_v2.0.pdf"),
    }


def build(cfg: dict) -> None:
    parity_result = parity(cfg)
    status = load_status(cfg)
    for stage in ("spanish_localization", "portuguese_localization", "technical_qa"):
        require_stage(status, stage)

    for exe in ("pandoc", "libreoffice", "pdftotext", "pdftoppm"):
        if not shutil.which(exe):
            die(f"Required publication executable not installed: {exe}")

    out = ROOT / cfg["publication_dir"]
    render_root = out / "rendered-pages"
    out.mkdir(parents=True, exist_ok=True)
    if render_root.exists():
        shutil.rmtree(render_root)
    render_root.mkdir(parents=True)

    outputs: list[Path] = []
    manifest = {
        "guide": cfg["guide"], "occupation": cfg["occupation"], "status": "PASS",
        "parity": parity_result, "languages": {}
    }

    for lang, src in source_paths(cfg).items():
        docx_name, pdf_name = publication_names(cfg)[lang]
        docx = out / docx_name
        pdf = out / pdf_name
        run(["pandoc", str(src), "-o", str(docx), "--standalone"])
        run(["libreoffice", "--headless", "--convert-to", "pdf", "--outdir", str(out), str(docx)])
        produced = out / (docx.stem + ".pdf")
        if produced != pdf:
            if not produced.exists():
                die(f"LibreOffice did not create expected PDF for {lang}")
            produced.replace(pdf)
        require_path(docx, f"{lang} DOCX")
        require_path(pdf, f"{lang} PDF")
        text_path = out / f".{lang}.txt"
        with text_path.open("w", encoding="utf-8") as fh:
            subprocess.run(["pdftotext", str(pdf), "-"], check=True, text=True, stdout=fh)
        extracted = read_utf8(text_path)
        text_path.unlink(missing_ok=True)
        if len(extracted.strip()) < 1000:
            die(f"{lang} PDF text extraction unexpectedly short")
        render_dir = render_root / lang
        render_dir.mkdir(parents=True, exist_ok=True)
        run(["pdftoppm", "-png", "-r", "120", str(pdf), str(render_dir / "page")])
        pages = sorted(render_dir.glob("page-*.png"))
        if not pages:
            die(f"No rendered PDF pages for {lang}")
        manifest["languages"][lang] = {
            "source": str(src.relative_to(ROOT)), "docx": docx.name, "pdf": pdf.name,
            "rendered_pages": len(pages)
        }
        outputs.extend([docx, pdf])

    checksums = []
    for path in sorted(outputs, key=lambda p: p.name):
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        checksums.append(f"{digest}  {path.name}")
    (out / "SHA256SUMS.txt").write_text("\n".join(checksums) + "\n", encoding="utf-8")
    (out / f"GUIDE_{cfg['guide']}_PUBLICATION_QA_MANIFEST.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"PASS publication build Guide {cfg['guide']}")


def verify_checksums(out: Path) -> None:
    sums = out / "SHA256SUMS.txt"
    require_path(sums, "SHA256SUMS")
    for line in read_utf8(sums).splitlines():
        if not line.strip():
            continue
        digest, name = line.split("  ", 1)
        path = out / name
        require_path(path, "checksummed publication file")
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual != digest:
            die(f"Checksum mismatch: {name}")


def release_audit(cfg: dict) -> None:
    validate_config(cfg, require_localizations=True)
    status = load_status(cfg)
    for stage in (
        "research", "english_editorial", "evidence_traceability", "english_source_freeze",
        "spanish_localization", "portuguese_localization", "technical_qa", "publication"
    ):
        require_stage(status, stage)
    parity(cfg)
    out = ROOT / cfg["publication_dir"]
    manifest_path = out / f"GUIDE_{cfg['guide']}_PUBLICATION_QA_MANIFEST.json"
    require_path(manifest_path, "publication QA manifest")
    manifest = json.loads(read_utf8(manifest_path))
    if manifest.get("status") != "PASS":
        die("Publication QA manifest is not PASS")
    verify_checksums(out)
    visual = ROOT / cfg["visual_review_evidence"]
    require_path(visual, "full-page visual-review evidence")
    visual_text = read_utf8(visual)
    if "PASS" not in visual_text:
        die("Visual-review evidence does not contain PASS")
    for lang in ("en", "es-419", "pt-BR"):
        docx_name, pdf_name = publication_names(cfg)[lang]
        require_path(out / docx_name, f"{lang} DOCX")
        require_path(out / pdf_name, f"{lang} PDF")
        render_dir = out / "rendered-pages" / lang
        require_path(render_dir, f"{lang} rendered-page directory")
        if not list(render_dir.glob("page-*.png")):
            die(f"No rendered pages found for {lang}")
    print(f"PASS release audit Guide {cfg['guide']}")


def status_cmd(cfg: dict) -> None:
    print(json.dumps(load_status(cfg), indent=2, ensure_ascii=False))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["validate-config", "parity", "build", "release-audit", "status"])
    parser.add_argument("--guide", required=True)
    args = parser.parse_args()
    cfg = load_config(args.guide)
    if args.command == "validate-config":
        validate_config(cfg, require_localizations=False)
    elif args.command == "parity":
        parity(cfg)
    elif args.command == "build":
        build(cfg)
    elif args.command == "release-audit":
        release_audit(cfg)
    else:
        status_cmd(cfg)


if __name__ == "__main__":
    main()
