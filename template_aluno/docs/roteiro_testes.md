# Roteiro de Testes — BiblioTech

# CT-01

## Requisito

RF01

## Título

Empréstimo permitido para usuário ativo sem pendência e com 0 empréstimos

## Tipo

- [x] Caixa Preta
- [ ] Caixa Branca

## Prioridade

- [x] Alta
- [ ] Média
- [ ] Baixa

## Objetivo

Verificar se um usuário ativo, sem pendências e com nenhum empréstimo ativo pode realizar um novo empréstimo.

## Pré-condições

Usuário cadastrado e apto para realizar empréstimo.

## Dados de teste

- usuario_ativo = True
- possui_pendencia = False
- emprestimos_ativos = 0

## Passos

1. Informar os dados do usuário.
2. Solicitar um novo empréstimo.
3. Verificar o resultado.

## Resultado esperado

O empréstimo deve ser permitido.

## Resultado obtido

Preencher após a execução.

## Status

- [ ] PASSOU
- [ ] FALHOU

## Técnica utilizada

- [x] Particionamento de equivalência
- [ ] Análise de valor-limite
- [x] Cenário positivo
- [ ] Cenário negativo

## Evidência

Saída do pytest.

## Observações

- Cenário válido.

---

# CT-02

## Requisito

RF01

## Título

Empréstimo recusado para usuário inativo

## Tipo

- [x] Caixa Preta
- [ ] Caixa Branca

## Prioridade

- [x] Alta
- [ ] Média
- [ ] Baixa

## Objetivo

Verificar se um usuário inativo tem o empréstimo recusado.

## Pré-condições

Usuário cadastrado como inativo.

## Dados de teste

- usuario_ativo = False
- possui_pendencia = False
- emprestimos_ativos = 0

## Passos

1. Informar os dados do usuário.
2. Solicitar um novo empréstimo.
3. Verificar o resultado.

## Resultado esperado

O empréstimo deve ser recusado.

## Resultado obtido

Preencher após a execução.

## Status

- [ ] PASSOU
- [ ] FALHOU

## Técnica utilizada

- [x] Particionamento de equivalência
- [ ] Análise de valor-limite
- [ ] Cenário positivo
- [x] Cenário negativo

## Evidência

Saída do pytest.

## Observações

- Usuário inativo.

---

# CT-03

## Requisito

RF01

## Título

Empréstimo recusado para usuário com pendência

## Tipo

- [x] Caixa Preta
- [ ] Caixa Branca

## Prioridade

- [x] Alta
- [ ] Média
- [ ] Baixa

## Objetivo

Verificar se um usuário com pendência não pode realizar novo empréstimo.

## Pré-condições

Usuário ativo com pendência registrada.

## Dados de teste

- usuario_ativo = True
- possui_pendencia = True
- emprestimos_ativos = 0

## Passos

1. Informar os dados do usuário.
2. Solicitar um novo empréstimo.
3. Verificar o resultado.

## Resultado esperado

O empréstimo deve ser recusado.

## Resultado obtido

Preencher após a execução.

## Status

- [ ] PASSOU
- [ ] FALHOU

## Técnica utilizada

- [x] Particionamento de equivalência
- [ ] Análise de valor-limite
- [ ] Cenário positivo
- [x] Cenário negativo

## Evidência

Saída do pytest.

## Observações

- Usuário possui pendência.

---

# CT-04

## Requisito

RF01

## Título

Fronteira de 3 empréstimos ativos

## Tipo

- [x] Caixa Preta
- [ ] Caixa Branca

## Prioridade

- [x] Alta
- [ ] Média
- [ ] Baixa

## Objetivo

Verificar o comportamento na fronteira do limite máximo permitido de empréstimos ativos.

## Pré-condições

Usuário ativo e sem pendências.

## Dados de teste

- usuario_ativo = True
- possui_pendencia = False
- emprestimos_ativos = 3

## Passos

1. Informar os dados do usuário.
2. Solicitar um novo empréstimo.
3. Verificar o resultado.

## Resultado esperado

O empréstimo deve ser recusado, pois o requisito determina que o usuário deve possuir menos de 3 empréstimos ativos.

## Resultado obtido

Preencher após a execução.

## Status

- [ ] PASSOU
- [ ] FALHOU

## Técnica utilizada

- [ ] Particionamento de equivalência
- [x] Análise de valor-limite
- [ ] Cenário positivo
- [x] Cenário negativo

## Evidência

Saída do pytest e mensagem de falha, caso ocorra.

## Observações

- Caso de fronteira do RF01.

---

# CT-05

## Requisito

RF02

## Título

Sem atraso

## Tipo

- [x] Caixa Preta
- [ ] Caixa Branca

## Prioridade

- [x] Alta
- [ ] Média
- [ ] Baixa

## Objetivo

Verificar se não há multa quando não existe atraso.

## Pré-condições

Empréstimo encerrado sem atraso.

## Dados de teste

- dias_atraso = 0

## Passos

1. Informar 0 dias de atraso.
2. Calcular a multa.
3. Verificar o valor retornado.

## Resultado esperado

A multa deve ser R$ 0,00.

## Resultado obtido

Preencher após a execução.

## Status

- [ ] PASSOU
- [ ] FALHOU

## Técnica utilizada

- [x] Particionamento de equivalência
- [x] Análise de valor-limite
- [x] Cenário positivo
- [ ] Cenário negativo

## Evidência

Saída do pytest.

## Observações

- Fronteira inferior.

---

# CT-06

## Requisito

RF02

## Título

Multa no primeiro dia de atraso

## Tipo

- [x] Caixa Preta
- [ ] Caixa Branca

## Prioridade

- [x] Alta
- [ ] Média
- [ ] Baixa

## Objetivo

Verificar o início da faixa de cobrança de multa.

## Pré-condições

Empréstimo com atraso.

## Dados de teste

- dias_atraso = 1

## Passos

1. Informar 1 dia de atraso.
2. Calcular a multa.
3. Verificar o valor retornado.

## Resultado esperado

A multa deve ser R$ 2,00.

## Resultado obtido

Preencher após a execução.

## Status

- [ ] PASSOU
- [ ] FALHOU

## Técnica utilizada

- [ ] Particionamento de equivalência
- [x] Análise de valor-limite
- [x] Cenário positivo
- [ ] Cenário negativo

## Evidência

Saída do pytest.

## Observações

- Início da faixa de 1 a 7 dias.

---

# CT-07

## Requisito

RF02

## Título

Multa no limite de 7 dias

## Tipo

- [x] Caixa Preta
- [ ] Caixa Branca

## Prioridade

- [x] Alta
- [ ] Média
- [ ] Baixa

## Objetivo

Verificar o valor da multa exatamente no limite superior da primeira faixa.

## Pré-condições

Empréstimo com atraso de 7 dias.

## Dados de teste

- dias_atraso = 7

## Passos

1. Informar 7 dias de atraso.
2. Calcular a multa.
3. Verificar o valor retornado.

## Resultado esperado

A multa deve ser R$ 14,00.

## Resultado obtido

Preencher após a execução.

## Status

- [ ] PASSOU
- [ ] FALHOU

## Técnica utilizada

- [ ] Particionamento de equivalência
- [x] Análise de valor-limite
- [x] Cenário positivo
- [ ] Cenário negativo

## Evidência

Saída do pytest.

## Observações

- Fronteira entre as duas faixas de multa.

---

# CT-08

## Requisito

RF02

## Título

Multa após 7 dias de atraso

## Tipo

- [x] Caixa Preta
- [ ] Caixa Branca

## Prioridade

- [x] Alta
- [ ] Média
- [ ] Baixa

## Objetivo

Verificar o cálculo da multa quando o atraso ultrapassa 7 dias.

## Pré-condições

Empréstimo com atraso superior a 7 dias.

## Dados de teste

- dias_atraso = 8

## Passos

1. Informar 8 dias de atraso.
2. Calcular a multa.
3. Verificar o valor retornado.

## Resultado esperado

A multa deve ser R$ 17,00.

## Resultado obtido

Preencher após a execução.

## Status

- [ ] PASSOU
- [ ] FALHOU

## Técnica utilizada

- [x] Particionamento de equivalência
- [x] Análise de valor-limite
- [x] Cenário positivo
- [ ] Cenário negativo

## Evidência

Saída do pytest.

## Observações

- Primeiro valor da faixa acima de 7 dias.

---

# CT-09

## Requisito

RF03

## Título

Classificação sem atraso

## Tipo

- [x] Caixa Preta
- [ ] Caixa Branca

## Prioridade

- [x] Alta
- [ ] Média
- [ ] Baixa

## Objetivo

Verificar a classificação quando não há atraso.

## Pré-condições

Empréstimo sem atraso.

## Dados de teste

- dias_atraso = 0

## Passos

1. Informar 0 dias de atraso.
2. Classificar o atraso.
3. Verificar o resultado.

## Resultado esperado

A classificação deve ser "sem atraso".

## Resultado obtido

Preencher após a execução.

## Status

- [ ] PASSOU
- [ ] FALHOU

## Técnica utilizada

- [x] Particionamento de equivalência
- [x] Análise de valor-limite
- [x] Cenário positivo
- [ ] Cenário negativo

## Evidência

Saída do pytest.

## Observações

- Fronteira de ausência de atraso.

---

# CT-10

## Requisito

RF03

## Título

Classificação de atraso leve

## Tipo

- [x] Caixa Preta
- [ ] Caixa Branca

## Prioridade

- [x] Alta
- [ ] Média
- [ ] Baixa

## Objetivo

Verificar a classificação para atrasos entre 1 e 7 dias.

## Pré-condições

Empréstimo com atraso.

## Dados de teste

- dias_atraso = 7

## Passos

1. Informar 7 dias de atraso.
2. Classificar o atraso.
3. Verificar o resultado.

## Resultado esperado

A classificação deve ser "atraso leve".

## Resultado obtido

Preencher após a execução.

## Status

- [ ] PASSOU
- [ ] FALHOU

## Técnica utilizada

- [ ] Particionamento de equivalência
- [x] Análise de valor-limite
- [x] Cenário positivo
- [ ] Cenário negativo

## Evidência

Saída do pytest.

## Observações

- Limite superior do atraso leve.

---

# CT-11

## Requisito

RF03

## Título

Classificação de atraso moderado

## Tipo

- [x] Caixa Preta
- [ ] Caixa Branca

## Prioridade

- [x] Alta
- [ ] Média
- [ ] Baixa

## Objetivo

Verificar a classificação para atrasos entre 8 e 30 dias.

## Pré-condições

Empréstimo com atraso.

## Dados de teste

- dias_atraso = 30

## Passos

1. Informar 30 dias de atraso.
2. Classificar o atraso.
3. Verificar o resultado.

## Resultado esperado

A classificação deve ser "atraso moderado".

## Resultado obtido

Preencher após a execução.

## Status

- [ ] PASSOU
- [ ] FALHOU

## Técnica utilizada

- [ ] Particionamento de equivalência
- [x] Análise de valor-limite
- [x] Cenário positivo
- [ ] Cenário negativo

## Evidência

Saída do pytest.

## Observações

- Limite superior do atraso moderado.

---

# CT-12

## Requisito

RF03

## Título

Classificação de atraso grave

## Tipo

- [x] Caixa Preta
- [ ] Caixa Branca

## Prioridade

- [x] Alta
- [ ] Média
- [ ] Baixa

## Objetivo

Verificar a classificação para atrasos superiores a 30 dias.

## Pré-condições

Empréstimo com atraso superior a 30 dias.

## Dados de teste

- dias_atraso = 31

## Passos

1. Informar 31 dias de atraso.
2. Classificar o atraso.
3. Verificar o resultado.

## Resultado esperado

A classificação deve ser "atraso grave".

## Resultado obtido

Preencher após a execução.

## Status

- [ ] PASSOU
- [ ] FALHOU

## Técnica utilizada

- [x] Particionamento de equivalência
- [x] Análise de valor-limite
- [x] Cenário positivo
- [ ] Cenário negativo

## Evidência

Saída do pytest.

## Observações

- Primeiro valor da faixa de atraso grave.
