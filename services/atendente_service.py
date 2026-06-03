from models.atendente import Atendente
from utils.file_manager import salvar_json, carregar_json


ARQUIVO_ATENDENTES = "data/atendentes.json"

atendentes = []


def carregar_atendentes():

    dados = carregar_json(
        ARQUIVO_ATENDENTES
    )

    for item in dados:

        atendente = Atendente(
            item["id"],
            item["nome"]
        )

        atendentes.append(atendente)


def cadastrar_atendente():

    try:

        id_atendente = int(
            input("ID: ")
        )

        nome = input("Nome: ")

        atendente = Atendente(
            id_atendente,
            nome
        )

        atendentes.append(
            atendente
        )

        salvar_atendentes()

        print("Atendente cadastrado")

    except ValueError:
        print("ID inválido")


def listar_atendentes():

    for atendente in atendentes:

        print(
            atendente.id,
            atendente.nome
        )


def salvar_atendentes():

    dados = []

    for atendente in atendentes:

        dados.append({

            "id": atendente.id,
            "nome": atendente.nome

        })

    salvar_json(
        ARQUIVO_ATENDENTES,
        dados
    )