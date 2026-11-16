# Citizen Assist AI — Global Solution 2026.2

**Disciplina:** Data Structures and Algorithms (DSA)  
**Professor:** Álvaro  
**Linguagem:** Python 3  

## Integrantes

- Kaique Da Silva Assis
- André Debiazzi Baldi Negrini
- Vinicius Cristal de Oliveira

## 1. Objetivo

Protótipo de terminal para cadastrar, consultar, atualizar, excluir, pesquisar e organizar informações demonstrativas sobre serviços e orientações ao cidadão.

O recorte contempla as categorias Saúde, Assistência social, Documentação e cidadania, Educação e qualificação e Serviços urbanos.

**Observação:** apesar do nome Citizen Assist AI, a proposta de DSA não exige IA generativa nem integração com serviços públicos reais. Por isso, esta versão prioriza os requisitos obrigatórios de estruturas de dados e algoritmos. Os registros iniciais são exemplos didáticos e devem ser conferidos em canais oficiais antes de qualquer uso como orientação real.

## 2. Requisitos

- Python 3.9 ou superior.
- Não utiliza bibliotecas externas.

## 3. Como executar

1. Extraia a pasta `CitizenAssistAI`.
2. Abra o terminal dentro dessa pasta.
3. Execute:

```bash
python main.py
```

No Windows, também é possível usar `py main.py`.

O menu será exibido no terminal. O programa inicia com dez registros demonstrativos para facilitar a apresentação. Os novos cadastros feitos durante a execução ficam armazenados na memória e são perdidos quando o programa é encerrado.

## 4. Como executar a verificação e os testes

No terminal, dentro da pasta do projeto, execute:

```bash
python verificar_projeto.py
```

No Windows, também é possível usar:

```bash
py verificar_projeto.py
```

O verificador:

1. Confere se os arquivos essenciais estão presentes.
2. Verifica a sintaxe dos arquivos Python.
3. Executa um fluxo de integração com cadastro, busca, pesquisa, atualização, ordenação, exclusão e análise.
4. Executa os testes automatizados de `testes.py`.
5. Cria o arquivo `RELATORIO_TESTES.txt` na própria pasta.

Envie esse relatório junto com qualquer mensagem de erro apresentada no terminal para que o projeto possa ser revisado.

Para executar somente os testes automatizados:

```bash
python -m unittest -v testes
```

## 5. Organização dos arquivos

| Arquivo | Responsabilidade |
|---|---|
| `main.py` | Menu interativo e operações solicitadas pelo usuário. |
| `modelos.py` | Classes `Servico` e validação dos dados. |
| `lista_encadeada.py` | Classes `No` e `ListaEncadeada`, busca, remoção, percurso, ordenação e análise. |
| `dados_exemplo.py` | Dez registros demonstrativos para a apresentação. |
| `testes.py` | Testes automatizados com `unittest`. |
| `EVIDENCIAS_TESTES.md` | Exemplos de entradas, resultados esperados e observados dos testes. |
| `verificar_projeto.py` | Executa verificações e gera o relatório de testes. |

## 6. Estrutura de dados

A classe `No` armazena um objeto `Servico` e uma referência `proximo` para o nó seguinte. A classe `ListaEncadeada` mantém referências para `cabeca` e `cauda`, além de um contador `tamanho`.

A lista encadeada é a estrutura principal de armazenamento dos serviços. Listas auxiliares são usadas apenas para devolver resultados de pesquisa e não substituem a estrutura exigida.

## 7. Algoritmos e complexidade

A busca por identificador é **busca sequencial**: começa na `cabeca`, compara o ID do nó atual com o ID procurado e avança pela referência `proximo` até encontrar o registro ou chegar ao fim da lista. A pesquisa por título ou categoria também percorre os nós sequencialmente e verifica se o termo informado aparece no campo escolhido.

A ordenação utiliza **Selection Sort**: em cada posição, percorre o trecho ainda não ordenado para localizar o menor valor segundo o critério escolhido; depois troca os objetos `Servico` entre os nós e avança para a próxima posição. O algoritmo foi implementado com laços próprios, sem `sort()` ou `sorted()`.

Considere `n` como a quantidade de nós da lista.

| Operação | Complexidade | Justificativa |
|---|---:|---|
| Inserção no final | O(1) | A referência `cauda` permite ligar o novo nó diretamente ao último. A verificação de ID duplicado percorre a lista, portanto o cadastro completo com essa validação custa O(n). |
| Busca por ID | O(n) | No pior caso, todos os nós são percorridos. |
| Pesquisa por título ou categoria | O(n) | Cada nó é verificado uma vez; o custo de comparar o texto depende do tamanho dos campos. |
| Atualização | O(n) | Primeiro localiza o ID por busca sequencial; alterar os campos encontrados custa O(1). |
| Remoção | O(n) | Pode ser necessário percorrer a lista até localizar o nó. |
| Percurso | O(n) | Cada nó é visitado uma vez. |
| Selection Sort | O(n²) | Para cada posição, procura o menor elemento no trecho restante. |
| Contagem por categoria | O(n) | Percorre todos os nós e atualiza um dicionário de contagens. |

O método de ordenação foi implementado manualmente, sem utilizar `sort()` ou `sorted()`.

## 8. Validações e testes

O sistema trata identificadores duplicados, campos obrigatórios vazios, opções inválidas no menu, pesquisa sem resultados e exclusão/consulta de identificadores inexistentes. A remoção contempla nós no início, no meio, no fim e o único nó da lista.

Os testes automatizados cobrem criação de serviços, operações da lista, busca, pesquisa, atualização, remoção, Selection Sort, contagem por categoria e integridade dos ponteiros e do tamanho. A documentação `EVIDENCIAS_TESTES.md` reúne exemplos de entradas, resultados esperados e observados.

## 9. Limitações desta versão

- Os registros são mantidos apenas em memória durante a execução; não há persistência em arquivo ou banco de dados.
- Não há integração com APIs de órgãos públicos.
- Não há IA generativa, pois ela não é requisito obrigatório do enunciado de DSA.
- Os registros demonstrativos não devem ser tratados como orientação oficial atualizada.
