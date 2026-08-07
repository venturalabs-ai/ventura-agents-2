# Ventura Agents II

**2ª coleção** de **10 super agentes de IA de negócio** para o mercado, com a
identidade da família **Ventura.** — cada um especializado em uma função de
alta demanda **diferente** da 1ª coleção: produto, customer success, operações,
suprimentos, segurança cibernética, devops, pesquisa de mercado, precificação,
e-commerce e treinamento & desenvolvimento.

Cada agente é um **system prompt completo, plugável**: copie o arquivo, anexe
como system prompt no seu modelo/plataforma (ChatGPT, Claude, Gemini, copilots
empresariais) e adicione as ferramentas/APIs indicadas no bloco "Ferramentas".
Todos os agentes carregam **skills e referência de certificação MIT** (MIT
Sloan Executive Education, MIT xPRO, MIT Professional Education, MITx
MicroMasters e MIT OpenCourseWare), garantindo profundidade acadêmica e rigor
de método em cada domínio.

## Catálogo (2ª coleção — 10 funções de alta demanda)

| # | Agente | Função | Entrega principal |
|---|---|---|---|
| 1 | [ventura.produto](ventura.produto.md) | Product Management | descoberta, roadmap, backlog, validação e métricas de produto |
| 2 | [ventura.clientes](ventura.clientes.md) | Customer Success | onboarding, retenção, churn e expansão de conta |
| 3 | [ventura.operacoes](ventura.operacoes.md) | Operações & processos | SOPs, eficiência, melhoria contínua e KPIs operacionais |
| 4 | [ventura.suprimentos](ventura.suprimentos.md) | Supply chain & logística | estoque, fornecedores, distribuição e previsão de demanda |
| 5 | [ventura.seguranca](ventura.seguranca.md) | Cibersegurança | risco, políticas, resposta a incidentes e conformidade |
| 6 | [ventura.devops](ventura.devops.md) | DevOps & SRE | CI/CD, infraestrutura, observabilidade e confiabilidade |
| 7 | [ventura.pesquisa](ventura.pesquisa.md) | Pesquisa de mercado | inteligência competitiva, persona, tendências e insights |
| 8 | [ventura.precificacao](ventura.precificacao.md) | Estratégia de preços | pricing tiers, margem, elasticidade e promoções |
| 9 | [ventura.ecommerce](ventura.ecommerce.md) | E-commerce & marketplaces | catálogo, anúncios, reputação e operação de loja |
| 10 | [ventura.treinamento](ventura.treinamento.md) | Treinamento & desenvolvimento | trilhas, onboarding, conteúdo e avaliação de aprendizagem |

## Anatomia de cada agente

```
 1. Identidade            — nome (ventura.<função>), missão, tom de voz
 2. Domínio               — escopo de atuação, o que faz / não faz
 3. Regras de ouro        — princípios inegociáveis (dados, ética, segurança)
 4. Skill & Certificação  — competências-chave + programas MIT de referência
    MIT                      (Sloan Exec Ed, xPRO, Professional Education,
                             MicroMasters, OpenCourseWare)
 5. Workflow              — pipeline operacional passo a passo
 6. Entradas e saídas     — o que recebe, o que entrega (contrato)
 7. Métricas              — KPIs que o agente persegue
 8. Ferramentas           — integrações sugeridas (CRM, ERP, helpdesk...)
 9. Autonomia             — o que decide sozinho vs. o que sobe para humano
10. Exemplo de uso        — prompt de ativação pronto
```

## Como usar

```text
1. Escolha o agente no catálogo.
2. Copie o conteúdo do .md como system prompt.
3. Forneça as variáveis obrigatórias (empresa, persona, contexto, acesso).
4. Ative com o "Exemplo de uso" do próprio agente.
5. Conecte as integrações sugeridas para autonomia real.
```

## Sobre a certificação MIT

Os agentes referenciam programas reais do ecossistema MIT como base de método:
**MIT Sloan Executive Education** (gestão, estratégia, finanças),
**MIT xPRO** (tecnologia, dados, cloud/devops), **MIT Professional Education**
(ciência de dados aplicada, cibersegurança), **MITx MicroMasters**
(supply chain, estatística, gestão de projetos) e **MIT OpenCourseWare**
(fundamentos públicos). Isso não substitui certificações formais do MIT — é o
referencial de conhecimento que orienta o comportamento de cada agente.

## Família Ventura

| Projeto | Repositório | Foco |
|---|---|---|
| **Ventura Agents** | `ventura-agents` | 1ª coleção: 10 agentes de negócio |
| **Ventura Agents II** | `ventura-agents-2` | 2ª coleção: 10 agentes de negócio |
| Autor Ventura | `autor-ventura` | super agente escritor (livros) |
| Ventura Art | `ventura-art` | criação de vídeos multi-plataforma |
| Ventura Pro | `ventura-pro` | soluções tecnológicas |

Frase-guia do estúdio: **"Todo agente nasce de uma função; toda função, de
uma entrega; toda entrega, de uma obrigação com o negócio."**

## Arquitetura Token-Efficient & Regenerative

Este sistema foi projetado sob três princípios fundamentais:

1. **Economia de Tokens** — maximizar valor por token gasto  
2. **Loop de Alto Rendimento** — cada ciclo deve justificar o consumo  
3. **Comportamento Regenerativo** — o sistema se reconstrói melhor a cada execução

### Ciclo Principal: Explore → Compile → Replay

| Fase | Descrição | Consumo de Tokens |
|------|-----------|-------------------|
| **Explore** | Modelo forte descobre o melhor caminho | Alto (único) |
| **Compile** | Transforma o caminho em skill determinística | Baixo |
| **Replay** | Executa a skill sem raciocínio completo | Mínimo / Zero |
| **Regenerate** | Quando o domínio muda, regenera a skill | Sob demanda |

### Regras de Engenharia

- **Token Budget** explícito por especialista e por etapa
- **Context Engineering** + **Context Compaction** em todas as passagens
- **Context Firewall** entre sub-agentes (cada um só recebe o necessário)
- **Prefix Caching** com system prompt estável
- **Yield-based Stop Condition** (para quando o valor não justifica mais tokens)
- **Skill Distillation** após caminhos bem-sucedidos

### Resultado esperado

- Redução drástica de tokens em execuções recorrentes
- Qualidade mantida ou superior
- Sistema que se auto-otimiza com o uso
