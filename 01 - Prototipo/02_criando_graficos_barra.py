import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

varas = pd.read_csv('../dados-pje-MPF.csv',dtype='unicode')

#vara_6 = df.loc[df['Órgão Julgador']=="6ª Vara Federal", "Assunto"]

data = [go.Bar(x=varas['Órgão Julgador'],
               y=varas['Assunto']
        )]

layout = go.Layout(title='Litigiosidade por Varas no RN', barmode='stack')
fig = go.Figure(data=data,layout=layout)

pyo.plot(fig,filename='02_grafico_barra.html')
