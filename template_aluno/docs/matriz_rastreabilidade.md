# Matriz de Rastreabilidade — BiblioTech

| Requisito | Caso de teste | Descrição | Resultado |
|---|---|---|---|
| RF01 | CT-01 | Usuário ativo, sem pendência e com 0 empréstimos | Passou |
| RF01 | CT-02 | Usuário ativo, sem pendência e com 2 empréstimos | Passou |
| RF01 | CT-03 | Usuário inativo | Passou |
| RF01 | CT-04 | Usuário com pendência | Passou |
| RF01 | CT-05 | Usuário com exatamente 3 empréstimos | Falhou — defeito identificado |
| RF02 | CT-06 | Sem atraso | Passou |
| RF02 | CT-07 | 1 dia de atraso | Passou |
| RF02 | CT-08 | 7 dias de atraso | Passou |
| RF02 | CT-09 | 8 dias de atraso | Passou |
| RF02 | CT-10 | 10 dias de atraso | Passou |
| RF03 | CT-11 | Sem atraso | Passou |
| RF03 | CT-12 | Atraso leve | Passou |
| RF03 | CT-13 | Atraso moderado | Passou |
| RF03 | CT-14 | Atraso grave | Passou |
| RF03 | CT-15 | Atraso negativo | Passou |

## Cobertura dos requisitos

- RF01: coberto por CT-01 a CT-05.
- RF02: coberto por CT-06 a CT-10.
- RF03: coberto por CT-11 a CT-15.

## Observação

O CT-05 identifica uma divergência funcional no limite de 3 empréstimos ativos. Conforme o requisito RF01, usuários devem possuir menos de 3 empréstimos para realizar um novo empréstimo.
