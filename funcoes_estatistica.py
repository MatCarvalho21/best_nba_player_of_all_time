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

temporada_regular = pd.read_csv("bases_de_dados/stats_regular_season.csv")
playoffs = pd.read_csv("bases_de_dados/stats_playoffs.csv")

kobe_df_rs = temporada_regular[temporada_regular["PLAYER"] == "KOBE BRYANT"] 
kobe_df_po = playoffs[playoffs["PLAYER"] == "KOBE BRYANT"] 
lebron_df_rs = temporada_regular[temporada_regular["PLAYER"] == "LEBRON JAMES"] 
lebron_df_po = playoffs[playoffs["PLAYER"] == "LEBRON JAMES"] 
jordan_df_rs = temporada_regular[temporada_regular["PLAYER"] == "MICHAEL JORDAN"] 
jordan_df_po = playoffs[playoffs["PLAYER"] == "MICHAEL JORDAN"] 

lista_variaveis_quant = ["GP", "GS", "MIN", "PTS", "FGM", "FGA", "FG%", "3PM", "3PA", "3P%", "FTM",
                          "FTA", "FT%", "OREB", "DREB", "REB", "AST", "STL", "BLK", "TOV", "PF"]


def analise_bidimensional(base_de_dados):

    lista_variaveis_quant = ["GP", "GS", "MIN", "PTS", "FGM", "FGA", "FG%", "3PM", "3PA", "3P%", "FTM",
                          "FTA", "FT%", "OREB", "DREB", "REB", "AST", "STL", "BLK", "TOV", "PF"]
    lista_de_variaveis_quant1 = ["GP", "GS", "MIN", "PTS", "FGM", "FGA", "FG%", "3PM", "3PA", "3P%"]
    lista_de_variaveis_quant2 = ["FTM", "FTA", "FT%", "OREB", "DREB", "REB", "AST", "STL", "BLK", "TOV", "PF"]

    lista_de_covariancias1 = list()
    lista_de_correlacoes1 = list()
    lista_de_covariancias2 = list()
    lista_de_correlacoes2 = list()

    indice = 0
    for cada_coluna in lista_variaveis_quant:
        
        if indice <= 9:
            lista_de_apoio_covar1 = [cada_coluna]
            lista_de_apoio_corre1 = [cada_coluna]
        else:
            lista_de_apoio_covar2 = [cada_coluna]
            lista_de_apoio_corre2 = [cada_coluna]

        if indice <= 9:
            for cada_variavel in lista_de_variaveis_quant1:
                covar = str(round(st.covariance(list(base_de_dados[cada_coluna]), list(base_de_dados[cada_variavel])), 1))
                corre = str(round(st.correlation(list(base_de_dados[cada_coluna]), list(base_de_dados[cada_variavel])), 1))
        else:
            for cada_variavel in lista_de_variaveis_quant2:
                covar = str(round(st.covariance(list(base_de_dados[cada_coluna]), list(base_de_dados[cada_variavel])), 1))
                corre = str(round(st.correlation(list(base_de_dados[cada_coluna]), list(base_de_dados[cada_variavel])), 1))
        
        if indice <= 9:
                lista_de_apoio_covar1.append(covar)
                lista_de_apoio_corre1.append(corre)
        else:
                lista_de_apoio_covar2.append(covar)
                lista_de_apoio_corre2.append(corre)

        if indice <= 9:
            lista_de_covariancias1.append(lista_de_apoio_covar1)
            lista_de_correlacoes1.append(lista_de_apoio_corre1)
        else:
            lista_de_covariancias2.append(lista_de_apoio_covar2)
            lista_de_correlacoes2.append(lista_de_apoio_corre2)
        
        indice += 1

    lista_de_colunas_1 = ["VARIÁVEIS", "GP", "GS", "MIN", "PTS", "FGM", "FGA", "FG%", "3PM", "3PA", "3P%"]
    lista_de_colunas_2 = ["VARIÁVEIS","FTM","FTA", "FT%", "OREB", "DREB", "REB", "AST", "STL", "BLK", "TOV", "PF"]

    console = Console()

    table1 = Table(title="Covariância")

    for column in lista_de_colunas_1:
        table1.add_column(column)

    for row in lista_de_covariancias1:
        table1.add_row(*row, style='black')

    console.print(table1)

    table2 = Table(title="Covariância")

    for column in lista_de_colunas_2:
        table2.add_column(column)

    for row in lista_de_covariancias2:
        table2.add_row(*row, style='black')

    console.print(table2)

    table3 = Table(title="Correlação")

    for column in lista_de_colunas_1:
        table3.add_column(column)

    for row in lista_de_correlacoes1:
        table3.add_row(*row, style='black')

    console.print(table3)

    table4 = Table(title="Correlação")

    for column in lista_de_colunas_2:
        table4.add_column(column)

    for row in lista_de_correlacoes2:
        table4.add_row(*row, style='black')

    console.print(table4)

analise_bidimensional(kobe_df_rs)
