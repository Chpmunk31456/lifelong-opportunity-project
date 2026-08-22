# Guia de Oportunidades para Toda a Vida 92 — Técnico em Sistemas de Informação Geográfica

**Versão:** 2.0 — mestre de trabalho controlado  
**Idioma:** Português do Brasil (`pt-BR`)  
**Referência principal dos EUA:** O*NET-SOC 15-1299.02 — Geographic Information Systems Technologists and Technicians  
**Comparação do Canadá:** NOC 22214 — Technical occupations in geomatics and meteorology  
**Comparação da Colômbia:** CUOC 31123 — Técnicos en cartografía  
**Data de revisão:** 2026-08-22  
**Fonte inglesa congelada:** blob `5fc776670bc33d9e2b01a5dda8084a9099627165`

## O que é esta carreira

Um Técnico em Sistemas de Informação Geográfica (SIG/GIS) ajuda a coletar, organizar, validar, analisar, mapear e manter informação relacionada à localização. O trabalho pode envolver edição de camadas, manutenção de bases espaciais, digitalização, georreferenciamento, controle de geometrias e atributos, produção de mapas/relatórios, suporte a usuários, análise espacial, automação e publicação autorizada de mapas ou serviços web.

O título se sobrepõe a GIS Technologist, Geomatics Technician, Mapping Technician, Cartographic Technician e funções geoespaciais junior. Algumas vagas são principalmente de produção; outras envolvem mais análise, programação, banco de dados ou suporte. As funções reais importam mais do que o nome do cargo ou uma interface específica.

Nos Estados Unidos há uma ocupação direta em **O*NET-SOC 15-1299.02**. O Canadá usa **NOC 22214**, que inclui GIS Technician. Na Colômbia, **CUOC 31123 — Técnicos en cartografía** inclui explicitamente **Técnico sistemas de información geográfica**.

## Divulgação crítica das estatísticas dos EUA

O*NET informa explicitamente que salários e emprego de 15-1299.02 são coletados de **Computer Occupations, All Other**. São dados oficiais, mas não formam uma população salarial pura do título GIS Technician.

Isso é especialmente importante porque uma estimativa não governamental atual e específica do título GIS Technician é muito menor que a mediana crosswalk do O*NET. Não se deve calcular média entre os dois conjuntos; eles representam populações e metodologias diferentes.

## O que um técnico GIS faz

As tarefas atuais de O*NET apoiam atividades como:
- criar/atualizar camadas, mapas, tabelas e relatórios;
- manter bancos GIS;
- digitalizar/converter features;
- revisar atualidade, utilidade, qualidade e documentação;
- dar suporte a usuários/clientes;
- analisar relações espaciais;
- integrar dados espaciais e não espaciais;
- interpretar imagens aéreas/ortofotos;
- apoiar remote sensing/cartografia;
- desenvolver scripts/aplicações GIS quando atribuído;
- publicar/suportar produtos web GIS;
- documentar métodos e limitações.

Um mapa bonito pode estar errado se CRS, linhagem, atributos, geometria ou classificação estiverem errados.

## Modelos de dados espaciais

### Vetor
Dados vetoriais representam entidades discretas como:
- **pontos** — árvores, sensores, endereços ou ativos;
- **linhas** — estradas, rios, tubulações ou rotas;
- **polígonos** — lotes, zonas, lagos ou áreas de serviço.

Cada feature pode ter atributos em uma tabela.

### Raster
Raster usa células/pixels para imagem, elevação, temperatura, cobertura do solo e outras superfícies contínuas. Resolução e tamanho de célula importam. Ampliar um raster de baixa resolução não cria detalhe espacial verdadeiro.

### Atributos e bancos espaciais
Entenda tipos de campo, domínios/valores codificados, nulos, validação, joins/relates, identificadores, dicionários de dados, tabelas, chaves, índices, permissões, transações e workflows de versão/edição conforme o ambiente.

## Sistemas de referência de coordenadas

Erros de CRS podem invalidar trabalho aparentemente correto.

Distinga:
- sistemas geográficos com latitude/longitude;
- sistemas projetados com unidades lineares;
- datum e reference framework;
- projeção cartográfica;
- unidades;
- códigos EPSG conceitualmente;
- transformação/reprojeção.

Uma camada aparecer no lugar certo na tela não prova que sua metadata de CRS esteja correta. O software pode reprojetar dinamicamente apenas para visualização.

## Distorção e adequação da projeção

Toda projeção envolve tradeoffs. Área, forma, direção ou distância podem ser distorcidas.

Antes de medir, verifique finalidade, extensão geográfica, unidades e se a projeção preserva a propriedade relevante. Não reporte área/distância precisa em um CRS inadequado apenas porque o software retorna um número.

## Linhagem e metadata

Um dataset defensável deve preservar:
- fonte/proveniência;
- data/período de captura;
- organização responsável;
- precisão posicional;
- precisão dos atributos;
- completude;
- consistência lógica;
- escala/resolução;
- CRS e datum;
- transformações;
- processamento;
- histórico de edição;
- status autoritativo versus derivado;
- limitações conhecidas.

Se os dados forem transformados, generalizados, recortados, unidos, classificados ou derivados, documente o suficiente para compreender/reproduzir o resultado.

## Qualidade de dados

Qualidade é adequação ao objetivo. Verifique atributos ausentes/inválidos, duplicatas, valores impossíveis, dados obsoletos, unidades inconsistentes, CRS incompatíveis, defeitos geométricos, cobertura incompleta, códigos inconsistentes, conflitos de fonte e outliers.

Não “corrija” silenciosamente uma fonte autoritativa quando a ação correta é registrar e escalar ao proprietário dos dados.

## Geometria e topologia

Problemas comuns incluem self-intersections, duplicatas, anéis inválidos, overlaps, gaps, dangling lines, undershoots/overshoots, slivers, segmentos desconectados e snapping/tolerance inadequados.

Regras topológicas dependem do domínio. Ferramentas automáticas detectam condições, mas não definem todas as regras de negócio sem requisitos.

## Georreferenciamento

Fluxo defensável:
1. identificar imagem/mapa de origem e CRS alvo;
2. escolher control points confiáveis e distribuídos;
3. selecionar transformação apropriada;
4. revisar residual/error;
5. inspecionar resultado;
6. validar contra referências independentes quando possível;
7. documentar fonte, método, pontos e limitações.

Residual baixo não prova precisão real se os pontos de controle forem ruins.

## Digitalização

Use escala/zoom adequados, regras de snapping/tolerance, atributos consistentes, precisão compatível com a fonte, validação geométrica e documentação. Não crie falsa precisão rastreando uma fonte borrada em zoom extremo.

## Cartografia e comunicação

Mapas profissionais precisam de finalidade e audiência claras. Considere extensão, escala, simbologia, classificação, labels, legenda, título, fonte/data, unidades, incerteza, contraste, acessibilidade e alternativas textuais/tabulares.

Evite escolhas visuais enganosas, como símbolos excessivos, paletas dramáticas ou quebras de classe que exagerem diferenças.

## Métodos de classificação

Mapas coropléticos podem mudar de significado conforme equal interval, quantile, natural breaks ou faixas definidas pelo domínio. Inspecione distribuição, diferencie contagens de taxas, identifique outliers e documente o método quando ele afetar interpretação.

## Análise espacial

Pode incluir buffers, overlays/intersections, clipping, dissolve, proximity, spatial joins, network analysis, raster analysis e terrain/surface analysis. Verifique CRS, unidades, qualidade, premissas e parâmetros antes de interpretar resultados.

Um geoprocesso concluído sem erro pode ainda responder a pergunta errada.

## SQL e bancos espaciais

SQL pode apoiar consultas, joins, validação e operações espaciais. Use ambientes read-only/não produtivos para prática. Não execute updates destrutivos em dados autoritativos sem permissão, backup/change control e plano de validação.

## Python e automação

Python, ArcPy e outras abordagens podem automatizar geoprocessamento. Preserve inputs, parâmetros, versão do script, ambiente/software, outputs, warnings/errors e validações.

Automação escala erros tão rapidamente quanto acertos. Teste em subconjunto controlado antes de batch destrutivo ou amplo.

## Sinais tecnológicos atuais

O*NET/Lightcast 2025 mostra:
- ESRI ArcGIS **75%**;
- GIS systems **67%**;
- Python **34%**;
- SQL **22%**;
- GIS software **21%**;
- Microsoft Office **14%**;
- Excel **14%**;
- JavaScript **13%**;
- AutoCAD **10%**;
- ArcMap **7%**;
- QGIS **7%**;
- ArcGIS Survey123 **6%**;
- Access **6%**;
- PowerPoint **6%**;
- Azure **5%**;
- ArcPy **5%**;
- Outlook **5%**;
- AWS **5%**.

São sinais de vagas, não requisitos universais. CRS, qualidade, raciocínio espacial, linhagem e reproducibilidade são competências mais duráveis.

## Web GIS e compartilhamento

Web GIS pode envolver hosted layers, map/tile services, dashboards, web maps e permissões públicas/privadas.

Antes de publicar:
- confirme audiência;
- revise permissões;
- examine campos sensíveis;
- verifique se a precisão locacional é apropriada;
- revise dependências;
- documente owner/fonte;
- confira a visualização pública.

Uma camada pública pode revelar localização sensível mesmo com banco de dados privado.

## Privacidade e localizações sensíveis

Dados geoespaciais podem revelar residências/pessoas, clientes/ativos, infraestrutura crítica, rotas operacionais, recursos ambientais/culturais ou populações vulneráveis.

Use necessidade de acesso, publicação aprovada, agregação/generalização/redação, remoção de identificadores desnecessários, proteção de credenciais e escalonamento de incidentes.

Não publique coordenadas protegidas, camadas privadas ou infraestrutura crítica em mapas públicos, armazenamento pessoal, repositórios públicos ou IA não aprovada.

## Dados de campo e móveis

Considere segurança de dispositivo/conta, cópias offline, conflitos de sync, timestamps, precisão GPS, validação de formulários, fotos/anexos, informação pessoal, perda de dispositivo, retenção e autorização de upload.

Uma coordenada GPS não é automaticamente survey-grade.

## Versionamento e change control

Para dados autoritativos, saiba quem pode editar, aprovar ou publicar. Pode haver versioning, branch workflows, edit tracking ou tickets formais.

Acesso técnico de escrita não significa autoridade para alterar limites oficiais, lotes legais, utilidades ou outros datasets controlados.

## Limite com levantamento e registros legais

Trabalhar com dados de survey, parcelas, engenharia ou limites legais não cria autoridade profissional de levantamento. Não afirme survey-grade accuracy, altere limites legais ou certifique registros cadastrais sem autoridade e evidência. Encaminhe interpretação ao profissional autorizado.

## Remote sensing e imagens

Verifique data de aquisição, resolução, nuvens/obstruções, correção geométrica, CRS, método de classificação, referência/ground truth e incerteza.

Classificação automatizada deve ser validada antes de conclusões operacionais.

## IA responsável

IA aprovada pode ajudar com código, metadata, ideias de geoprocessamento, geocoding, feature extraction, classificação, documentação e dados sintéticos.

Controles:
- não enviar coordenadas protegidas, locations de clientes/ativos, camadas proprietárias, credenciais ou imagery restrita a ferramentas não aprovadas;
- validar código/lógica GIS;
- verificar CRS, unidades e premissas;
- identificar funções/pacotes inventados;
- avaliar bias/error de extração/classificação;
- preservar linhagem;
- não permitir que IA invente coordenadas autoritativas, limites legais ou precisão survey-grade;
- manter validação humana/de domínio.

Output de IA não é prova de execução geoespacial correta.

## Acessibilidade

Use fontes legíveis, contraste suficiente, codificação não baseada apenas em cor, labels/legendas claros, formas/padrões quando úteis, contexto/alt text em mapas estáticos, alternativas de texto/tabela e controles web acessíveis por teclado quando possível.

Scanner automático não prova conformidade legal.

## Estados Unidos — educação e workforce

O*NET 15-1299.02 é uma ocupação GIS direta, mas requisitos variam. Rotas podem incluir GIS/geospatial technology, geografia, ciência ambiental, planning, informática, surveying/mapping e áreas relacionadas.

CareerOneStop/American Job Centers ajuda a investigar WIOA e recursos locais. Elegibilidade/financiamento variam; o locator não garante pagamento.

## Estados Unidos — salários e perspectiva oficiais crosswalk

O*NET usa **Computer Occupations, All Other** para os dados oficiais 2025:

| Percentil | Anual | Por hora |
|---|---:|---:|
| 10 | $55,940 | $26.89 |
| 25 | $79,370 | $38.16 |
| Mediana | $116,580 | $56.05 |
| 75 | $157,500 | $75.72 |
| 90 | $188,470 | $90.61 |

Perspectiva 2024–2034, também crosswalk:
- emprego 2024: **472,000**;
- projetado 2034: **510,500**;
- crescimento: **8%**;
- aberturas anuais: **31,300**.

São oficiais, mas não representam população pura do título GIS Technician.

### Contexto específico do título e não governamental

Indeed, atualizado em **2 de agosto de 2026**, mostra para **GIS Technician** aproximadamente:
- **$25.88/hora média**;
- **$17.60/hora baixa**;
- **$38.06/hora alta**;
- **749** observações;
- **36 meses**.

A diferença em relação ao O*NET vem de populações/metodologias diferentes. Não faça média entre os conjuntos nem trate um como correção exata do outro.

## Canadá

Job Bank mapeia GIS Technician diretamente a **NOC 22214**.

Salários nacionais:
- **C$23.08/hora** baixo;
- **C$38.10/hora** mediano;
- **C$53.85/hora** alto.

A preparação pode envolver college em geomatics, cartography, photogrammetry, aerial survey, remote sensing, GIS ou formação relacionada. O perfil atual exige conclusão do ensino médio.

Em Quebec, Job Bank informa membership no órgão regulatório para uso do título **Professional Technologist**. Trate como requisito de título/status profissional e não como afirmação de que toda atividade GIS no Canadá é regulada da mesma forma.

### Perspectiva do Canadá

A projeção nacional 2024–2033 para NOC 22214 indica **strong risk of labour surplus**. Perspectivas de três anos variam e são Limited ou Moderate em muitas regiões. Verifique a província/território alvo.

## Colômbia

**CUOC 31123 — Técnicos en cartografía**, nível de competência 3, inclui explicitamente **Técnico sistemas de información geográfica**.

Funções incluem apoio a conteúdo/desenho de mapas, coleta a partir de fotografias aéreas/registros/mapas, produção digital, controle de completude/precisão, interpretação aérea, sistemas cartográficos digitais e remote sensing.

Não fabrique salário nacional representativo quando a metodologia de indicadores históricos não sustenta essa conclusão.

## Colômbia — rotas SENA

### Introducción a los Sistemas de Información Geográfica
- curso especial/complementar;
- **80 horas**;
- ofertas presenciais atuais;
- competência de operar SIG segundo necessidades do usuário.

### Sistemas de Información Geográfica
- curso especial complementar;
- **48 horas**;
- ofertas presenciais 2026;
- alguns cohorts exigem conhecimentos básicos.

### Aplicación de SIG en Sistemas Forestales y Agroecológicos
- formação complementar virtual;
- **48 horas**;
- estrutura/captura/gestão/avaliação/qualidade de dados espaciais para projetos florestais/agroecológicos.

São rotas úteis, porém suplementares. Confirme centro, modalidade, pré-requisitos, datas e vagas.

## América Latina e Caribe

OIT/Cinterfor ajuda a localizar instituições nacionais de formação profissional. Não garante curso GIS, vaga, financiamento ou admissão.

## Portfólio seguro

Use dados públicos/abertos, dados pessoais coletados legalmente ou sintéticos. Exemplos:
- mapa temático com fonte/CRS documentados;
- georreferenciamento com imagem não sensível;
- QA/topologia vetorial;
- SQL/Python espacial em open data;
- mapa acessível com alternativa texto/tabela;
- metadata/linhagem;
- mapa sintético de inspeção de ativos;
- exercício de sharing web com dados não sensíveis.

Nunca publique camadas protegidas de empregadores/clientes, endereços privados, infraestrutura crítica exata, locais culturais/ambientais restritos ou schemas proprietários.

## Plano inicial de quatro semanas

### Semana 1 — fundamentos espaciais
Vetor/raster/atributos, CRS, datums, projeções e metadata. Carregue open data e inspecione CRS/fonte.

### Semana 2 — edição e qualidade
Digitalização, atributos, geometry/topology, joins, georreferenciamento e cartografia. Documente mudanças.

### Semana 3 — análise e automação
Buffers, overlays, spatial joins e um workflow SQL/Python reproducível. Verifique unidades, CRS e parâmetros.

### Semana 4 — comunicação e portfólio
Crie mapa/relatório seguro, documente fontes/limitações, adicione alternativa acessível, revise sharing e prepare exemplos de julgamento de qualidade.

## Preparação para entrevistas

Explique vetor versus raster; CRS geográfico versus projetado; datum/reprojeção; por que visualização correta não prova CRS correto; erros topológicos; validação de georreferenciamento; linhagem/metadata; escolhas de classificação; proteção de localizações; validação de scripts/IA; e por que GIS não implica precisão topográfica/legal.

## Perguntas ao empregador

- Quais plataformas e bancos GIS são usados?
- O papel é produção, análise, gestão, suporte ou desenvolvimento?
- Quais layers são autoritativos?
- Quem aprova mudanças oficiais?
- Quais CRS/datums são padrão?
- Quais regras de QA/topologia se aplicam?
- Há field data?
- Como localizações sensíveis são protegidas?
- Existem layers públicos?
- SQL/scripting é esperado?
- Que training é oferecido?
- Quais responsabilidades survey/legal ficam fora do cargo?

## Links de verificação para leitores

1. https://www.onetonline.org/link/details/15-1299.02
2. https://www.onetonline.org/link/summary/15-1299.02
3. https://www.onetonline.org/link/localwages/15-1299.02
4. https://www.onetonline.org/link/localtrends/15-1299.02
5. https://www.onetonline.org/link/demand/15-1299.02
6. https://www.indeed.com/career/gis-technician/salaries
7. https://www.careeronestop.org/LocalHelp/EmploymentAndTraining/find-WIOA-training-programs.aspx
8. https://www.jobbank.gc.ca/marketreport/summary-occupation/3493/ca
9. https://www.jobbank.gc.ca/marketreport/wages-occupation/3493/ca
10. https://www.jobbank.gc.ca/marketreport/requirements/3493/AB
11. https://www.jobbank.gc.ca/marketreport/outlook-occupation/3493/ca
12. https://www.canada.ca/en/services/jobs/training.html
13. https://ocupacol.mintrabajo.gov.co/Profile/OccupationalProfile/31123
14. https://betowa.sena.edu.co/oferta/introduccion-a-los-sistemas-de-informacion-geografica?modality=P&offertype=company&programId=85021
15. https://betowa.sena.edu.co/oferta/sistemas-de-informacion-geografica?modality=P&offertype=company&programId=164857
16. https://betowa.sena.edu.co/oferta/aplicacion-de-sig-en-sistemas-forestales-y-agroecologicos?modality=V&programId=173415
17. https://www.oitcinterfor.org/statsfp/paises
18. https://www.nist.gov/privacy-framework
19. https://www.nist.gov/itl/ai-risk-management-framework
20. https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
21. https://www.cisa.gov/secure-our-world
22. https://www.section508.gov/create/
23. https://www.w3.org/TR/WCAG22/

## Limites importantes

Este guia fornece informação educacional e de planejamento profissional. Não garante emprego, remuneração, admissão, financiamento, disponibilidade de cursos, status profissional ou promoção. Não constitui certificação legal, topográfica, cadastral, de privacidade, cibersegurança, precisão geoespacial ou acessibilidade. Os dados salariais/de emprego do O*NET são crosswalk de **Computer Occupations, All Other** e não são apresentados como população pura de GIS Technician. As edições linguísticas são localizações controladas, não traduções certificadas.
