# mostrando o top 5 de assuntos por mês
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

ano = 2018
vara = '12ª Vara Federal'

dados_varas = pd.read_csv('../dados-pje-MPF.csv',dtype='unicode')

dados_varas['ano_primeira_dist'] = pd.DatetimeIndex(dados_varas['Data Primeira Distribuição']).year

dados_varas=dados_varas[dados_varas.ano_primeira_dist > 2014]

dados_varas['mes_primeira_dist'] = pd.DatetimeIndex(dados_varas['Data Primeira Distribuição']).month

#dados_varas.sort_values(['ano_primeira_dist','mes_primeira_dist'])

dados_varas.sort_values(['mes_primeira_dist'])

dados_varas = dados_varas[dados_varas['Órgão Julgador'] == vara]
dados_varas = dados_varas[dados_varas['ano_primeira_dist'] == ano]

dados_varas['mes_primeira_dist'] = dados_varas['mes_primeira_dist'].replace(1,'01 - Jan')
dados_varas['mes_primeira_dist'] = dados_varas['mes_primeira_dist'].replace(2,'02 - Fev')
dados_varas['mes_primeira_dist'] = dados_varas['mes_primeira_dist'].replace(3,'03 - Mar')
dados_varas['mes_primeira_dist'] = dados_varas['mes_primeira_dist'].replace(4,'04 - Abr')
dados_varas['mes_primeira_dist'] = dados_varas['mes_primeira_dist'].replace(5,'05 - Mai')
dados_varas['mes_primeira_dist'] = dados_varas['mes_primeira_dist'].replace(6,'06 - Jun')
dados_varas['mes_primeira_dist'] = dados_varas['mes_primeira_dist'].replace(7,'07 - Jul')
dados_varas['mes_primeira_dist'] = dados_varas['mes_primeira_dist'].replace(8,'08 - Ago')
dados_varas['mes_primeira_dist'] = dados_varas['mes_primeira_dist'].replace(9,'09 - Set')
dados_varas['mes_primeira_dist'] = dados_varas['mes_primeira_dist'].replace(10,'10 - Out')
dados_varas['mes_primeira_dist'] = dados_varas['mes_primeira_dist'].replace(11,'11 - Nov')
dados_varas['mes_primeira_dist'] = dados_varas['mes_primeira_dist'].replace(12,'12 - Dez')


# parte complicada:
dados_agrupados = dados_varas['Assunto'].groupby(dados_varas['mes_primeira_dist']).value_counts()

dados_agrupados = dados_agrupados.groupby(level=0).nlargest(5).reset_index(level=0, drop=True)

#ax = dados_agrupados.plot.bar(stacked=True)
print("a média de processos na {} é: {}".format(vara,dados_agrupados.mean()))
print("a mediana de processos {} é: {}".format(vara,dados_agrupados.median()))
