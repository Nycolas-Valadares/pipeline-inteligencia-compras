# 📦 Pipeline de Inteligência de Compras: Automação de Cotações

## 🎯 O Problema de Negócio
No setor de Suprimentos e Compras Internacionais, o monitoramento diário de taxas de câmbio (como USD/BRL) é fundamental para a análise de viabilidade de importações, cotação de fretes e negociação com fornecedores. A coleta manual desses dados consome tempo operacional valioso e está sujeita a erros de digitação, dificultando a criação de um histórico confiável para cálculo de *saving*.

## 💡 A Solução
Este projeto é um pipeline automatizado de extração de dados (ETL) construído em Python. O script acessa uma API pública de câmbio, coleta a cotação do Dólar em tempo real, realiza o tratamento estruturado das informações utilizando a biblioteca Pandas e armazena os registros automaticamente em um banco de dados relacional (SQLite).

## ⚙️ Impacto Operacional
* **Eliminação de Trabalho Manual:** Substitui a atualização diária de planilhas por um robô de extração.
* **Acurácia de Dados:** Garante que as cotações utilizadas nas negociações de compras sejam exatas e padronizadas.
* **Base para Decisão Estratégica:** A criação de um banco de dados histórico (SQL) permite análises futuras de sazonalidade e identificação do momento ideal de compra (*saving*).

## 🛠️ Tecnologias Utilizadas
* **Python:** Orquestração do pipeline.
* **Requests:** Consumo da API de dados (REST).
* **Pandas:** Tratamento e modelagem do DataFrame.
* **SQLite3:** Armazenamento histórico e estruturação do banco de dados.

---
*Desenvolvido focado na otimização de rotinas de suprimentos e inteligência logística.*
