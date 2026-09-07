# Revisão de QA — Parecer Final

## 1. Resultado dos testes

Foram elaborados testes para os requisitos RF01, RF02 e RF03.

Os testes contemplaram:

- Particionamento de equivalência;
- Análise de valores-limite;
- Cenários positivos;
- Cenários negativos;
- Testes automatizados com pytest.

## 2. Defeito identificado

Foi identificado um defeito no requisito RF01 — Permissão para empréstimo.

O requisito determina que o usuário deve possuir menos de 3 empréstimos ativos para realizar um novo empréstimo.

O teste de valor-limite verificou o caso de exatamente 3 empréstimos ativos e constatou uma divergência entre o comportamento esperado e o comportamento obtido.

## 3. Evidência

O teste automatizado referente ao limite de 3 empréstimos é utilizado para verificar essa fronteira.

A falha desse teste deve ser interpretada como evidência de um possível defeito no software, e não como motivo para alterar um teste correto.

## 4. Decisão de QA

- [ ] APROVAR
- [x] NÃO APROVAR

## 5. Justificativa

A versão atual não deve ser liberada para produção enquanto a divergência encontrada no RF01 não for corrigida e novamente validada.

Os requisitos RF01, RF02 e RF03 foram contemplados pela suíte de testes, porém existe uma falha funcional na fronteira de 3 empréstimos ativos.

Recomenda-se corrigir o defeito e executar novamente a suíte completa de testes antes da liberação.
