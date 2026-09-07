# Roteiro de Testes — BiblioTech

## CT-01

### Requisito

RF01

### Título

Usuário ativo, sem pendências e sem empréstimos ativos

### Tipo

* [x] Caixa Preta
* [ ] Caixa Branca

### Prioridade

* [x] Alta
* [ ] Média
* [ ] Baixa

### Objetivo

Verificar se um usuário ativo, sem pendências e com quantidade de empréstimos abaixo do limite pode realizar um novo empréstimo.

### Pré-condições

Usuário ativo e sem pendências.

### Dados de teste

* usuario_ativo = True
* possui_pendencia = False
* emprestimos_ativos = 0

### Passos

1. Informar que o usuário está ativo.
2. Informar que o usuário não possui pendências.
3. Informar que possui 0 empréstimos ativos e solicitar um novo empréstimo.

### Resultado esperado

O empréstimo deve ser permitido.

### Resultado obtido

Preencher após a execução.

### Status

* [ ] PASSOU
* [ ] FALHOU

### Técnica utilizada

* [x] Particionamento de equivalência
* [ ] Análise de valor-limite
* [x] Cenário positivo
* [ ] Cenário negativo

### Evidência

Preencher após a execução.

### Observações

Cenário pertencente à classe válida do RF01.

---

## CT-02

### Requisito

RF01

### Título

Usuário inativo não pode realizar empréstimo

### Tipo

* [x] Caixa Preta
* [ ] Caixa Branca

### Prioridade

* [x] Alta
* [ ] Média
* [ ] Baixa

### Objetivo

Verificar se um usuário inativo tem seu empréstimo recusado.

### Pré-condições

Usuário sem pendências e sem empréstimos ativos.

### Dados de teste

* usuario_ativo = False
* possui_pendencia = False
* emprestimos_ativos = 0

### Passos

1. Informar que o usuário está inativo.
2. Informar que não possui pendências.
3. Solicitar um novo empréstimo.

### Resultado esperado

O empréstimo deve ser recusado.

### Resultado obtido

Preencher após a execução.

### Status

* [ ] PASSOU
* [ ] FALHOU

### Técnica utilizada

* [x] Particionamento de equivalência
* [ ] Análise de valor-limite
* [ ] Cenário positivo
* [x] Cenário negativo

### Evidência

Preencher após a execução.

### Observações

Cenário pertencente à classe inválida de usuário inativo.

---

## CT-03

### Requisito

RF01

### Título

Usuário com pendência não pode realizar empréstimo

### Tipo

* [x] Caixa Preta
* [ ] Caixa Branca

### Prioridade

* [x] Alta
* [ ] Média
* [ ] Baixa

### Objetivo

Verificar se a existência de pendência impede a realização de um novo empréstimo.

### Pré-condições

Usuário ativo e sem empréstimos ativos.

### Dados de teste

* usuario_ativo = True
* possui_pendencia = True
* emprestimos_ativos = 0

### Passos

1. Informar que o usuário está ativo.
2. Informar que possui pendência.
3. Solicitar um novo empréstimo.

### Resultado esperado

O empréstimo deve ser recusado.

### Resultado obtido

Preencher após a execução.

### Status

* [ ] PASSOU
* [ ] FALHOU

### Técnica utilizada

* [x] Particionamento de equivalência
* [ ] Análise de valor-limite
* [ ] Cenário positivo
* [x] Cenário negativo

### Evidência

Preencher após a execução.

### Observações

Cenário pertencente à classe inválida de usuário com pendência.

---

## CT-04

### Requisito

RF01

### Título

Usuário com exatamente 3 empréstimos ativos não pode realizar novo empréstimo

### Tipo

* [x] Caixa Preta
* [ ] Caixa Branca

### Prioridade

* [x] Alta
* [ ] Média
* [ ] Baixa

### Objetivo

Verificar o comportamento na fronteira do limite de empréstimos ativos.

### Pré-condições

Usuário ativo e sem pendências.

### Dados de teste

* usuario_ativo = True
* possui_pendencia = False
* emprestimos_ativos = 3

### Passos

1. Informar que o usuário está ativo.
2. Informar que não possui pendências.
3. Informar que possui exatamente 3 empréstimos ativos.
4. Solicitar um novo empréstimo.

### Resultado esperado

O empréstimo deve ser recusado, pois o requisito determina que o usuário deve possuir menos de 3 empréstimos ativos.

### Resultado obtido

Preencher após a execução.

### Status

* [ ] PASSOU
* [ ] FALHOU

### Técnica utilizada

* [ ] Particionamento de equivalência
* [x] Análise de valor-limite
* [ ] Cenário positivo
* [x] Cenário negativo

### Evidência

Preencher após a execução.

### Observações

Este caso testa diretamente a fronteira do RF01 e pode revelar o defeito intencional da atividade.

---

## CT-05

### Requisito

RF02

### Título

Multa para zero dias de atraso

### Tipo

* [x] Caixa Preta
* [ ] Caixa Branca

### Prioridade

* [x] Alta
* [ ] Média
* [ ] Baixa

### Objetivo

Verificar que não há cobrança de multa quando não existe atraso.

### Pré-condições

Operação de cálculo de multa disponível.

### Dados de teste

* dias_atraso = 0

### Passos

1. Informar 0 dias de atraso.
2. Calcular a multa.
3. Comparar o resultado com o valor esperado.

### Resultado esperado

A multa deve ser R$ 0,00.

### Resultado obtido

Preencher após a execução.

### Status

* [ ] PASSOU
* [ ] FALHOU

### Técnica utilizada

* [x] Particionamento de equivalência
* [x] Análise de valor-limite
* [x] Cenário positivo
* [ ] Cenário negativo

### Evidência

Preencher após a execução.

### Observações

Testa a fronteira entre ausência de atraso e atraso.

---

## CT-06

### Requisito

RF02

### Título

Multa para um dia de atraso

### Tipo

* [x] Caixa Preta
* [ ] Caixa Branca

### Prioridade

* [ ] Alta
* [x] Média
* [ ] Baixa

### Objetivo

Verificar o cálculo da multa para o início da faixa de atraso de 1 a 7 dias.

### Pré-condições

Operação de cálculo de multa disponível.

### Dados de teste

* dias_atraso = 1

### Passos

1. Informar 1 dia de atraso.
2. Calcular a multa.
3. Comparar o resultado com o valor esperado.

### Resultado esperado

A multa deve ser R$ 2,00.

### Resultado obtido

Preencher após a execução.

### Status

* [ ] PASSOU
* [ ] FALHOU

### Técnica utilizada

* [x] Particionamento de equivalência
* [x] Análise de valor-limite
* [x] Cenário positivo
* [ ] Cenário negativo

### Evidência

Preencher após a execução.

### Observações

Testa o limite inferior da faixa de 1 a 7 dias.

---

## CT-07

### Requisito

RF02

### Título

Multa para sete dias de atraso

### Tipo

* [x] Caixa Preta
* [ ] Caixa Branca

### Prioridade

* [ ] Alta
* [x] Média
* [ ] Baixa

### Objetivo

Verificar o cálculo da multa no limite superior da faixa de 1 a 7 dias.

### Pré-condições

Operação de cálculo de multa disponível.

### Dados de teste

* dias_atraso = 7

### Passos

1. Informar 7 dias de atraso.
2. Calcular a multa.
3. Comparar o resultado com o valor esperado.

### Resultado esperado

A multa deve ser R$ 14,00.

### Resultado obtido

Preencher após a execução.

### Status

* [ ] PASSOU
* [ ] FALHOU

### Técnica utilizada

* [x] Particionamento de equivalência
* [x] Análise de valor-limite
* [x] Cenário positivo
* [ ] Cenário negativo

### Evidência

Preencher após a execução.

### Observações

Testa a fronteira superior da faixa de 1 a 7 dias.

---

## CT-08

### Requisito

RF02

### Título

Multa para oito dias de atraso

### Tipo

* [x] Caixa Preta
* [ ] Caixa Branca

### Prioridade

* [x] Alta
* [ ] Média
* [ ] Baixa

### Objetivo

Verificar o cálculo da multa imediatamente após a fronteira de 7 dias.

### Pré-condições

Operação de cálculo de multa disponível.

### Dados de teste

* dias_atraso = 8

### Passos

1. Informar 8 dias de atraso.
2. Calcular a multa.
3. Comparar o resultado com o valor esperado.

### Resultado esperado

A multa deve ser R$ 17,00.

### Resultado obtido

Preencher após a execução.

### Status

* [ ] PASSOU
* [ ] FALHOU

### Técnica utilizada

* [ ] Particionamento de equivalência
* [x] Análise de valor-limite
* [x] Cenário positivo
* [ ] Cenário negativo

### Evidência

Preencher após a execução.

### Observações

Testa o primeiro valor da faixa acima de 7 dias.

---

## CT-09

### Requisito

RF03

### Título

Classificação para zero dias de atraso

### Tipo

* [x] Caixa Preta
* [ ] Caixa Branca

### Prioridade

* [x] Alta
* [ ] Média
* [ ] Baixa

### Objetivo

Verificar a classificação de um empréstimo sem atraso.

### Pré-condições

Operação de classificação disponível.

### Dados de teste

* dias_atraso = 0

### Passos

1. Informar 0 dias de atraso.
2. Solicitar a classificação.
3. Comparar com o resultado esperado.

### Resultado esperado

A classificação deve ser "sem atraso".

### Resultado obtido

Preencher após a execução.

### Status

* [ ] PASSOU
* [ ] FALHOU

### Técnica utilizada

* [x] Particionamento de equivalência
* [x] Análise de valor-limite
* [x] Cenário positivo
* [ ] Cenário negativo

### Evidência

Preencher após a execução.

### Observações

Testa a fronteira inicial da classificação.

---

## CT-10

### Requisito

RF03

### Título

Classificação para sete dias de atraso

### Tipo

* [x] Caixa Preta
* [ ] Caixa Branca

### Prioridade

* [ ] Alta
* [x] Média
* [ ] Baixa

### Objetivo

Verificar a classificação no limite superior do atraso leve.

### Pré-condições

Operação de classificação disponível.

### Dados de teste

* dias_atraso = 7

### Passos

1. Informar 7 dias de atraso.
2. Solicitar a classificação.
3. Comparar com o resultado esperado.

### Resultado esperado

A classificação deve ser "atraso leve".

### Resultado obtido

Preencher após a execução.

### Status

* [ ] PASSOU
* [ ] FALHOU

### Técnica utilizada

* [x] Particionamento de equivalência
* [x] Análise de valor-limite
* [x] Cenário positivo
* [ ] Cenário negativo

### Evidência

Preencher após a execução.

### Observações

Testa o limite superior da faixa de atraso leve.

---

## CT-11

### Requisito

RF03

### Título

Classificação para oito dias de atraso

### Tipo

* [x] Caixa Preta
* [ ] Caixa Branca

### Prioridade

* [x] Alta
* [ ] Média
* [ ] Baixa

### Objetivo

Verificar a classificação imediatamente após a fronteira de 7 dias.

### Pré-condições

Operação de classificação disponível.

### Dados de teste

* dias_atraso = 8

### Passos

1. Informar 8 dias de atraso.
2. Solicitar a classificação.
3. Comparar com o resultado esperado.

### Resultado esperado

A classificação deve ser "atraso moderado".

### Resultado obtido

Preencher após a execução.

### Status

* [ ] PASSOU
* [ ] FALHOU

### Técnica utilizada

* [ ] Particionamento de equivalência
* [x] Análise de valor-limite
* [x] Cenário positivo
* [ ] Cenário negativo

### Evidência

Preencher após a execução.

### Observações

Testa a mudança entre atraso leve e atraso moderado.

---

## CT-12

### Requisito

RF03

### Título

Classificação para mais de 30 dias de atraso

### Tipo

* [x] Caixa Preta
* [ ] Caixa Branca

### Prioridade

* [x] Alta
* [ ] Média
* [ ] Baixa

### Objetivo

Verificar a classificação de um atraso superior a 30 dias.

### Pré-condições

Operação de classificação disponível.

### Dados de teste

* dias_atraso = 31

### Passos

1. Informar 31 dias de atraso.
2. Solicitar a classificação.
3. Comparar com o resultado esperado.

### Resultado esperado

A classificação deve ser "atraso grave".

### Resultado obtido

Preencher após a execução.

### Status

* [ ] PASSOU
* [ ] FALHOU

### Técnica utilizada

* [x] Particionamento de equivalência
* [x] Análise de valor-limite
* [x] Cenário positivo
* [ ] Cenário negativo

### Evidência

Preencher após a execução.

### Observações

Testa o primeiro valor acima da fronteira de 30 dias.

---

# Registro de Defeito

## BUG-01

### Requisito associado

RF01 — Permissão para empréstimo.

### Caso de teste

CT-04 — Usuário com exatamente 3 empréstimos ativos não pode realizar novo empréstimo.

### Entrada utilizada

* usuario_ativo = True
* possui_pendencia = False
* emprestimos_ativos = 3

### Resultado esperado

O empréstimo deve ser recusado, pois o usuário deve possuir menos de 3 empréstimos ativos.

### Resultado obtido

Preencher após a execução.

### Prioridade sugerida

* [x] Alta
* [ ] Média
* [ ] Baixa

### Evidência

Preencher após a execução do teste automatizado.

### Justificativa

O caso testa diretamente o valor-limite do RF01. Caso o sistema permita o empréstimo com exatamente 3 empréstimos ativos, haverá divergência entre o comportamento observado e o requisito especificado.

### Observações

O código de produção não deve ser corrigido durante a atividade. O defeito deve ser apenas registrado e analisado.
