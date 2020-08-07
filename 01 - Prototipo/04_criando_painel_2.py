import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd
from numpy import random
import plotly.graph_objs as go
import pandas_datareader.data as web
from datetime import datetime
import numpy as np
import os

app = dash.Dash()

dados_varas = pd.read_csv('../dados-pje-MPF.csv',dtype='unicode')

dados_varas['ano_primeira_dist'] = pd.DatetimeIndex(dados_varas['Data Primeira Distribuição']).year
dados_varas['mes_primeira_dist'] = pd.DatetimeIndex(dados_varas['Data Primeira Distribuição']).month

'''
Index(['Unnamed: 0', '%ID_PROCESSO_TRF', 'Sistema', 'Número Processo',
       'Status do Processo', 'Data Última Distribuição', 'Assunto Código',
       'Assunto', 'Data Primeira Distribuição', 'Classe Judicial',
       'Órgão Julgador', 'Parte Polo Ativo?', 'Parte Polo Passivo?',
       'Parte Outros Participantes?', 'Parte Documento', 'Parte Descrição',
       '%ID_PESSOA_REU', 'Data Trânsito Julgado', 'Número Tempo em Anos'],
'''

opcoes_ano = []
for ano in dados_varas['ano_primeira_dist'].unique():
    opcoes_ano.append({'label':ano,'value':ano})

opcoes_vara = []
for vara in dados_varas['Órgão Julgador'].unique():
    opcoes_vara.append({'label':str(vara),'value':vara})

app.layout = html.Div([
             html.H1('Painel de visualização dos assuntos mês a mês'),
             html.Div([html.H3('Selecione uma vara: ', style={'paddingRight':'30px'}),
             dcc.Dropdown(id='escolhe-vara',options=opcoes_vara,value='None')],
             style={'display':'inline-block','verticalAlign':'top','width':'30%'}),

             html.Div([html.H3('Selecione o ano a ser visualizado: ',style={'paddingRight':'30px'}),
             dcc.Dropdown(id='escolhe-ano',options=opcoes_ano,value='None')],
             style={'display':'inline-block','verticalAlign':'top','width':'30%'}),
             dcc.Graph(id='grafico')
])

@app.callback(Output('grafico','figure'),
             [Input('escolhe-vara','value')],
             [State('escolhe-ano','value')])
def update_figure(vara_selecionada,ano_escolhido):
    #dados apenas para seleção do menu dropdown
    vara_escolhida = dados_varas[dados_varas['Órgão Julgador']==vara_selecionada]
    vara_escolhida = vara_escolhida[vara_escolhida['ano_primeira_dist']==ano_escolhido]
    traces = []

    for assunto_processo in vara_escolhida['Assunto'].unique():
        vara_filtrada = vara_escolhida[vara_escolhida['Assunto']==assunto_processo]
        traces.append(go.Bar(
               x=vara_filtrada['mes_primeira_dist'],
               y=vara_filtrada['Assunto']
         ))

    return {'data':traces,
            'layout':go.Layout(title= 'Assunto dos processos por Vara',
                               xaxis = {'title':'Data da distrubuição'},
                               yaxis = {'title':'Assunto'})}


if __name__ == '__main__':
    app.run_server()
