import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

ano = 2019
vara = '12ª Vara Federal'

dados_varas = pd.read_csv('../dados-pje-MPF.csv',dtype='unicode')

dados_varas['ano_primeira_dist'] = pd.DatetimeIndex(dados_varas['Data Primeira Distribuição']).year

dados_varas=dados_varas[dados_varas.ano_primeira_dist > 2014]

dados_varas['mes_primeira_dist'] = pd.DatetimeIndex(dados_varas['Data Primeira Distribuição']).month

#dados_varas.sort_values(['ano_primeira_dist','mes_primeira_dist'])

dados_varas.sort_values(['mes_primeira_dist'])

dados_varas = dados_varas[dados_varas['Órgão Julgador'] == vara]
dados_varas = dados_varas[dados_varas['ano_primeira_dist'] == ano]

dados_filtrados = dados_varas.groupby(['mes_primeira_dist', 'Assunto'])['Assunto Código'].count()
dados_ajustados = dados_filtrados.groupby(level='mes_primeira_dist').nlargest(25).reset_index(level=0, drop=True).reset_index()

estatisticas_ano = dados_ajustados["Assunto Código"].describe()
'''
O ".describe()" retorna uma lista n com a seguinte estrutura:
n[0] = total
n[1] = média
n[2] = desvio padrão
n[3] = valor mínimo (nesse caso o Assunto que teve menos ocorrências)
n[4] = 25% (quartil)
n[5] = mediana
n[6] = 75%
n[7] = valor máximo (de forma semelhante ao mínimo, é o Assunto que teve mais ocorrências)
'''

media_ano = estatisticas_ano[1]
desvio_padrao_ano = estatisticas_ano[2]
anomalia_ano = 2*desvio_padrao_ano + media_ano

print("A média de processos por assunto no ano {} na {} foi de {}, uma anomalia é considerada se houverem mais que {} processos de determinado Assunto".format(ano, vara, round(media_ano,2), round(anomalia_ano,2)))

dados_janeiro = dados_ajustados[dados_ajustados['mes_primeira_dist'] == 1]
#janeiro = dados_janeiro["Assunto Código"].describe()

# isso abaixo é um DataFrame
janeiro_acima_media = dados_janeiro[dados_janeiro["Assunto Código"] > media_ano]
janeiro_anomalia = dados_janeiro[dados_janeiro["Assunto Código"] > anomalia_ano]

janeiro_acima_media_lista = janeiro_acima_media["Assunto"].tolist()
janeiro_anomalia_lista = janeiro_anomalia["Assunto"].tolist()

'''
#['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
prototipo de dataframe para mostrar em gráfico de barras

df = {'Meses':['Janeiro'],
      'Anomalia':janeiro_anomalia_lista,
      'Média':janeiro_acima_media_lista}
'''

print("A seguir serão mostrados os Assuntos que apareceram em Janeiro numa frequência acima da média: ")
for i in range(len(janeiro_acima_media_lista)):
    print (janeiro_acima_media_lista[i])

print("A seguir serão mostrados os Assuntos que apareceram em Janeiro numa frequência muito acima da média: ")
for j in range(len(janeiro_anomalia_lista)):
    print (janeiro_anomalia_lista[j])

df = {'Meses':['Janeiro'],
      'Anomalia':janeiro_anomalia_lista,
      'Média':janeiro_acima_media_lista}
