
import pandas as pd
import plotly.express as px
import plotly

dados = {'Varas':['1a','2a','3a','4a','5a','6a','7a','14a'],'Cidade':['Natal','Natal','Natal','Natal','Natal','Natal','Natal','Natal'],
         'Latitude':[-5.7793,-5.7795,-5.7792,-5.7790,-5.7791,-5.7795,-5.7793,-5.7791],'Longitude':[-35.2009,-35.2007,-35.2008,-35.2009,-35.2011,-35.2010,-35.2010,-35.2009],
         'Congestionamento':[1.2,1.5,2.3,2.0,1.1,1.3,1.8,2.9]}

dataframe_varas = pd.DataFrame(dados)


#, size="car_hours"
fig = px.scatter_mapbox(dataframe_varas, lat="Latitude", lon="Longitude", color="Congestionamento",size="Congestionamento",
                 color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=14,
                 mapbox_style="carto-positron")

fig.show()


#6.4600° S, 37.0937° W
#px.colors.sequential.Plasma
#color_continuous_scale=px.colors.cyclical.IceFire
#px.colors.sequential.swatches()
#color_continuous_scale=["red", "green", "blue"]
#color_continuous_scale=[(0, "red"), (0.5, "green"), (1, "blue")]
