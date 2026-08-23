# Guia de Oportunidades para Toda a Vida 85 — Analista de Dados

**Versão:** 2.0 — mestre de trabalho controlado  
**Idioma:** Português do Brasil (`pt-BR`)  
**Referência quantitativa principal dos EUA:** O*NET-SOC 15-2041.00 — Statisticians  
**Referência adjacente dos EUA:** O*NET-SOC 15-2051.01 — Business Intelligence Analysts  
**Comparação do Canadá:** NOC 21223 — Database analysts and data administrators  
**Comparações da Colômbia:** CUOC 25210, CUOC 25110 e CUOC 21200, selecionadas conforme as funções da vaga  
**Data de revisão:** 2026-08-21  
**Fonte inglesa congelada:** blob `6139ca58f49692ef57556c3fd593e6d8b6d33f8b`

## O que é esta carreira

Um analista de dados transforma perguntas em evidências. O trabalho normalmente envolve localizar dados relevantes, compreender o significado de cada campo e de cada linha, limpar e validar informações, analisar padrões, testar hipóteses, criar tabelas ou visualizações compreensíveis e explicar o que os dados sustentam — e o que não sustentam.

O título **Analista de Dados** é muito amplo. Algumas vagas se aproximam de business intelligence e relatórios. Outras se relacionam mais com bancos de dados, pesquisa operacional, estatística, finanças, analytics de marketing, qualidade, fraude, políticas públicas, saúde, cibersegurança, cadeia de suprimentos, pesquisa ou analytics de produto. Por isso, este guia não finge que um único código ocupacional oficial representa perfeitamente todas as vagas chamadas Data Analyst.

Para comparações controladas do mercado de trabalho, este guia usa **O*NET-SOC 15-2041.00 — Statisticians** como principal referência quantitativa dos Estados Unidos porque suas funções oficiais incluem preparação de dados, análise estatística, identificação de tendências, elaboração de relatórios e avaliação da qualidade dos dados, e porque o O*NET lista títulos de aprendizagem aprovados como Data Analyst e Junior Data Analyst. Entretanto, a referência de Statisticians é matematicamente mais avançada e mais concentrada em formação de pós-graduação do que muitas vagas comerciais de Data Analyst de nível inicial. Essa limitação deve permanecer visível sempre que salários, educação ou perspectivas oficiais forem apresentados.

O Guia 84 trata Business Intelligence Analyst em mais profundidade. As duas carreiras se sobrepõem, mas não são intercambiáveis.

## Por que análise de dados pode ser uma boa oportunidade

Organizações coletam dados em quase todas as funções, incluindo:

- vendas;
- atendimento ao cliente;
- marketing;
- finanças;
- contabilidade;
- operações;
- logística;
- cadeia de suprimentos;
- qualidade;
- saúde;
- educação;
- governo;
- cibersegurança;
- recursos humanos;
- manufatura;
- transporte;
- programas sem fins lucrativos;
- pesquisa científica e social.

Dados só geram valor quando alguém consegue convertê-los em informação confiável. Um bom analista combina habilidades técnicas com julgamento, documentação e comunicação.

É possível migrar para análise de dados a partir de:

- trabalhos administrativos com muitos relatórios ou planilhas;
- operações de negócios;
- suporte financeiro ou contábil;
- operações de atendimento;
- suporte de TI;
- bancos de dados ou gestão de registros;
- garantia da qualidade;
- marketing;
- logística;
- assistência de pesquisa;
- suporte técnico ou de engenharia;
- estatística ou matemática;
- programação ou suporte de software.

Uma progressão possível é:

**assistente de dados/relatórios → analista de dados júnior → analista de dados → analista sênior → líder de analytics, analista de BI, engenheiro de analytics, engenheiro de dados, cientista de dados, analista de produto, analista de operações, analista de risco ou função de gestão.**

O caminho exato depende da profundidade técnica, do conhecimento do setor, da formação, das expectativas do empregador e da capacidade demonstrada de produzir análises confiáveis.

## Analista de Dados não é um único tipo de trabalho

### Analista orientado a relatórios

Pode se concentrar em:

- relatórios recorrentes;
- planilhas;
- acompanhamento de KPI;
- dashboards;
- SQL simples;
- reconciliação;
- resumos operacionais.

### Analista de negócios ou operações com ênfase em dados

Pode se concentrar em:

- métricas de processos;
- investigação de causa raiz;
- análise de custos ou produtividade;
- níveis de serviço;
- apoio a previsões;
- recomendações para partes interessadas.

### Analista estatístico ou de pesquisa

Pode usar:

- amostragem;
- probabilidade;
- inferência estatística;
- regressão;
- métodos experimentais ou de pesquisa;
- R, Python, SAS ou SPSS;
- documentação formal de pesquisa.

### Analista orientado a banco de dados ou gestão de dados

Pode trabalhar mais profundamente com:

- modelos de dados;
- estruturas de banco de dados;
- SQL;
- data warehouses;
- qualidade de dados;
- governança de dados;
- dicionários de dados;
- controles de acesso.

### Analista de produto, marketing, finanças, risco ou cibersegurança

Aplica os mesmos princípios analíticos dentro de um domínio especializado. O conhecimento do setor pode ser tão importante quanto as ferramentas.

Leia sempre a descrição real da vaga; não presuma que o título revela todo o nível técnico.

## Primeira regra: defina a pergunta antes de tocar nos dados

Uma análise fraca costuma começar com um conjunto de dados e perguntar: “O que consigo encontrar?”. Uma análise sólida começa com uma decisão ou pergunta.

Antes de criar uma consulta, fórmula ou gráfico, esclareça:

1. Qual pergunta estamos tentando responder?
2. Qual decisão esta análise apoiará?
3. Quem é o público?
4. Qual população ou processo está no escopo?
5. Qual período é relevante?
6. O que uma linha representa?
7. Qual fonte de dados é autoritativa?
8. Quais regras de negócio, filtros e exclusões se aplicam?
9. Qual nível de precisão é necessário?
10. Que incerteza ou limitação deve ser declarada?
11. Quem tem autorização para acessar os dados e o resultado?
12. Como a saída será validada?

Se a pergunta estiver vaga, escreva uma versão testável antes de continuar.

## Fonte, linhagem e granularidade dos dados

Todo resultado importante deve ser rastreável à sua origem.

Documente, quando aplicável:

- sistema de origem;
- tabela, arquivo, API ou relatório;
- data/hora da extração;
- proprietário ou responsável;
- frequência de atualização;
- definições dos campos;
- granularidade da linha;
- transformações;
- joins;
- filtros;
- exclusões;
- campos derivados;
- regras de cálculo;
- versão da saída;
- correções ou histórico de mudanças.

### Granularidade

Granularidade significa o que cada linha representa.

Uma linha pode representar:

- um cliente;
- um pedido;
- uma linha de pedido;
- um chamado de suporte;
- um funcionário-mês;
- uma leitura de máquina;
- um pagamento;
- uma resposta de pesquisa.

Unir tabelas com granularidades incompatíveis pode multiplicar linhas e inflar totais. Antes de cada join importante, pergunte:

- A chave é única?
- A relação é um-para-um, um-para-muitos ou muitos-para-muitos?
- O que acontece com linhas sem correspondência?
- O join pode duplicar medidas?
- Devo agregar antes de unir?

## Habilidades com planilhas

Planilhas continuam comuns em trabalhos de análise. Habilidades úteis incluem:

- ordenar e filtrar;
- tabelas;
- referências relativas e absolutas;
- `SUM`, `AVERAGE`, `COUNT`, `COUNTIF(S)`, `SUMIF(S)`;
- funções de procura;
- funções de texto e data;
- funções lógicas;
- tabelas dinâmicas;
- gráficos;
- formatação condicional;
- validação de dados;
- importação/exportação;
- verificação de erros;
- intervalos protegidos e disciplina de acesso;
- Power Query ou ferramentas equivalentes de transformação, quando disponíveis.

Uma planilha não é automaticamente um sistema analítico confiável. Trabalhos importantes devem evitar alterações manuais sem documentação, fórmulas ocultas, totais codificados manualmente, valores copiados sem explicação e versões sem controle.

## SQL

SQL é uma das habilidades mais transferíveis para um analista.

Conceitos fundamentais incluem:

- `SELECT`;
- filtros com `WHERE`;
- ordenação;
- agregação;
- `GROUP BY`;
- joins;
- lógica `CASE`;
- common table expressions;
- subconsultas;
- funções de janela;
- lógica de data/hora;
- tratamento de nulos;
- deduplicação;
- validação da contagem de linhas.

Uma consulta não está correta apenas porque executa sem erro.

Valide consultas importantes verificando:

- contagens esperadas de linhas;
- chaves duplicadas;
- registros de amostra conhecidos;
- totais contra um relatório autoritativo;
- limites de datas;
- nulos e categorias ausentes;
- efeitos dos joins;
- filtros e exclusões;
- conversões de unidades;
- valores inesperados.

## Python, R e ferramentas estatísticas

Algumas funções de analista usam programação para análise reproduzível. Os sinais atuais de vagas do O*NET para a referência de Statisticians mostram forte demanda por R, SAS, Python e SQL, embora essa referência seja mais estatística do que muitas vagas gerais de Data Analyst.

Capacidades úteis podem incluir:

- importar dados;
- limpar e remodelar;
- agrupar e agregar;
- unir conjuntos de dados;
- estatística descritiva;
- visualização;
- notebooks ou scripts reproduzíveis;
- testes estatísticos simples;
- validação;
- exportação de resultados controlados.

Não tente aprender todas as linguagens de uma vez. Para muitas pessoas, uma sequência prática é:

1. fundamentos de planilhas;
2. SQL;
3. visualização;
4. uma linguagem de script como Python ou R;
5. estatística mais profunda conforme aumentam as exigências da função.

## Limpeza de dados

Tarefas comuns incluem:

- padronizar categorias;
- corrigir mapeamentos aprovados;
- interpretar datas;
- converter tipos de dados;
- tratar valores ausentes;
- identificar registros duplicados;
- resolver identificadores inconsistentes;
- remover espaços desnecessários;
- validar intervalos;
- reconciliar totais com a fonte;
- documentar transformações.

Limpeza nunca deve significar alterar registros legítimos até que a saída conte a história desejada.

Se os dados de origem parecerem incorretos, siga o processo autorizado de correção. Preserve a distinção entre a fonte original, a fonte corrigida e as transformações analíticas.

## Dados ausentes

Valores ausentes podem significar coisas diferentes:

- realmente desconhecido;
- não aplicável;
- não coletado;
- ainda não disponível;
- suprimido por privacidade;
- falha de transferência;
- campo ignorado pelo usuário;
- valor padrão do sistema.

Nunca suponha que ausente significa zero.

Antes de preencher, excluir ou imputar dados ausentes, documente a razão e avalie se o tratamento pode enviesar o resultado.

## Duplicados

Um duplicado não é simplesmente “duas linhas parecidas”. Duas transações podem legitimamente ter o mesmo cliente, valor e data.

Uma regra defensável para duplicados deve identificar:

- a chave única esperada;
- o evento de negócio representado;
- quais campos determinam unicidade;
- se vários registros podem ser válidos;
- o processo de correção quando duplicados forem confirmados.

## Estatística descritiva

Fundamentos úteis incluem:

- contagem;
- soma;
- média;
- mediana;
- mínimo;
- máximo;
- percentis;
- proporções;
- taxas;
- variância;
- desvio padrão;
- distribuições;
- tabelas de frequência.

### Média versus mediana

A média pode ser fortemente influenciada por valores extremos. A mediana muitas vezes representa melhor distribuições assimétricas, como salários, valores de imóveis ou tempos de resposta.

Use a estatística adequada à pergunta e explique-a claramente.

## Outliers

Outliers podem indicar:

- eventos realmente incomuns;
- erros de entrada;
- fraude;
- problemas de equipamento;
- clientes raros, mas importantes;
- falhas de processo;
- resultados extremos válidos.

Não os remova apenas porque tornam um gráfico ou modelo menos conveniente.

Um fluxo defensável é:

1. definir a regra de outlier;
2. inspecionar registros de origem;
3. determinar se o valor é válido;
4. documentar qualquer exclusão ou correção;
5. comparar resultados com e sem a observação, quando útil;
6. divulgar sensibilidade material.

## Amostragem e viés de seleção

Um conjunto de dados pode ser enorme e ainda assim induzir ao erro.

Pergunte:

- Quem teve chance de ser incluído?
- Quem está ausente?
- A participação foi voluntária?
- A amostra representa demais certas localidades, clientes, dispositivos ou períodos?
- Uma mudança de política ou sistema alterou quem aparece nos dados?
- Apenas casos bem-sucedidos são registrados?
- Existe viés de sobrevivência?

Mais linhas não eliminam automaticamente o viés.

## Correlação não é causalidade

Duas variáveis se moverem juntas não prova que uma causou a outra.

Uma relação pode surgir de:

- coincidência;
- uma terceira variável;
- causalidade reversa;
- viés de seleção;
- tendências temporais;
- diferenças de medição.

Use linguagem causal somente quando o desenho do estudo e as evidências sustentarem isso. Caso contrário, use termos como **associado a**, **correlacionado com**, **mais alto entre** ou **observado junto com**.

## Confiança e incerteza

Analistas iniciantes não precisam se tornar estatísticos imediatamente, mas precisam entender que estimativas têm incerteza.

Conceitos importantes incluem:

- tamanho da amostra;
- variabilidade;
- intervalos de confiança;
- margem de erro;
- significância estatística versus prática;
- incerteza do modelo;
- erro de previsão;
- sensibilidade a premissas.

Não transforme uma estimativa pontual em falsa certeza.

## Visualização de dados

Um bom gráfico deve facilitar a comparação pretendida, não manipular o leitor.

Boas práticas incluem:

- usar títulos claros;
- rotular unidades;
- mostrar períodos relevantes;
- usar texto legível;
- evitar decoração desnecessária;
- usar linha de base zero em gráficos de barras quando a comparação depende do comprimento das barras;
- declarar eixos interrompidos quando forem justificáveis;
- evitar efeitos 3D que distorçam tamanhos;
- manter a ordem das categorias significativa;
- fornecer rótulos de dados ou tabelas quando valores exatos forem importantes;
- usar contraste e padrões acessíveis;
- incluir texto alternativo ou resumo textual acessível quando exigido pelo contexto de publicação.

### Evite gráficos enganosos

Não:

- trunque eixos para exagerar diferenças sem explicação;
- compare totais de populações muito diferentes quando taxas seriam adequadas;
- selecione períodos apenas porque favorecem a narrativa;
- esconda categorias que enfraquecem a história preferida;
- use escalas inconsistentes entre gráficos semelhantes;
- sugira causalidade apenas por uma associação visual.

## Qualidade de dados

Dimensões comuns incluem:

- exatidão;
- completude;
- consistência;
- atualidade;
- validade;
- unicidade;
- integridade.

A qualidade deve ser avaliada conforme o uso pretendido. Um campo suficiente para uma contagem operacional interna pode não ser adequado para uma alegação regulatória, financeira, clínica ou pública.

## Validação e reconciliação

Antes de publicar um resultado importante:

- compare totais com uma fonte autoritativa;
- verifique registros de amostra;
- inspecione padrões de dados ausentes e duplicados;
- confirme limites de datas;
- confira denominadores;
- teste casos extremos;
- revise unidades e moeda;
- verifique filtros;
- inspecione cardinalidade dos joins;
- compare tendências com eventos conhecidos;
- peça revisão de outra pessoa qualificada para lógica de alto impacto quando a organização exigir.

Se o resultado não reconciliar, investigue antes de apresentá-lo como final.

## Documentação e reprodutibilidade

Um bom analista deixa um caminho que outra pessoa competente consegue seguir.

Documente:

- objetivo;
- responsável;
- fonte;
- data de atualização;
- definições;
- lógica;
- consultas ou fórmulas;
- exclusões;
- premissas;
- limitações;
- versão;
- validação realizada;
- histórico de correções.

Quando apropriado, use:

- controle de versão;
- SQL salvo;
- scripts reutilizáveis;
- notebooks;
- dicionários de dados;
- definições de métricas;
- repositórios controlados de relatórios;
- logs de mudanças.

## Comunicação de resultados

Um resumo analítico útil deve responder:

1. O que analisamos?
2. O que encontramos?
3. Qual é o tamanho do efeito ou diferença?
4. Que evidências sustentam o resultado?
5. Quais são as limitações?
6. Que decisão ou próximo passo é sustentado?

Evite jargão quando uma explicação em linguagem simples funcionar.

Separe:

- fatos observados;
- cálculos;
- premissas;
- interpretações;
- previsões;
- recomendações.

## Privacidade, segurança e controle de acesso

Analistas podem trabalhar com dados de clientes, funcionários, finanças, operações, saúde, localização, autenticação, dispositivos ou informações comerciais confidenciais.

Controles práticos incluem:

- usar sistemas aprovados pelo empregador;
- seguir o princípio do menor privilégio;
- não copiar conjuntos protegidos para armazenamento pessoal;
- não enviar extratos para e-mail pessoal;
- não contornar controles de acesso para “fazer o trabalho”;
- usar armazenamento e transferência criptografados e aprovados;
- minimizar a coleta;
- remover campos desnecessários;
- respeitar regras de retenção e exclusão;
- confirmar destinatários antes de compartilhar extratos;
- reportar suspeita de exposição ou acesso não autorizado;
- usar MFA e práticas de senha aprovadas;
- seguir a política organizacional para exportações, capturas de tela e arquivos locais.

O analista não deve inventar política jurídica ou de segurança. Siga a governança aprovada pela organização e escale dúvidas.

## IA responsável e automação

A IA pode ajudar em trabalho analítico de baixo risco quando a política organizacional permitir.

Possíveis usos:

- explicar uma fórmula;
- rascunhar SQL, Python ou R;
- sugerir perguntas exploratórias;
- gerar dados sintéticos de teste;
- rascunhar documentação;
- resumir informação pública não sensível;
- sugerir alternativas de gráficos;
- revisar estilo de código.

A validação humana continua obrigatória.

Não:

- envie dados confidenciais, credenciais, contratos privados, registros regulados ou extratos protegidos para ferramenta de IA não aprovada;
- suponha que SQL ou código gerado por IA esteja correto;
- publique interpretação escrita por IA sem verificar os cálculos subjacentes;
- aceite campos, definições ou citações inventados;
- permita que IA escolha exclusões que alterem materialmente o resultado sem revisão humana documentada;
- trate saída de IA como evidência;
- apresente previsões de IA como fatos observados;
- permita publicação autônoma de analytics críticos para decisão fora da governança aprovada.

Regra prática: **a IA pode ajudar a rascunhar, explicar ou testar; dados autoritativos, lógica aprovada e revisão humana responsável determinam o resultado final.**

O NIST AI Risk Management Framework e o Generative AI Profile oferecem orientação voluntária de gestão de riscos. Eles não substituem governança organizacional ou responsabilidades profissionais.

## Limites éticos

Um Analista de Dados não deve:

- alterar dados de origem para produzir conclusão preferida;
- esconder filtros ou exclusões;
- remover outliers válidos porque enfraquecem a narrativa;
- escolher denominador depois de ver qual resultado parece melhor;
- apresentar correlação como causalidade;
- fabricar dados, registros, citações, resultados ou amostras;
- suprimir limitações materiais;
- contornar controles de acesso;
- publicar informação protegida ou confidencial fora da autorização;
- alegar certeza estatística não sustentada pelo método;
- apresentar conclusões contábeis, jurídicas, clínicas, regulatórias ou de engenharia fora da competência atribuída;
- manipular visualização para enganar;
- representar previsão ou modelo como garantia.

Boa análise é rastreável, reproduzível, transparente sobre incerteza e aberta a correção.

## Acessibilidade e comunicação inclusiva de dados

Análises acessíveis melhoram a utilidade para todos.

Práticas úteis:

- títulos descritivos de gráficos;
- rótulos significativos nos eixos;
- contraste suficiente;
- não depender apenas de cor;
- usar padrões ou rótulos diretos quando apropriado;
- tamanhos de fonte legíveis;
- tabelas acessíveis;
- texto alternativo ou resumo textual para gráficos importantes;
- ordem lógica de leitura em documentos;
- explicação em linguagem simples dos achados importantes;
- dashboards acessíveis por teclado quando a plataforma permitir;
- testar com ferramentas de acessibilidade integradas quando disponíveis.

Normas e obrigações legais de acessibilidade variam conforme jurisdição e contexto. Este guia não certifica dashboard, relatório ou sistema como legalmente acessível.

## Educação e caminhos de entrada — Estados Unidos

A referência oficial de Statisticians é fortemente orientada à pós-graduação: o O*NET informa que muitos novos contratados nessa ocupação têm mestrado. Isso **não** deve ser interpretado como requisito universal para toda vaga de Data Analyst.

Vagas comerciais e operacionais podem aceitar combinações de:

- bacharelado;
- associate degree;
- certificado técnico;
- treinamento do empregador;
- aprendizagem profissional;
- experiência de trabalho relevante;
- evidências de portfólio;
- boas habilidades em planilhas, SQL e relatórios;
- conhecimento do domínio.

Áreas de estudo comuns incluem:

- estatística;
- matemática;
- data analytics;
- ciência da computação;
- sistemas de informação;
- negócios;
- economia;
- finanças;
- engenharia;
- ciências sociais;
- saúde ou outras áreas específicas do domínio.

### Localizadores de treinamento gratuito/de baixo custo e financiamento nos EUA

CareerOneStop pode ajudar a localizar:

- American Job Centers;
- programas de treinamento elegíveis para WIOA;
- serviços locais de treinamento;
- informações de carreira.

Elegibilidade e financiamento WIOA não são automáticos. Um American Job Center pode explicar elegibilidade local, provedores aprovados e serviços de apoio.

Pesquise além de “Data Analyst”. Programas relevantes podem aparecer como:

- data analytics;
- estatística;
- business analytics;
- sistemas de informação;
- tecnologia de bancos de dados;
- business intelligence;
- programação;
- Excel/SQL;
- habilidades digitais.

### Aprendizagem e experiência prática

O perfil Statisticians do O*NET vincula títulos de aprendizagem aprovados como **Data Analyst**, **Data Analyst (Nof)** e **Junior Data Analyst**.

A disponibilidade varia por localidade e empregador. Verifique oportunidades ativas no Apprenticeship.gov e nos sistemas locais de força de trabalho.

Outras rotas de experiência prática podem incluir:

- estágios remunerados;
- vagas de analista trainee;
- funções de assistente de relatórios;
- capacitação patrocinada pelo empregador;
- projetos com dados internos autorizados;
- pesquisa ou trabalho operacional supervisionado.

## Canadá

O Job Bank do Canadá mapeia **Data Analyst - Informatics and Systems** para **NOC 21223 — Database analysts and data administrators**. É uma comparação útil, mas mais orientada à gestão de dados do que muitas funções analíticas gerais.

Os requisitos atuais do Job Bank indicam que normalmente é exigido diploma universitário ou programa de college, em geral em ciência da computação, engenharia da computação ou matemática, junto com programação ou experiência relacionada. O Job Bank atualmente identifica essa ocupação como não regulamentada nacionalmente, embora requisitos de empregadores variem.

### Referência salarial do Canadá

Os salários nacionais atuais do Job Bank, atualizados em 19 de novembro de 2025, mostram aproximadamente:

- **C$25.00/hora — baixo**;
- **C$40.87/hora — mediana**;
- **C$61.03/hora — alto**.

Esses valores correspondem ao NOC 21223, não a todo título possível de Data Analyst.

### Treinamento e apoios de financiamento no Canadá

Canada.ca fornece links nacionais para:

- auxílio estudantil;
- capacitação profissional;
- serviços de emprego;
- programas provinciais/territoriais;
- oportunidades reconhecidas de treinamento de curta duração;
- informações de Employment Insurance e treinamento, quando aplicável.

Elegibilidade, financiamento e desenho do programa variam por província, território e circunstâncias individuais.

## Colômbia

O título genérico **Analista de datos** abrange vários grupos CUOC. Este guia usa comparações baseadas nas funções, e não afirma um único código colombiano exclusivo.

### CUOC 25210 — Diseñadores y administradores de bases de datos

Relevante quando a vaga enfatiza:

- estruturas de banco de dados;
- arquitetura de dados;
- warehouses;
- administração de dados;
- qualidade de dados;
- limpeza/extração/transformação;
- visualização e comunicação;
- segurança e integridade de bancos de dados.

O grupo oficial inclui o título **Analista de datos comerciales**.

### CUOC 25110 — Analistas de sistemas

Relevante para funções de analytics e BI. Denominações oficiais incluem:

- Analista de analytics;
- Analista de inteligencia de negocios;
- Analista de Power BI;
- Analista de información comercial;
- Analista de procesamiento de información.

### CUOC 21200 — Matemáticos, actuarios y estadísticos

Relevante quando o trabalho é fortemente estatístico ou de pesquisa. Inclui **Analista estadístico**.

O OCUPACOL alerta que os indicadores de mercado por ocupação exibidos em seus perfis não têm representatividade estatística sob a metodologia aplicada. Por isso, este guia não apresenta essas faixas como salário nacional representativo de Data Analyst.

### Caminhos SENA

O SENA Betowa lista atualmente caminhos relevantes para análise de dados, incluindo:

**Programación para analítica de datos**  
- Técnico;
- **2,208 horas**;
- formação titulada;
- competências em processamento, integração, visualização e análise de dados.

**Visualización de datos usando Power BI**  
- curso complementar/especial;
- **48 horas**;
- treinamento suplementar focado, e não qualificação profissional completa por si só.

**Analítica de datos para procesos logísticos**  
- formação complementar virtual;
- **48 horas**;
- conteúdo de analytics específico de logística.

Disponibilidade do programa, cidade, modalidade, turmas, vagas, requisitos de admissão e datas podem mudar. Verifique os anúncios ativos no Betowa antes de se candidatar.

## América Latina e Caribe

A OIT/Cinterfor oferece uma rede regional e um localizador de formação profissional por país. Pode ajudar leitores a identificar instituições nacionais de treinamento e comparar sistemas de qualificação na América Latina e no Caribe.

É um localizador e uma rede de conhecimento, não uma garantia de curso, bolsa ou financiamento específico de Data Analyst em todos os países.

Verifique catálogo atual, elegibilidade, custo, modalidade e reconhecimento do empregador diretamente com a instituição nacional relevante.

## Pesquisa de renda atual — use com cuidado

### Referência quantitativa oficial dos Estados Unidos

Para **Statisticians (O*NET-SOC 15-2041.00)**, os dados salariais BLS de 2025 exibidos pelo O*NET mostram:

| Percentil | Anual | Por hora |
|---|---:|---:|
| 10º | $54,680 | $26.29 |
| 25º | $70,710 | $33.99 |
| Mediana | $105,650 | $50.79 |
| 75º | $143,140 | $68.82 |
| 90º | $170,700 | $82.07 |

Esses são salários de **Statisticians**, não uma tabela salarial universal de Data Analyst.

### Perspectivas dos EUA para a referência Statisticians

Dados O*NET/BLS mostram:

- emprego em 2024: cerca de **32,200**;
- emprego projetado para 2034: cerca de **34,900**;
- crescimento projetado: **9%**;
- vagas anuais projetadas: cerca de **2,000**.

Esses números também pertencem à referência Statisticians.

### Estimativa atual não governamental nos EUA

A página atual do Indeed dos EUA para **Data Analyst** informa salário-base médio de aproximadamente **$85,108/ano**, faixa exibida de aproximadamente **$52,084–$139,074/ano** e cerca de **8.1k observações salariais de anúncios de emprego nos 36 meses anteriores** na página de 2026 revisada.

Trata-se de uma **estimativa de mercado não governamental e específica do título**, não de estatística salarial oficial nem remuneração garantida. Páginas de mercado mudam; verifique a página ativa antes de tomar decisões de remuneração.

### Canadá

Os salários nacionais do Job Bank para NOC 21223 são aproximadamente:

- C$25.00/hora — baixo;
- C$40.87/hora — mediana;
- C$61.03/hora — alto.

Eles pertencem à comparação de database analyst/data administrator e não devem ser tratados como taxa universal exata para Data Analyst.

### Colômbia

Como os mapeamentos oficiais CUOC/OCUPACOL dependem da função e o próprio OCUPACOL alerta que os indicadores de mercado ocupacional exibidos não têm representatividade estatística, este guia não fabrica um único salário nacional oficial e representativo para Data Analyst na Colômbia.

Para decisões atuais de remuneração, compare vários anúncios ativos e fontes de mercado confiáveis para o escopo exato da vaga, cidade, senioridade, idiomas, stack tecnológica e vínculo de trabalho.

## Uma sequência prática de aprendizagem

### Etapa 1 — fundamentos

Aprenda:

- planilhas básicas;
- porcentagens e taxas;
- estatística descritiva;
- tabelas limpas;
- gráficos básicos;
- privacidade de dados;
- documentação.

### Etapa 2 — consultas

Aprenda:

- conceitos relacionais;
- chaves;
- joins;
- filtragem e agregação em SQL;
- verificações de qualidade de dados;
- validação.

### Etapa 3 — análise

Aprenda:

- distribuições;
- dados ausentes;
- outliers;
- amostragem;
- viés;
- correlação versus causalidade;
- visualização acessível;
- comunicação com partes interessadas.

### Etapa 4 — automação

Adicione uma linguagem como Python ou R para:

- limpeza reproduzível;
- conjuntos maiores;
- análise repetível;
- fluxos estatísticos;
- validação automatizada.

### Etapa 5 — profundidade de domínio

Escolha um domínio de negócio ou técnico, por exemplo:

- finanças;
- marketing;
- saúde;
- cibersegurança;
- logística;
- qualidade;
- políticas públicas;
- operações;
- analytics de produto.

Conhecimento do domínio ajuda a fazer perguntas melhores e detectar resultados implausíveis.

## Projetos de portfólio sem expor dados privados

Um portfólio pode demonstrar capacidade sem usar informação confidencial do empregador.

Fontes seguras incluem:

- conjuntos de dados públicos do governo;
- portais de dados abertos;
- dados com licença explícita;
- dados sintéticos criados por você;
- conjuntos de treinamento cujos termos permitem uso em portfólio.

Um bom projeto iniciante pode incluir:

1. pergunta;
2. fonte e licença;
3. dicionário de dados;
4. etapas de limpeza;
5. SQL ou código;
6. verificações de validação;
7. gráficos ou dashboard;
8. achados;
9. limitações;
10. resumo acessível;
11. README com passos de reprodução.

Não publique:

- dados de empregadores;
- registros de clientes;
- informações de funcionários;
- capturas de telas de sistemas confidenciais;
- SQL interno com identificadores sensíveis;
- definições proprietárias de relatórios;
- credenciais ou tokens.

## Plano inicial de quatro semanas

### Semana 1 — planilha e qualidade de dados

- escolha um conjunto público ou sintético;
- identifique o que uma linha representa;
- crie um dicionário simples;
- verifique valores ausentes e duplicados;
- calcule contagens, taxas, média e mediana;
- crie um gráfico honesto.

### Semana 2 — SQL

- crie ou use um pequeno banco de prática;
- escreva consultas de filtro e agregação;
- pratique joins;
- valide contagens antes e depois dos joins;
- documente uma consulta em linguagem simples.

### Semana 3 — análise e comunicação

- escreva uma pergunta clara de negócio ou pesquisa;
- analise-a com seu conjunto de dados;
- identifique pelo menos duas limitações;
- crie um gráfico acessível e um resumo curto;
- diferencie observação de interpretação.

### Semana 4 — portfólio e preparação para emprego

- organize o README;
- documente fonte e licença dos dados;
- inclua passos reproduzíveis;
- remova qualquer informação sensível;
- escreva dois bullets de currículo descrevendo o projeto com precisão;
- pesquise vagas atuais usando vários títulos relacionados;
- compare os requisitos reais antes de decidir o que aprender em seguida.

## Títulos de vagas para pesquisar

Dependendo das suas habilidades, pesquise:

- Data Analyst;
- Junior Data Analyst;
- Reporting Analyst;
- Business Data Analyst;
- Operations Analyst;
- Marketing Analyst;
- Sales Analyst;
- Quality Analyst;
- Research Analyst;
- Data Quality Analyst;
- BI Analyst;
- Power BI Analyst;
- SQL Analyst;
- Analytics Specialist;
- Data Coordinator;
- Reporting Specialist.

Leia as responsabilidades com atenção. Duas vagas com o mesmo título podem ter exigências técnicas e educacionais muito diferentes.

## Perguntas antes de aceitar uma vaga

Considere perguntar:

- Quais são as principais fontes de dados?
- SQL é usado diariamente?
- Quais ferramentas são usadas para dashboards e análise?
- Como as definições de métricas são governadas?
- Quem é responsável pela qualidade dos dados?
- Como os analistas devem validar resultados?
- Existe revisão de código ou por pares?
- Quais dados podem ser acessados remotamente?
- Que treinamento de privacidade/segurança é exigido?
- Horas extras, plantões ou picos de prazo são comuns?
- A função é principalmente relatório, análise estatística, análise de negócios ou banco de dados?
- Que habilidades diferenciam analista júnior de sênior nesta organização?
- O empregador oferece treinamento ou apoio a certificações?

## Fontes e links de verificação

Verifique valores e disponibilidade de programas antes de tomar uma decisão importante.

### Estados Unidos

- O*NET — Statisticians: https://www.onetonline.org/link/details/15-2041.00
- O*NET — Business Intelligence Analysts: https://www.onetonline.org/link/details/15-2051.01
- CareerOneStop WIOA training locator: https://www.careeronestop.org/LocalHelp/EmploymentAndTraining/find-WIOA-training-programs.aspx
- Apprenticeship.gov: https://www.apprenticeship.gov/
- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework

### Canadá

- Job Bank — NOC 21223 occupational information: https://www.jobbank.gc.ca/
- Canada training gateway: https://www.canada.ca/en/services/jobs/training.html

### Colômbia

- OCUPACOL: https://ocupacol.mintrabajo.gov.co/
- SENA Betowa: https://betowa.sena.edu.co/

### América Latina e Caribe

- OIT/Cinterfor: https://www.oitcinterfor.org/

### Contexto atual de mercado não governamental

- Indeed U.S. Data Analyst salary page: https://www.indeed.com/career/data-analyst/salaries

## Aviso importante

Este guia oferece informação geral para educação e planejamento de carreira. Não garante emprego, renda, admissão, financiamento, vaga de aprendizagem, certificação, promoção ou qualquer outro resultado. Mapeamentos ocupacionais são comparações e podem não ser equivalentes exatos entre jurisdições. Requisitos, salários, expectativas de tecnologia, disponibilidade de treinamento e condições de emprego mudam ao longo do tempo.

Não se declara certificação humana independente, acreditação profissional, revisão jurídica, certificação estatística, certificação de acessibilidade ou certificação de tradução, salvo se documentadas separadamente.

## Autor e assistência de IA

Criado e dirigido por **Alberto “Al” Leiva**. O ChatGPT apoiou pesquisa, organização, edição, suporte à tradução e preparação de documentos sob direção do autor. O autor permanece responsável pelas decisões editoriais e de publicação.

## Licença

Salvo indicação em contrário em um arquivo, este material é licenciado sob **CC BY-NC-SA 4.0**.
