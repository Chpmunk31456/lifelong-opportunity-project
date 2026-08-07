#!/usr/bin/env python3
from pathlib import Path
from difflib import SequenceMatcher
import re

R=Path(__file__).resolve().parents[1]
S=R/'project/revision-2026/guide-02/source'
Q=R/'project/revision-2026/guide-02/qa'
D=S/'GUIDE_02_ENGLISH_DOCX_EXTRACTED_BASELINE.md'
P=S/'GUIDE_02_ENGLISH_PDF_EXTRACTED_BASELINE.txt'
O=Q/'GUIDE_02_ENGLISH_DIVERGENCE_CHARACTERIZATION_06.md'

def blocks(t):
    return [re.sub(r'\s+',' ',x).strip() for x in re.split(r'\n\s*\n',t) if re.sub(r'\s+',' ',x).strip()]

def norm(t):
    return re.sub(r'[^\w]+',' ',t).strip().casefold()

def short(t,n=220):
    t=re.sub(r'\s+',' ',t).strip().replace('|','\\|')
    return t if len(t)<=n else t[:n-1]+'…'

db=blocks(D.read_text(encoding='utf-8'))
pb=blocks(P.read_text(encoding='utf-8'))
m=SequenceMatcher(None,[norm(x) for x in db],[norm(x) for x in pb],autojunk=False)
do=[]; po=[]; eq=0
for tag,i1,i2,j1,j2 in m.get_opcodes():
    if tag=='equal': eq+=i2-i1
    elif tag=='delete': do+=db[i1:i2]
    elif tag=='insert': po+=pb[j1:j2]
    else: do+=db[i1:i2]; po+=pb[j1:j2]

def head(x): return len(x.split())<=14 and len(x)<=120 and not x.endswith(('.',',',';'))
dh=[x for x in db if head(x)]; ph=[x for x in pb if head(x)]
pn={norm(x) for x in ph}; dn={norm(x) for x in dh}
du=[x for x in dh if norm(x) not in pn]; pu=[x for x in ph if norm(x) not in dn]
L=['# Guide 02 English DOCX/PDF divergence characterization 06','',f'- DOCX blocks: **{len(db)}**',f'- PDF blocks: **{len(pb)}**',f'- Exactly aligned blocks: **{eq}**',f'- DOCX divergent blocks: **{len(do)}**',f'- PDF divergent blocks: **{len(po)}**',f'- DOCX-only heading-like blocks: **{len(du)}**',f'- PDF-only heading-like blocks: **{len(pu)}**','','## DOCX-only heading-like samples','']+[f'- {short(x)}' for x in du[:20]]+['','## PDF-only heading-like samples','']+[f'- {short(x)}' for x in pu[:30]]+['','## Representative DOCX divergent content','']+[f'- {short(x)}' for x in do[:20]]+['','## Representative PDF divergent content','']+[f'- {short(x)}' for x in po[:30]]+['','## Control decision','','The artifacts are materially different text sources, not simple formatting variants. Baseline selection must therefore use content completeness and provenance, not file format preference. This automated diagnostic does not designate either artifact authoritative or certify publication quality.','']
Q.mkdir(parents=True,exist_ok=True)
O.write_text('\n'.join(L),encoding='utf-8',newline='\n')
print(O.relative_to(R))
