from models.cliente import Cliente
from structures.linked_list import LinkedList
from utils.file_manager import salvar_json, carregar_json


ARQUIVO_CLIENTES = "data/clientes.json"

clientes_ativos = LinkedList()


def carregar_clientes():

    dados = carregar_json(ARQUIVO_CLIENTES)

    for item in dados:

        cliente = Cliente(
            item["id"],
            item["nome"],
            item["telefone"],
            item["prioridade"]
        )

        clientes_ativos.add(cliente)


def cadastrar_cliente():

    try:

        id_cliente = int(input("ID: "))
        nome = input("Nome: ")
        telefone = input("Telefone: ")

        prioridade = input(
            "Prioridade (S/N): "
        ).upper() == "S"

        cliente = Cliente(
            id_cliente,
            nome,
            telefone,
            prioridade
        )

        clientes_ativos.add(cliente)

        salvar_clientes()

        print("Cliente cadastrado!")

    except ValueError:
        print("ID inválido")


def listar_clientes():

    atual = clientes_ativos.head

    while atual:

        cliente = atual.cliente

        print(
            cliente.id,
            cliente.nome,
            cliente.telefone,
            cliente.prioridade
        )

        atual = atual.next


def buscar_cliente(id_cliente):

    return clientes_ativos.find(id_cliente)


def remover_cliente(id_cliente):

    removido = clientes_ativos.remove(id_cliente)

    if removido:
        salvar_clientes()
        print("Cliente removido")
    else:
        print("Cliente não encontrado")


def salvar_clientes():

    lista = []

    atual = clientes_ativos.head

    while atual:

        cliente = atual.cliente

        lista.append({
            "id": cliente.id,
            "nome": cliente.nome,
            "telefone": cliente.telefone,
            "prioridade": cliente.prioridade
        })

        atual = atual.next

    salvar_json(
        ARQUIVO_CLIENTES,
        lista
    )