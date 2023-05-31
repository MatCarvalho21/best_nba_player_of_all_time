import pandas as pd   

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
