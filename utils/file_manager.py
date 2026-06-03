import json
import os


def salvar_json(nome_arquivo, dados):

    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(
            dados,
            arquivo,
            ensure_ascii=False,
            indent=4
        )


def carregar_json(nome_arquivo):

    if not os.path.exists(nome_arquivo):
        return []

    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)