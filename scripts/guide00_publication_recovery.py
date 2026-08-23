#!/usr/bin/env python3
"""Fail-closed publication requalification for legacy Guide 00.

Build mode creates a fresh trilingual Markdown/DOCX/PDF publication candidate,
renders every page, and records automated QA while leaving Publication and
Release Audit PENDING. close-status is permitted only after a separate full-page
visual-review record exists and is PASS.
"""
from __future__ import annotations

import hashlib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

GUIDE = Path("project/revision-2026/guide-00")
STATUS = GUIDE / "GUIDE_00_HELPER_STATUS.json"
QA = GUIDE / "qa"
SRCROOT = Path("00-foundation-guide/source")
OUT = Path("00-foundation-guide/publication-candidate")

SOURCES = [
    ("en", SRCROOT / "Lifelong_Opportunity_Foundation_Guide_English_v1.1_INTEGRATED_MASTER.md", "Lifelong_Opportunity_Foundation_Guide_English_v1.1"),
    ("es-419", SRCROOT / "Lifelong_Opportunity_Foundation_Guide_es-419_v1.1_INTEGRATED_MASTER.md", "Lifelong_Opportunity_Foundation_Guide_es-419_v1.1"),
    ("pt-BR", SRCROOT / "Lifelong_Opportunity_Foundation_Guide_pt-BR_v1.1_INTEGRATED_MASTER.md", "Lifelong_Opportunity_Foundation_Guide_pt-BR_v1.1"),
]
EXPECTED_BLOBS = {
    "en": "1a2d9e709ee70e49d6fec75e45710782851f234b",
    "es-419": "ecb072697eb6faab41fc752fa6d8744c34e3bbfd",
    "pt-BR": "5e42545073518337d29c95c04879aec08d6465db",
}
OBSOLETE_RED_SEAL = "https://www.red-seal.ca/eng/contact/c.4nt.1ct.shtml"
VISUAL_QA = QA / "GUIDE_00_FULL_PAGE_VISUAL_REVIEW_09B.md"
AUTO_QA = QA / "GUIDE_00_PUBLICATION_AUTOMATED_QA_09A.md"
FINAL_QA = QA / "GUIDE_00_PUBLICATION_QA_09.md"
RELEASE_QA = QA / "GUIDE_00_RELEASE_AUDIT_10.md"


def run(cmd: list[str], **kwargs):
    return subprocess.run(cmd, check=True, **kwargs)


def git_blob(path: Path) -> str:
    return subprocess.check_output(["git", "hash-object", str(path)], text=True).strip()


def read_status() -> dict:
    return json.loads(STATUS.read_text(encoding="utf-8-sig"))


def extract_urls(text: str) -> set[str]:
    return {u.rstrip(".,;:") for u in re.findall(r"https?://[^\s)<>\]`]+", text)}


def preflight() -> tuple[list[dict], list[str]]:
    d = read_status()
    for stage in (
        "baseline_inventory", "research", "english_editorial", "evidence_traceability",
        "english_source_freeze", "spanish_localization", "portuguese_localization", "technical_qa",
    ):
        if d["stages"][stage]["status"] != "PASS":
            raise SystemExit(f"Guide 00 preflight: {stage} is not PASS")
    if d["stages"]["publication"]["status"] != "PENDING":
        raise SystemExit("Guide 00 preflight: Publication must be PENDING")
    if d["stages"]["release_audit"]["status"] != "PENDING":
        raise SystemExit("Guide 00 preflight: Release Audit must be PENDING")
    if d.get("blockers"):
        raise SystemExit(f"Guide 00 preflight: blockers present {d['blockers']}")

    records: list[dict] = []
    urlsets: list[set[str]] = []
    for locale, source, stem in SOURCES:
        if not source.is_file():
            raise SystemExit(f"missing source: {source}")
        blob = git_blob(source)
        if blob != EXPECTED_BLOBS[locale]:
            raise SystemExit(f"{locale}: source blob changed: expected {EXPECTED_BLOBS[locale]}, got {blob}")
        text = source.read_text(encoding="utf-8-sig")
        if text.startswith("\ufeff") or "\ufffd" in text:
            raise SystemExit(f"{locale}: encoding defect")
        if OBSOLETE_RED_SEAL in text:
            raise SystemExit(f"{locale}: obsolete Red Seal URL remains")
        sections = [int(x) for x in re.findall(r"(?m)^#\s+(\d+)\.", text)]
        if sections != list(range(1, 18)):
            raise SystemExit(f"{locale}: numbered sections are not exactly 1..17: {sections}")
        urls = extract_urls(text)
        if len(urls) != 27:
            raise SystemExit(f"{locale}: expected 27 controlled URLs, found {len(urls)}")
        urlsets.append(urls)
        records.append({"locale": locale, "source": source, "stem": stem, "blob": blob, "chars": len(text), "urls": len(urls)})

    if not (urlsets[0] == urlsets[1] == urlsets[2]):
        raise SystemExit("Guide 00 source URL parity changed after Technical QA")
    return records, sorted(urlsets[0])


def check_links(urls: list[str]) -> list[dict]:
    results: list[dict] = []
    hard: list[str] = []
    for url in urls:
        proc = subprocess.run(
            ["curl", "-L", "-sS", "-o", "/dev/null", "-w", "%{http_code}",
             "--connect-timeout", "15", "--max-time", "35", "-A", "Mozilla/5.0 Guide00-QA", url],
            text=True, capture_output=True,
        )
        code = (proc.stdout or "000").strip()[-3:]
        results.append({"url": url, "http_code": code})
        if code in {"404", "410"}:
            hard.append(f"{code} {url}")
        print(f"LINK {code} {url}")
    if hard:
        raise SystemExit("Hard link failures:\n" + "\n".join(hard))
    return results


def clean_output() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "pdf").mkdir(parents=True)
    (OUT / "rendered").mkdir(parents=True)


def build_documents(records: list[dict]) -> None:
    lua = Path("/tmp/guide00_url_safe.lua")
    lua.write_text(
        "local function long_url(s) return string.match(s,'^https?://') and string.len(s)>45 end\n"
        "function Link(el) local t=pandoc.utils.stringify(el.content); if long_url(t) then return pandoc.Link({pandoc.Str('Source link')},el.target,el.title) end; return el end\n"
        "function Str(el) if long_url(el.text) then return pandoc.Link({pandoc.Str('Source link')},el.text) end; return el end\n",
        encoding="utf-8",
    )
    for rec in records:
        source: Path = rec["source"]
        stem: str = rec["stem"]
        md = OUT / f"{stem}.md"
        docx = OUT / f"{stem}.docx"
        pdf = OUT / "pdf" / f"{stem}.pdf"
        shutil.copy2(source, md)
        run(["pandoc", str(md), "-f", "gfm-tex_math_dollars", "-t", "docx", "--standalone", f"--lua-filter={lua}", "-o", str(docx)])
        run(["unzip", "-t", str(docx)], stdout=subprocess.DEVNULL)

        # Check that DOCX hyperlink relationships retain the official source set.
        rels = subprocess.check_output(["unzip", "-p", str(docx), "word/_rels/document.xml.rels"], text=True)
        docx_urls = set(re.findall(r'Target="(https?://[^\"]+)"', rels))
        if len(docx_urls) < 20:
            raise SystemExit(f"{stem}: too few DOCX hyperlink targets ({len(docx_urls)})")
        rec["docx_hyperlinks"] = len(docx_urls)

        tmp = OUT / f"lo-{stem}"
        tmp.mkdir()
        run(["libreoffice", "--headless", "--convert-to", "pdf", "--outdir", str(tmp), str(docx)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        generated = tmp / f"{stem}.pdf"
        if not generated.exists():
            raise SystemExit(f"LibreOffice did not create {generated}")
        shutil.move(str(generated), pdf)
        tmp.rmdir()
        run(["pdfinfo", str(pdf)], stdout=subprocess.DEVNULL)
        text = subprocess.check_output(["pdftotext", str(pdf), "-"], text=True)
        compact = re.sub(r"\s+", "", text)
        if len(compact) < 7000:
            raise SystemExit(f"{stem}: searchable PDF text too short ({len(compact)})")
        rec["pdf_searchable_chars"] = len(compact)
        # pdfinfo -url is available in poppler and surfaces retained URI annotations.
        urls_out = subprocess.check_output(["pdfinfo", "-url", str(pdf)], text=True, stderr=subprocess.STDOUT)
        pdf_urls = set(re.findall(r"https?://\S+", urls_out))
        rec["pdf_hyperlinks"] = len(pdf_urls)
        if len(pdf_urls) < 20:
            raise SystemExit(f"{stem}: too few PDF hyperlink annotations ({len(pdf_urls)})")


def render_and_analyze(records: list[dict]) -> dict:
    from PIL import Image, ImageChops, ImageDraw

    all_pages: list[dict] = []
    problems: list[str] = []
    for rec in records:
        stem = rec["stem"]
        pdf = OUT / "pdf" / f"{stem}.pdf"
        dest = OUT / "rendered" / stem
        dest.mkdir(parents=True)
        run(["pdftoppm", "-png", "-r", "130", str(pdf), str(dest / "page")], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        pages = sorted(dest.glob("page-*.png"))
        if not pages:
            raise SystemExit(f"{stem}: no rendered pages")
        rec["rendered_pages"] = len(pages)

        thumbs: list[Image.Image] = []
        for page in pages:
            with Image.open(page) as im0:
                im = im0.convert("RGB")
                gray = im.convert("L")
                diff = ImageChops.difference(gray, Image.new("L", gray.size, 255))
                bbox = diff.point(lambda p: 255 if p > 12 else 0).getbbox()
                if bbox is None:
                    problems.append(f"{page}: blank page")
                    margins = None
                else:
                    l, t, r, b = bbox
                    w, h = gray.size
                    margins = {"left": l, "top": t, "right": w-r, "bottom": h-b}
                    if min(margins.values()) < 2:
                        problems.append(f"{page}: possible clipping {margins}")
                all_pages.append({"file": str(page.relative_to(OUT / 'rendered')), "edge_margins": margins})
                thumb = im.copy()
                thumb.thumbnail((900, 1200))
                thumbs.append(thumb)

        # Contact sheets group four full-page thumbnails at a readable inspection scale.
        sheets = []
        for batch_index in range(0, len(thumbs), 4):
            batch = thumbs[batch_index:batch_index+4]
            cell_w, cell_h = 920, 1220
            sheet = Image.new("RGB", (cell_w * 2, cell_h * 2), "white")
            draw = ImageDraw.Draw(sheet)
            for j, thumb in enumerate(batch):
                x = (j % 2) * cell_w + 10
                y = (j // 2) * cell_h + 10
                sheet.paste(thumb, (x, y))
                draw.text((x, y), f"Page {batch_index+j+1}", fill="black")
            sheet_path = dest / f"sheet-{batch_index//4+1:02d}.png"
            sheet.save(sheet_path)
            sheets.append(sheet_path.name)
        rec["contact_sheets"] = sheets

        info = subprocess.check_output(["pdfinfo", str(pdf)], text=True)
        pdf_pages = next(int(line.split(":", 1)[1]) for line in info.splitlines() if line.startswith("Pages:"))
        rec["pdf_pages"] = pdf_pages
        if pdf_pages != len(pages):
            problems.append(f"{stem}: PDF pages {pdf_pages} != rendered pages {len(pages)}")

    result = {"status": "FAIL" if problems else "PASS", "pages": all_pages, "problems": problems}
    if problems:
        raise SystemExit("Render QA failures:\n" + "\n".join(problems))
    return result


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_automated_evidence(records: list[dict], links: list[dict], render: dict) -> None:
    editions = []
    for rec in records:
        stem = rec["stem"]
        md = OUT / f"{stem}.md"
        docx = OUT / f"{stem}.docx"
        pdf = OUT / "pdf" / f"{stem}.pdf"
        editions.append({
            "language": rec["locale"],
            "source_blob": rec["blob"],
            "markdown": md.name,
            "docx": docx.name,
            "pdf": f"pdf/{pdf.name}",
            "markdown_bytes": md.stat().st_size,
            "docx_bytes": docx.stat().st_size,
            "pdf_bytes": pdf.stat().st_size,
            "pdf_pages": rec["pdf_pages"],
            "rendered_pages": rec["rendered_pages"],
            "docx_hyperlinks": rec["docx_hyperlinks"],
            "pdf_hyperlinks": rec["pdf_hyperlinks"],
            "pdf_searchable_chars": rec["pdf_searchable_chars"],
            "automated_status": "PASS",
        })

    manifest = {
        "guide": "00",
        "occupation": "Lifelong Opportunity Foundation Guide",
        "version": "1.1",
        "build_date": "2026-08-22",
        "status": "automated QA PASS; full-page visual review pending",
        "independent_certification": False,
        "shared_reader_urls": 27,
        "editions": editions,
        "assurance_boundary": "Internal controlled publication QA only until full-page visual review and final release audit pass. No independent certification, certified translation, legal/medical/safety/accessibility/licensure/accreditation review, funding approval, employment guarantee, or earnings guarantee is claimed.",
    }
    (OUT / "GUIDE_00_PUBLICATION_QA_MANIFEST.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (OUT / "RENDER_QA.json").write_text(json.dumps(render, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (OUT / "LINK_QA.json").write_text(json.dumps({"status": "PASS", "results": links}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    checksum_files = sorted([*OUT.glob("*.md"), *OUT.glob("*.docx"), *OUT.glob("*.json"), *OUT.glob("pdf/*.pdf")])
    (OUT / "SHA256SUMS.txt").write_text(
        "\n".join(f"{sha256(p)}  {p.relative_to(OUT).as_posix()}" for p in checksum_files) + "\n",
        encoding="utf-8",
    )

    page_total = sum(rec["pdf_pages"] for rec in records)
    AUTO_QA.write_text(
        "# Guide 00 — Publication Automated QA 09A\n\n"
        "**Stage:** Publication requalification — automated checks **PASS**; full-page visual review **PENDING**\n\n"
        f"Fresh publication artifacts were rebuilt from the three controlled Version 1.1 masters. All three sources preserved 17 numbered sections and the same 27 official reader URLs. Live-link preflight found no HTTP 404/410 hard failure. DOCX ZIP integrity, DOCX hyperlink relationships, PDF generation, PDF URI annotations, searchable text, page-count reconciliation, edge-clipping heuristics, metadata inspection inputs and SHA-256 checksums passed.\n\n"
        f"Total PDF/rendered pages awaiting direct visual review: **{page_total}**. Rendered page PNGs and contact sheets are emitted as a workflow artifact for inspection.\n\n"
        "This record does not close Publication. `GUIDE_00_FULL_PAGE_VISUAL_REVIEW_09B.md` must separately record a PASS before final Publication QA and Release Audit may be generated.\n",
        encoding="utf-8",
    )


def build() -> None:
    records, urls = preflight()
    clean_output()
    link_results = check_links(urls)
    build_documents(records)
    render = render_and_analyze(records)
    write_automated_evidence(records, link_results, render)
    print(f"Guide 00 automated publication build PASS; {len(urls)} shared URLs; {sum(r['pdf_pages'] for r in records)} pages; visual review still PENDING")


def close_status() -> None:
    d = read_status()
    if d["stages"]["technical_qa"]["status"] != "PASS":
        raise SystemExit("Technical QA is not PASS")
    if d["stages"]["publication"]["status"] != "PENDING" or d["stages"]["release_audit"]["status"] != "PENDING":
        raise SystemExit("Publication/Release Audit not in expected PENDING state")
    if d.get("blockers"):
        raise SystemExit(f"blockers present: {d['blockers']}")
    for required in (AUTO_QA, VISUAL_QA, OUT / "GUIDE_00_PUBLICATION_QA_MANIFEST.json", OUT / "RENDER_QA.json", OUT / "LINK_QA.json", OUT / "SHA256SUMS.txt"):
        if not required.exists():
            raise SystemExit(f"required closure evidence missing: {required}")
    visual = VISUAL_QA.read_text(encoding="utf-8-sig")
    if "**Full-page visual review: PASS.**" not in visual:
        raise SystemExit("visual review does not contain required PASS decision")
    manifest_path = OUT / "GUIDE_00_PUBLICATION_QA_MANIFEST.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if not str(manifest.get("status", "")).startswith("automated QA PASS"):
        raise SystemExit(f"unexpected automated manifest status: {manifest.get('status')}")
    if any(row.get("automated_status") != "PASS" for row in manifest.get("editions", [])):
        raise SystemExit("one or more publication editions lack automated PASS")
    if len(manifest.get("editions", [])) != 3:
        raise SystemExit("manifest does not contain three editions")
    render = json.loads((OUT / "RENDER_QA.json").read_text(encoding="utf-8"))
    if render.get("status") != "PASS" or render.get("problems"):
        raise SystemExit("render automated QA is not clean PASS")
    links = json.loads((OUT / "LINK_QA.json").read_text(encoding="utf-8"))
    if links.get("status") != "PASS" or len(links.get("results", [])) != 27:
        raise SystemExit("link QA is not clean PASS")

    manifest["status"] = "PASS"
    manifest["full_page_visual_review"] = "PASS"
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    page_total = sum(int(row["pdf_pages"]) for row in manifest["editions"])
    FINAL_QA.write_text(
        "# Guide 00 — Publication QA 09\n\n"
        "**Stage:** Publication — **PASS**\n\n"
        "Publication is requalified under the final controlled standard. Fresh English, neutral Latin American Spanish (`es-419`) and Brazilian Portuguese (`pt-BR`) Markdown/DOCX/PDF editions passed controlled-source blob checks, 17-section structure, exact 27-link trilingual source parity, live hard-link checks, DOCX integrity and hyperlink checks, searchable-PDF and PDF-link checks, page-count reconciliation, automated render preflight, SHA-256 generation and a separate direct full-page visual review.\n\n"
        f"Total visually reviewed PDF pages: **{page_total}**.\n\n"
        "No independent certification, certified translation, legal/medical/safety/accessibility/licensure/accreditation review, funding approval, employment guarantee or earnings guarantee is claimed.\n",
        encoding="utf-8",
    )
    RELEASE_QA.write_text(
        "# Guide 00 — Release Audit 10\n\n"
        "**Stage:** Release Audit — **PASS**\n\n"
        "The release audit confirms all ten Guide 00 controlled gates have evidence-supported closure: source research and traceability, English editorial/freeze, Spanish and Portuguese localization, final trilingual technical parity, fresh publication artifacts, link/checksum/searchability/render controls, direct all-page visual review and zero blockers.\n\n"
        "Guide 00 may be treated as closed under the final gate model. This audit does not retroactively erase the earlier publication-candidate history; it records the later requalification performed on 2026-08-22.\n",
        encoding="utf-8",
    )
    # Manifest changed after checksum generation; refresh checksums to cover final manifest.
    checksum_files = sorted([*OUT.glob("*.md"), *OUT.glob("*.docx"), *OUT.glob("*.json"), *OUT.glob("pdf/*.pdf")])
    (OUT / "SHA256SUMS.txt").write_text(
        "\n".join(f"{sha256(p)}  {p.relative_to(OUT).as_posix()}" for p in checksum_files) + "\n",
        encoding="utf-8",
    )

    d["stages"]["publication"] = {"status": "PASS", "evidence": [
        "project/revision-2026/guide-00/qa/GUIDE_00_PUBLICATION_AUTOMATED_QA_09A.md",
        "project/revision-2026/guide-00/qa/GUIDE_00_FULL_PAGE_VISUAL_REVIEW_09B.md",
        "project/revision-2026/guide-00/qa/GUIDE_00_PUBLICATION_QA_09.md",
        "00-foundation-guide/publication-candidate/GUIDE_00_PUBLICATION_QA_MANIFEST.json",
        "00-foundation-guide/publication-candidate/LINK_QA.json",
        "00-foundation-guide/publication-candidate/RENDER_QA.json",
        "00-foundation-guide/publication-candidate/SHA256SUMS.txt",
    ]}
    d["stages"]["release_audit"] = {"status": "PASS", "evidence": [
        "project/revision-2026/guide-00/qa/GUIDE_00_RELEASE_AUDIT_10.md"
    ]}
    d["updated"] = "2026-08-22"
    d["notes"] = "Legacy closure reconciliation complete. Guide 00 requalified through Publication and Release Audit PASS under the final gate model."
    STATUS.write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("Guide 00 publication and release audit closed PASS")


def main() -> None:
    if len(sys.argv) != 2 or sys.argv[1] not in {"build", "close-status"}:
        raise SystemExit("usage: guide00_publication_recovery.py {build|close-status}")
    build() if sys.argv[1] == "build" else close_status()


if __name__ == "__main__":
    main()
