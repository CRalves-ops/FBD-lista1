# 🏦 Questão 2: BancoBIN

Este diretório contém a resolução da segunda questão da lista de Fundamentos de Bancos de Dados. O objetivo é evoluir o simulador bancário anterior, agora persistindo os dados em um **arquivo binário (`.bin`)**.

## 🔄 O que mudou em relação à Q1?

Graças à arquitetura modularizada criada na primeira questão, os arquivos `main.py` e `operacoes.py` permaneceram intactos. A única alteração necessária ocorreu no arquivo **`persistencia.py`**.

Em vez de manipular strings e salvar em texto plano, este módulo agora utiliza a biblioteca nativa `pickle` do Python. 

### Vantagens do uso do `pickle`:
* **Eficiência:** Permite serializar e desserializar objetos complexos do Python (como dicionários) diretamente para o disco.
* **Simplicidade:** Não é necessário fazer o *parse* (separação por ponto e vírgula `;`) na hora de ler os dados. O `pickle.load()` já devolve o dicionário montado e com os tipos de dados corretos (float para saldo, string para número da conta).

## 🚀 Como executar

1. Certifique-se de estar dentro da pasta `q2_bancobin` no seu terminal.
2. Execute o arquivo principal com o comando:
   ```bash
   python main.py