#!/usr/bin/env python3
from collections import Counter
from difflib import SequenceMatcher
from pathlib import Path
import re

R = Path(__file__).resolve().parents[1]
S = R / 'project/revision-2026/guide-02/source'
Q = R / 'project/revision-2026/guide-02/qa'
D = S / 'GUIDE_02_ENGLISH_DOCX_EXTRACTED_BASELINE.md'
P = S / 'GUIDE_02_ENGLISH_PDF_EXTRACTED_BASELINE.txt'
O = Q / 'GUIDE_02_ENGLISH_DIVERGENCE_CHARACTERIZATION_06.md'
SOUT = Q / 'GUIDE_02_ENGLISH_SEMANTIC_EQUIVALENCE_RESULT_08.md'

REPEATED_PDF_LINES = (
    'Lifelong Opportunity Guides | Peer Support Specialist v1.0',
    'Free educational resource • Alberto (Al) Leiva • CC BY-NC-SA 4.0',
)


def blocks(text):
    return [re.sub(r'\s+', ' ', x).strip() for x in re.split(r'\n\s*\n', text)
            if re.sub(r'\s+', ' ', x).strip()]


def norm(text):
    return re.sub(r'[^\w]+', ' ', text).strip().casefold()


def short(text, n=220):
    text = re.sub(r'\s+', ' ', text).strip().replace('|', '\\|')
    return text if len(text) <= n else text[:n - 1] + '…'


def clean_source(text, source):
    # Remove the extraction-only Markdown heading from the DOCX baseline.
    if source == 'docx':
        text = re.sub(r'^# Guide 02 English DOCX extracted baseline\s*', '', text, flags=re.I)

    # Join words split only because a PDF line ended with a hyphen.
    text = re.sub(r'(?<=\w)-\s*\n\s*(?=\w)', '', text)

    lines = []
    for raw in text.splitlines():
        line = raw.strip()
        if source == 'pdf' and line in REPEATED_PDF_LINES:
            continue
        lines.append(raw)
    text = '\n'.join(lines)

    # Normalize typographic punctuation without changing lexical content.
    return (text.replace('’', "'")
                .replace('‘', "'")
                .replace('“', '"')
                .replace('”', '"')
                .replace('–', '-')
                .replace('—', '-'))


def tokens(text):
    return re.findall(r"[a-z0-9]+(?:'[a-z0-9]+)?", text.casefold())


def multiset_coverage(a, b):
    ca, cb = Counter(a), Counter(b)
    common = sum((ca & cb).values())
    return common / len(a) if a else 0.0


def ngrams(seq, n=5):
    if len(seq) < n:
        return set()
    return {tuple(seq[i:i+n]) for i in range(len(seq) - n + 1)}


def set_coverage(a, b):
    return len(a & b) / len(a) if a else 0.0


def headings(text):
    found = set()
    for raw in text.splitlines():
        line = re.sub(r'\s+', ' ', raw).strip()
        if re.match(r'^\d{1,2}\.\s+[A-Z]', line):
            found.add(norm(line))
        elif line in {
            'Why I Created This Guide', 'Acknowledgment of AI Assistance',
            'Ethical and Practical Limits', 'How This Guide Relates to the Foundation Guide',
            'Table of Contents'
        }:
            found.add(norm(line))
    return found


docx_raw = D.read_text(encoding='utf-8')
pdf_raw = P.read_text(encoding='utf-8')

# Preserve the original block-level characterization as a diagnostic, but do not
# use it alone to decide source equivalence because PDF extraction is page-oriented.
db = blocks(docx_raw)
pb = blocks(pdf_raw)
m = SequenceMatcher(None, [norm(x) for x in db], [norm(x) for x in pb], autojunk=False)
do, po, eq = [], [], 0
for tag, i1, i2, j1, j2 in m.get_opcodes():
    if tag == 'equal':
        eq += i2 - i1
    elif tag == 'delete':
        do += db[i1:i2]
    elif tag == 'insert':
        po += pb[j1:j2]
    else:
        do += db[i1:i2]
        po += pb[j1:j2]


def head(x):
    return len(x.split()) <= 14 and len(x) <= 120 and not x.endswith(('.', ',', ';'))


dh = [x for x in db if head(x)]
ph = [x for x in pb if head(x)]
pn = {norm(x) for x in ph}
dn = {norm(x) for x in dh}
du = [x for x in dh if norm(x) not in pn]
pu = [x for x in ph if norm(x) not in dn]

L = [
    '# Guide 02 English DOCX/PDF divergence characterization 06', '',
    '- **Control note:** block comparison is diagnostic only because DOCX extraction is paragraph-oriented while PDF extraction is page-oriented.',
    f'- DOCX blocks: **{len(db)}**',
    f'- PDF blocks: **{len(pb)}**',
    f'- Exactly aligned blocks: **{eq}**',
    f'- DOCX divergent blocks: **{len(do)}**',
    f'- PDF divergent blocks: **{len(po)}**',
    f'- DOCX-only heading-like blocks: **{len(du)}**',
    f'- PDF-only heading-like blocks: **{len(pu)}**', '',
    '## DOCX-only heading-like samples', '',
] + [f'- {short(x)}' for x in du[:20]] + [
    '', '## PDF-only heading-like samples', '',
] + [f'- {short(x)}' for x in pu[:30]] + [
    '', '## Representative DOCX divergent content', '',
] + [f'- {short(x)}' for x in do[:20]] + [
    '', '## Representative PDF divergent content', '',
] + [f'- {short(x)}' for x in po[:30]] + [
    '', '## Control decision', '',
    'The block-level result alone is not sufficient to designate either artifact authoritative. '
    'The companion semantic-equivalence result removes known extraction noise and tests token, n-gram, and heading coverage before baseline selection.', ''
]
Q.mkdir(parents=True, exist_ok=True)
O.write_text('\n'.join(L), encoding='utf-8', newline='\n')

# Robust semantic-equivalence analysis.
docx_clean = clean_source(docx_raw, 'docx')
pdf_clean = clean_source(pdf_raw, 'pdf')
dt = tokens(docx_clean)
pt = tokens(pdf_clean)
d5 = ngrams(dt, 5)
p5 = ngrams(pt, 5)
dhset = headings(docx_clean)
phset = headings(pdf_clean)

seq_ratio = SequenceMatcher(None, dt, pt, autojunk=False).ratio()
docx_token_cov = multiset_coverage(dt, pt)
pdf_token_cov = multiset_coverage(pt, dt)
docx_5gram_cov = set_coverage(d5, p5)
pdf_5gram_cov = set_coverage(p5, d5)
docx_heading_cov = set_coverage(dhset, phset)
pdf_heading_cov = set_coverage(phset, dhset)

if (min(docx_token_cov, pdf_token_cov) >= 0.97
        and min(docx_5gram_cov, pdf_5gram_cov) >= 0.95
        and min(docx_heading_cov, pdf_heading_cov) >= 0.95):
    decision = ('**SEMANTIC-EQUIVALENCE CANDIDATE:** after removal of known extraction noise, '
                'content coverage is high enough for a provenance review to determine whether the DOCX can serve as the editable baseline.')
elif docx_token_cov >= 0.97 and docx_5gram_cov >= 0.95:
    decision = ('**PDF-SUPERSET CANDIDATE:** nearly all DOCX lexical content is represented in the PDF, '
                'but the PDF contains additional content or extraction material that must be classified before baseline selection.')
elif pdf_token_cov >= 0.97 and pdf_5gram_cov >= 0.95:
    decision = ('**DOCX-SUPERSET CANDIDATE:** nearly all PDF lexical content is represented in the DOCX, '
                'but the DOCX contains additional content that must be classified before baseline selection.')
else:
    decision = ('**SUBSTANTIVE DIVERGENCE HOLD:** normalized semantic coverage remains below the controlled thresholds; '
                'reconstruct the English baseline only after identifying which unmatched content is substantive.')

SL = [
    '# Guide 02 English semantic-equivalence result 08', '',
    '- **Purpose:** distinguish real content divergence from predictable DOCX/PDF extraction noise.',
    '- **Controls applied:** removal of extraction-only DOCX heading; removal of repeated PDF page headers/footers; PDF line-break de-hyphenation; punctuation normalization; token, five-token n-gram, and numbered-heading coverage.',
    '- **Not a certification:** automated evidence only; no claim of independent human review, accessibility certification, accreditation, legal review, or factual validation.', '',
    '## Metrics', '',
    '| Metric | Result |', '|---|---:|',
    f'| DOCX cleaned tokens | {len(dt)} |',
    f'| PDF cleaned tokens | {len(pt)} |',
    f'| Token sequence similarity | {seq_ratio:.6f} |',
    f'| DOCX token coverage by PDF | {docx_token_cov:.6f} |',
    f'| PDF token coverage by DOCX | {pdf_token_cov:.6f} |',
    f'| DOCX 5-gram coverage by PDF | {docx_5gram_cov:.6f} |',
    f'| PDF 5-gram coverage by DOCX | {pdf_5gram_cov:.6f} |',
    f'| DOCX heading coverage by PDF | {docx_heading_cov:.6f} |',
    f'| PDF heading coverage by DOCX | {pdf_heading_cov:.6f} |', '',
    '## Gate interpretation', '', decision, '',
    'This result does not by itself designate an authoritative source. A baseline-selection record must also consider editability, document provenance, version metadata, substantive unmatched passages, and the requirement to preserve the most complete verified content.', ''
]
SOUT.write_text('\n'.join(SL), encoding='utf-8', newline='\n')
print(O.relative_to(R))
print(SOUT.relative_to(R))
