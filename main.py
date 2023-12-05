import numpy as np
import pandas as pd

dados = pd.read_csv('./heart.csv', sep=',', encoding='iso-8859-1') 

'''
EXPLORAÇÃO DE DADOS
    dados.head() - mostra as primeiras linhas
    dados.head(x) - mostra as x primeiras linhas
    dados.tail() =mostra as últimas linhas
    dados.shape - mostra a quantidade de linhas e colunas
'''