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
        html.Div([dcc.Graph(id='grafico_1')],style={"width": "100%", "display": "inline-block"}),
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
        html.Div(id="table2",children='tabela_atualizada')
        #html.Div(id='submit-button',children='Ver tabela')
])
        ,md=12)
])


content_fourth_row = dbc.Row([
        dbc.Col(
        html.Div([
        html.Div(id="table1",children='tabela_atualizada')
        #html.Div(id='submit-button-2', children='Ver tabela')
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


content = html.Div(
    [
        html.H2('Painel do Centro de Inteligência', style=TEXT_STYLE),
        html.Hr(),
        content_first_row,
        html.Hr(),
        content_second_row,
        html.Hr(),
        content_third_row,
        html.Hr(),
        content_fourth_row,
        html.Hr(),
        content_fifth_row

    ],
    style=CONTENT_STYLE
)

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
auth = dash_auth.BasicAuth(app,USERNAME_PASSWORD_PAIRS)
app.layout = html.Div([sidebar, content])
server = app.server


@app.callback(Output('grafico_1','figure'),
             [Input('escolhe-vara','value'),
              Input('escolhe-ano','value')])
def update_figure(vara_selecionada,ano_escolhido):

    ajustes_dados = dados_varas[dados_varas['ano_primeira_dist'] == ano_escolhido]
    ajustes_dados = ajustes_dados[ajustes_dados['Órgão Julgador'] == vara_selecionada]

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

    traces = []

    traces.append(go.Bar(
               x=['Janeiro'],
               y=top_5_janeiro,
               showlegend=False
         ))

    traces.append(go.Bar(
               x=['Fevereiro'],
               y=top_5_fevereiro,
               showlegend=False
         ))

    traces.append(go.Bar(
               x=['Março'],
               y=top_5_marco,
               showlegend=False
         ))

    return {'data':traces,
            'layout':go.Layout(title= {"text": "Distribuição de processos por mês da {} no ano {}".format(vara_selecionada,ano_escolhido)},
                               xaxis = {'title':'Mês da distribuição','categoryorder':'category ascending'},
                               yaxis = {'title':'Assunto','visible':False},
                               barmode='stack')}

@app.callback(Output('table1','children'),
             [Input('escolhe-ano','value')])
def update_datatable(ano_escolhido):

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

    estilo_celula = [{
            'if': {'row_index': 'odd'},
            'backgroundColor': 'rgb(248, 248, 248)'
    }]
    estilo_cabecalho = {
        'backgroundColor': 'rgb(230, 230, 230)',
        'fontWeight': 'bold'
    }

    data = dados_por_vara.to_dict('rows')
    columns =  [{"name": i, "id": i,} for i in (dados_por_vara.columns)]
    return (html.H3('Tabela com as maiores demandas da Justiça Federal no ano {}:'.format(ano_escolhido), style=TEXT_STYLE),
            dt.DataTable(data=data, columns=columns,style_table={'overflowX': 'auto'},style_data_conditional=estilo_celula,style_header = estilo_cabecalho))

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
