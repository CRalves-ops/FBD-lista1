# 🏦 Simulação de Sistema Bancário (BancoTXT e BancoBIN)

Este repositório contém a resolução da primeira lista de exercícios da disciplina de **Fundamentos de Bancos de Dados** , ofertada pelo Departamento de Computação (DC) do Centro de Ciências (CC) da Universidade Federal do Ceará (UFC).

## 🎯 Objetivo da Atividade
O objetivo principal desta atividade é introduzir os conceitos primordiais de bancos de dados, focando especificamente na persistência de dados em arquivos locais usando a linguagem Python. 

A atividade propõe a criação de um programa que simula as operações de um banco, garantindo que os dados das contas (número e saldo) não sejam perdidos ao encerrar a execução. Para isso, o sistema foi implementado em duas versões:

1.**BancoTXT:** Salva os registros (dicionários) das contas em um arquivo de texto plano (`.txt`).

2. **BancoBIN:** Uma evolução do programa anterior, que salva os mesmos registros em um arquivo binário (`.bin`).

## ⚙️ Funcionalidades Implementadas
O programa roda em um loop de menu, permitindo as seguintes operações de um sistema CRUD:
- **Criar Conta:** Adiciona uma nova conta com número e saldo inicial.
- **Consultar Saldo:** Exibe o saldo atual de uma conta específica.
- **Creditar:** Adiciona um valor ao saldo de uma conta.
- **Debitar:** Subtrai um valor do saldo de uma conta.
- **Transferir:** Move um valor entre uma conta de origem e uma de destino.
- **Remover Conta:** Exclui o registro de uma conta do sistema.

*(Nota: O sistema possui tratamento de erros para alertar o usuário caso tente interagir com uma conta inexistente.*

## 🛠️ Tecnologias Utilizadas
* **Python 3:** Linguagem base para a lógica do sistema.
* **Manipulação de Arquivos (I/O):** Leitura e escrita em modo texto (`txt`) e binário (`pickle`).

## 🚀 Como Executar
1. Clone este repositório:
   `git clone https://github.com/CRalves-ops/FBD-lista1.git`
2. Navegue até o diretório:
   `cd FBD-lista1`
3. Execute a versão desejada do banco:
   `python bancotxt.py` ou `python bancobin.py`

---
> *"Minha esperança é necessária, mas não é suficiente. Ela, só, não ganha a luta, mas sem ela a luta fraqueja e titubeia" - Paulo Freire*
