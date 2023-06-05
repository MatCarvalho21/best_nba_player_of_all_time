import pandas as pd   
import statistics as st
from rich.console import Console
from rich.table import Table

def contagem(base_de_dados, lista_de_variáveis):
    for variável in lista_de_variáveis:
        lista = list(base_de_dados[variável])
        conjunto = set(base_de_dados[variável])

        dicionario = {}
        for valor in conjunto:
            dicionario[valor] = 0

        for valor in lista:
            dicionario[valor] += 1

        print(f"{variável}:")
        for key in dicionario:
            print(f"O item {key} tem {dicionario[key]} ocorrências nessa base de dados.")

def medidas_de_resumo(base_de_dados_rs, base_de_dados_po, lista_de_variáveis, titulo):

    linhas = []
    for variável in lista_de_variáveis:
        lista_de_valores_rs = list(base_de_dados_rs[variável])

        media_rs = str(round(st.mean(lista_de_valores_rs), 1))
        mediana_rs = str(round(st.median(lista_de_valores_rs), 1))
        desvio_padrao_rs = str(round(st.pstdev(lista_de_valores_rs), 1))
        variancia_rs = str(round(st.variance(lista_de_valores_rs)/100, 1))
        máximo_rs = str(max(lista_de_valores_rs))
        minimo_rs = str(min(lista_de_valores_rs))
                       
        lista_de_valores_po = list(base_de_dados_po[variável])

        media_po = str(round(st.mean(lista_de_valores_po), 1))
        mediana_po = str(round(st.median(lista_de_valores_po), 1))
        desvio_padrao_po = str(round(st.pstdev(lista_de_valores_po), 1))
        variancia_po = str(round(st.variance(lista_de_valores_po)/100, 1))
        máximo_po = str(max(lista_de_valores_po))
        minimo_po = str(min(lista_de_valores_po))

        linhas.append([variável, media_rs, mediana_rs, desvio_padrao_rs, variancia_rs, máximo_rs, minimo_rs, 
                       media_po, mediana_po, desvio_padrao_po, variancia_po, máximo_po, minimo_po])
    lista = ["VARIÁVEL", "MÉDIA_RS", "MEDIANA_RS", "DP_RS", "VAR_RS_LOG100", "MÁX_RS", "MÍN_RS", "MÉDIA_PO", "MEDIANA_PO", "DP_PO", "VAR_PO_LOG100", "MÁX_PO", "MÍN_PO"]
    
    table = Table(title=f"{titulo}")

    for column in lista:
        table.add_column(column)

    for row in linhas:
        table.add_row(*row, style='black')

    console = Console()
    console.print(table)

def analise_bidimensional(base_de_dados, nome_da_coluna1, nome_da_coluna2):
    jogadores = set(base_de_dados["PLAYER"])

    for cada_jogador in jogadores:
        base_de_dados = base_de_dados[base_de_dados["PLAYER"] == cada_jogador]
        print(f"- {cada_jogador.title()}")
        print(f"A correlação das variáveis {nome_da_coluna1.title()} e {nome_da_coluna2.title()} é {st.correlation(list(base_de_dados[nome_da_coluna1]), list(base_de_dados[nome_da_coluna2]))}")
        print(f"A covariância das variáveis {nome_da_coluna1.title()} e {nome_da_coluna2.title()} é {st.covariance(list(base_de_dados[nome_da_coluna1]), list(base_de_dados[nome_da_coluna2]))}")
        print()