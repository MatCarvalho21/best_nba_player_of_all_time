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

        media_rs = round(st.mean(lista_de_valores_rs), 2)
        mediana_rs = round(st.median(lista_de_valores_rs), 2)
        desvio_padrao_rs = round(st.pstdev(lista_de_valores_rs), 2)
        variancia_rs = round(st.variance(lista_de_valores_rs), 2)
        máximo_rs = max(lista_de_valores_rs)
        minimo_rs = min(lista_de_valores_rs)

        lista_de_valores_po = list(base_de_dados_po[variável])

        media_po = round(st.mean(lista_de_valores_po), 2)
        mediana_po = round(st.median(lista_de_valores_po), 2)
        desvio_padrao_po = round(st.pstdev(lista_de_valores_po), 2)
        variancia_po = round(st.variance(lista_de_valores_po), 2)
        máximo_po = max(lista_de_valores_po)
        minimo_po = min(lista_de_valores_po)

        linhas.append([variável, media_rs, mediana_rs, desvio_padrao_rs, variancia_rs, máximo_rs, minimo_rs, 
                       media_po, mediana_po, desvio_padrao_po, variancia_po, máximo_po, minimo_po])
    lista = ["VARIÁVEL", "MÉDIA", "MEDIANA", "DP", "VAR", "MÁX", "MÍN", "MÉDIA", "MEDIANA", "DP", "VAR", "MÁX", "MÍN"]
    
    table = Table(title=f"{titulo}")

    for column in lista:
        table.add_column(column)

    for row in linhas:
        table.add_row(*row, style='bright_green')

    console = Console()
    console.print(table)
    