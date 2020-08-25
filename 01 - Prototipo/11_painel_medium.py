import dash
import dash_auth
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import pandas as pd
from numpy import random
import plotly.graph_objs as go
import numpy as np
import plotly.express as px

USERNAME_PASSWORD_PAIRS = [
    ['EliasJacob', 'PinkFloyd1973']
]

dados_varas = pd.read_csv('../dados-pje-MPF.csv',dtype='unicode')

dados_varas['ano_primeira_dist'] = pd.DatetimeIndex(dados_varas['Data Primeira Distribuição']).year

dados_varas=dados_varas[dados_varas.ano_primeira_dist > 2014]

dados_varas['mes_primeira_dist'] = pd.DatetimeIndex(dados_varas['Data Primeira Distribuição']).month

dados_varas.sort_values(['ano_primeira_dist','mes_primeira_dist'])

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

# the style arguments for the sidebar.
SIDEBAR_STYLE = {
    'position': 'fixed',
    'top': 0,
    'left': 0,
    'bottom': 0,
    'width': '20%',
    'padding': '20px 10px',
    'background-color': '#f8f9fa'
}

# the style arguments for the main content page.
CONTENT_STYLE = {
    'margin-left': '25%',
    'margin-right': '5%',
    'padding': '20px 10p'
}

TEXT_STYLE = {
    'textAlign': 'center',
    'color': '#191970'
}

CARD_TEXT_STYLE = {
    'textAlign': 'center',
    'color': '#0074D9'
}

controls = dbc.FormGroup([
           html.P("Escolha o órgão julgador: ", style={'textAlign': 'center'}),
           dcc.Dropdown(id='escolhe-vara',options=opcoes_vara,value='None'),
           html.Br(),
           html.P("Escolha o ano a ser visualizado: ",style={'textAlign': 'center'}),
           dcc.Dropdown(id='escolhe-ano',options=opcoes_ano,value='None')
])

sidebar = html.Div(
    [
        html.H2("Parâmetros", style=TEXT_STYLE),
        html.Hr(),
        controls
    ],
    style=SIDEBAR_STYLE,
)


content_first_row = dbc.Row([
    dbc.Col(
        html.Div([dcc.Graph(id='grafico_1',responsive=True)],style={"border":"2px black solid"}),
    ),
    dbc.Col(
        html.Div([dcc.Graph(id='grafico_2',responsive=True)],style={"border":"2px black solid"})
        )
])



content = html.Div(
    [
        html.H2('Painel do Centro de Inteligência', style=TEXT_STYLE),
        html.Hr(),
        content_first_row
        #content_second_row,
        #content_third_row,
        #content_fourth_row
    ],
    style=CONTENT_STYLE
)

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = html.Div([sidebar, content])


@app.callback(Output('grafico_1','figure'),
             [Input('escolhe-vara','value'),
              Input('escolhe-ano','value')])
def update_figure(vara_selecionada,ano_escolhido):
    #dados apenas para seleção do menu dropdown
    vara_escolhida = dados_varas[dados_varas['Órgão Julgador']==vara_selecionada]
    vara_escolhida = vara_escolhida[vara_escolhida['ano_primeira_dist']==ano_escolhido]

    vara_escolhida.sort_values(['mes_primeira_dist'])

    vara_escolhida['mes_primeira_dist'] = vara_escolhida['mes_primeira_dist'].replace(1,'01 - Jan')
    vara_escolhida['mes_primeira_dist'] = vara_escolhida['mes_primeira_dist'].replace(2,'02 - Fev')
    vara_escolhida['mes_primeira_dist'] = vara_escolhida['mes_primeira_dist'].replace(3,'03 - Mar')
    vara_escolhida['mes_primeira_dist'] = vara_escolhida['mes_primeira_dist'].replace(4,'04 - Abr')
    vara_escolhida['mes_primeira_dist'] = vara_escolhida['mes_primeira_dist'].replace(5,'05 - Mai')
    vara_escolhida['mes_primeira_dist'] = vara_escolhida['mes_primeira_dist'].replace(6,'06 - Jun')
    vara_escolhida['mes_primeira_dist'] = vara_escolhida['mes_primeira_dist'].replace(7,'07 - Jul')
    vara_escolhida['mes_primeira_dist'] = vara_escolhida['mes_primeira_dist'].replace(8,'08 - Ago')
    vara_escolhida['mes_primeira_dist'] = vara_escolhida['mes_primeira_dist'].replace(9,'09 - Set')
    vara_escolhida['mes_primeira_dist'] = vara_escolhida['mes_primeira_dist'].replace(10,'10 - Out')
    vara_escolhida['mes_primeira_dist'] = vara_escolhida['mes_primeira_dist'].replace(11,'11 - Nov')
    vara_escolhida['mes_primeira_dist'] = vara_escolhida['mes_primeira_dist'].replace(12,'12 - Dez')

    traces = []

    for assunto_processo in vara_escolhida['Assunto'].unique():
        vara_filtrada = vara_escolhida[vara_escolhida['Assunto']==assunto_processo]
        traces.append(go.Bar(
               x=vara_filtrada['mes_primeira_dist'],
               y=vara_filtrada['Assunto'],
               showlegend=False
         ))

    return {'data':traces,
            'layout':go.Layout(title= {"text": "Distribuição de processos por mês da {}".format(vara_selecionada)},
                               xaxis = {'title':'Mês da distrubuição','categoryorder':'category ascending'},
                               yaxis = {'title':'Assunto','visible':False},
                               barmode='stack')}


@app.callback(Output('grafico_2','figure'),
             [Input('escolhe-ano','value')])
def update_figure_2(ano_escolhido):
    ano_selecionado = dados_varas[dados_varas['ano_primeira_dist']==ano_escolhido]

    traces_vara = []
    for assunto_vara in ano_selecionado['Assunto'].unique():
        vara_filtrada = ano_selecionado[ano_selecionado['Assunto']==assunto_vara]
        traces_vara.append(go.Bar(
               x=vara_filtrada['Órgão Julgador'],
               y=vara_filtrada['Assunto'],
               showlegend=False
         ))

    return {'data':traces_vara,
            'layout':go.Layout(title= 'Distribuição de processos pelos Órgãos Julgadores no ano {}'.format(ano_escolhido),
                               xaxis = {'title':'Órgão Julgador','categoryorder':'category ascending'},
                               yaxis = {'title':'Total de Processos'},
                               barmode='stack')}


if __name__ == '__main__':
    app.run_server()
