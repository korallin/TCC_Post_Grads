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

print(ajustes_dados.head(20))
