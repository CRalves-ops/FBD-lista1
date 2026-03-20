import os
import pickle

ARQUIVO_DADOS = 'contas.bin'

def carregar_dados():
    """
    Lê o arquivo binário e retorna um dicionário com as contas. 
    """

    if os.path.exists(ARQUIVO_DADOS):
        # 'rb' significa Read Binary (Ler Binário)
        with open(ARQUIVO_DADOS, 'rb') as f:
            try:
                # O pickle reconstrói o dicionario exatamente como ele era
                return pickle.load(f)
            except EOFError:
                # Retorna diconário vazio se o arquivo estiver vazio
                return {}
    
    return {}

def salvar_dados(contas):
    """
    Salva o dicionário de contas no arquivo binário.
    """

    # 'wb' significa Write Binay (Escrever Binário)
    with open(ARQUIVO_DADOS, 'wb') as f:
        # O pickle converte o dicionário para binário e salva no arquivo
        pickle.dump(contas, f)