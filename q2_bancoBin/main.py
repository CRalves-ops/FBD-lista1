from persistencia import carregar_dados
import operacoes

def main():
    # Carrega os dados do arquivo .txt assim que o programa abre
    contas = carregar_dados()

    while True:
        print("\n--- Sistema Bancário (BancoTXT) ---" \
        "\n 1. Criar Conta" \
        "\n 2. Consultar Saldo" \
        "\n 3. Creditar" \
        "\n 4. Debitar" \
        "\n 5. Transferir" \
        "\n 6. Remover Conta" \
        "\n 0. Sair")

        opcao = input("Escolha uma operação: ")

        if opcao == '0':
            print("Sair do sistema...")
            break
        elif opcao == '1':
            operacoes.criar_conta(contas)
        elif opcao == '2':
            operacoes.consultar_saldo(contas)
        elif opcao == '3':
            operacoes.creditar(contas)
        elif opcao == '4':
            operacoes.debitar(contas)
        elif opcao == '5':
            operacoes.transferir(contas)
        elif opcao == '6':
            operacoes.remover_conta(contas)
        else:
            print("Opção invalida!")

if __name__ == "__main__":
    main()