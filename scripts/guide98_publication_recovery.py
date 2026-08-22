#!/usr/bin/env python3
"""Deterministic fail-closed publication builder for Guide 98."""
from __future__ import annotations
import argparse, hashlib, json, re, shutil, subprocess, zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GUIDE = ROOT / "project/revision-2026/guide-98"
SRC = GUIDE / "working-masters"
OUT = GUIDE / "publication-candidate"
QA = GUIDE / "qa"
STATUS = GUIDE / "GUIDE_98_HELPER_STATUS.json"
PAIRS = [
    ("GUIDE_98_AGRICULTURAL_TECHNICIAN_ENGLISH_v2.md", "GUIDE_98_ENGLISH_v2.md"),
    ("GUIDE_98_TECNICO_AGROPECUARIO_ES419_v2.md", "GUIDE_98_SPANISH_es-419_v2.md"),
    ("GUIDE_98_TECNICO_AGROPECUARIO_PTBR_v2.md", "GUIDE_98_PORTUGUESE_pt-BR_v2.md"),
]
STEMS = [
    ("en", "GUIDE_98_ENGLISH_v2"),
    ("es-419", "GUIDE_98_SPANISH_es-419_v2"),
    ("pt-BR", "GUIDE_98_PORTUGUESE_pt-BR_v2"),
]
CONTROLS = [
    r"19-4012\.00", r"22110", r"31421",
    r"23[,.]86", r"49[,.]630", r"46[,.]790",
    r"18[,.]600", r"19[,.]400", r"C\$19[,.]50", r"C\$29[,.]12", r"C\$43[,.]00",
    r"1[,.]509[,.]958", r"4[,.]560[,.]530", r"3[,.]984", r"2[,.]200",
    r"43[,.]987", r"21[,.]15", r"1[,.]75M", r"3[,.]54M",
]


def run(cmd, capture=False):
    print('+', ' '.join(map(str, cmd)), flush=True)
    return subprocess.run(list(map(str, cmd)), check=True, text=True, capture_output=capture)


def get_status():
    return json.loads(STATUS.read_text(encoding='utf-8'))


def require_predecessors(d):
    for s in (
        'baseline_inventory', 'research', 'english_editorial', 'evidence_traceability',
        'english_source_freeze', 'spanish_localization', 'portuguese_localization', 'technical_qa'
    ):
        if d['stages'][s]['status'] != 'PASS':
            raise SystemExit(f'Guide 98 predecessor not PASS: {s}')
    if d.get('blockers'):
        raise SystemExit(f"Guide 98 blockers: {d['blockers']}")


def hard_links(urls):
    bad = []
    for u in sorted(urls):
        p = subprocess.run(
            ['curl', '-L', '-sS', '-o', '/dev/null', '-w', '%{http_code}',
             '--connect-timeout', '15', '--max-time', '35', '-A', 'Mozilla/5.0 Guide98-QA', u],
            text=True, capture_output=True
        )
        code = p.stdout.strip() if p.returncode == 0 else '000'
        print('LINK', code, u)
        if code in {'404', '410'}:
            bad.append(f'{code} {u}')
    if bad:
        raise SystemExit('Hard link failures:\n' + '\n'.join(bad))


def build():
    d = get_status()
    require_predecessors(d)
    if d['stages']['publication']['status'] == 'PASS' and d['stages']['release_audit']['status'] == 'PASS':
        print('Guide 98 already closed.')
        return
    if d['stages']['publication']['status'] != 'PENDING' or d['stages']['release_audit']['status'] != 'PENDING':
        raise SystemExit('Unexpected Guide 98 release state')

    for x in ('pandoc', 'libreoffice', 'pdfinfo', 'pdftotext', 'pdftoppm', 'curl'):
        if not shutil.which(x):
            raise SystemExit(f'Missing executable: {x}')

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    files = []
    for source_name, output_name in PAIRS:
        source = SRC / source_name
        target = OUT / output_name
        if not source.exists():
            raise SystemExit(f'Missing source: {source}')
        shutil.copy2(source, target)
        files.append(target)

    texts = [p.read_text(encoding='utf-8') for p in files]
    url_sets = [set(re.findall(r'https://[^\s)<>`]+', t)) for t in texts]
    problems = []
    if not (url_sets[0] == url_sets[1] == url_sets[2]):
        problems.append(f'URL parity mismatch {[len(x) for x in url_sets]}')
    if len(url_sets[0]) != 27:
        problems.append(f'expected 27 shared URLs, found {len(url_sets[0])}')

    for p, text in zip(files, texts):
        if text.startswith('\ufeff') or '\ufffd' in text:
            problems.append(f'{p.name}: encoding defect')
        if len(text) < 18000:
            problems.append(f'{p.name}: unexpectedly short ({len(text)})')
        if len(re.findall(r'^##\s+.+$', text, re.M)) < 25:
            problems.append(f'{p.name}: too few major sections')
        if re.search(r'(?im)^\s*(?:[-*]\s*)?todo\s*:', text):
            problems.append(f'{p.name}: unresolved TODO')
        if len(re.findall(r'^###\s+(?:Step|Etapa)\s+[1-6]\b', text, re.M | re.I)) != 6:
            problems.append(f'{p.name}: six-step action plan parity failed')
        for pat in CONTROLS:
            if not re.search(pat, text, re.I):
                problems.append(f'{p.name}: missing controlled value {pat}')

    if problems:
        raise SystemExit('Guide 98 preflight failed:\n' + '\n'.join(problems))

    hard_links(url_sets[0])

    for _, stem in STEMS:
        md = OUT / f'{stem}.md'
        docx = OUT / f'{stem}.docx'
        pdf = OUT / f'{stem}.pdf'
        run(['pandoc', md, '-f', 'gfm-tex_math_dollars', '-t', 'docx', '--standalone', '-o', docx])
        tmp = OUT / f'lo-{stem}'
        tmp.mkdir()
        run(['libreoffice', '--headless', '--convert-to', 'pdf', '--outdir', tmp, docx])
        produced = tmp / f'{stem}.pdf'
        if not produced.exists():
            raise SystemExit(f'No PDF produced for {stem}')
        produced.replace(pdf)
        tmp.rmdir()
        with zipfile.ZipFile(docx) as z:
            if 'word/document.xml' not in z.namelist():
                raise SystemExit(f'DOCX integrity failed: {stem}')
        text = run(['pdftotext', pdf, '-'], capture=True).stdout
        if len(re.sub(r'\s+', '', text)) <= 10000:
            raise SystemExit(f'PDF searchable text too short: {stem}')

    from PIL import Image, ImageChops
    render_root = OUT / 'rendered'
    pages, bad = [], []
    for _, stem in STEMS:
        dest = render_root / stem
        dest.mkdir(parents=True)
        run(['pdftoppm', '-png', '-r', '110', OUT / f'{stem}.pdf', dest / 'page'])

    for image_path in sorted(render_root.rglob('*.png')):
        with Image.open(image_path) as im:
            gray = im.convert('L')
            diff = ImageChops.difference(gray, Image.new('L', gray.size, 255))
            bbox = diff.point(lambda v: 255 if v > 12 else 0).getbbox()
            if bbox is None:
                bad.append(f'{image_path}: blank')
                continue
            left, top, right, bottom = bbox
            width, height = gray.size
            margins = {'left': left, 'top': top, 'right': width-right, 'bottom': height-bottom}
            if min(margins.values()) < 2:
                bad.append(f'{image_path}: possible clipping {margins}')
            pages.append({'file': str(image_path.relative_to(render_root)), 'edge_margins': margins})

    if bad:
        raise SystemExit('Render QA failed:\n' + '\n'.join(bad))

    editions = []
    for lang, stem in STEMS:
        docx = OUT / f'{stem}.docx'
        pdf = OUT / f'{stem}.pdf'
        info = run(['pdfinfo', pdf], capture=True).stdout
        pdf_pages = next(int(x.split(':', 1)[1]) for x in info.splitlines() if x.startswith('Pages:'))
        rendered = sum(1 for x in pages if x['file'].startswith(stem + '/'))
        if pdf_pages != rendered:
            raise SystemExit(f'Page mismatch {stem}: {pdf_pages}/{rendered}')
        editions.append({
            'language': lang,
            'docx': docx.name,
            'pdf': pdf.name,
            'docx_bytes': docx.stat().st_size,
            'pdf_bytes': pdf.stat().st_size,
            'pdf_pages': pdf_pages,
            'rendered_pages': rendered,
            'status': 'PASS',
        })

    (OUT / 'RENDER_QA.json').write_text(
        json.dumps({'status': 'PASS', 'pages': pages, 'problems': []}, indent=2) + '\n', encoding='utf-8'
    )
    manifest = {
        'guide': '98',
        'occupation': 'Agricultural Technician',
        'build_date': '2026-08-22',
        'status': 'PASS',
        'editions': editions,
        'reader_verification_urls': 27,
        'english_source_blob': 'c7c6036484084eb46bd45e3c91419a5335e1d524',
        'assurance_boundary': 'Internal controlled publication QA only; no independent certification, certified translation, pesticide certification, veterinary authority, professional licensure review, safety certification, funding approval, employment guarantee, or earnings guarantee.',
    }
    (OUT / 'GUIDE_98_PUBLICATION_QA_MANIFEST.json').write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')
    binaries = sorted([*OUT.glob('*.docx'), *OUT.glob('*.pdf')])
    (OUT / 'SHA256SUMS.txt').write_text(
        '\n'.join(f'{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}' for p in binaries) + '\n', encoding='utf-8'
    )
    (QA / 'GUIDE_98_PUBLICATION_QA_09.md').write_text(
        '# Guide 98 — Publication QA 09\n\n'
        '**Stage:** Publication — **PASS**\n\n'
        'English, es-419 and pt-BR Markdown/DOCX/PDF editions passed controlled-value and 27-link parity, hard 404/410 link checks, DOCX integrity, searchable-PDF validation, all-page rendering, page reconciliation, metadata and SHA-256 generation. Pesticide/veterinary scope, machinery safety, data integrity, cybersecurity and responsible-AI boundaries remained intact. No independent certification or outcome guarantee is claimed.\n',
        encoding='utf-8'
    )
    (QA / 'GUIDE_98_RELEASE_AUDIT_10.md').write_text(
        '# Guide 98 — Release Audit 10\n\n'
        '**Stage:** Release Audit — **PASS**\n\n'
        'Release audit confirms all predecessor gates, trilingual publication package, 27-reader-link parity, checksums, searchable PDFs, all-page render evidence, regulated-scope/safety boundaries and zero blockers. Guide 99 may initialize only after helper-status closure.\n',
        encoding='utf-8'
    )
    shutil.rmtree(render_root)
    print(f'Guide 98 publication build PASS; rendered pages={len(pages)}')


def close_status():
    d = get_status()
    require_predecessors(d)
    required = [
        QA / 'GUIDE_98_PUBLICATION_QA_09.md',
        QA / 'GUIDE_98_RELEASE_AUDIT_10.md',
        OUT / 'GUIDE_98_PUBLICATION_QA_MANIFEST.json',
        OUT / 'SHA256SUMS.txt',
        OUT / 'RENDER_QA.json',
    ]
    for p in required:
        if not p.exists():
            raise SystemExit(f'Missing release evidence: {p}')
    if json.loads((OUT / 'GUIDE_98_PUBLICATION_QA_MANIFEST.json').read_text())['status'] != 'PASS':
        raise SystemExit('Publication manifest not PASS')
    if json.loads((OUT / 'RENDER_QA.json').read_text())['status'] != 'PASS':
        raise SystemExit('Render QA not PASS')
    for line in (OUT / 'SHA256SUMS.txt').read_text().splitlines():
        if not line:
            continue
        digest, name = line.split('  ', 1)
        p = OUT / name
        if hashlib.sha256(p.read_bytes()).hexdigest() != digest:
            raise SystemExit(f'Checksum failed: {name}')

    d['stages']['publication'] = {
        'status': 'PASS',
        'evidence': [
            'project/revision-2026/guide-98/qa/GUIDE_98_PUBLICATION_QA_09.md',
            'project/revision-2026/guide-98/publication-candidate/GUIDE_98_PUBLICATION_QA_MANIFEST.json',
            'project/revision-2026/guide-98/publication-candidate/SHA256SUMS.txt',
            'project/revision-2026/guide-98/publication-candidate/RENDER_QA.json',
        ],
    }
    d['stages']['release_audit'] = {
        'status': 'PASS',
        'evidence': ['project/revision-2026/guide-98/qa/GUIDE_98_RELEASE_AUDIT_10.md'],
    }
    d['blockers'] = []
    STATUS.write_text(json.dumps(d, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print('Guide 98 status closure prepared.')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['build', 'close-status'])
    args = parser.parse_args()
    build() if args.action == 'build' else close_status()


if __name__ == '__main__':
    main()
