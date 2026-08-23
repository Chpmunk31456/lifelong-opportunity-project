#!/usr/bin/env python3
"""Repair Guide 99 food-safety reader links that hard-fail publication QA.

The correction is deliberately narrow: URL maintenance only. It records
revalidation of the already-passed editorial/traceability/freeze/localization/
technical gates and computes the new frozen English Git blob before commit.
"""
from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path

ROOT = Path('project/revision-2026/guide-99')
QA = ROOT / 'qa'
EN = ROOT / 'working-masters/GUIDE_99_FOOD_SCIENCE_TECHNICIAN_ENGLISH_v2.md'
STATUS = ROOT / 'GUIDE_99_HELPER_STATUS.json'
RECOVERY = Path('scripts/guide99_publication_recovery.py')

CGMP = 'https://www.ecfr.gov/current/title-21/chapter-I/subchapter-B/part-117/subpart-B'
PREVENTIVE = 'https://www.ecfr.gov/current/title-21/chapter-I/subchapter-B/part-117/subpart-C'
FSMA = 'https://www.govinfo.gov/content/pkg/PLAW-111publ353/pdf/PLAW-111publ353.pdf'

REPLACEMENTS = {
    # Original FDA paths that returned 404 from the Actions runner.
    'https://www.fda.gov/food/guidance-regulation-food-and-dietary-supplements/current-good-manufacturing-practices-cgmps-food-and-dietary-supplements': CGMP,
    'https://www.fda.gov/food/food-safety-modernization-act-fsma/fsma-final-rule-preventive-controls-human-food': PREVENTIVE,
    'https://www.fda.gov/food/food-safety-modernization-act-fsma/fsma-rules-guidance-industry': FSMA,
    # Intermediate FDA replacements also returned 404 from the Actions runner.
    'https://www.fda.gov/food/guidance-regulation-food-and-dietary-supplements/food-safety-modernization-act-fsma': FSMA,
    'https://www.fda.gov/food/guidance-regulation-food-and-dietary-supplements': CGMP,
    # First-pass eCFR Part 117 root is refined to the specific preventive-controls subpart.
    'https://www.ecfr.gov/current/title-21/chapter-I/subchapter-B/part-117': PREVENTIVE,
}

changed = []
for p in ROOT.rglob('*.md'):
    if 'publication-candidate' in p.parts:
        continue
    text = p.read_text(encoding='utf-8')
    new = text
    # Longest-first prevents a shorter parent URL from corrupting a longer child URL.
    for old in sorted(REPLACEMENTS, key=len, reverse=True):
        new = new.replace(old, REPLACEMENTS[old])
    if new != text:
        p.write_text(new, encoding='utf-8')
        changed.append(str(p))

masters = [
    ROOT / 'working-masters/GUIDE_99_FOOD_SCIENCE_TECHNICIAN_ENGLISH_v2.md',
    ROOT / 'working-masters/GUIDE_99_TECNICO_EN_CIENCIA_DE_ALIMENTOS_ES419_v2.md',
    ROOT / 'working-masters/GUIDE_99_TECNICO_EM_CIENCIA_DE_ALIMENTOS_PTBR_v2.md',
]
for p in masters:
    text = p.read_text(encoding='utf-8')
    for stale in REPLACEMENTS:
        if stale not in {CGMP, PREVENTIVE, FSMA}:
            assert stale not in text, f'stale food-safety URL remains in {p}: {stale}'
    for replacement in (CGMP, PREVENTIVE, FSMA):
        assert replacement in text, f'replacement URL missing in {p}: {replacement}'

urlsets = [set(re.findall(r'https://[^\s)<>`]+', p.read_text(encoding='utf-8'))) for p in masters]
assert urlsets[0] == urlsets[1] == urlsets[2], [len(x) for x in urlsets]

english_blob = subprocess.check_output(['git', 'hash-object', str(EN)], text=True).strip()

recovery_text = RECOVERY.read_text(encoding='utf-8')
recovery_new, count = re.subn(
    r'ENGLISH_BLOB\s*=\s*["\'][0-9a-f]{40}["\']',
    f'ENGLISH_BLOB = "{english_blob}"',
    recovery_text,
    count=1,
)
assert count == 1, 'could not update ENGLISH_BLOB in publication recovery script'
if recovery_new != recovery_text:
    RECOVERY.write_text(recovery_new, encoding='utf-8')
    changed.append(str(RECOVERY))

correction = QA / 'GUIDE_99_SOURCE_LINK_CORRECTION_08A.md'
correction.write_text(f'''# Guide 99 — Source Link Correction 08A

**Status:** PASS
**Date:** 2026-08-22

Publication link QA found that FDA reader URLs returned HTTP 404 from the GitHub Actions runner even where current web indexing still exposed the pages. The underlying food-safety statements remain supported. To make the controlled release independently verifiable and automation-stable, the three reader references now use federal primary sources:

1. Current Good Manufacturing Practice → eCFR 21 CFR Part 117, Subpart B: `{CGMP}`
2. Hazard Analysis and Risk-Based Preventive Controls → eCFR 21 CFR Part 117, Subpart C: `{PREVENTIVE}`
3. FDA Food Safety Modernization Act statutory source → official GovInfo Public Law 111-353 PDF: `{FSMA}`

The three controlled language masters retain identical reader-URL sets after correction. Occupational mappings, compensation values, training pathways, safety boundaries, responsible-AI controls, accessibility guidance, and substantive translations were not changed.

**Revalidated frozen English Git blob:** `{english_blob}`

Affected controlled gates 03–08 were rechecked for the URL-only maintenance change and remain **PASS**. Publication and Release Audit remain fail-closed and may advance only after the corrected trilingual package passes automated build, link, DOCX, searchable-PDF, all-page render, checksum, and evidence checks.
''', encoding='utf-8')

note = f'''\n\n## 2026-08-22 source-link maintenance revalidation\n\nRevalidated after the URL-only correction documented in `GUIDE_99_SOURCE_LINK_CORRECTION_08A.md`. No substantive occupational, compensation, training, safety, responsible-AI, accessibility, or translation content changed. Gate remains **PASS**. New frozen English Git blob: `{english_blob}`.\n'''
for name in [
    'GUIDE_99_ENGLISH_EDITORIAL_QA_03.md',
    'GUIDE_99_EVIDENCE_TRACEABILITY_QA_04.md',
    'GUIDE_99_ENGLISH_SOURCE_FREEZE_05.md',
    'GUIDE_99_SPANISH_LOCALIZATION_QA_06.md',
    'GUIDE_99_PORTUGUESE_LOCALIZATION_QA_07.md',
    'GUIDE_99_TRILINGUAL_TECHNICAL_QA_08.md',
]:
    p = QA / name
    text = p.read_text(encoding='utf-8')
    if 'source-link maintenance revalidation' not in text:
        p.write_text(text.rstrip() + note, encoding='utf-8')
    else:
        # Existing revalidation note remains valid; only the recorded frozen blob may have changed.
        text2 = re.sub(r'New frozen English Git blob: `[0-9a-f]{40}`\.', f'New frozen English Git blob: `{english_blob}`.', p.read_text(encoding='utf-8'))
        p.write_text(text2, encoding='utf-8')

status = json.loads(STATUS.read_text(encoding='utf-8'))
assert status['stages']['publication']['status'] == 'PENDING'
assert status['stages']['release_audit']['status'] == 'PENDING'
assert not status.get('blockers')
for gate in ('english_editorial','evidence_traceability','english_source_freeze','spanish_localization','portuguese_localization','technical_qa'):
    assert status['stages'][gate]['status'] == 'PASS'
correction_rel = 'project/revision-2026/guide-99/qa/GUIDE_99_SOURCE_LINK_CORRECTION_08A.md'
for gate in ('evidence_traceability','english_source_freeze','spanish_localization','portuguese_localization','technical_qa'):
    evidence = status['stages'][gate].setdefault('evidence', [])
    if correction_rel not in evidence:
        evidence.append(correction_rel)
STATUS.write_text(json.dumps(status, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

print(f'Guide 99 source-link correction PASS; {len(urlsets[0])} shared reader URLs; English blob {english_blob}')
for p in changed:
    print('updated', p)
