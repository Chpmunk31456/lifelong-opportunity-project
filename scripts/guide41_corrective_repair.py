from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
ES = ROOT / 'project/revision-2026/guide-41/working-masters/GUIDE_41_CARPENTER_AND_CABINETMAKING_TECHNICIAN_ES419_v2.md'
PT = ROOT / 'project/revision-2026/guide-41/working-masters/GUIDE_41_CARPENTER_AND_CABINETMAKING_TECHNICIAN_PTBR_v2.md'
EN = ROOT / 'project/revision-2026/guide-41/working-masters/GUIDE_41_CARPENTER_AND_CABINETMAKING_TECHNICIAN_ENGLISH_v2.md'

URL_RE = re.compile(r'https://[^\s)<>`]+')

ES_BLOCK = '''## Fuentes actuales

Fuentes oficiales/públicas:

- U.S. Department of Labor O*NET OnLine — Carpenters: https://www.onetonline.org/link/summary/47-2031.00
- Apprenticeship.gov: https://www.apprenticeship.gov/
- CareerOneStop — recursos de formación WIOA: https://www.careeronestop.org/LocalHelp/EmploymentAndTraining/find-WIOA-training-programs.aspx
- Government of Canada Job Bank — salarios de carpinteros: https://www.jobbank.gc.ca/wagereport/occupation/6388
- Government of Canada Job Bank — requisitos de Carpenter (NOC 72310): https://www.jobbank.gc.ca/marketreport/requirements/6408/ca
- Government of Canada — apoyos para oficios especializados y aprendizaje: https://www.canada.ca/en/services/jobs/training/support-skilled-trades-apprentices.html
- Government of Canada — estado de Apprenticeship Grants: https://www.canada.ca/en/services/jobs/training/support-skilled-trades-apprentices/grants.html
- Government of Canada — oportunidades de financiación para oficios especializados y aprendizaje: https://www.canada.ca/en/services/jobs/training/support-skilled-trades-apprentices/funding-opportunities.html
- Government of Canada — Apprenticeship Service: https://www.canada.ca/en/employment-social-development/programs/apprentice-service-program.html
- SENA Betowa — Básico de carpintería y ebanistería: https://betowa.sena.edu.co/oferta/basico-de-carpinteria-y-ebanisteria?offertype=company&programId=12174
- OIT/Cinterfor: https://www.oitcinterfor.org/

Fuentes salariales suplementarias no gubernamentales:

- Salary.com — Cabinetmaker and Bench Carpenter: https://www.salary.com/research/salary/benchmark/cabinetmaker-and-bench-carpenter-salary
- Salary.com — Cabinet Maker: https://www.salary.com/research/salary/listing/cabinet-maker-salary
'''

PT_BLOCK = '''## Fontes atuais

Fontes oficiais/públicas:

- U.S. Department of Labor O*NET OnLine — Carpenters: https://www.onetonline.org/link/summary/47-2031.00
- Apprenticeship.gov: https://www.apprenticeship.gov/
- CareerOneStop — recursos de treinamento WIOA: https://www.careeronestop.org/LocalHelp/EmploymentAndTraining/find-WIOA-training-programs.aspx
- Government of Canada Job Bank — salários de carpinteiros: https://www.jobbank.gc.ca/wagereport/occupation/6388
- Government of Canada Job Bank — requisitos de Carpenter (NOC 72310): https://www.jobbank.gc.ca/marketreport/requirements/6408/ca
- Government of Canada — apoios para ofícios especializados e aprendizagem: https://www.canada.ca/en/services/jobs/training/support-skilled-trades-apprentices.html
- Government of Canada — situação dos Apprenticeship Grants: https://www.canada.ca/en/services/jobs/training/support-skilled-trades-apprentices/grants.html
- Government of Canada — oportunidades de financiamento para ofícios especializados e aprendizagem: https://www.canada.ca/en/services/jobs/training/support-skilled-trades-apprentices/funding-opportunities.html
- Government of Canada — Apprenticeship Service: https://www.canada.ca/en/employment-social-development/programs/apprentice-service-program.html
- SENA Betowa — Básico de carpintería y ebanistería: https://betowa.sena.edu.co/oferta/basico-de-carpinteria-y-ebanisteria?offertype=company&programId=12174
- OIT/Cinterfor: https://www.oitcinterfor.org/

Fontes salariais suplementares não governamentais:

- Salary.com — Cabinetmaker and Bench Carpenter: https://www.salary.com/research/salary/benchmark/cabinetmaker-and-bench-carpenter-salary
- Salary.com — Cabinet Maker: https://www.salary.com/research/salary/listing/cabinet-maker-salary
'''


def replace_block(path: Path, start_heading: str, end_heading: str, new_block: str) -> None:
    text = path.read_text(encoding='utf-8')
    start = text.find(start_heading)
    end = text.find(end_heading, start)
    if start < 0 or end < 0 or end <= start:
        raise SystemExit(f'{path}: expected source-section anchors not found')
    updated = text[:start] + new_block.rstrip() + '\n\n' + text[end:]
    path.write_text(updated, encoding='utf-8')


replace_block(ES, '## Fuentes actuales', '## Nota sobre fuentes y revisión', ES_BLOCK)
replace_block(PT, '## Fontes atuais', '## Nota de fonte e revisão', PT_BLOCK)

# Fail closed: localized source URL sets must exactly equal the frozen English source set.
en_urls = set(URL_RE.findall(EN.read_text(encoding='utf-8')))
for locale, path in [('es-419', ES), ('pt-BR', PT)]:
    localized = set(URL_RE.findall(path.read_text(encoding='utf-8')))
    if localized != en_urls:
        raise SystemExit(
            f'{locale}: URL parity repair failed; missing={sorted(en_urls-localized)}; extra={sorted(localized-en_urls)}'
        )

print(f'Guide 41 localization parity repair PASS: exact frozen-English source URL parity ({len(en_urls)} URLs).')
