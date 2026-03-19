# 🏦 Questão 1: BancoTXT

Este diretório contém a resolução da primeira questão da lista de Fundamentos de Bancos de Dados. O objetivo deste programa é simular um sistema bancário básico (CRUD) persistindo os dados em um **arquivo de texto plano (`.txt`)**.

## 🏗️ Estrutura do Projeto (Modularização)

Para garantir um código limpo e de fácil manutenção, a solução foi dividida em três arquivos principais:

* **`main.py`**: É o ponto de entrada do programa. Responsável apenas por exibir o menu interativo no terminal e capturar as escolhas do usuário.
* **`operacoes.py`**: Contém as "regras de negócio" do banco. Aqui estão as lógicas de criar conta, consultar saldo, creditar, debitar, transferir e remover.
* **`persistencia.py`**: O módulo encarregado de conversar com o "banco de dados". Ele possui as funções de ler e salvar os dicionários no arquivo `contas.txt`.

## ⚙️ Como os dados são salvos?
As contas são manipuladas em memória através de dicionários no Python (onde a chave é o número da conta e o valor é o saldo). A cada alteração, o estado atual do dicionário é reescrito no arquivo `contas.txt` no formato `numero_da_conta;saldo`.

## 🚀 Como executar

1. Certifique-se de estar dentro da pasta `q1_bancotxt` no seu terminal.
2. Execute o arquivo principal com o comando:
   ```bash
   python main.py