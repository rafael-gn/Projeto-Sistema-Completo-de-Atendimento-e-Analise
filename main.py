from services.cliente_service import (
    cadastrar_cliente,
    listar_clientes
)

from services.atendente_service import (
    cadastrar_atendente,
    listar_atendentes
)


def exibir_menu():

    print("\n=== SISTEMA DE ATENDIMENTO ===")
    print("1 - Cadastrar Cliente")
    print("2 - Listar Clientes")
    print("3 - Cadastrar Atendente")
    print("4 - Listar Atendentes")
    print("5 - Abrir Atendimento")
    print("6 - Chamar Próximo")
    print("7 - Finalizar Atendimento")
    print("8 - Histórico Cliente")
    print("9 - Relatórios")
    print("10 - Exportar CSV")
    print("0 - Sair")


def main():

    while True:

        exibir_menu()

        opcao = input("\nEscolha: ")

        if opcao == "1":
            cadastrar_cliente()

        elif opcao == "2":
            listar_clientes()

        elif opcao == "3":
            cadastrar_atendente()

        elif opcao == "4":
            listar_atendentes()

        elif opcao == "0":
            print("Encerrando sistema...")
            break

        else:
            print("Opção inválida")


if __name__ == "__main__":
    main()