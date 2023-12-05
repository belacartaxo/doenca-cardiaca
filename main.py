import numpy as np
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

dados = pd.read_csv('./heart.csv', sep=',', encoding='iso-8859-1') 

'''
EXPLORAÇÃO DE DADOS
    import pandas as pd
>>> dados.head() - mostra as primeiras linhas
>>> dados.head(x) - mostra as x primeiras linhas
>>> dados.tail() =mostra as últimas linhas
>>> dados.shape - mostra a quantidade de linhas e colunas

>>> dados['Age'].valur_counts() - conta quantas pessoas tem com cada idade
>>> dados['Age'].valur_counts().sort_index() - coloca as idades em ordem
'''

'''
DADOS IDADE
    import plotly.express as px
    hist1 = px.histogram(dados,x='Age',nbins=60) 
    #(tabela de dados, conteudo do eixo x, largura do jistograma)

    hist1.update_layout(width=800, height=500, title_text='Distribuição de idades')
    #configuração do layout - (largura, altura, título) 

    hist1.show() 
    #mostra o gráfico

    OUTRA FORMA DE MOSTRAR
    import seaborn as sns
    import matplotlib.pyplot as plt

    sns.histplot(dados, x='Age', bins= 30, color='orange', kde=True, stat='count')
    #kde - mostra uma linha de tendência de distribuição, stat - contagem

    plt.show()
'''

'''
DADOS SEXO
    import seaborn as sns
    import matplotlib.pyplot as plt
>>> dados['Sex'].value_counts()
>>> sns.countplot(x='Sex', data=dados)
>>> plt.show()
'''
