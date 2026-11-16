"""Interface de terminal do Citizen Assist AI."""

from dados_exemplo import carregar_dados_exemplo
from lista_encadeada import ListaEncadeada
from modelos import Servico


def exibir_servico(servico):
    print("\n" + "-" * 48)
    print(servico)
    print("-" * 48)


def ler_obrigatorio(mensagem):
    while True:
        valor = input(mensagem).strip()
        if valor:
            return valor
        print("Este campo é obrigatório. Tente novamente.")


def cadastrar_servico(lista):
    print("\n--- CADASTRAR SERVIÇO ---")
    identificador = ler_obrigatorio("Identificador único (ex.: S011): ")
    titulo = ler_obrigatorio("Título: ")
    categoria = ler_obrigatorio("Categoria: ")
    descricao = ler_obrigatorio("Descrição: ")
    requisitos = input("Requisitos (Enter para não informado): ").strip()
    local = input("Local de atendimento (Enter para não informado): ").strip()

    try:
        servico = Servico(identificador, titulo, categoria, descricao, requisitos, local)
        lista.inserir(servico)
        print("Serviço cadastrado com sucesso.")
    except (ValueError, TypeError) as erro:
        print(f"Não foi possível cadastrar: {erro}")


def consultar_servico(lista):
    identificador = input("Digite o ID do serviço: ").strip()
    servico = lista.buscar_por_id(identificador)
    if servico is None:
        print("Nenhum serviço encontrado com esse ID.")
    else:
        exibir_servico(servico)


def atualizar_servico(lista):
    identificador = input("Digite o ID do serviço que deseja atualizar: ").strip()
    servico = lista.buscar_por_id(identificador)
    if servico is None:
        print("Nenhum serviço encontrado com esse ID.")
        return

    exibir_servico(servico)
    print("\nPressione Enter para manter o valor atual.")
    campos = {}
    for campo, rotulo in (
        ("titulo", "Novo título"),
        ("categoria", "Nova categoria"),
        ("descricao", "Nova descrição"),
        ("requisitos", "Novos requisitos"),
        ("local_atendimento", "Novo local de atendimento"),
    ):
        atual = getattr(servico, campo)
        novo = input(f"{rotulo} [{atual}]: ").strip()
        if novo:
            campos[campo] = novo

    try:
        if not campos:
            print("Nenhuma alteração informada.")
        else:
            lista.atualizar(identificador, **campos)
            print("Serviço atualizado com sucesso.")
    except ValueError as erro:
        print(f"Não foi possível atualizar: {erro}")


def excluir_servico(lista):
    identificador = input("Digite o ID do serviço que deseja excluir: ").strip()
    if lista.buscar_por_id(identificador) is None:
        print("Nenhum serviço encontrado com esse ID.")
        return
    confirmacao = input("Confirma a exclusão? (s/N): ").strip().casefold()
    if confirmacao == "s":
        if lista.remover(identificador):
            print("Serviço excluído com sucesso.")
        else:
            print("Não foi possível excluir o serviço.")
    else:
        print("Exclusão cancelada.")


def pesquisar_servicos(lista):
    print("\nPesquisar por: 1 - Título | 2 - Categoria")
    opcao = input("Escolha: ").strip()
    atributos = {"1": "titulo", "2": "categoria"}
    if opcao not in atributos:
        print("Opção de pesquisa inválida.")
        return

    termo = input("Digite o termo da pesquisa: ").strip()
    encontrados = lista.pesquisar(atributos[opcao], termo)
    if not encontrados:
        print("Nenhum serviço encontrado.")
        return

    print(f"\nForam encontrados {len(encontrados)} serviço(s):")
    for servico in encontrados:
        exibir_servico(servico)


def listar_ordenados(lista):
    print("\nOrdenar por: 1 - Título | 2 - Categoria | 3 - ID")
    opcao = input("Escolha: ").strip()
    criterios = {"1": "titulo", "2": "categoria", "3": "identificador"}
    if opcao not in criterios:
        print("Critério inválido.")
        return

    lista.ordenar(criterios[opcao])
    if lista.esta_vazia():
        print("Não há serviços cadastrados.")
        return

    print("\nSERVIÇOS ORDENADOS")
    for servico in lista:
        print(f"{servico.identificador} | {servico.titulo} | {servico.categoria}")


def apresentar_analise(lista):
    print("\n--- ANÁLISE DOS SERVIÇOS ---")
    print(f"Total de registros: {len(lista)}")
    contagens = lista.contar_por_categoria()
    if not contagens:
        print("Ainda não existem categorias cadastradas.")
        return

    print("Quantidade por categoria:")
    for categoria, quantidade in contagens.items():
        print(f"- {categoria}: {quantidade}")


def criar_lista_inicial():
    lista = ListaEncadeada()
    carregar_dados_exemplo(lista)
    return lista


def executar_menu():
    lista = criar_lista_inicial()
    print("Citizen Assist AI - protótipo de consulta de serviços públicos")
    print("Foram carregados registros demonstrativos para facilitar os testes.")

    while True:
        print("\n" + "=" * 46)
        print("             CITIZEN ASSIST AI")
        print("=" * 46)
        print("1 - Cadastrar serviço")
        print("2 - Consultar serviço por ID")
        print("3 - Atualizar serviço")
        print("4 - Excluir serviço")
        print("5 - Pesquisar serviços")
        print("6 - Listar serviços ordenados")
        print("7 - Apresentar análise dos serviços")
        print("0 - Encerrar programa")

        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            cadastrar_servico(lista)
        elif opcao == "2":
            consultar_servico(lista)
        elif opcao == "3":
            atualizar_servico(lista)
        elif opcao == "4":
            excluir_servico(lista)
        elif opcao == "5":
            pesquisar_servicos(lista)
        elif opcao == "6":
            listar_ordenados(lista)
        elif opcao == "7":
            apresentar_analise(lista)
        elif opcao == "0":
            print("Sistema encerrado. Obrigado por utilizar o Citizen Assist AI.")
            break
        else:
            print("Opção inválida. Escolha uma opção exibida no menu.")


if __name__ == "__main__":
    try:
        executar_menu()
    except (KeyboardInterrupt, EOFError):
        print("\nExecução encerrada pelo usuário.")
