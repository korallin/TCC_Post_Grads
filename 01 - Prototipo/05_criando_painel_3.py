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

app.layout = html.Div([
             html.Div([
                 dcc.Dropdown(id='xaxis',
                              options=[{'label':i,'value':i}for i in features],
                              value='displacement')
             ],style={'width':'48%','display':'inline-block'}),
             html.Div([
                 dcc.Dropdown(id='yaxis',
                              options=[{'label':i,'value':i}for i in features],
                              value='mpg')
             ],style={'width':'48%','display':'inline-block'}),
             dcc.Graph(id='feature-graphic')

],style={'padding':10})

@app.callback(Output('feature-graphic','figure'),
             [Input('xaxis','value'),
              Input('yaxis','value')])
def update_graph(xaxis_name,yaxis_name):
    return {'data':[go.Scatter(x=df[xaxis_name],
                               y=df[yaxis_name],
                               text=df['name'],
                               mode='markers',
                               marker={'size':15,
                                       'opacity':0.5,
                                       'line':{'width':0.5,'color':'white'}})],

            'layout':go.Layout(title='Painel para o dataset MPG',
                               xaxis={'title':xaxis_name},
                               yaxis={'title':yaxis_name},
                               hovermode='closest')}

if __name__ == "__main__":
    app.run_server()
