"""Testes automatizados das classes, operações e algoritmos do projeto."""

import unittest

from lista_encadeada import ListaEncadeada
from modelos import Servico


def criar_servico(identificador, titulo, categoria="Saúde"):
    return Servico(
        identificador,
        titulo,
        categoria,
        f"Descrição de {titulo}",
        "Documento de identificação",
        "Unidade de atendimento",
    )


class TestesServico(unittest.TestCase):
    def test_criacao_de_servico(self):
        servico = criar_servico("S1", "Consulta")
        self.assertEqual(servico.identificador, "S1")
        self.assertEqual(servico.titulo, "Consulta")

    def test_identificador_obrigatorio(self):
        with self.assertRaises(ValueError):
            Servico("", "Título", "Saúde", "Descrição")

    def test_campos_obrigatorios(self):
        with self.assertRaises(ValueError):
            Servico("S1", "", "Saúde", "Descrição")

    def test_atualizacao_de_servico(self):
        servico = criar_servico("S1", "Consulta")
        servico.atualizar(titulo="Consulta especializada")
        self.assertEqual(servico.titulo, "Consulta especializada")

    def test_identificador_nao_pode_ser_atualizado(self):
        servico = criar_servico("S1", "Consulta")
        with self.assertRaises(ValueError):
            servico.atualizar(identificador="S2")


class TestesListaEncadeada(unittest.TestCase):
    def setUp(self):
        self.lista = ListaEncadeada()

    def preencher(self):
        self.lista.inserir(criar_servico("S3", "Vacinação", "Saúde"))
        self.lista.inserir(criar_servico("S1", "Cadastro Único", "Assistência social"))
        self.lista.inserir(criar_servico("S2", "Curso técnico", "Educação"))

    def test_lista_inicia_vazia(self):
        self.assertTrue(self.lista.esta_vazia())
        self.assertEqual(len(self.lista), 0)
        self.assertTrue(self.lista.verificar_integridade())

    def test_insercao_e_percurso(self):
        self.preencher()
        self.assertEqual(len(self.lista), 3)
        self.assertEqual([s.identificador for s in self.lista], ["S3", "S1", "S2"])
        self.assertTrue(self.lista.verificar_integridade())

    def test_insercao_com_id_duplicado(self):
        self.lista.inserir(criar_servico("S1", "Primeiro"))
        with self.assertRaises(ValueError):
            self.lista.inserir(criar_servico("S1", "Duplicado"))
        self.assertEqual(len(self.lista), 1)

    def test_busca_por_id_existente_e_inexistente(self):
        self.preencher()
        self.assertEqual(self.lista.buscar_por_id("S1").titulo, "Cadastro Único")
        self.assertIsNone(self.lista.buscar_por_id("S99"))

    def test_busca_por_id_ignora_maiusculas(self):
        self.lista.inserir(criar_servico("abc", "Consulta"))
        self.assertIsNotNone(self.lista.buscar_por_id("ABC"))

    def test_pesquisa_por_titulo_ignora_acentos(self):
        self.preencher()
        encontrados = self.lista.pesquisar("titulo", "unico")
        self.assertEqual([s.identificador for s in encontrados], ["S1"])

    def test_pesquisa_por_categoria(self):
        self.preencher()
        encontrados = self.lista.pesquisar("categoria", "saúde")
        self.assertEqual([s.identificador for s in encontrados], ["S3"])

    def test_pesquisa_sem_resultado(self):
        self.preencher()
        self.assertEqual(self.lista.pesquisar("titulo", "inexistente"), [])

    def test_pesquisa_com_atributo_invalido(self):
        with self.assertRaises(ValueError):
            self.lista.pesquisar("descricao", "texto")

    def test_atualizacao_existente_e_inexistente(self):
        self.preencher()
        self.assertTrue(self.lista.atualizar("S1", titulo="Cadastro atualizado"))
        self.assertEqual(self.lista.buscar_por_id("S1").titulo, "Cadastro atualizado")
        self.assertFalse(self.lista.atualizar("S99", titulo="Não existe"))

    def test_atualizacao_nao_aceita_titulo_vazio(self):
        self.preencher()
        with self.assertRaises(ValueError):
            self.lista.atualizar("S1", titulo="   ")

    def test_remocao_do_inicio(self):
        self.preencher()
        self.assertTrue(self.lista.remover("S3"))
        self.assertEqual([s.identificador for s in self.lista], ["S1", "S2"])
        self.assertTrue(self.lista.verificar_integridade())

    def test_remocao_do_meio(self):
        self.preencher()
        self.assertTrue(self.lista.remover("S1"))
        self.assertEqual([s.identificador for s in self.lista], ["S3", "S2"])
        self.assertTrue(self.lista.verificar_integridade())

    def test_remocao_do_final(self):
        self.preencher()
        self.assertTrue(self.lista.remover("S2"))
        self.assertEqual([s.identificador for s in self.lista], ["S3", "S1"])
        self.assertTrue(self.lista.verificar_integridade())

    def test_remocao_do_unico_elemento(self):
        self.lista.inserir(criar_servico("S1", "Consulta"))
        self.assertTrue(self.lista.remover("S1"))
        self.assertTrue(self.lista.esta_vazia())
        self.assertTrue(self.lista.verificar_integridade())

    def test_remocao_inexistente(self):
        self.assertFalse(self.lista.remover("S99"))
        self.assertTrue(self.lista.verificar_integridade())

    def test_selection_sort_por_titulo(self):
        self.preencher()
        self.lista.ordenar("titulo")
        titulos = [s.titulo for s in self.lista]
        self.assertEqual(titulos, ["Cadastro Único", "Curso técnico", "Vacinação"])
        self.assertTrue(self.lista.verificar_integridade())

    def test_selection_sort_por_categoria(self):
        self.preencher()
        self.lista.ordenar("categoria")
        categorias = [s.categoria for s in self.lista]
        self.assertEqual(categorias, ["Assistência social", "Educação", "Saúde"])

    def test_selection_sort_por_id(self):
        self.preencher()
        self.lista.ordenar("identificador")
        ids = [s.identificador for s in self.lista]
        self.assertEqual(ids, ["S1", "S2", "S3"])

    def test_ordenacao_com_criterio_invalido(self):
        with self.assertRaises(ValueError):
            self.lista.ordenar("invalido")

    def test_ordenacao_de_lista_vazia(self):
        self.lista.ordenar("titulo")
        self.assertTrue(self.lista.esta_vazia())

    def test_contagem_por_categoria(self):
        self.preencher()
        self.lista.inserir(criar_servico("S4", "Retirada de medicamento", "Saúde"))
        self.assertEqual(
            self.lista.contar_por_categoria(),
            {"Saúde": 2, "Assistência social": 1, "Educação": 1},
        )

    def test_lista_vazia_sem_contagens(self):
        self.assertEqual(self.lista.contar_por_categoria(), {})

    def test_integridade_apos_varias_operacoes(self):
        self.preencher()
        self.lista.ordenar("titulo")
        self.lista.remover("S1")
        self.lista.inserir(criar_servico("S4", "Novo serviço"))
        self.assertTrue(self.lista.verificar_integridade())
        self.assertEqual(len(self.lista), 3)


if __name__ == "__main__":
    unittest.main(verbosity=2)
