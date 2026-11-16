# Citizen Assist AI — Evidências dos testes

**Disciplina:** Data Structures and Algorithms (DSA)  
**Linguagem:** Python  
**Data da execução registrada:** 16/11/2026  
**Ambiente registrado:** Windows 11 · Python 3.14.5

Este documento complementa `RELATORIO_TESTES.txt` com exemplos de entradas, resultados esperados e resultados observados. Os resultados observados abaixo correspondem aos testes automatizados aprovados em `testes.py` e à execução registrada no relatório.

## Casos de teste representativos

| Caso | Entrada / condição | Resultado esperado | Resultado observado |
|---|---|---|---|
| Cadastro e percurso | Inserir `S3`, `S1` e `S2`, nessa ordem | A lista deve manter os três registros na ordem de inserção e informar tamanho 3 | Aprovado: os três IDs foram percorridos na ordem `S3`, `S1`, `S2`; tamanho 3 |
| Identificador duplicado | Inserir dois serviços com ID `S1` | A segunda inserção deve ser recusada e a lista deve continuar com um registro | Aprovado: ocorreu `ValueError`; tamanho permaneceu 1 |
| Busca por ID existente | Consultar `S1` após preencher a lista de teste | Retornar o serviço com título `Cadastro Único` | Aprovado: serviço encontrado |
| Busca por ID inexistente | Consultar `S99` | Retornar `None`, sem interromper o programa | Aprovado: retorno `None` |
| Pesquisa sem acento | Pesquisar o título pelo termo `unico` | Encontrar `Cadastro Único`, mesmo sem acento na consulta | Aprovado: encontrado o registro `S1` |
| Pesquisa sem resultado | Pesquisar título pelo termo `inexistente` | Retornar uma coleção vazia | Aprovado: nenhum registro retornado |
| Atualização | Atualizar o título de `S1` para `Cadastro atualizado` | O novo título deve ser consultável pelo mesmo ID | Aprovado: título atualizado; ID preservado |
| Atualização inválida | Atualizar o título de `S1` com texto vazio | Recusar a alteração com `ValueError` | Aprovado: alteração recusada |
| Remoção do início | Lista `S3 → S1 → S2`; remover `S3` | A lista deve passar a ser `S1 → S2`, com referências íntegras | Aprovado: ordem e integridade confirmadas |
| Remoção do meio | Lista `S3 → S1 → S2`; remover `S1` | A lista deve passar a ser `S3 → S2`, com referências íntegras | Aprovado: ordem e integridade confirmadas |
| Remoção do final | Lista `S3 → S1 → S2`; remover `S2` | A lista deve passar a ser `S3 → S1`, com `cauda` correta | Aprovado: ordem e integridade confirmadas |
| Selection Sort por título | Títulos `Vacinação`, `Cadastro Único`, `Curso técnico` | Ordenar para `Cadastro Único`, `Curso técnico`, `Vacinação` | Aprovado: sequência ordenada conforme esperado |
| Critério de ordenação inválido | Chamar `ordenar("invalido")` | Recusar o critério com `ValueError` | Aprovado: critério recusado |
| Lista vazia | Ordenar e analisar uma lista sem registros | Não gerar erro; análise deve retornar contagem vazia | Aprovado: lista permaneceu vazia e contagens retornaram `{}` |
| Contagem por categoria | Inserir dois serviços de Saúde, um de Assistência social e um de Educação | Retornar Saúde: 2; Assistência social: 1; Educação: 1 | Aprovado: contagens conferidas |

## Resultado consolidado da execução

Conforme `RELATORIO_TESTES.txt`:

- Arquivos essenciais: aprovado.
- Sintaxe Python: aprovada.
- Teste de integração: aprovado.
- Menu principal: aprovado.
- Testes automatizados: 29 executados, 0 falhas, 0 erros e 0 ignorados.

**Resultado final registrado: 5/5 verificações aprovadas.**

## Como reproduzir

Na pasta do projeto, executar:

```bash
py verificar_projeto.py
```

O comando executa novamente as verificações e atualiza `RELATORIO_TESTES.txt` com a data, a versão do Python, o sistema operacional e o resultado dos testes.
