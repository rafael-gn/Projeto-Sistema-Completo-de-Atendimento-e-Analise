import csv

from services.atendimento_service import historico


def tempo_medio():

    if not historico:
        return 0

    total = 0

    for atendimento in historico:

        total += atendimento.duracao

    return total / len(historico)


def top_clientes():

    contador = {}

    for atendimento in historico:

        nome = (
            atendimento.cliente.nome
        )

        contador[nome] = (
            contador.get(nome, 0)
            + 1
        )

    ordenado = sorted(
        contador.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return ordenado[:5]


def exportar_csv():

    with open(
            "relatorio.csv",
            "w",
            newline="",
            encoding="utf-8"
    ) as arquivo:

        writer = csv.writer(
            arquivo
        )

        writer.writerow([
            "Cliente",
            "Duração"
        ])

        for atendimento in historico:

            writer.writerow([
                atendimento.cliente.nome,
                atendimento.duracao
            ])

    print(
        "CSV exportado"
    )