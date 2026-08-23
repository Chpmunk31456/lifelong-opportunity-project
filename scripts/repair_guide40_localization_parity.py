from pathlib import Path
import re

ROOT = Path('project/revision-2026/guide-40/working-masters')
EN = ROOT / 'GUIDE_40_CONSTRUCTION_LABORER_AND_TRADE_HELPER_ENGLISH_v2.md'
ES = ROOT / 'GUIDE_40_CONSTRUCTION_LABORER_AND_TRADE_HELPER_SPANISH_es-419_v2.md'
PT = ROOT / 'GUIDE_40_CONSTRUCTION_LABORER_AND_TRADE_HELPER_PORTUGUESE_pt-BR_v2.md'

COMMON_URLS = [
    'https://www.bls.gov/ooh/construction-and-extraction/construction-laborers-and-helpers.htm',
    'https://www.onetonline.org/link/summary/47-2061.00',
    'https://www.onetonline.org/link/localwages/47-2061.00',
    'https://www.osha.gov/laws-regs/regulations/standardnumber/1926/',
    'https://www.osha.gov/training/outreach/',
    'https://www.apprenticeship.gov/apprenticeship-industries/construction',
    'https://www.apprenticeship.gov/apprenticeship-job-finder',
    'https://www.careeronestop.org/LocalHelp/AmericanJobCenters/american-job-centers.aspx',
    'https://www.careeronestop.org/LocalHelp/EmploymentAndTraining/find-WIOA-training-programs.aspx',
    'https://www23.statcan.gc.ca/imdb/p3VD.pl?CLV=1&CPV=7511&CST=01052021&CVD=1322706&D=1&Function=getVD&MLV=5&TVD=1322554',
    'https://www.jobbank.gc.ca/marketreport/requirements/8447/ca',
    'https://www.jobbank.gc.ca/wagereport/occupation/8449',
    'https://red-seal.ca/eng/trades/const-craft-work.shtml',
    'https://www.canada.ca/en/services/jobs/training/support-skilled-trades-apprentices/funding-opportunities.html',
    'https://www.sena.edu.co/es-co/Noticias/Paginas/noticia.aspx?IdNoticia=8975',
    'https://betowa.sena.edu.co/oferta/mamposteria?modality=P&offertype=company&programId=219657',
    'https://www.sena.edu.co/es-co/formacion/Paginas/trabajo-seguro-en-alturas.aspx',
    'https://ape.sena.edu.co/Paginas/Inicio.aspx',
    'https://www.oitcinterfor.org/red-institucional',
    'https://www.salary.com/research/salary/opening/construction-laborer-helper-salary',
]

ES_TAIL = '''## Fuentes y notas de verificación

Las fuentes oficiales deben revisarse nuevamente antes de tomar decisiones de seguridad, capacitación, licencias, financiación, traslado o empleo. Las ofertas de programas, salarios, reglas y periodos de inscripción cambian.

### Estados Unidos

- BLS — Construction Laborers and Helpers: https://www.bls.gov/ooh/construction-and-extraction/construction-laborers-and-helpers.htm
- O*NET — Construction Laborers 47-2061.00: https://www.onetonline.org/link/summary/47-2061.00
- O*NET — salarios nacionales, Construction Laborers: https://www.onetonline.org/link/localwages/47-2061.00
- OSHA — normas de construcción: https://www.osha.gov/laws-regs/regulations/standardnumber/1926/
- OSHA — Outreach Training Program: https://www.osha.gov/training/outreach/
- Apprenticeship.gov — Construction: https://www.apprenticeship.gov/apprenticeship-industries/construction
- Apprenticeship.gov — Apprenticeship Finder: https://www.apprenticeship.gov/apprenticeship-job-finder
- CareerOneStop — American Job Centers: https://www.careeronestop.org/LocalHelp/AmericanJobCenters/american-job-centers.aspx
- CareerOneStop — buscador de programas elegibles para WIOA: https://www.careeronestop.org/LocalHelp/EmploymentAndTraining/find-WIOA-training-programs.aspx

### Canadá

- Statistics Canada — contexto NOC 75110: https://www23.statcan.gc.ca/imdb/p3VD.pl?CLV=1&CPV=7511&CST=01052021&CVD=1322706&D=1&Function=getVD&MLV=5&TVD=1322554
- Job Bank — requisitos NOC 75110: https://www.jobbank.gc.ca/marketreport/requirements/8447/ca
- Job Bank — salarios NOC 75110: https://www.jobbank.gc.ca/wagereport/occupation/8449
- Red Seal — Construction Craft Worker: https://red-seal.ca/eng/trades/const-craft-work.shtml
- Canadá — financiación para oficios y aprendizaje: https://www.canada.ca/en/services/jobs/training/support-skilled-trades-apprentices/funding-opportunities.html

### Colombia y América Latina

- SENA — información sobre oferta gratuita 2026: https://www.sena.edu.co/es-co/Noticias/Paginas/noticia.aspx?IdNoticia=8975
- SENA Betowa — Mampostería: https://betowa.sena.edu.co/oferta/mamposteria?modality=P&offertype=company&programId=219657
- SENA — Trabajo seguro en alturas: https://www.sena.edu.co/es-co/formacion/Paginas/trabajo-seguro-en-alturas.aspx
- SENA — Agencia Pública de Empleo: https://ape.sena.edu.co/Paginas/Inicio.aspx
- OIT/Cinterfor — Red institucional: https://www.oitcinterfor.org/red-institucional

### Fuente privada complementaria de remuneración

- Salary.com — Construction Laborer/Helper: https://www.salary.com/research/salary/opening/construction-laborer-helper-salary

## Aviso importante

Esta guía ofrece información general educativa y de planificación profesional. No garantiza empleo, ingresos, admisión, financiación, ingreso a un aprendizaje, licenciamiento, certificación, ascenso ni ningún otro resultado. Los requisitos cambian según la jurisdicción, el empleador, el proyecto, la tarea y el tiempo.

Esta guía no sustituye la capacitación de seguridad en el trabajo, la supervisión calificada, la asesoría legal, la orientación médica o financiera, la orientación sobre licencias ni las instrucciones de un empleador o autoridad reguladora.

No se afirma certificación humana independiente de traducción, certificación de accesibilidad, revisión profesional de acreditación, revisión legal ni aprobación de un organismo certificador salvo que exista documentación separada.

## Autor y asistencia de IA

Creado y dirigido por **Alberto “Al” Leiva**. ChatGPT apoyó la investigación, organización, edición, apoyo de traducción y preparación documental bajo la dirección del autor. El autor conserva la responsabilidad por las decisiones editoriales y de publicación.
'''

PT_TAIL = '''## Fontes e notas de verificação

Reconfirme as fontes oficiais antes de tomar decisões sobre segurança, treinamento, licenciamento, financiamento, mudança ou emprego. Programas, salários, regras e períodos de matrícula mudam.

### Estados Unidos

- BLS — Construction Laborers and Helpers: https://www.bls.gov/ooh/construction-and-extraction/construction-laborers-and-helpers.htm
- O*NET — Construction Laborers 47-2061.00: https://www.onetonline.org/link/summary/47-2061.00
- O*NET — salários nacionais, Construction Laborers: https://www.onetonline.org/link/localwages/47-2061.00
- OSHA — normas de construção: https://www.osha.gov/laws-regs/regulations/standardnumber/1926/
- OSHA — Outreach Training Program: https://www.osha.gov/training/outreach/
- Apprenticeship.gov — Construction: https://www.apprenticeship.gov/apprenticeship-industries/construction
- Apprenticeship.gov — Apprenticeship Finder: https://www.apprenticeship.gov/apprenticeship-job-finder
- CareerOneStop — American Job Centers: https://www.careeronestop.org/LocalHelp/AmericanJobCenters/american-job-centers.aspx
- CareerOneStop — WIOA-Eligible Training Program Finder: https://www.careeronestop.org/LocalHelp/EmploymentAndTraining/find-WIOA-training-programs.aspx

### Canadá

- Statistics Canada — contexto NOC 75110: https://www23.statcan.gc.ca/imdb/p3VD.pl?CLV=1&CPV=7511&CST=01052021&CVD=1322706&D=1&Function=getVD&MLV=5&TVD=1322554
- Job Bank — requisitos NOC 75110: https://www.jobbank.gc.ca/marketreport/requirements/8447/ca
- Job Bank — salários NOC 75110: https://www.jobbank.gc.ca/wagereport/occupation/8449
- Red Seal — Construction Craft Worker: https://red-seal.ca/eng/trades/const-craft-work.shtml
- Canadá — financiamento para ofícios e aprendizagem: https://www.canada.ca/en/services/jobs/training/support-skilled-trades-apprentices/funding-opportunities.html

### Colômbia e América Latina

- SENA — informações sobre oferta gratuita de 2026: https://www.sena.edu.co/es-co/Noticias/Paginas/noticia.aspx?IdNoticia=8975
- SENA Betowa — Mampostería: https://betowa.sena.edu.co/oferta/mamposteria?modality=P&offertype=company&programId=219657
- SENA — Trabajo seguro en alturas: https://www.sena.edu.co/es-co/formacion/Paginas/trabajo-seguro-en-alturas.aspx
- SENA — Agencia Pública de Empleo: https://ape.sena.edu.co/Paginas/Inicio.aspx
- OIT/Cinterfor — Red institucional: https://www.oitcinterfor.org/red-institucional

### Fonte privada complementar de remuneração

- Salary.com — Construction Laborer/Helper: https://www.salary.com/research/salary/opening/construction-laborer-helper-salary

## Aviso importante

Este guia fornece informações gerais educacionais e de planejamento de carreira. Não garante emprego, renda, admissão, financiamento, vaga de aprendizagem, licenciamento, certificação, promoção nem qualquer outro resultado. Os requisitos variam conforme jurisdição, empregador, projeto, tarefa e momento.

Este guia não substitui treinamento de segurança no trabalho, supervisão qualificada, orientação jurídica, orientação médica ou financeira, orientação sobre licenciamento nem instruções de um empregador ou autoridade reguladora.

Não se declara certificação humana independente de tradução, certificação de acessibilidade, revisão profissional de acreditação, revisão jurídica nem aprovação por organismo certificador, salvo quando houver documentação separada.

## Autor e assistência de IA

Criado e dirigido por **Alberto “Al” Leiva**. O ChatGPT apoiou pesquisa, organização, edição, suporte à tradução e preparação documental sob a direção do autor. O autor permanece responsável pelas decisões editoriais e de publicação.
'''


def replace_tail(path: Path, heading: str, new_tail: str) -> None:
    text = path.read_text(encoding='utf-8')
    marker = f'## {heading}'
    if marker not in text:
        raise SystemExit(f'{path}: missing source heading {marker!r}')
    prefix = text.split(marker, 1)[0].rstrip() + '\n\n'
    path.write_text(prefix + new_tail, encoding='utf-8')

replace_tail(ES, 'Fuentes y notas de verificación', ES_TAIL)
replace_tail(PT, 'Fontes e notas de verificação', PT_TAIL)

en_text = EN.read_text(encoding='utf-8')
expected_urls = set(re.findall(r'https://[^\s)<>`]+', en_text))
if expected_urls != set(COMMON_URLS):
    missing = expected_urls - set(COMMON_URLS)
    extra = set(COMMON_URLS) - expected_urls
    raise SystemExit(f'Canonical URL inventory drift: missing={sorted(missing)} extra={sorted(extra)}')

for path in (ES, PT):
    text = path.read_text(encoding='utf-8')
    sections = len(re.findall(r'^##\s+.+$', text, re.M))
    urls = set(re.findall(r'https://[^\s)<>`]+', text))
    if sections != 21:
        raise SystemExit(f'{path}: expected 21 level-2 sections, found {sections}')
    if urls != expected_urls:
        raise SystemExit(f'{path}: source URL parity failed')

print('Guide 40 es-419 and pt-BR structural/source parity repair PASS')
