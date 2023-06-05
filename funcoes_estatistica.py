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

def analise_bidimensional(base_de_dados, lista_variaveis_quant, título1, título2):
    lista_covar = [lista_variaveis_quant]
    lista_corre = [lista_variaveis_quant]

    for indice in range(0, len(base_de_dados[["GP"]]), 1):
        for cada_variavel in lista_variaveis_quant:
            base_de_dados[cada_variavel][indice] = base_de_dados[cada_variavel][indice] / base_de_dados["GP"][indice]
    
    for cada_variavel in lista_variaveis_quant:
        
        lista_1 = []
        lista_2 = []
        for cada_elemento in lista_variaveis_quant:
            lista_1.append(round(st.covariance(base_de_dados[cada_variavel], base_de_dados[cada_elemento]), 10))
            lista_2.append(round(st.correlation(base_de_dados[cada_variavel], base_de_dados[cada_elemento]), 0))

        print(lista_1)
        print(lista_2)

        lista_covar.append(lista_1)
        lista_corre.append(lista_2)
    

            
    lista_colunas = ["Variável", "GP", "GS", "MIN", "PTS", "FGM", "FGA", "FG%", "3PM", "3PA", "3P%",
                     "FTM", "FTA", "FT%", "OREB", "DREB", "REB", "AST", "STL", "BLK", "TOV", "PF"]
    
    '''
    table1 = Table(title=f"{título1}")

    for colunas in lista_colunas:
        table1.add_column(colunas)
        
    for row in lista_covar:
        table1.add_row(*row, style='black')
        
    table2 = Table(title=f"{título2}")

    for colunas in lista_colunas:
        table2.add_column(colunas)
        
    for row in lista_corre:
        table2.add_row(*row, style='black')
        
    console = Console()
    console.print(table1)
    print()
    console.print(table2)
    '''

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
analise_bidimensional(kobe_df_rs, lista_variaveis_quant, "Covariância Kobe RS", "Correlação Kobe RS")