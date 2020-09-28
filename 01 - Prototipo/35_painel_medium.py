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
           dcc.Dropdown(id='escolhe-vara',options=opcoes_vara,value='6ª Vara Federal'),
           html.Br(),
           html.P("Escolha o ano a ser visualizado: ",style={'textAlign': 'center'}),
           dcc.Dropdown(id='escolhe-ano',options=opcoes_ano,value='2015')
])

controls_2 = dbc.FormGroup([
           html.P("Escolha o órgão julgador: ", style={'textAlign': 'center'}),
           dcc.Dropdown(id='escolhe-vara-2',options=opcoes_vara,value='6ª Vara Federal'),
           html.Br(),
           html.P("Escolha o ano a ser visualizado: ",style={'textAlign': 'center'}),
           dcc.Dropdown(id='escolhe-ano-2',options=opcoes_ano,value='2015')
])

sidebar = html.Div(
    [
        html.H2("Parâmetros", style=TEXT_STYLE),
        html.Hr(),
        controls
    ],
    style=SIDEBAR_STYLE,
)

sidebar_2 = html.Div(
    [
        html.H2("Parâmetros", style=TEXT_STYLE),
        html.Hr(),
        controls_2
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
    html.Div([
    html.Div(id="grafico_3",children='tabela_atualizada')
    #html.Div(id='submit-button-2', children='Ver tabela')
])
    ,md=12)
])

'''
content_fourth_row = dbc.Row([
        dbc.Col(
        html.Div([
        html.Div(id="table1",children='tabela_atualizada')
        #html.Div(id='submit-button-2', children='Ver tabela')
])
        ,md=12)
])
import plotly.express as px
df = px.data.gapminder().query("year == 2007").query("continent == 'Europe'")
df.loc[df['pop'] < 2.e6, 'country'] = 'Other countries' # Represent only large countries
fig = px.pie(df, values='pop', names='country', title='Population of European continent')
fig.show()

'''

content_third_row = dbc.Row([
        dbc.Col(
        html.Div([
        html.Div(id="table2",children='tabela_atualizada')
        #html.Div(id='submit-button',children='Ver tabela')
])
        ,md=12)
])


content_fifth_row = dbc.Row([
        dbc.Col(
        html.Div([
        html.H3('Mapa de calor com taxa de retenção de processos: ', style=TEXT_STYLE),
        html.Div([dcc.Graph(id='mapa1')],style={"width": "100%", "display": "inline-block"})
        #html.Div(id='submit-button',children='Ver tabela')
])
        ,md=12)
])

# html.H1('Hello Dash', style={'background-image': 'url(https://upload.wikimedia.org/wikipedia/commons/2/22/North_Star_-_invitation_background.png)'})
content_tab_1 = html.Div(
    [
        html.H1(html.Div(html.Img(src="https://intranet2.jfrn.jus.br/intranet/javax.faces.resource/logo-nti.png.xhtml?ln=img", style={'height':'10%', 'width':'10%', 'float':'right'}))),
        html.H1('Painel do Centro de Inteligência', style=TEXT_STYLE),
        html.Hr(),
        content_first_row,
        html.Hr(),
        content_second_row,
        html.Hr(),
        content_third_row,
        html.Hr(),
        content_fifth_row

    ],
    style=CONTENT_STYLE
)
content_tab_2 = html.Div(
    [
        html.H1(html.Div(html.Img(src="https://intranet2.jfrn.jus.br/intranet/javax.faces.resource/logo-nti.png.xhtml?ln=img", style={'height':'10%', 'width':'10%', 'float':'right'}))),
        html.H1('Painel do Centro de Inteligência', style=TEXT_STYLE),
        html.Hr(),
        dcc.Graph(figure={
                    'data': [
                        {'x': [1, 2, 3], 'y': [2, 4, 3],
                            'type': 'bar', 'name': 'SF'},
                        {'x': [1, 2, 3], 'y': [5, 4, 3],
                         'type': 'bar', 'name': u'Montréal'},]})],
    style=CONTENT_STYLE
)

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
#auth = dash_auth.BasicAuth(app,USERNAME_PASSWORD_PAIRS)
app.layout = html.Div([dcc.Tabs(children=[
                       dcc.Tab(label='Análises Gerais', children=[sidebar,content_tab_1]),
                       dcc.Tab(label='Competência', children=[sidebar_2,content_tab_2])])
             ])

server = app.server

@app.callback(Output('grafico_3','children'),
            [Input('escolhe-ano','value'),
            Input('escolhe-vara','value')])
def update_datatable(ano_escolhido, vara_escolhida):

    #dados_varas.sort_values(['mes_primeira_dist'])
    ano_escolhido = float(ano_escolhido)

    dados_1 = dados_varas[dados_varas['Órgão Julgador'] == vara_escolhida]
    dados_2 = dados_1[dados_1['ano_primeira_dist'] <= ano_escolhido]
    ano_anterior = ano_escolhido - 1.0
    dados_2 = dados_2[dados_2['ano_primeira_dist'] >= ano_anterior]

    dados_2 = dados_2.groupby(['mes_primeira_dist', 'Assunto'])['Assunto Código'].count()
    dados_ajustados_estatistica = dados_2.groupby(level='mes_primeira_dist').nlargest(25).reset_index(level=0, drop=True).reset_index()

    estatisticas_ano = dados_ajustados_estatistica["Assunto Código"].describe()
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
    anomalia_ano_1 = desvio_padrao_ano + media_ano
    anomalia_ano_2 = 2*desvio_padrao_ano + media_ano

    construcao_grafico = dados_varas[dados_varas['Órgão Julgador'] == vara_escolhida]
    construcao_grafico = construcao_grafico[construcao_grafico['ano_primeira_dist'] == ano_escolhido]
    dados_ajustados = construcao_grafico.groupby(['mes_primeira_dist', 'Assunto'])['Assunto Código'].count()
    dados_ajustados = dados_ajustados.groupby(level='mes_primeira_dist').nlargest(25).reset_index(level=0, drop=True).reset_index()


    # janeiro
    dados_janeiro = dados_ajustados[dados_ajustados['mes_primeira_dist'] == 1]
    # janeiro = dados_janeiro["Assunto Código"].describe()
    # isso abaixo é um DataFrame
    janeiro_acima_media = dados_janeiro[dados_janeiro["Assunto Código"] > media_ano]
    janeiro_anomalia = dados_janeiro[dados_janeiro["Assunto Código"] > media_ano]
    # encontrando os assuntos de janeiro
    janeiro_acima_media_lista = janeiro_acima_media["Assunto"].tolist()
    janeiro_anomalia_lista = janeiro_anomalia["Assunto Código"].tolist()

    # fevereiro
    dados_fevereiro = dados_ajustados[dados_ajustados['mes_primeira_dist'] == 2]
    fevereiro_acima_media = dados_fevereiro[dados_fevereiro["Assunto Código"] > media_ano]
    fevereiro_anomalia = dados_fevereiro[dados_fevereiro["Assunto Código"] > media_ano]
    # encontrando os assuntos de fevereiro
    fevereiro_acima_media_lista = fevereiro_acima_media["Assunto"].tolist()
    fevereiro_anomalia_lista = fevereiro_anomalia["Assunto Código"].tolist()

    # março
    dados_marco = dados_ajustados[dados_ajustados['mes_primeira_dist'] == 3]
    marco_acima_media = dados_marco[dados_marco["Assunto Código"] > media_ano]
    marco_anomalia = dados_marco[dados_marco["Assunto Código"] > media_ano]
    # encontrando os assuntos de fevereiro
    marco_acima_media_lista = marco_acima_media["Assunto"].tolist()
    marco_anomalia_lista = marco_anomalia["Assunto Código"].tolist()

    # abril
    dados_abril = dados_ajustados[dados_ajustados['mes_primeira_dist'] == 4]
    abril_acima_media = dados_abril[dados_abril["Assunto Código"] > media_ano]
    abril_anomalia = dados_abril[dados_abril["Assunto Código"] > media_ano]
    # encontrando os assuntos de fevereiro
    abril_acima_media_lista = abril_acima_media["Assunto"].tolist()
    abril_anomalia_lista = abril_anomalia["Assunto Código"].tolist()

    # maio
    dados_maio = dados_ajustados[dados_ajustados['mes_primeira_dist'] == 5]
    maio_acima_media = dados_maio[dados_maio["Assunto Código"] > media_ano]
    maio_anomalia = dados_maio[dados_maio["Assunto Código"] > media_ano]
    # encontrando os assuntos de fevereiro
    maio_acima_media_lista = maio_acima_media["Assunto"].tolist()
    maio_anomalia_lista = maio_anomalia["Assunto Código"].tolist()

    # junho
    dados_junho = dados_ajustados[dados_ajustados['mes_primeira_dist'] == 6]
    junho_acima_media = dados_junho[dados_junho["Assunto Código"] > media_ano]
    junho_anomalia = dados_junho[dados_junho["Assunto Código"] > media_ano]
    # encontrando os assuntos de fevereiro
    junho_acima_media_lista = junho_acima_media["Assunto"].tolist()
    junho_anomalia_lista = junho_anomalia["Assunto Código"].tolist()

    # julho
    dados_julho = dados_ajustados[dados_ajustados['mes_primeira_dist'] == 7]
    julho_acima_media = dados_julho[dados_julho["Assunto Código"] > media_ano]
    julho_anomalia = dados_julho[dados_julho["Assunto Código"] > media_ano]
    # encontrando os assuntos de fevereiro
    julho_acima_media_lista = julho_acima_media["Assunto"].tolist()
    julho_anomalia_lista = julho_anomalia["Assunto Código"].tolist()

    # agosto
    dados_agosto = dados_ajustados[dados_ajustados['mes_primeira_dist'] == 8]
    agosto_acima_media = dados_agosto[dados_agosto["Assunto Código"] > media_ano]
    agosto_anomalia = dados_agosto[dados_agosto["Assunto Código"] > media_ano]
    # encontrando os assuntos de fevereiro
    agosto_acima_media_lista = agosto_acima_media["Assunto"].tolist()
    agosto_anomalia_lista = agosto_anomalia["Assunto Código"].tolist()

    # setembro
    dados_setembro = dados_ajustados[dados_ajustados['mes_primeira_dist'] == 9]
    setembro_acima_media = dados_setembro[dados_setembro["Assunto Código"] > media_ano]
    setembro_anomalia = dados_setembro[dados_setembro["Assunto Código"] > media_ano]
    # encontrando os assuntos de fevereiro
    setembro_acima_media_lista = setembro_acima_media["Assunto"].tolist()
    setembro_anomalia_lista = setembro_anomalia["Assunto Código"].tolist()

    # outubro
    dados_outubro = dados_ajustados[dados_ajustados['mes_primeira_dist'] == 10]
    outubro_acima_media = dados_outubro[dados_outubro["Assunto Código"] > media_ano]
    outubro_anomalia = dados_outubro[dados_outubro["Assunto Código"] > media_ano]
    # encontrando os assuntos de fevereiro
    outubro_acima_media_lista = outubro_acima_media["Assunto"].tolist()
    outubro_anomalia_lista = outubro_anomalia["Assunto Código"].tolist()

    # novembro
    dados_novembro = dados_ajustados[dados_ajustados['mes_primeira_dist'] == 11]
    novembro_acima_media = dados_novembro[dados_novembro["Assunto Código"] > media_ano]
    novembro_anomalia = dados_novembro[dados_novembro["Assunto Código"] > media_ano]
    # encontrando os assuntos de fevereiro
    novembro_acima_media_lista = novembro_acima_media["Assunto"].tolist()
    novembro_anomalia_lista = novembro_anomalia["Assunto Código"].tolist()

    # dezembro
    dados_dezembro = dados_ajustados[dados_ajustados['mes_primeira_dist'] == 12]
    dezembro_acima_media = dados_dezembro[dados_dezembro["Assunto Código"] > media_ano]
    dezembro_anomalia = dados_dezembro[dados_dezembro["Assunto Código"] > media_ano]
    # encontrando os assuntos de fevereiro
    dezembro_acima_media_lista = dezembro_acima_media["Assunto"].tolist()
    dezembro_anomalia_lista = dezembro_anomalia["Assunto Código"].tolist()


    dados_analise_estatistica = pd.DataFrame({

                     "Janeiro": pd.Series(janeiro_acima_media_lista),
                     "01_total": pd.Series(janeiro_anomalia_lista),
                     "Fevereiro": pd.Series(fevereiro_acima_media_lista),
                     "02_total": pd.Series(fevereiro_anomalia_lista),
                     "Março:": pd.Series(marco_acima_media_lista),
                     "03_total": pd.Series(marco_anomalia_lista),
                     "Abril:": pd.Series(abril_acima_media_lista),
                     "04_total": pd.Series(abril_anomalia_lista),
                     "Maio:": pd.Series(maio_acima_media_lista),
                     "05_total": pd.Series(maio_anomalia_lista),
                     "Junho:": pd.Series(junho_acima_media_lista),
                     "06_total": pd.Series(junho_anomalia_lista),
                     "Julho:": pd.Series(julho_acima_media_lista),
                     "07_total": pd.Series(julho_anomalia_lista),
                     "Agosto:": pd.Series(agosto_acima_media_lista),
                     "08_total": pd.Series(agosto_anomalia_lista),
                     "Setembro:":pd.Series(setembro_acima_media_lista),
                     "09_total": pd.Series(setembro_anomalia_lista),
                     "Outubro:": pd.Series(outubro_acima_media_lista),
                     "10_total": pd.Series(outubro_anomalia_lista),
                     "Novembro:": pd.Series(novembro_acima_media_lista),
                     "11_total": pd.Series(novembro_anomalia_lista),
                     "Dezembro:": pd.Series(dezembro_acima_media_lista),
                     "12_total": pd.Series(dezembro_anomalia_lista)

    })

    estilo_cabecalho = {
        'backgroundColor': 'rgb(230, 230, 230)',
        'fontWeight': 'bold'
    }
    data = dados_analise_estatistica.to_dict('records')
    columns =  [{"name": i, "id": i,} for i in (dados_analise_estatistica.columns)]

    style_data_conditional=[
        {
            'if': {
                'filter_query': '{{01_total}} > {}'.format(anomalia_ano_2),
                'column_id': '01_total'
            },
            'backgroundColor': '#FF4136',
            'color': 'white',
            'fontWeight': 'bold'
        },
        {
            'if': {
                'filter_query': '{{01_total}} > {} && {{01_total}} <= {}'.format(anomalia_ano_1,anomalia_ano_2),
                'column_id': '01_total'
            },
            'backgroundColor': '#FFFF00',
            'color': 'black',
            'fontWeight': 'bold'
        },
        {
            'if': {
                'filter_query': '{{01_total}} >= {} && {{01_total}} <= {}'.format(media_ano,anomalia_ano_1),
                'column_id': '01_total'
            },
            'backgroundColor': '#008000',
            'color': 'white',
            'fontWeight': 'bold'
        },
        {
            'if': {
                'filter_query': '{{02_total}} > {}'.format(anomalia_ano_2),
                'column_id': '02_total'
            },
            'backgroundColor': '#FF4136',
            'color': 'white',
            'fontWeight': 'bold'
            },
        {
            'if': {
                'filter_query': '{{02_total}} > {} && {{02_total}} <= {}'.format(anomalia_ano_1,anomalia_ano_2),
                'column_id': '02_total'
        },
            'backgroundColor': '#FFFF00',
            'color': 'black',
            'fontWeight': 'bold'
        },
        {
            'if': {
                'filter_query': '{{02_total}} >= {} && {{02_total}} <= {}'.format(media_ano,anomalia_ano_1),
                'column_id': '02_total'
        },
            'backgroundColor': '#008000',
            'color': 'white',
            'fontWeight': 'bold'
        },
        {
            'if': {
                'filter_query': '{{03_total}} > {}'.format(anomalia_ano_2),
                'column_id': '03_total'
            },
            'backgroundColor': '#FF4136',
            'color': 'white',
            'fontWeight': 'bold'
            },
        {
            'if': {
                'filter_query': '{{03_total}} > {} && {{03_total}} <= {}'.format(anomalia_ano_1,anomalia_ano_2),
                'column_id': '03_total'
        },
            'backgroundColor': '#FFFF00',
            'color': 'black',
            'fontWeight': 'bold'
        },
        {
            'if': {
                'filter_query': '{{03_total}} >= {} && {{03_total}} <= {}'.format(media_ano,anomalia_ano_1),
                'column_id': '03_total'
        },
            'backgroundColor': '#008000',
            'color': 'white',
            'fontWeight': 'bold'
        },
        {
            'if': {
                'filter_query': '{{04_total}} > {}'.format(anomalia_ano_2),
                'column_id': '04_total'
            },
            'backgroundColor': '#FF4136',
            'color': 'white',
            'fontWeight': 'bold'
            },
        {
            'if': {
                'filter_query': '{{04_total}} > {} && {{04_total}} <= {}'.format(anomalia_ano_1,anomalia_ano_2),
                'column_id': '04_total'
        },
            'backgroundColor': '#FFFF00',
            'color': 'black',
            'fontWeight': 'bold'
        },
        {
            'if': {
                'filter_query': '{{04_total}} >= {} && {{04_total}} <= {}'.format(media_ano,anomalia_ano_1),
                'column_id': '04_total'
        },
            'backgroundColor': '#008000',
            'color': 'white',
            'fontWeight': 'bold'
        },
        {
            'if': {
                'filter_query': '{{05_total}} > {}'.format(anomalia_ano_2),
                'column_id': '05_total'
            },
            'backgroundColor': '#FF4136',
            'color': 'white',
            'fontWeight': 'bold'
            },
        {
            'if': {
                'filter_query': '{{05_total}} > {} && {{05_total}} <= {}'.format(anomalia_ano_1,anomalia_ano_2),
                'column_id': '05_total'
        },
            'backgroundColor': '#FFFF00',
            'color': 'black',
            'fontWeight': 'bold'
        },
        {
            'if': {
                'filter_query': '{{05_total}} >= {} && {{05_total}} <= {}'.format(media_ano,anomalia_ano_1),
                'column_id': '05_total'
        },
            'backgroundColor': '#008000',
            'color': 'white',
            'fontWeight': 'bold'
        },
        {
            'if': {
                'filter_query': '{{06_total}} > {}'.format(anomalia_ano_2),
                'column_id': '06_total'
            },
            'backgroundColor': '#FF4136',
            'color': 'white',
            'fontWeight': 'bold'
            },
        {
            'if': {
                'filter_query': '{{06_total}} > {} && {{06_total}} <= {}'.format(anomalia_ano_1,anomalia_ano_2),
                'column_id': '06_total'
        },
            'backgroundColor': '#FFFF00',
            'color': 'black',
            'fontWeight': 'bold'
        },
        {
            'if': {
                'filter_query': '{{06_total}} >= {} && {{06_total}} <= {}'.format(media_ano,anomalia_ano_1),
                'column_id': '06_total'
        },
            'backgroundColor': '#008000',
            'color': 'white',
            'fontWeight': 'bold'
        },
        {
            'if': {
                'filter_query': '{{07_total}} > {}'.format(anomalia_ano_2),
                'column_id': '07_total'
            },
            'backgroundColor': '#FF4136',
            'color': 'white',
            'fontWeight': 'bold'
            },
        {
            'if': {
                'filter_query': '{{07_total}} > {} && {{07_total}} <= {}'.format(anomalia_ano_1,anomalia_ano_2),
                'column_id': '07_total'
        },
            'backgroundColor': '#FFFF00',
            'color': 'black',
            'fontWeight': 'bold'
        },
        {
            'if': {
                'filter_query': '{{07_total}} >= {} && {{07_total}} <= {}'.format(media_ano,anomalia_ano_1),
                'column_id': '07_total'
        },
            'backgroundColor': '#008000',
            'color': 'white',
            'fontWeight': 'bold'
        },
        {
            'if': {
                'filter_query': '{{08_total}} > {}'.format(anomalia_ano_2),
                'column_id': '08_total'
            },
            'backgroundColor': '#FF4136',
            'color': 'white',
            'fontWeight': 'bold'
            },
        {
            'if': {
                'filter_query': '{{08_total}} > {} && {{08_total}} <= {}'.format(anomalia_ano_1,anomalia_ano_2),
                'column_id': '08_total'
        },
            'backgroundColor': '#FFFF00',
            'color': 'black',
            'fontWeight': 'bold'
        },
        {
            'if': {
                'filter_query': '{{08_total}} >= {} && {{08_total}} <= {}'.format(media_ano,anomalia_ano_1),
                'column_id': '08_total'
        },
            'backgroundColor': '#008000',
            'color': 'white',
            'fontWeight': 'bold'
        },
        {
            'if': {
                'filter_query': '{{09_total}} > {}'.format(anomalia_ano_2),
                'column_id': '09_total'
            },
            'backgroundColor': '#FF4136',
            'color': 'white',
            'fontWeight': 'bold'
            },
        {
            'if': {
                'filter_query': '{{09_total}} > {} && {{09_total}} <= {}'.format(anomalia_ano_1,anomalia_ano_2),
                'column_id': '09_total'
        },
            'backgroundColor': '#FFFF00',
            'color': 'black',
            'fontWeight': 'bold'
        },
        {
            'if': {
                'filter_query': '{{09_total}} >= {} && {{09_total}} <= {}'.format(media_ano,anomalia_ano_1),
                'column_id': '09_total'
        },
            'backgroundColor': '#008000',
            'color': 'white',
            'fontWeight': 'bold'
        },
        {
            'if': {
                'filter_query': '{{10_total}} > {}'.format(anomalia_ano_2),
                'column_id': '10_total'
            },
            'backgroundColor': '#FF4136',
            'color': 'white',
            'fontWeight': 'bold'
            },
        {
            'if': {
                'filter_query': '{{10_total}} > {} && {{10_total}} <= {}'.format(anomalia_ano_1,anomalia_ano_2),
                'column_id': '10_total'
        },
            'backgroundColor': '#FFFF00',
            'color': 'black',
            'fontWeight': 'bold'
        },
        {
            'if': {
                'filter_query': '{{10_total}} >= {} && {{10_total}} <= {}'.format(media_ano,anomalia_ano_1),
                'column_id': '10_total'
        },
            'backgroundColor': '#008000',
            'color': 'white',
            'fontWeight': 'bold'
        },
        {
            'if': {
                'filter_query': '{{11_total}} > {}'.format(anomalia_ano_2),
                'column_id': '11_total'
            },
            'backgroundColor': '#FF4136',
            'color': 'white',
            'fontWeight': 'bold'
            },
        {
            'if': {
                'filter_query': '{{11_total}} > {} && {{11_total}} <= {}'.format(anomalia_ano_1,anomalia_ano_2),
                'column_id': '11_total'
        },
            'backgroundColor': '#FFFF00',
            'color': 'black',
            'fontWeight': 'bold'
        },
        {
            'if': {
                'filter_query': '{{11_total}} >= {} && {{11_total}} <= {}'.format(media_ano,anomalia_ano_1),
                'column_id': '11_total'
        },
            'backgroundColor': '#008000',
            'color': 'white',
            'fontWeight': 'bold'
        },
        {
            'if': {
                'filter_query': '{{12_total}} > {}'.format(anomalia_ano_2),
                'column_id': '12_total'
            },
            'backgroundColor': '#FF4136',
            'color': 'white',
            'fontWeight': 'bold'
            },
        {
            'if': {
                'filter_query': '{{12_total}} > {} && {{12_total}} <= {}'.format(anomalia_ano_1,anomalia_ano_2),
                'column_id': '12_total'
        },
            'backgroundColor': '#FFFF00',
            'color': 'black',
            'fontWeight': 'bold'
        },
        {
            'if': {
                'filter_query': '{{12_total}} >= {} && {{12_total}} <= {}'.format(media_ano,anomalia_ano_1),
                'column_id': '12_total'
        },
            'backgroundColor': '#008000',
            'color': 'white',
            'fontWeight': 'bold'
        },
    ]
    return (html.H3('Tabela com as maiores demandas da {}, detalhadas por mês, no ano {}:'.format(vara_escolhida,int(ano_escolhido)), style=TEXT_STYLE),
            dt.DataTable(data=data,
            columns=columns,
            style_table={'overflowX': 'auto'},
            style_data_conditional=style_data_conditional,
            style_header = estilo_cabecalho,
            merge_duplicate_headers=True))

@app.callback(Output('table2','children'),
            [Input('escolhe-ano','value'),
            Input('escolhe-vara','value')])
def update_datatable(ano_escolhido, vara_escolhida):

    ajustes_dados = dados_varas[dados_varas['ano_primeira_dist'] == ano_escolhido]
    ajustes_dados = ajustes_dados[ajustes_dados['Órgão Julgador'] == vara_escolhida]

    top_janeiro = ajustes_dados[ajustes_dados['mes_primeira_dist']== 1]
    top_5_janeiro = top_janeiro['Assunto'].value_counts()[:5].index.tolist()

    top_fevereiro = ajustes_dados[ajustes_dados['mes_primeira_dist']== 2]
    top_5_fevereiro = top_fevereiro['Assunto'].value_counts()[:5].index.tolist()

    top_marco = ajustes_dados[ajustes_dados['mes_primeira_dist']== 3]
    top_5_marco = top_marco['Assunto'].value_counts()[:5].index.tolist()

    top_abril = ajustes_dados[ajustes_dados['mes_primeira_dist']== 4]
    top_5_abril = top_abril['Assunto'].value_counts()[:5].index.tolist()

    top_maio = ajustes_dados[ajustes_dados['mes_primeira_dist']== 5]
    top_5_maio = top_maio['Assunto'].value_counts()[:5].index.tolist()

    top_junho = ajustes_dados[ajustes_dados['mes_primeira_dist']== 6]
    top_5_junho = top_junho['Assunto'].value_counts()[:5].index.tolist()

    top_julho = ajustes_dados[ajustes_dados['mes_primeira_dist']== 7]
    top_5_julho = top_julho['Assunto'].value_counts()[:5].index.tolist()

    top_agosto = ajustes_dados[ajustes_dados['mes_primeira_dist']== 8]
    top_5_agosto = top_agosto['Assunto'].value_counts()[:5].index.tolist()

    top_setembro = ajustes_dados[ajustes_dados['mes_primeira_dist']== 9]
    top_5_setembro = top_setembro['Assunto'].value_counts()[:5].index.tolist()

    top_outubro = ajustes_dados[ajustes_dados['mes_primeira_dist']== 10]
    top_5_outubro = top_outubro['Assunto'].value_counts()[:5].index.tolist()

    top_novembro = ajustes_dados[ajustes_dados['mes_primeira_dist']== 11]
    top_5_novembro = top_novembro['Assunto'].value_counts()[:5].index.tolist()

    top_dezembro = ajustes_dados[ajustes_dados['mes_primeira_dist']== 12]
    top_5_dezembro = top_dezembro['Assunto'].value_counts()[:5].index.tolist()

    dados_top5_assunto_por_mes = pd.DataFrame({

                     "Janeiro":top_5_janeiro,
                     "Fevereiro":top_5_fevereiro,
                     "Março":top_5_marco,
                     "Abril":top_5_abril,
                     "Maio":top_5_maio,
                     "Junho":top_5_junho,
                     "Julho":top_5_julho,
                     "Agosto":top_5_agosto,
                     "Setembro":top_5_setembro,
                     "Outubro":top_5_outubro,
                     "Novembro":top_5_novembro,
                     "Dezembro":top_5_dezembro
    })

    estilo_celula = [{
            'if': {'row_index': 'odd'},
            'backgroundColor': 'rgb(248, 248, 248)'
    }]
    estilo_cabecalho = {
        'backgroundColor': 'rgb(230, 230, 230)',
        'fontWeight': 'bold'
    }
    data = dados_top5_assunto_por_mes.to_dict('rows')
    columns =  [{"name": i, "id": i,} for i in (dados_top5_assunto_por_mes.columns)]
    return (html.H3('Tabela com as maiores demandas da {} no ano {}:'.format(vara_escolhida,ano_escolhido), style=TEXT_STYLE),
            dt.DataTable(data=data, columns=columns,style_table={'overflowX': 'auto'},style_data_conditional=estilo_celula,style_header = estilo_cabecalho))

@app.callback(Output('mapa1','figure'),
            [Input('escolhe-ano','value'),
            Input('escolhe-vara','value')])
def update_datatable(ano_escolhido, vara_escolhida):
    dados = {'Órgão Julgador':['1ª Vara Federal','2ª Vara Federal','3ª Vara Federal','4ª Vara Federal','5ª Vara Federal','6ª Vara Federal','7ª Vara Federal','14ª Vara Federal','8ª Vara Federal','10ª Vara Federal','13ª Vara Federal','9ª Vara Federal','11ª Vara Federal','12ª Vara Federal'],
             'Cidade':['Natal','Natal','Natal','Natal','Natal','Natal','Natal','Natal','Mossoró','Mossoró','Mossoró','Caicó','Assu','Pau dos Ferros'],
             'Latitude':[-5.7793,-5.7795,-5.7792,-5.7790,-5.7791,-5.7795,-5.7793,-5.7791,-5.1841,-5.1843,-5.1839,-6.4600,-5.5756,-6.1124],
             'Longitude':[-35.2009,-35.2007,-35.2008,-35.2009,-35.2011,-35.2010,-35.2010,-35.2009,-37.3478,-37.3476,-37.3480,-37.0937,-36.9150,-38.2052],
             'Congestionamento':[1.2,1.5,2.3,2.0,1.1,1.3,1.8,2.9,2.8,1.1,1.5,1.8,2.1,2.2]} #6.1124° S, 38.2052° W

    dataframe_varas = pd.DataFrame(dados)

    #, size="car_hours"

    return(px.scatter_mapbox(dataframe_varas, lat="Latitude", lon="Longitude", color="Congestionamento",size="Congestionamento",
                     color_continuous_scale="Bluered", size_max=15, zoom=7,
                     mapbox_style="carto-positron", text="Órgão Julgador"))


if __name__ == '__main__':
    app.run_server()

'''
if __name__ == '__main__':
    app.run_server(debug=True, port=8050, host='0.0.0.0')
'''
