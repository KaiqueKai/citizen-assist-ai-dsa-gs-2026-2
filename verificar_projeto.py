"""Executa verificações e gera RELATORIO_TESTES.txt para conferência do projeto."""

import contextlib
import io
import platform
import subprocess
import sys
import unittest
from datetime import datetime
from pathlib import Path

import compileall

from lista_encadeada import ListaEncadeada
from modelos import Servico
from dados_exemplo import carregar_dados_exemplo


PASTA = Path(__file__).resolve().parent
ARQUIVO_RELATORIO = PASTA / "RELATORIO_TESTES.txt"


def verificar_arquivos_essenciais():
    arquivos = [
        "main.py",
        "modelos.py",
        "lista_encadeada.py",
        "dados_exemplo.py",
        "testes.py",
        "README.md",
    ]
    ausentes = [nome for nome in arquivos if not (PASTA / nome).is_file()]
    return not ausentes, ausentes


def testar_integracao():
    """Executa um fluxo de ponta a ponta usando a lista encadeada real."""
    lista = ListaEncadeada()
    total_exemplos = carregar_dados_exemplo(lista)
    assert total_exemplos == 10
    assert len(lista) == 10
    assert lista.buscar_por_id("S001") is not None
    assert len(lista.pesquisar("titulo", "consulta")) == 1
    assert lista.atualizar("S001", titulo="Agendamento atualizado") is True
    assert lista.buscar_por_id("S001").titulo == "Agendamento atualizado"
    lista.ordenar("titulo")
    titulos = [servico.titulo.casefold() for servico in lista]
    assert titulos == sorted(titulos)
    assert lista.remover("S010") is True
    assert lista.buscar_por_id("S010") is None
    assert sum(lista.contar_por_categoria().values()) == 9
    assert lista.verificar_integridade() is True
    return "Cadastro de exemplos, busca, pesquisa, atualização, ordenação, exclusão e análise"


def testar_menu_principal():
    """Abre o programa real com entradas simuladas e confirma o encerramento."""
    processo = subprocess.run(
        [sys.executable, str(PASTA / "main.py")],
        input="7\n0\n",
        text=True,
        capture_output=True,
        cwd=str(PASTA),
        timeout=15,
        check=False,
    )
    if processo.returncode != 0:
        detalhe = processo.stderr.strip() or f"Código de saída: {processo.returncode}"
        raise RuntimeError(detalhe)
    if "Total de registros: 10" not in processo.stdout:
        raise RuntimeError("O menu não apresentou a análise esperada dos dez registros.")
    if "Sistema encerrado" not in processo.stdout:
        raise RuntimeError("O menu não encerrou corretamente.")
    return "Menu principal iniciado, análise exibida e encerramento confirmado"


def main():
    resultados = []
    linhas = []
    linhas.append("CITIZEN ASSIST AI - RELATÓRIO AUTOMÁTICO DE VERIFICAÇÃO")
    linhas.append("=" * 62)
    linhas.append(f"Data/hora da execução: {datetime.now().astimezone().isoformat(timespec='seconds')}")
    linhas.append(f"Python: {platform.python_version()}")
    linhas.append(f"Sistema: {platform.platform()}")
    linhas.append("")

    arquivos_ok, ausentes = verificar_arquivos_essenciais()
    resultados.append(("Arquivos essenciais", arquivos_ok,
                       "Todos os arquivos encontrados." if arquivos_ok
                       else "Arquivos ausentes: " + ", ".join(ausentes)))

    sintaxe_ok = compileall.compile_dir(str(PASTA), quiet=1, force=True)
    resultados.append(("Verificação de sintaxe Python", sintaxe_ok,
                       "Arquivos Python compilados sem erros." if sintaxe_ok
                       else "Foi encontrado erro de sintaxe em arquivo Python."))

    fluxo_ok = False
    fluxo_detalhe = ""
    try:
        fluxo_detalhe = testar_integracao()
        fluxo_ok = True
    except Exception as erro:  # O relatório deve registrar falhas em vez de fechar sem explicação.
        fluxo_detalhe = f"{type(erro).__name__}: {erro}"
    resultados.append(("Teste de integração", fluxo_ok, fluxo_detalhe))

    menu_ok = False
    menu_detalhe = ""
    try:
        menu_detalhe = testar_menu_principal()
        menu_ok = True
    except Exception as erro:
        menu_detalhe = f"{type(erro).__name__}: {erro}"
    resultados.append(("Teste do menu principal", menu_ok, menu_detalhe))

    fluxo_testes = io.StringIO()
    suite = unittest.defaultTestLoader.discover(
        start_dir=str(PASTA), pattern="testes.py", top_level_dir=str(PASTA)
    )
    with contextlib.redirect_stdout(fluxo_testes), contextlib.redirect_stderr(fluxo_testes):
        resultado_testes = unittest.TextTestRunner(
            stream=fluxo_testes, verbosity=2
        ).run(suite)
    testes_ok = resultado_testes.wasSuccessful()
    resumo = (
        f"Executados: {resultado_testes.testsRun}; "
        f"falhas: {len(resultado_testes.failures)}; "
        f"erros: {len(resultado_testes.errors)}; "
        f"ignorados: {len(resultado_testes.skipped)}."
    )
    resultados.append(("Testes automatizados (unittest)", testes_ok, resumo))

    linhas.append("RESULTADOS")
    linhas.append("-" * 62)
    for nome, passou, detalhe in resultados:
        status = "APROVADO" if passou else "FALHOU"
        linhas.append(f"[{status}] {nome}")
        linhas.append(f"  {detalhe}")
    linhas.append("")
    linhas.append("DETALHES DOS TESTES AUTOMATIZADOS")
    linhas.append("-" * 62)
    linhas.append(fluxo_testes.getvalue().strip() or "Nenhuma saída de teste foi produzida.")
    linhas.append("")

    total_ok = sum(1 for _, passou, _ in resultados if passou)
    total = len(resultados)
    aprovado = total_ok == total
    linhas.append("RESULTADO FINAL: " + ("TODAS AS VERIFICAÇÕES PASSARAM" if aprovado
                                        else "EXISTEM VERIFICAÇÕES QUE FALHARAM"))
    linhas.append(f"Verificações aprovadas: {total_ok}/{total}")

    conteudo = "\n".join(linhas) + "\n"
    ARQUIVO_RELATORIO.write_text(conteudo, encoding="utf-8")

    print("\n" + "=" * 62)
    print("CITIZEN ASSIST AI - VERIFICAÇÃO DO PROJETO")
    print("=" * 62)
    for nome, passou, detalhe in resultados:
        print(f"[{'OK' if passou else 'ERRO'}] {nome}: {detalhe}")
    print("-" * 62)
    print(f"Testes unitários: {resumo}")
    print("RESULTADO FINAL:", "APROVADO" if aprovado else "REVISAR FALHAS")
    print(f"Relatório salvo em: {ARQUIVO_RELATORIO}")
    print("Envie o arquivo RELATORIO_TESTES.txt para revisão.")

    return 0 if aprovado else 1


if __name__ == "__main__":
    raise SystemExit(main())
