def busca_binaria(lista, alvo):

    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:

        meio = (inicio + fim) // 2

        if lista[meio].id == alvo:
            return lista[meio]

        if lista[meio].id < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return None