from persistencia import salvar_dados

def criar_conta(contas):
    numero = input("Digite o número da nova conta: ")
    if numero in contas:
        print("Erro: Esta conta já existe!")

    else:
        saldo_inicial = float(input("Digite o saldo inicial: "))
        contas[numero] = saldo_inicial
        
        salvar_dados(contas)
        print("Conta criada com sucesso!")

def consultar_saldo(contas):
    numero = input("Digite o número da conta: ")

    if numero in contas:
        print(f"Saldo atual da conta {numero}: R$ {contas[numero]}")

    else:
        print("Erro: Conta inexistente.")

def creditar(contas):
    numero = input("Digite o número da conta para crédito: ")
    if numero in contas:
        valor = float(input("Digire o valor a ser creditado: "))
        contas[numero] += valor
        salvar_dados(contas)
        print("Créditado com sucesso!")

    else:
        print("Erro: Conta inexistente")

def debitar(contas):
    numero = input("Digite o número da conta para debitar: ")
    if numero in contas:
        valor = float(input("Digite o valor a ser debitado: "))
        if valor <= contas[numero]:
            contas[numero] -= valor
            salvar_dados(contas)
            print("Valor debitado com sucesso!")
        else:
            print(f"O saldo da conta é insuficiente! Saldo no valor de {contas[numero]}")

    else:
        print("Conta Inexistente!")

def transferir(contas):
    origem = input("Digite o número da conta de origem: ")
    destino = input("Digite o número da conta de destino: ")

    if origem not in contas or destino not in contas:
        print("Erro: Conta de origem ou destino não encontrados! ")
        return
    
    valor =  float(input("Digite o valor a transferir: "))
    if valor <= contas[origem]:
        contas[origem] -= valor
        contas[destino] += valor
        salvar_dados(contas)

        print("transferencia realizada com sucesso!")

    else:
        print("Conta de origem não tem saldo suficiente! ")

def remover_conta(contas):
    numero = input("Digite o número da conta que será excluida: ")
    if numero in contas:
        del contas[numero]
        salvar_dados(contas)
        print("Conta removida com sucesso!")
    else:
        print("Erro: conta não encontrada! ")
        