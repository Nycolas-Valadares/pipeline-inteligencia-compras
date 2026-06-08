import requests
import pandas as pd
from datetime import datetime
import sqlite3

def extrair_cotacao_dolar():
    print("Iniciando extração da API...")
    url = "https://open.er-api.com/v6/latest/USD"
    requisicao = requests.get(url)
    dados_json = requisicao.json()
    
    valor_extraido = float(dados_json['rates']['BRL'])
    data_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    dados = {
        "Ativo": ["Dólar (USD)"],
        "Cotacao_BRL": [valor_extraido],
        "Data_Coleta": [data_atual]
    }
    
    return pd.DataFrame(dados)

def salvar_no_banco(dataframe):
    print("Salvando dados no banco SQL...")
    conexao = sqlite3.connect("banco_suprimentos.db")
    dataframe.to_sql(name="historico_cambio", con=conexao, if_exists="append", index=False)
    conexao.close()
    print("✅ Processo concluído com sucesso!")

# Execução do Pipeline
if __name__ == "__main__":
    tabela_cambio = extrair_cotacao_dolar()
    salvar_no_banco(tabela_cambio)
