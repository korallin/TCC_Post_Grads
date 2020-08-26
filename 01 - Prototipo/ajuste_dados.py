import pandas as pd
from numpy import random
import numpy as np


ajustes_dados = pd.read_csv('../dados-pje-MPF.csv',dtype='unicode')

ajustes_dados['ano_primeira_dist'] = pd.DatetimeIndex(ajustes_dados['Data Primeira Distribuição']).year

ajustes_dados=ajustes_dados[ajustes_dados.ano_primeira_dist > 2014]

ajustes_dados['mes_primeira_dist'] = pd.DatetimeIndex(ajustes_dados['Data Primeira Distribuição']).month

ajustes_dados.sort_values(['ano_primeira_dist','mes_primeira_dist'])

#ajustes_dados.groupby('Órgão Julgador')['Assunto'].nlargest(5))

ajustes_dados = ajustes_dados.drop(['Unnamed: 0', '%ID_PROCESSO_TRF', 'Sistema',
'Parte Polo Ativo?', 'Parte Polo Passivo?','Parte Outros Participantes?',
'Parte Documento', 'Parte Descrição', '%ID_PESSOA_REU',
'Data Trânsito Julgado', 'Número Tempo em Anos'], axis=1)

ajustes_dados.groupby('Órgão Julgador')['Assunto']

'''
array(['1ª Vara Federal', '12ª Vara Federal', '4ª Vara Federal',
       '5ª Vara Federal', '10ª Vara Federal', '9ª Vara Federal',
       '2ª Vara Federal', '11ª Vara Federal', '8ª Vara Federal',
       '14ª Vara Federal', '15ª Vara Federal',
       'Corregedoria Judicial da Penitenciária Federal',
       '6ª Vara Federal', 'Ambiente de Inquérito',
       'Ambiente de Audiência de Custódia'], dtype=object)
'''

dados_1a_vara = ajustes_dados[ajustes_dados['Órgão Julgador'] == '1ª Vara Federal']
dados_2a_vara = ajustes_dados[ajustes_dados['Órgão Julgador'] == '2ª Vara Federal']
dados_4a_vara = ajustes_dados[ajustes_dados['Órgão Julgador'] == '4ª Vara Federal']
dados_5a_vara = ajustes_dados[ajustes_dados['Órgão Julgador'] == '5ª Vara Federal']



print(ajustes_dados.head(20))

print("Top 10 de assuntos geral: ")
print(ajustes_dados['Assunto'].value_counts()[:10].index.tolist())

print("Top 10 de assuntos da 1ª Vara: ")
print(dados_1a_vara['Assunto'].value_counts()[:10].index.tolist())

print("Top 10 de assuntos da 2ª Vara: ")
print(dados_2a_vara['Assunto'].value_counts()[:10].index.tolist())

print("Top 10 de assuntos da 4ª Vara: ")
print(dados_4a_vara['Assunto'].value_counts()[:10].index.tolist())

print("Top 10 de assuntos da 5ª Vara: ")
print(dados_5a_vara['Assunto'].value_counts()[:10].index.tolist())
