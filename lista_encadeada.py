"""Implementação própria de lista simplesmente encadeada e algoritmos."""

import unicodedata

from modelos import Servico


class No:
    """Nó que guarda um serviço e uma referência para o próximo nó."""

    def __init__(self, servico):
        if not isinstance(servico, Servico):
            raise TypeError("O nó deve armazenar um objeto da classe Servico.")
        self.servico = servico
        self.proximo = None


class ListaEncadeada:
    """Lista simplesmente encadeada com referência ao primeiro e ao último nó."""

    def __init__(self):
        self.cabeca = None
        self.cauda = None
        self.tamanho = 0

    def __len__(self):
        return self.tamanho

    def esta_vazia(self):
        return self.cabeca is None

    @staticmethod
    def _normalizar(texto):
        texto = unicodedata.normalize("NFD", str(texto).casefold())
        return "".join(caractere for caractere in texto
                       if unicodedata.category(caractere) != "Mn")

    def inserir(self, servico):
        """Insere no final em O(1), mantendo identificadores únicos."""
        if not isinstance(servico, Servico):
            raise TypeError("É necessário inserir um objeto da classe Servico.")
        if self.buscar_por_id(servico.identificador) is not None:
            raise ValueError(f"Já existe um serviço com o ID {servico.identificador}.")

        novo_no = No(servico)
        if self.esta_vazia():
            self.cabeca = novo_no
            self.cauda = novo_no
        else:
            self.cauda.proximo = novo_no
            self.cauda = novo_no
        self.tamanho += 1
        return True

    def buscar_por_id(self, identificador):
        atual = self.cabeca
        procurado = self._normalizar(identificador)
        while atual is not None:
            if self._normalizar(atual.servico.identificador) == procurado:
                return atual.servico
            atual = atual.proximo
        return None

    def pesquisar(self, atributo, termo):
        """Pesquisa por trecho do título ou da categoria (sem diferenciar acentos)."""
        if atributo not in ("titulo", "categoria"):
            raise ValueError("A pesquisa deve utilizar 'titulo' ou 'categoria'.")
        termo_normalizado = self._normalizar(termo)
        if not termo_normalizado:
            return []

        encontrados = []
        atual = self.cabeca
        while atual is not None:
            valor = self._normalizar(getattr(atual.servico, atributo))
            if termo_normalizado in valor:
                encontrados.append(atual.servico)
            atual = atual.proximo
        return encontrados

    def atualizar(self, identificador, **campos):
        servico = self.buscar_por_id(identificador)
        if servico is None:
            return False
        servico.atualizar(**campos)
        return True

    def remover(self, identificador):
        """Remove um nó, tratando separadamente início, meio e fim da lista."""
        procurado = self._normalizar(identificador)
        anterior = None
        atual = self.cabeca

        while atual is not None:
            if self._normalizar(atual.servico.identificador) == procurado:
                if anterior is None:
                    self.cabeca = atual.proximo
                else:
                    anterior.proximo = atual.proximo

                if atual is self.cauda:
                    self.cauda = anterior

                self.tamanho -= 1
                if self.tamanho == 0:
                    self.cabeca = None
                    self.cauda = None
                atual.proximo = None
                return True

            anterior = atual
            atual = atual.proximo
        return False

    def percorrer(self):
        """Percorre os nós em sequência, sem copiar a estrutura de armazenamento."""
        atual = self.cabeca
        while atual is not None:
            yield atual.servico
            atual = atual.proximo

    def ordenar(self, criterio="titulo"):
        """Ordena por Selection Sort, trocando os dados armazenados nos nós."""
        if criterio not in ("titulo", "categoria", "identificador"):
            raise ValueError("Critério inválido para ordenação.")

        inicio = self.cabeca
        while inicio is not None:
            menor = inicio
            candidato = inicio.proximo
            while candidato is not None:
                chave_candidato = self._normalizar(
                    getattr(candidato.servico, criterio)
                )
                chave_menor = self._normalizar(getattr(menor.servico, criterio))
                if chave_candidato < chave_menor:
                    menor = candidato
                candidato = candidato.proximo

            if menor is not inicio:
                inicio.servico, menor.servico = menor.servico, inicio.servico
            inicio = inicio.proximo

    def contar_por_categoria(self):
        contagens = {}
        atual = self.cabeca
        while atual is not None:
            categoria = atual.servico.categoria
            contagens[categoria] = contagens.get(categoria, 0) + 1
            atual = atual.proximo
        return contagens

    def verificar_integridade(self):
        """Confere quantidade, encadeamento e referência ao último nó."""
        quantidade = 0
        ultimo = None
        atual = self.cabeca
        while atual is not None:
            quantidade += 1
            ultimo = atual
            atual = atual.proximo

        if quantidade != self.tamanho:
            return False
        if ultimo is not self.cauda:
            return False
        if self.tamanho == 0 and (self.cabeca is not None or self.cauda is not None):
            return False
        if self.tamanho > 0 and (self.cabeca is None or self.cauda is None):
            return False
        return True

    def __iter__(self):
        return self.percorrer()
