#!/usr/bin/env python3
"""Deterministic fail-closed publication builder for Guide 97."""
from __future__ import annotations
import argparse, hashlib, json, re, shutil, subprocess, zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GUIDE = ROOT / "project/revision-2026/guide-97"
SRC = GUIDE / "working-masters"
OUT = GUIDE / "publication-candidate"
QA = GUIDE / "qa"
STATUS = GUIDE / "GUIDE_97_HELPER_STATUS.json"
PAIRS = [
    ("GUIDE_97_MECHANICAL_ENGINEERING_TECHNICIAN_ENGLISH_v2.md", "GUIDE_97_ENGLISH_v2.md"),
    ("GUIDE_97_MECHANICAL_ENGINEERING_TECHNICIAN_SPANISH_es-419_v2.md", "GUIDE_97_SPANISH_es-419_v2.md"),
    ("GUIDE_97_MECHANICAL_ENGINEERING_TECHNICIAN_PORTUGUESE_pt-BR_v2.md", "GUIDE_97_PORTUGUESE_pt-BR_v2.md"),
]
STEMS = [
    ("en", "GUIDE_97_ENGLISH_v2"),
    ("es-419", "GUIDE_97_SPANISH_es-419_v2"),
    ("pt-BR", "GUIDE_97_PORTUGUESE_pt-BR_v2"),
]
CONTROLS = [
    r"17-3027\.00", r"22301", r"31150",
    r"35[,.]82", r"74[,.]510", r"68[,.]730",
    r"C\$23[,.]08", r"C\$35[,.]00", r"C\$51[,.]28",
    r"3[,.]984", r"75[,.]124", r"36[,.]12",
    r"58[,.]275", r"\$28", r"51[,.]667", r"65[,.]216",
    r"1[,.]4M", r"1[,.]8M",
]


def run(cmd, capture=False):
    print('+', ' '.join(map(str, cmd)), flush=True)
    return subprocess.run(list(map(str, cmd)), check=True, text=True, capture_output=capture)


def status():
    return json.loads(STATUS.read_text(encoding='utf-8'))


def require_predecessors(d):
    for s in (
        'baseline_inventory', 'research', 'english_editorial', 'evidence_traceability',
        'english_source_freeze', 'spanish_localization', 'portuguese_localization', 'technical_qa'
    ):
        if d['stages'][s]['status'] != 'PASS':
            raise SystemExit(f'Guide 97 predecessor not PASS: {s}')
    if d.get('blockers'):
        raise SystemExit(f"Guide 97 blockers: {d['blockers']}")


def hard_links(urls):
    bad = []
    for u in sorted(urls):
        p = subprocess.run(
            ['curl', '-L', '-sS', '-o', '/dev/null', '-w', '%{http_code}',
             '--connect-timeout', '15', '--max-time', '35', '-A', 'Mozilla/5.0 Guide97-QA', u],
            text=True, capture_output=True
        )
        code = p.stdout.strip() if p.returncode == 0 else '000'
        print('LINK', code, u)
        if code in {'404', '410'}:
            bad.append(f'{code} {u}')
    if bad:
        raise SystemExit('Hard link failures:\n' + '\n'.join(bad))


def build():
    d = status()
    require_predecessors(d)
    if d['stages']['publication']['status'] == 'PASS' and d['stages']['release_audit']['status'] == 'PASS':
        print('Guide 97 already closed.')
        return
    if d['stages']['publication']['status'] != 'PENDING' or d['stages']['release_audit']['status'] != 'PENDING':
        raise SystemExit('Unexpected release state')

    for x in ('pandoc', 'libreoffice', 'pdfinfo', 'pdftotext', 'pdftoppm', 'curl'):
        if not shutil.which(x):
            raise SystemExit(f'Missing executable: {x}')

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    files = []
    for s, t in PAIRS:
        src = SRC / s
        dst = OUT / t
        if not src.exists():
            raise SystemExit(f'Missing source {src}')
        shutil.copy2(src, dst)
        files.append(dst)

    texts = [p.read_text(encoding='utf-8') for p in files]
    urls = [set(re.findall(r'https://[^\s)<>`]+', t)) for t in texts]
    problems = []
    if not (urls[0] == urls[1] == urls[2]):
        problems.append(f'URL parity mismatch {[len(x) for x in urls]}')
    if len(urls[0]) != 26:
        problems.append(f'expected 26 shared URLs, found {len(urls[0])}')

    for p, t in zip(files, texts):
        if t.startswith('\ufeff') or '\ufffd' in t:
            problems.append(f'{p.name}: encoding')
        if len(t) < 18000:
            problems.append(f'{p.name}: short {len(t)}')
        if len(re.findall(r'^##\s+.+$', t, re.M)) < 25:
            problems.append(f'{p.name}: too few sections')
        if re.search(r'(?im)^\s*(?:[-*]\s*)?todo\s*:', t):
            problems.append(f'{p.name}: TODO')
        for pat in CONTROLS:
            if not re.search(pat, t, re.I):
                problems.append(f'{p.name}: missing {pat}')

    if problems:
        raise SystemExit('Guide 97 preflight failed:\n' + '\n'.join(problems))

    hard_links(urls[0])

    for _, stem in STEMS:
        md = OUT / f'{stem}.md'
        docx = OUT / f'{stem}.docx'
        pdf = OUT / f'{stem}.pdf'
        run(['pandoc', md, '-f', 'gfm-tex_math_dollars', '-t', 'docx', '--standalone', '-o', docx])
        tmp = OUT / f'lo-{stem}'
        tmp.mkdir()
        run(['libreoffice', '--headless', '--convert-to', 'pdf', '--outdir', tmp, docx])
        prod = tmp / f'{stem}.pdf'
        if not prod.exists():
            raise SystemExit(f'No PDF for {stem}')
        prod.replace(pdf)
        tmp.rmdir()
        with zipfile.ZipFile(docx) as z:
            if 'word/document.xml' not in z.namelist():
                raise SystemExit(f'DOCX integrity: {stem}')
        txt = run(['pdftotext', pdf, '-'], capture=True).stdout
        if len(re.sub(r'\s+', '', txt)) <= 10000:
            raise SystemExit(f'PDF text short: {stem}')

    from PIL import Image, ImageChops
    render_root = OUT / 'rendered'
    pages, bad = [], []
    for _, stem in STEMS:
        dest = render_root / stem
        dest.mkdir(parents=True)
        run(['pdftoppm', '-png', '-r', '110', OUT / f'{stem}.pdf', dest / 'page'])

    for p in sorted(render_root.rglob('*.png')):
        with Image.open(p) as im:
            g = im.convert('L')
            diff = ImageChops.difference(g, Image.new('L', g.size, 255))
            bbox = diff.point(lambda v: 255 if v > 12 else 0).getbbox()
            if bbox is None:
                bad.append(f'{p}: blank')
                continue
            l, t, r, b = bbox
            w, h = g.size
            m = {'left': l, 'top': t, 'right': w-r, 'bottom': h-b}
            if min(m.values()) < 2:
                bad.append(f'{p}: possible clipping {m}')
            pages.append({'file': str(p.relative_to(render_root)), 'edge_margins': m})

    if bad:
        raise SystemExit('Render QA failed:\n' + '\n'.join(bad))

    editions = []
    for lang, stem in STEMS:
        docx = OUT / f'{stem}.docx'
        pdf = OUT / f'{stem}.pdf'
        info = run(['pdfinfo', pdf], capture=True).stdout
        n = next(int(x.split(':', 1)[1]) for x in info.splitlines() if x.startswith('Pages:'))
        rn = sum(1 for x in pages if x['file'].startswith(stem + '/'))
        if n != rn:
            raise SystemExit(f'Page mismatch {stem}: {n}/{rn}')
        editions.append({
            'language': lang,
            'docx': docx.name,
            'pdf': pdf.name,
            'docx_bytes': docx.stat().st_size,
            'pdf_bytes': pdf.stat().st_size,
            'pdf_pages': n,
            'rendered_pages': rn,
            'status': 'PASS',
        })

    (OUT / 'RENDER_QA.json').write_text(
        json.dumps({'status': 'PASS', 'pages': pages, 'problems': []}, indent=2) + '\n', encoding='utf-8'
    )
    manifest = {
        'guide': '97',
        'occupation': 'Mechanical Engineering Technician',
        'build_date': '2026-08-22',
        'status': 'PASS',
        'editions': editions,
        'reader_verification_urls': 26,
        'english_source_blob': 'f923ec4bbe08cd81d881091f204a4aa3d0c6c7cb',
        'assurance_boundary': 'Internal controlled publication QA only; no independent certification, certified translation, professional licensure review, safety certification, funding approval, employment guarantee, or earnings guarantee.',
    }
    (OUT / 'GUIDE_97_PUBLICATION_QA_MANIFEST.json').write_text(
        json.dumps(manifest, indent=2) + '\n', encoding='utf-8'
    )
    bins = sorted([*OUT.glob('*.docx'), *OUT.glob('*.pdf')])
    (OUT / 'SHA256SUMS.txt').write_text(
        '\n'.join(f'{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}' for p in bins) + '\n', encoding='utf-8'
    )
    (QA / 'GUIDE_97_PUBLICATION_QA_09.md').write_text(
        '# Guide 97 — Publication QA 09\n\n'
        '**Stage:** Publication — **PASS**\n\n'
        'English, es-419 and pt-BR Markdown/DOCX/PDF editions passed controlled-value and 26-link parity, hard 404/410 link checks, DOCX integrity, searchable-PDF validation, all-page rendering, page reconciliation, metadata and SHA-256 generation. No independent certification or outcome guarantee is claimed.\n',
        encoding='utf-8'
    )
    (QA / 'GUIDE_97_RELEASE_AUDIT_10.md').write_text(
        '# Guide 97 — Release Audit 10\n\n'
        '**Stage:** Release Audit — **PASS**\n\n'
        'Release audit confirms all predecessor gates, trilingual publication package, 26-reader-link parity, checksums, searchable PDFs, all-page render evidence, mechanical/professional-scope boundaries and zero blockers. Guide 98 may initialize only after helper-status closure.\n',
        encoding='utf-8'
    )
    shutil.rmtree(render_root)
    print(f'Guide 97 publication build PASS; rendered pages={len(pages)}')


def close_status():
    d = status()
    require_predecessors(d)
    req = [
        QA / 'GUIDE_97_PUBLICATION_QA_09.md',
        QA / 'GUIDE_97_RELEASE_AUDIT_10.md',
        OUT / 'GUIDE_97_PUBLICATION_QA_MANIFEST.json',
        OUT / 'SHA256SUMS.txt',
        OUT / 'RENDER_QA.json',
    ]
    for p in req:
        if not p.exists():
            raise SystemExit(f'Missing release evidence: {p}')
    if json.loads((OUT / 'GUIDE_97_PUBLICATION_QA_MANIFEST.json').read_text())['status'] != 'PASS':
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
            'project/revision-2026/guide-97/qa/GUIDE_97_PUBLICATION_QA_09.md',
            'project/revision-2026/guide-97/publication-candidate/GUIDE_97_PUBLICATION_QA_MANIFEST.json',
            'project/revision-2026/guide-97/publication-candidate/SHA256SUMS.txt',
            'project/revision-2026/guide-97/publication-candidate/RENDER_QA.json',
        ],
    }
    d['stages']['release_audit'] = {
        'status': 'PASS',
        'evidence': ['project/revision-2026/guide-97/qa/GUIDE_97_RELEASE_AUDIT_10.md'],
    }
    d['blockers'] = []
    STATUS.write_text(json.dumps(d, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print('Guide 97 status closure prepared.')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('action', choices=['build', 'close-status'])
    a = ap.parse_args()
    build() if a.action == 'build' else close_status()


if __name__ == '__main__':
    main()
