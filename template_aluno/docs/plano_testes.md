# Mini Plano de Testes — BiblioTech

## 1. Identificação

**Equipe:** Individual

**Integrantes:** Davi Abras Scalabrini / RA: 325145524

**Data:** 07/09/2026

---

## 2. Objetivo

Verificar se as funcionalidades do módulo de empréstimos do BiblioTech atendem aos requisitos especificados, utilizando técnicas de teste de Caixa Preta e Caixa Branca, automatização com pytest e análise de cobertura de código, produzindo evidências para apoiar o parecer técnico de QA sobre a liberação da versão.

---

## 3. Escopo

### Funcionalidades que serão testadas

- RF01 — Permissão para empréstimo
- RF02 — Cálculo de multa
- RF03 — Classificação de atraso

### Fora do escopo

- Interface gráfica
- Banco de dados
- Autenticação
- Segurança
- Desempenho
- Acessibilidade
- Integração com sistemas externos
- Validação de tipos de dados
- Persistência das operações

---

## 4. Estratégia

### Caixa Preta

Marque as técnicas utilizadas:

- [x] Particionamento de equivalência
- [x] Análise de valores-limite
- [x] Cenários positivos
- [x] Cenários negativos

### Caixa Branca

Preencher após o checkpoint.

Aspectos estruturais analisados:

- Condições
- Decisões
- Caminhos de execução
- Branches
- Retornos das funções
  
---

## 5. Ambiente

**Sistema operacional:** Windows

**Versão do Python:** Python 3.12

**Framework de testes:** pytest

**Repositório:** GitHub

--- 

## 6. Critérios de entrada

- Requisitos disponíveis para análise
- Ambiente de testes configurado
- Código do projeto disponível no repositório
- Dependências necessárias instaladas
- Casos de teste elaborados com base nos requisitos
- Arquivos de produção preservados sem alteração

---

## 7. Critérios de saída

- Casos de teste definidos e executados
- Testes automatizados implementados
- Resultados dos testes registrados
- Cobertura de código analisada
- Defeitos identificados e documentados
- Matriz de rastreabilidade preenchida
- Parecer técnico de QA elaborado
- Pull Request criado com as evidências da atividade

---

## 8. Riscos

| Risco | Impacto | Mitigação |
|---|---|---|
| Interpretação incorreta dos requisitos | Casos de teste inadequados | Utilizar os requisitos como fonte para elaboração dos testes |
| Alteração acidental do código de produção | Comprometimento da avaliação | Não modificar arquivos da pasta src/ |
| Testes incorretos serem considerados falhas do sistema | Resultado de QA incorreto | Conferir requisito, entrada, resultado esperado e resultado obtido |
| Cobertura insuficiente | Evidências incompletas | Utilizar pytest-cov e analisar linhas e branches |

---

## 9. Entregáveis

- [x] Casos de teste
- [x] Testes automatizados
- [x] Matriz de rastreabilidade
- [x] Evidência de cobertura
- [x] Registro de defeitos
- [x] Pull Request
- [x] Parecer de QA

---

## 10. Observações

- A equipe atuará como QA, sem realizar alterações no código de produção
- Durante a etapa de Caixa Preta, os casos de teste serão elaborados com base nos requisitos, sem consulta ao código-fonte localizado em src/.
- Defeitos encontrados serão registrados e analisados, sem correção do código de produção
