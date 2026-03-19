import os

ARQUIVO_DADOS = 'contas.txt'

def carregar_dados():
    """
    Lê o arquivo de texto e retorna um dicionário com as contas.
    """
    contas = {}
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, 'r') as f:
            for linha in f:
                if linha:
                    numero, saldo = linha.split(';')
                    contas[numero] = float(saldo)

    return contas

def salvar_dados(contas):
    """
    Salva o dicionario de contas no arquivo de texto.
    """
    with open(ARQUIVO_DADOS, 'w') as f:
        for numero, saldo in contas.items():
            f.write(f"{numero};{saldo}\n")