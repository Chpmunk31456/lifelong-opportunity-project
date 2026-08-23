# Guia de Oportunidades para Toda a Vida 88 — Desenvolvedor Web

**Versão:** 2.0 — mestre de trabalho controlado  
**Idioma:** Português do Brasil (`pt-BR`)  
**Referência principal dos EUA:** O*NET-SOC 15-1254.00 — Web Developers  
**Comparação do Canadá:** NOC 21234 — Web developers and programmers  
**Comparação da Colômbia:** CUOC 25130 — Desarrolladores Web y multimedia  
**Data de revisão:** 2026-08-22  
**Fonte inglesa congelada:** blob `a25d99dc19dcc0ed795ea9e55be20d95101ef1e2`

## O que é esta carreira

Um desenvolvedor web cria, modifica e mantém sites e aplicações web. Dependendo da função, pode trabalhar com interfaces no navegador, layouts responsivos, lógica do lado do cliente, serviços de servidor, APIs, bancos de dados, autenticação, desempenho, testes, implantação, acessibilidade e suporte de produção.

O título é amplo. Um desenvolvedor front-end costuma se concentrar mais na experiência no navegador. Um desenvolvedor back-end pode trabalhar principalmente com lógica de servidor, APIs e dados. Um desenvolvedor full-stack pode atuar em várias camadas. Outros cargos se concentram em CMS, comércio eletrônico ou integrações de plataformas.

Nos Estados Unidos há uma correspondência direta em **O*NET-SOC 15-1254.00 — Web Developers**, Bright Outlook e atualizada em 2026. O Canadá usa **NOC 21234 — Web developers and programmers**. Na Colômbia existe uma correspondência direta em **CUOC 25130 — Desarrolladores Web y multimedia**.

## Por que desenvolvimento web continua relevante

Sistemas web sustentam comércio, bancos, saúde, educação, governo, mídia, portais internos, software como serviço e identidade. Ferramentas mudam rapidamente, mas continuam valiosas habilidades como entender requisitos, escrever código sustentável, integrar APIs e dados, testar comportamento, proteger credenciais, construir interfaces acessíveis e usar controle de versão.

## Famílias de funções

### Front-end
Pode trabalhar com HTML, CSS, JavaScript/TypeScript, design responsivo, APIs do navegador, acessibilidade, desempenho e frameworks como React, Angular ou Vue.

### Back-end
Pode trabalhar com código de servidor, APIs, autenticação/autorização, bancos de dados, filas, cache, logging, integrações e implantação.

### Full-stack
Combina várias camadas. Não significa ser especialista em toda tecnologia existente.

### CMS e comércio eletrônico
Pode trabalhar com WordPress, Shopify ou outras plataformas, templates, plugins, conteúdo, integrações e manutenção.

## Fundamentos da web

Aprenda:

- HTML semântico;
- CSS e design responsivo;
- JavaScript;
- DOM e eventos;
- formulários;
- URLs;
- HTTP;
- cookies/sessões;
- JSON;
- APIs;
- acessibilidade;
- Git;
- fundamentos de segurança e privacidade.

## HTML semântico

Use elementos conforme seu significado, não apenas a aparência. Uma boa estrutura melhora manutenção, navegação por teclado, interpretação por leitores de tela, formulários e testes. Prefira controles nativos quando atendem ao requisito; componentes personalizados podem exigir trabalho adicional de teclado, foco e acessibilidade.

## CSS e design responsivo

Entenda cascade, especificidade, box model, Flexbox, Grid, unidades, media/container queries quando apropriadas, imagens responsivas, tipografia, contraste, foco visível, reduced motion e reflow.

Não presuma que uma página é responsiva porque parece correta em um telefone e um monitor. Teste faixas de viewport e estados reais do conteúdo.

## JavaScript e TypeScript

Sinais atuais do O*NET mostram **JavaScript 47%** e **TypeScript 22%**. Fundamentos úteis incluem variáveis, funções, objetos, arrays, módulos, promises, async/await, tratamento de erros, eventos, DOM, network requests, estado, debugging e testes.

TypeScript pode melhorar a manutenção, mas não substitui validação em runtime nem controles de segurança.

## Tecnologias atuais

As vagas associadas ao O*NET em 2025 mostram:

- JavaScript **47%**;
- React **35%**;
- CSS **33%**;
- AWS **27%**;
- HTML **26%**;
- RESTful API **24%**;
- Java **23%**;
- TypeScript e Git **22%**;
- Python e SQL **21%**;
- Node.js e Angular **18%**;
- Docker e Azure **16%**;
- Kubernetes **15%**;
- PostgreSQL **12%**;
- MySQL, PHP e GitHub **10%**;
- Vue.js **9%**;
- GraphQL **8%**;
- Jenkins CI **7%**;
- WordPress e MongoDB **6%**;
- JIRA, JSON e Linux **5%**.

Esses números são sinais do mercado, não requisitos universais.

## HTTP e APIs

Entenda métodos GET/POST/PUT/PATCH/DELETE, códigos de status, headers, content types, tokens, cache, paginação, rate limits, timeouts, retries, idempotência quando relevante e CORS em nível conceitual.

Nunca exponha segredos no código do navegador. Usuários podem inspecionar o código e as requisições de rede.

## Autenticação versus autorização

- **Autenticação:** quem é a pessoa?
- **Autorização:** o que ela pode fazer?

Ocultar um botão na interface não substitui autorização no servidor. Um usuário autenticado não deve automaticamente receber acesso a todos os objetos ou ações administrativas.

## Sessões, cookies e tokens

Siga a arquitetura aprovada para cookies, tokens, expiração, revogação, CSRF quando aplicável e scopes mínimos. Evite segredos em URLs e logs. Não invente uma nova arquitetura de segurança quando a organização já tiver padrões definidos.

## Desenvolvimento no servidor

Pode incluir routing, validação, regras de negócio, acesso a dados, background jobs, cache, integrações, arquivos, autenticação/autorização, logging e tratamento de erros. Valide entradas não confiáveis no servidor; validação no cliente melhora UX, mas não é fronteira de segurança.

## Bancos de dados e SQL

Conceitos úteis:

- tabelas/documentos;
- chaves e relacionamentos;
- índices;
- transações;
- restrições;
- queries parametrizadas;
- migrations;
- conexões;
- responsabilidade por backup/recovery.

### Limite de SQL injection

Não concatene input não confiável diretamente em consultas. Use prepared statements/queries parametrizadas ou ORM aprovado. Validação de entrada não substitui construção segura de consultas.

## Git e colaboração

Use branches, commits, diffs, pull/merge requests, reviews e resolução de conflitos conforme a prática da equipe. Nunca faça commit de senhas, API keys, certificados privados ou outros segredos. Se um segredo entrar no histórico, siga o processo de rotação/incidente.

## Testes

Podem incluir testes unitários, componentes, integração, API, end-to-end, acessibilidade, compatibilidade e desempenho. Testes de segurança requerem autorização.

Uma suíte aprovada é evidência; não prova por si só que a aplicação seja segura, legalmente acessível ou livre de defeitos.

## Acessibilidade

Considere:

- HTML semântico;
- teclado;
- foco visível;
- rótulos;
- mensagens de erro;
- contraste;
- zoom/reflow;
- comunicação não baseada somente em cor;
- alt text;
- alternativas para mídia;
- compatibilidade com leitores de tela.

Ferramentas automáticas detectam apenas parte dos problemas. Um PASS automatizado não estabelece conformidade legal.

## Desempenho

Fatores relevantes incluem tamanho de payload, imagens, fontes, execução JavaScript, rendering, latência, cache, queries, APIs, capacidade do servidor, CDN e lazy loading.

Core Web Vitals podem ser sinais úteis, mas nenhuma métrica garante ranking, conversão ou receita.

## Logging e monitoramento

Trate erros sem expor informações internas. Use logs estruturados, IDs de correlação quando adequados, monitoramento e alertas, protegendo dados sensíveis. Não registre senhas, tokens, dados completos de pagamento ou informações pessoais desnecessárias.

## Segredos e configuração

Não coloque no código-fonte senhas de banco de dados, private API keys, signing keys, OAuth client secrets, cloud credentials ou certificados privados. Use sistemas aprovados de segredos/configuração.

Um arquivo `.env` não é automaticamente seguro; respeite regras de ignore e gestão de segredos.

## Dependências

Dependências de terceiros aumentam risco de supply chain. Minimize pacotes desnecessários, acompanhe advisories, atualize versões suportadas, revise licenças quando necessário, evite pacotes abandonados e teste atualizações antes de produção.

## Implantação e rollback

Defina versão, ambiente, testes, migrations, monitoramento, rollback/forward-fix e autoridade de release. Não implante diretamente em produção apenas porque possui acesso técnico.

## Cloud e responsabilidade compartilhada

AWS e Azure aparecem com frequência nas vagas atuais. Serviços gerenciados não transferem automaticamente todas as responsabilidades de aplicação, identidade, dados, configuração e código ao provedor. Siga o modelo de responsabilidade compartilhada e a arquitetura da organização.

## Privacidade e minimização de dados

Colete e retenha apenas os dados necessários para finalidades aprovadas. Siga regras sobre informação pessoal, consentimento/preferências quando aplicável, analytics, cookies/tracking, retenção, exclusão, exports e dados de teste. Questões jurídicas/de privacidade devem ser escaladas ao responsável adequado.

## Desenvolvimento seguro

Práticas relevantes podem incluir validação no servidor, output encoding, queries parametrizadas, autenticação/autorização, session protections, secrets management, dependency management, configuração segura, logging e security review.

NIST SSDF e OWASP são referências úteis. Não dão autorização para penetration testing. Scanning intrusivo, exploração ou testes destrutivos exigem escopo e permissão explícitos.

## IA responsável

IA pode ajudar, quando a política permitir, com explicação de código, drafting, refactoring, testes, dados sintéticos, documentação e debugging.

Não envie código proprietário, dados de clientes, segredos, credenciais ou informação não publicada para ferramentas não aprovadas. Revise e teste código gerado. Verifique pacotes/APIs, licenças e padrões de segurança. Não permita deployment autônomo para produção fora da governança.

## Limites éticos e profissionais

Um desenvolvedor web não deve:

- implantar sem autoridade;
- ocultar defeitos críticos conhecidos;
- colocar segredos em repositórios públicos;
- contornar autenticação/autorização para cumprir prazo;
- usar dados de produção em demos pessoais;
- executar testes de segurança sem autorização;
- afirmar segurança, acessibilidade ou ausência de bugs apenas porque os testes passaram;
- garantir ranking SEO, receita ou conversão;
- publicar código ou arquitetura privada do empregador.

## Educação e entrada — Estados Unidos

O*NET coloca Web Developers em **Job Zone Three — Medium Preparation Needed**. É comum encontrar formação vocacional/técnica, experiência relacionada ou associate degree, embora os empregadores variem.

CareerOneStop/American Job Centers ajudam a localizar treinamento e WIOA. Elegibilidade e financiamento não são automáticos. Apprenticeship.gov pode ser usado para procurar oportunidades atuais; nenhuma vaga é garantida.

## Canadá

Job Bank usa **NOC 21234**. Requisitos típicos incluem bachelor’s degree em computação/programação/web/software engineering **ou** college program relacionado; experiência em programação costuma ser necessária.

Job Bank identifica atualmente a ocupação como **não regulamentada no Canadá**.

### Salários no Canadá

- **C$21.48/hora** baixo;
- **C$38.46/hora** mediano;
- **C$57.16/hora** alto.

### Perspectiva no Canadá

O panorama nacional 2024–2033 indica demanda e oferta amplamente equilibradas. As perspectivas de três anos variam por província/território; consulte a região específica.

## Colômbia

**CUOC 25130 — Desarrolladores Web y multimedia** é uma correspondência direta de nível de competência 4.

Não se fabrica um salário nacional representativo porque os indicadores disponíveis não permitem uma afirmação estatisticamente sólida.

### Rotas SENA

**Análisis y desarrollo de software**  
- Tecnólogo;
- **3.984 horas**;
- formação ampla em requisitos, design, desenvolvimento, implementação e qualidade;
- disponibilidade/vagas/modalidade variam.

**Desarrollo web con PHP**  
- complementar virtual;
- **40 horas**;
- requer conhecimentos prévios de programação/HTML;
- treinamento suplementar.

O curso de 40 horas não equivale ao Tecnólogo de 3.984 horas.

## América Latina e Caribe

OIT/Cinterfor funciona como localizador regional de instituições de formação profissional. Não garante cursos, bolsas, financiamento ou vagas.

## Renda e perspectiva atual

### Estados Unidos — dados oficiais

| Percentil | Anual | Por hora |
|---|---:|---:|
| 10 | $48,100 | $23.12 |
| 25 | $64,230 | $30.88 |
| Mediana | $92,650 | $44.54 |
| 75 | $126,230 | $60.69 |
| 90 | $162,290 | $78.03 |

Perspectiva 2024–2034:

- emprego 2024: **86,000**;
- projetado 2034: **92,500**;
- crescimento: **8%**;
- aberturas anuais: **5,400**.

### Contexto de mercado não governamental

Indeed, atualizado em **2 de agosto de 2026**, informa aproximadamente:

- média **$86,333/ano**;
- baixa **$50,037/ano**;
- alta **$148,958/ano**;
- cerca de **1.4 mil** observações;
- **36 meses** de vagas;
- contexto de bônus em dinheiro **$2,500/ano**.

É uma estimativa de mercado específica do título, não estatística oficial.

## Sequência prática de aprendizagem

1. Fundamentos do navegador: HTML, CSS, JavaScript, acessibilidade e Git.
2. Aplicação: framework, formulários, estado, APIs, validação e testes.
3. Servidor/dados: um stack server-side, SQL, autenticação/autorização e queries seguras.
4. Delivery: CI/CD, configuração, logging, monitoramento, deploy e rollback.
5. Especialização: front end, back end, full stack, CMS/e-commerce, acessibilidade, performance, cloud ou secure development.

## Portfólio seguro

Use sistemas próprios, open source ou demo e dados sintéticos/públicos. Pode demonstrar UI responsiva/semântica, APIs, autenticação demo, CRUD com queries parametrizadas, testes, Git, README, CI e deployment demo controlado.

Não publique código de empregadores, dados reais de clientes, credenciais, internal URLs, arquitetura privada ou vulnerabilidades sem autorização.

## Plano de quatro semanas

### Semana 1
Construa um site responsivo multipágina com HTML/CSS e teste teclado e viewports.

### Semana 2
Adicione JavaScript, validação, uma API pública/demo e estados de loading/error.

### Semana 3
Adicione um servidor/API e um pequeno banco de dados com queries parametrizadas e configuração segura.

### Semana 4
Adicione testes, README, notas de acessibilidade/performance, histórico Git e um deployment demo controlado.

## Títulos para busca

- Web Developer;
- Junior Web Developer;
- Front-End Developer;
- Back-End Web Developer;
- Full-Stack Developer;
- Web Application Developer;
- JavaScript Developer;
- React Developer;
- WordPress Developer;
- PHP Developer;
- UI Developer;
- E-commerce Developer.

## Perguntas antes de aceitar uma vaga

- A função é front end, back end, full stack ou CMS/e-commerce?
- Quais frameworks/linguagens são usados diariamente?
- Quem decide arquitetura e segurança?
- Como funcionam code review e CI/CD?
- Como mudanças chegam à produção?
- Como segredos e configuração são gerenciados?
- Como acessibilidade é verificada?
- Quais testes são esperados do desenvolvedor?
- Há on-call ou implantações fora de horário?
- O que diferencia júnior de sênior?

## Fontes e links de verificação

### Estados Unidos
- O*NET details: https://www.onetonline.org/link/details/15-1254.00
- O*NET summary: https://www.onetonline.org/link/summary/15-1254.00
- O*NET Job Zone: https://www.onetonline.org/skills/zone/15-1254.00
- O*NET wages: https://www.onetonline.org/link/localwages/15-1254.00
- O*NET outlook: https://www.onetonline.org/link/localtrends/15-1254.00
- O*NET technologies: https://www.onetonline.org/link/demand/15-1254.00
- CareerOneStop WIOA: https://www.careeronestop.org/LocalHelp/EmploymentAndTraining/find-WIOA-training-programs.aspx
- Apprenticeship.gov: https://www.apprenticeship.gov/
- Indeed: https://www.indeed.com/career/web-developer/salaries

### Canadá
- Job Bank summary: https://www.jobbank.gc.ca/marketreport/summary-occupation/17892/ca
- Job Bank requirements: https://www.jobbank.gc.ca/marketreport/requirements/17892/ca
- Job Bank wages: https://www.jobbank.gc.ca/marketreport/wages-occupation/17892/ca
- Job Bank outlook: https://www.jobbank.gc.ca/marketreport/outlook-occupation/17892/ca
- Canada training: https://www.canada.ca/en/services/jobs/training.html

### Colômbia e América Latina
- CUOC 25130: https://ocupacol.mintrabajo.gov.co/Profile/OccupationalProfile/25130
- SENA Análisis y desarrollo de software: https://betowa.sena.edu.co/oferta/analisis-y-desarrollo-de-software
- SENA Desarrollo web con PHP: https://betowa.sena.edu.co/oferta/desarrollo-web-con-php?modality=V&offertype=company
- OIT/Cinterfor: https://www.oitcinterfor.org/statsfp/paises

### Segurança, IA e acessibilidade
- NIST SSDF: https://csrc.nist.gov/pubs/sp/800/218/final
- OWASP WSTG: https://owasp.org/www-project-web-security-testing-guide/
- NIST AI RMF: https://www.nist.gov/itl/ai-risk-management-framework
- Section 508: https://www.section508.gov/create/
- WCAG 2.2: https://www.w3.org/TR/WCAG22/

## Aviso importante

Este guia fornece informação geral de educação e planejamento de carreira. Não garante emprego, renda, admissão, financiamento, apprenticeship, certificação, promoção, ranking, receita, conversão, segurança ou conformidade de acessibilidade.

Não se declara certificação humana independente, acreditação profissional, revisão jurídica, avaliação de segurança, certificação de acessibilidade, certificação cloud/vendor ou tradução certificada, salvo documentação separada.

## Autor e assistência de IA

Criado e dirigido por **Alberto “Al” Leiva**. O ChatGPT apoiou pesquisa, organização, edição, suporte à tradução e preparação de documentos sob direção do autor. O autor permanece responsável pelas decisões editoriais e de publicação.

## Licença

Salvo indicação contrária, este material é licenciado sob **CC BY-NC-SA 4.0**.
