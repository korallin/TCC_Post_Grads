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

# janeiro
dados_janeiro = dados_ajustados[dados_ajustados['mes_primeira_dist'] == 1]
#janeiro = dados_janeiro["Assunto Código"].describe()
# isso abaixo é um DataFrame
janeiro_acima_media = dados_janeiro[dados_janeiro["Assunto Código"] > media_ano]
janeiro_anomalia = dados_janeiro[dados_janeiro["Assunto Código"] > anomalia_ano]
# encontrando os assuntos de janeiro
janeiro_acima_media_lista = janeiro_acima_media["Assunto"].tolist()
janeiro_anomalia_lista = janeiro_anomalia["Assunto"].tolist()

# fevereiro
dados_fevereiro = dados_ajustados[dados_ajustados['mes_primeira_dist'] == 2]
fevereiro_acima_media = dados_fevereiro[dados_fevereiro["Assunto Código"] > media_ano]
fevereiro_anomalia = dados_fevereiro[dados_fevereiro["Assunto Código"] > anomalia_ano]
# encontrando os assuntos de fevereiro
fevereiro_acima_media_lista = fevereiro_anomalia_acima_media["Assunto"].tolist()
fevereiro_anomalia_lista = fevereiro_anomalia["Assunto"].tolist()

# março
dados_marco = dados_ajustados[dados_ajustados['mes_primeira_dist'] == 3]
marco_acima_media = dados_marco[dados_marco["Assunto Código"] > media_ano]
marco_anomalia = dados_marco[dados_marco["Assunto Código"] > anomalia_ano]
# encontrando os assuntos de fevereiro
marco_acima_media_lista = marco_acima_media["Assunto"].tolist()
marco_anomalia_lista = marco_anomalia["Assunto"].tolist()

# abril
dados_abril = dados_ajustados[dados_ajustados['mes_primeira_dist'] == 4]
abril_acima_media = dados_abril[dados_abril["Assunto Código"] > media_ano]
abril_anomalia = dados_abril[dados_abril["Assunto Código"] > anomalia_ano]
# encontrando os assuntos de fevereiro
abril_acima_media_lista = abril_acima_media["Assunto"].tolist()
abril_anomalia_lista = abril_anomalia["Assunto"].tolist()

# maio
dados_maio = dados_ajustados[dados_ajustados['mes_primeira_dist'] == 5]
maio_acima_media = dados_maio[dados_maio["Assunto Código"] > media_ano]
maio_anomalia = dados_maio[dados_maio["Assunto Código"] > anomalia_ano]
# encontrando os assuntos de fevereiro
maio_acima_media_lista = maio_acima_media["Assunto"].tolist()
maio_anomalia_lista = maio_anomalia["Assunto"].tolist()

# junho
dados_junho = dados_ajustados[dados_ajustados['mes_primeira_dist'] == 6]
junho_acima_media = dados_junho[dados_junho["Assunto Código"] > media_ano]
junho_anomalia = dados_junho[dados_junho["Assunto Código"] > anomalia_ano]
# encontrando os assuntos de fevereiro
junho_acima_media_lista = junho_acima_media["Assunto"].tolist()
junho_anomalia_lista = junho_anomalia["Assunto"].tolist()

# julho
dados_julho = dados_ajustados[dados_ajustados['mes_primeira_dist'] == 7]
julho_acima_media = dados_julho[dados_julho["Assunto Código"] > media_ano]
julho_anomalia = dados_julho[dados_julho["Assunto Código"] > anomalia_ano]
# encontrando os assuntos de fevereiro
julho_acima_media_lista = julho_acima_media["Assunto"].tolist()
julho_anomalia_lista = julho_anomalia["Assunto"].tolist()

# agosto
dados_agosto = dados_ajustados[dados_ajustados['mes_primeira_dist'] == 8]
agosto_acima_media = dados_agosto[dados_agosto["Assunto Código"] > media_ano]
agosto_anomalia = dados_agosto[dados_agosto["Assunto Código"] > anomalia_ano]
# encontrando os assuntos de fevereiro
agosto_acima_media_lista = agosto_acima_media["Assunto"].tolist()
agosto_anomalia_lista = agosto_anomalia["Assunto"].tolist()

# setembro
dados_setembro = dados_ajustados[dados_ajustados['mes_primeira_dist'] == 9]
setembro_acima_media = dados_setembro[dados_setembro["Assunto Código"] > media_ano]
setembro_anomalia = dados_setembro[dados_setembro["Assunto Código"] > anomalia_ano]
# encontrando os assuntos de fevereiro
setembro_acima_media_lista = setembro_acima_media["Assunto"].tolist()
setembro_anomalia_lista = setembro_anomalia["Assunto"].tolist()

# outubro
dados_outubro = dados_ajustados[dados_ajustados['mes_primeira_dist'] == 10]
outubro_acima_media = dados_outubro[dados_outubro["Assunto Código"] > media_ano]
outubro_anomalia = dados_outubro[dados_outubro["Assunto Código"] > anomalia_ano]
# encontrando os assuntos de fevereiro
outubro_acima_media_lista = outubro_acima_media["Assunto"].tolist()
outubro_anomalia_lista = outubro_anomalia["Assunto"].tolist()

# novembro
dados_novembro = dados_ajustados[dados_ajustados['mes_primeira_dist'] == 11]
novembro_acima_media = dados_novembro[dados_novembro["Assunto Código"] > media_ano]
novembro_anomalia = dados_novembro[dados_novembro["Assunto Código"] > anomalia_ano]
# encontrando os assuntos de fevereiro
novembro_acima_media_lista = novembro_acima_media["Assunto"].tolist()
novembro_anomalia_lista = novembro_anomalia["Assunto"].tolist()

# dezembro
dados_dezembro = dados_ajustados[dados_ajustados['mes_primeira_dist'] == 12]
dezembro_acima_media = dados_dezembro[dados_dezembro["Assunto Código"] > media_ano]
dezembro_anomalia = dados_dezembro[dados_dezembro["Assunto Código"] > anomalia_ano]
# encontrando os assuntos de fevereiro
dezembro_acima_media_lista = dezembro_acima_media["Assunto"].tolist()
dezembro_anomalia_lista = dezembro_anomalia["Assunto"].tolist()


'''
#['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
prototipo de dataframe para mostrar em gráfico de barras

df = {'Meses':['Janeiro'],
      'Anomalia':janeiro_anomalia_lista,
      'Média':janeiro_acima_media_lista}


print("A seguir serão mostrados os Assuntos que apareceram em Janeiro numa frequência acima da média: ")
for i in range(len(janeiro_acima_media_lista)):
    print (janeiro_acima_media_lista[i])

print("A seguir serão mostrados os Assuntos que apareceram em Janeiro numa frequência muito acima da média: ")
for j in range(len(janeiro_anomalia_lista)):
    print (janeiro_anomalia_lista[j])

df = {'Meses':['Janeiro'],
      'Anomalia':janeiro_anomalia_lista,
      'Média':janeiro_acima_media_lista}
'''
