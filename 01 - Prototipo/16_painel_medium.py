import dash
import dash_auth
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import dash_table as dt
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
        dbc.Card(
            [   dbc.CardHeader("JFRN"),
                dbc.CardBody(
                    [
                        html.P("Clique abaixo e visite o site da JFRN", style=CARD_TEXT_STYLE),
                        dbc.Button("JFRN", href="https://www.jfrn.jus.br/", color="primary")
                    ]
                )
            ],
            color="info",
            outline=True
        ),md=4
    ),
    dbc.Col(
        dbc.Card(
            [   dbc.CardHeader("Centro de Inteligência"),
                dbc.CardBody(
                    [
                        html.P("Acesse o Centro de Int. da JFRN", style=CARD_TEXT_STYLE),
                        dbc.Button("Centro de Inteligência", href="https://centrodeinteligencia.jfrn.jus.br/jfrn/#/",color="primary")

                    ]
                )
            ],
            color="info",
            outline=True
        ),md=4
    ),
    dbc.Col(
        dbc.Card(
            [   dbc.CardHeader("Residência T.I."),
                dbc.CardBody(
                    [
                        html.P("Conheça melhor a Residência em TI", style=CARD_TEXT_STYLE),
                        dbc.Button("Residência em TI", href="https://residencia.jfrn.jus.br/",color="primary")

                    ]
                )
            ],
            color="info",
            outline=True
        ),md=4
    )
])


content_second_row = dbc.Row([
    dbc.Col(
        html.Div([dcc.Graph(id='grafico_1',responsive=True)],style={"border":"2px black solid"}),
    )])

'''
import plotly.express as px
df = px.data.gapminder().query("year == 2007").query("continent == 'Europe'")
df.loc[df['pop'] < 2.e6, 'country'] = 'Other countries' # Represent only large countries
fig = px.pie(df, values='pop', names='country', title='Population of European continent')
fig.show()

'''

content_third_row = dbc.Row([
        dbc.Col(
        html.Div([
        html.H3('Tabela com as maiores demandas das Varas de acordo com o ano escolhido', style=TEXT_STYLE),
        html.Div(id="table1"),
        html.Div(id='submit-button',
                 children='Ver tabela')
    ])

,md=12)
])


content = html.Div(
    [
        html.H2('Painel do Centro de Inteligência', style=TEXT_STYLE),
        html.Hr(),
        content_first_row,
        content_second_row,
        content_third_row
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

    #vara_escolhida['Assunto'] = vara['Assunto'].value_counts()[:5].index.tolist()

    traces = []

    for assunto_processo in vara_escolhida['Assunto'].unique():
        vara_filtrada = vara_escolhida[vara_escolhida['Assunto']==assunto_processo]
        traces.append(go.Bar(
               x=vara_filtrada['mes_primeira_dist'],
               y=vara_filtrada['Assunto'].value_counts()[:5].index.tolist(),
               showlegend=False
         ))

    return {'data':traces,
            'layout':go.Layout(title= {"text": "Distribuição de processos por mês da {} no ano {}".format(vara_selecionada,ano_escolhido)},
                               xaxis = {'title':'Mês da distribuição','categoryorder':'category ascending'},
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


@app.callback(Output('table1','children'),
            [Input('escolhe-ano','value')])
def update_datatable(ano_escolhido):

    if True:

        ajustes_dados = dados_varas[dados_varas['ano_primeira_dist']==ano_escolhido]

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


        top_geral = ajustes_dados['Assunto'].value_counts()[:5].index.tolist()
        top_1a_vara = dados_1a_vara['Assunto'].value_counts()[:5].index.tolist()
        top_2a_vara = dados_2a_vara['Assunto'].value_counts()[:5].index.tolist()
        top_4a_vara = dados_4a_vara['Assunto'].value_counts()[:5].index.tolist()
        top_5a_vara = dados_5a_vara['Assunto'].value_counts()[:5].index.tolist()
        top_6a_vara = dados_6a_vara['Assunto'].value_counts()[:5].index.tolist()
        top_8a_vara = dados_8a_vara['Assunto'].value_counts()[:5].index.tolist()
        top_9a_vara = dados_9a_vara['Assunto'].value_counts()[:5].index.tolist()
        top_10a_vara = dados_10a_vara['Assunto'].value_counts()[:5].index.tolist()
        top_11a_vara = dados_11a_vara['Assunto'].value_counts()[:5].index.tolist()
        top_12a_vara = dados_12a_vara['Assunto'].value_counts()[:5].index.tolist()
        top_14a_vara = dados_14a_vara['Assunto'].value_counts()[:5].index.tolist()
        top_15a_vara = dados_15a_vara['Assunto'].value_counts()[:5].index.tolist()

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
        data = dados_por_vara.to_dict('rows')
        columns =  [{"name": i, "id": i,} for i in (dados_por_vara.columns)]
        return dt.DataTable(data=data, columns=columns,style_table={'overflowX': 'auto'})





if __name__ == '__main__':
    app.run_server()
