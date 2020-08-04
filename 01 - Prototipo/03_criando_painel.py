import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash()

dados_varas = pd.read_csv('../dados-pje-MPF.csv',dtype='unicode')

'''
Index(['Unnamed: 0', '%ID_PROCESSO_TRF', 'Sistema', 'Número Processo',
       'Status do Processo', 'Data Última Distribuição', 'Assunto Código',
       'Assunto', 'Data Primeira Distribuição', 'Classe Judicial',
       'Órgão Julgador', 'Parte Polo Ativo?', 'Parte Polo Passivo?',
       'Parte Outros Participantes?', 'Parte Documento', 'Parte Descrição',
       '%ID_PESSOA_REU', 'Data Trânsito Julgado', 'Número Tempo em Anos'],
'''

opcoes_vara = []
for vara in dados_varas['Órgão Julgador'].unique():
    opcoes_vara.append({'label':str(vara),'value':vara})

app.layout = html.Div([
             dcc.Graph(id='grafico'),
             dcc.Dropdown(id='escolhe-vara',options=opcoes_vara)
             ])


@app.callback(Output('grafico','figure'),
             [Input('escolhe-vara','value')])
def update_figure(vara_selecionada):
    #dados apenas para seleção do menu dorpdown
    vara_escolhida = dados_varas[dados_varas['Órgão Julgador']==vara_selecionada]
    traces = []

    for assunto_processo in vara_escolhida['Assunto'].unique():
        vara_filtrada = vara_escolhida[vara_escolhida['Assunto']==assunto_processo]
        traces.append(go.Bar(
               x=vara_filtrada['Data Primeira Distribuição'],
               y=vara_filtrada['Assunto'],
         ))

    return {'data':traces,
            'layout':go.Layout(title='Assunto dos processos por Vara',
                               xaxis = {'title':'Data da distrubuição'},
                               yaxis = {'title':'Assunto'})}


if __name__ == '__main__':
    app.run_server()
