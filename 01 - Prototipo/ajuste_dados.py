import pandas as pd
from numpy import random
import numpy as np


ajustes_dados = pd.read_csv('../dados-pje-MPF.csv',dtype='unicode')

ajustes_dados = ajustes_dados.drop(['%ID_PROCESSO_TRF', 'Sistema',
'Parte Polo Ativo?', 'Parte Polo Passivo?','Parte Outros Participantes?',
'Parte Documento', 'Parte Descrição', '%ID_PESSOA_REU','Número Processo',
'Data Trânsito Julgado', 'Número Tempo em Anos'], axis=1)

ajustes_dados.to_csv('dados-pje-mpf-2.csv', index = False)

ajustes_dados['ano_primeira_dist'] = pd.DatetimeIndex(ajustes_dados['Data Primeira Distribuição']).year

ajustes_dados=ajustes_dados[ajustes_dados.ano_primeira_dist > 2014]

ajustes_dados['mes_primeira_dist'] = pd.DatetimeIndex(ajustes_dados['Data Primeira Distribuição']).month

ajustes_dados.sort_values(['ano_primeira_dist','mes_primeira_dist'])

#ajustes_dados.groupby('Órgão Julgador')['Assunto'].nlargest(5))
#ajustes_dados.groupby('Órgão Julgador')['Assunto']

'''
array(['1ª Vara Federal', '12ª Vara Federal', '4ª Vara Federal',
       '5ª Vara Federal', '10ª Vara Federal', '9ª Vara Federal',
       '2ª Vara Federal', '11ª Vara Federal', '8ª Vara Federal',
       '14ª Vara Federal', '15ª Vara Federal',
       'Corregedoria Judicial da Penitenciária Federal',
       '6ª Vara Federal', 'Ambiente de Inquérito',
       'Ambiente de Audiência de Custódia'], dtype=object)


       # list of strings
lst = ['Geeks', 'For', 'Geeks', 'is', 'portal', 'for', 'Geeks']

# Calling DataFrame constructor on list
# with indices and columns specified
df = pd.DataFrame(lst, index =['a', 'b', 'c', 'd', 'e', 'f', 'g'],
                                              columns =['Names'])
df
'''

dados_1a_vara = ajustes_dados[ajustes_dados['Órgão Julgador'] == '1ª Vara Federal']
dados_2a_vara = ajustes_dados[ajustes_dados['Órgão Julgador'] == '2ª Vara Federal']
dados_4a_vara = ajustes_dados[ajustes_dados['Órgão Julgador'] == '4ª Vara Federal']
dados_5a_vara = ajustes_dados[ajustes_dados['Órgão Julgador'] == '5ª Vara Federal']
dados_6a_vara = ajustes_dados[ajustes_dados['Órgão Julgador'] == '6ª Vara Federal']
dados_8a_vara = ajustes_dados[ajustes_dados['Órgão Julgador'] == '8ª Vara Federal']
dados_9a_vara = ajustes_dados[ajustes_dados['Órgão Julgador'] == '9ª Vara Federal']
dados_10a_vara = ajustes_dados[ajustes_dados['Órgão Julgador'] == '10ª Vara Federal']
dados_11a_vara = ajustes_dados[ajustes_dados['Órgão Julgador'] == '11ª Vara Federal']
dados_12a_vara = ajustes_dados[ajustes_dados['Órgão Julgador'] == '12ª Vara Federal']
dados_14a_vara = ajustes_dados[ajustes_dados['Órgão Julgador'] == '14ª Vara Federal']
dados_15a_vara = ajustes_dados[ajustes_dados['Órgão Julgador'] == '15ª Vara Federal']


top_geral = ajustes_dados['Assunto'].value_counts()[:10].index.tolist()
top_1a_vara = dados_1a_vara['Assunto'].value_counts()[:10].index.tolist()
top_2a_vara = dados_2a_vara['Assunto'].value_counts()[:10].index.tolist()
top_4a_vara = dados_4a_vara['Assunto'].value_counts()[:10].index.tolist()
top_5a_vara = dados_5a_vara['Assunto'].value_counts()[:10].index.tolist()
top_6a_vara = dados_6a_vara['Assunto'].value_counts()[:10].index.tolist()
top_8a_vara = dados_8a_vara['Assunto'].value_counts()[:10].index.tolist()
top_9a_vara = dados_9a_vara['Assunto'].value_counts()[:10].index.tolist()
top_10a_vara = dados_10a_vara['Assunto'].value_counts()[:10].index.tolist()
top_11a_vara = dados_11a_vara['Assunto'].value_counts()[:10].index.tolist()
top_12a_vara = dados_12a_vara['Assunto'].value_counts()[:10].index.tolist()
top_14a_vara = dados_14a_vara['Assunto'].value_counts()[:10].index.tolist()
top_15a_vara = dados_15a_vara['Assunto'].value_counts()[:10].index.tolist()

dados_por_vara = pd.DataFrame({

                 "1ª Vara Federal":top_1a_vara,
                 "2ª Vara Federal":top_2a_vara,
                 "4ª Vara Federal":top_4a_vara,
                 "5ª Vara Federal":top_5a_vara,
                 "6ª Vara Federal":top_6a_vara,
                 "8ª Vara Federal":top_8a_vara,
                 "9ª Vara Federal":top_9a_vara,
                 "10ª Vara Federal":top_10a_vara,
                 "11ª Vara Federal":top_11a_vara,
                 "12ª Vara Federal":top_12a_vara,
                 "14ª Vara Federal":top_14a_vara,
                 "15ª Vara Federal":top_15a_vara
})

#table = dbc.Table.from_dataframe(dados_por_vara, striped=True, bordered=True, hover=True)


#=======================================================
# quero um dataframe com o top 5 de assuntos da vara por mês:
