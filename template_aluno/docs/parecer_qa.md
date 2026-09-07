# Revisão de QA — Parecer Final

## 1. Resultado dos testes

Foram elaborados e automatizados testes para os requisitos RF01, RF02 e RF03.

Os testes contemplaram:

- Particionamento de equivalência;
- Análise de valores-limite;
- Cenários positivos;
- Cenários negativos;
- Testes automatizados com pytest.

## 2. Defeito identificado

Foi identificado um defeito no requisito RF01 — Permissão para empréstimo.

O requisito determina que o usuário deve possuir **menos de 3 empréstimos ativos** para realizar um novo empréstimo.

O teste de valor-limite verificou o caso de exatamente 3 empréstimos ativos e constatou que o sistema permite o empréstimo, quando o comportamento esperado é recusá-lo.

## 3. Evidências

O teste automatizado referente ao limite de 3 empréstimos falha porque o comportamento implementado não corresponde ao requisito especificado.

A falha do teste é considerada uma evidência de defeito e não um erro do caso de teste.

## 4. Decisão de QA

- [ ] APROVAR
- [x] NÃO APROVAR

## 5. Justificativa

A versão atual não deve ser liberada para produção.

Embora os requisitos RF01, RF02 e RF03 tenham sido contemplados pelos testes, foi encontrada uma divergência funcional no limite do RF01.

O defeito permite que um usuário com exatamente 3 empréstimos ativos realize um novo empréstimo, contrariando o requisito de que o usuário deve possuir menos de 3 empréstimos ativos.

Recomenda-se corrigir o defeito e executar novamente a suíte de testes antes da liberação da versão.
