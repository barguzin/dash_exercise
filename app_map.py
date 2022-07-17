from dash import Dash, dcc, html
import numpy as np
import pandas as pd
from dash.dependencies import Input, Output
import plotly.express as px
import geopandas as gpd

app = Dash(__name__)

np.random.seed(123)

counties = gpd.read_file('https://raw.githubusercontent.com/deldersveld/topojson/master/countries/us-states/CA-06-california-counties.json')

# generate random vector 
counties['rand_num'] = np.random.randint(1, 100, counties.shape[0])

# index data by fips 
counties.set_index(counties.STATEFP + counties.COUNTYFP, inplace=True)

# make sure the data reads correctly
#print(counties.shape)
#print(counties.columns) 
#print(counties.head())

fig = px.choropleth(counties.rand_num, geojson=counties.geometry, locations=counties.index, color='rand_num',
                           color_continuous_scale="Viridis",
                           locationmode = 'geojson-id',
                           # range_color=(0, 12),
                           # scope="usa",
                           labels={'rand_num':'My Random Rate'}
                          )

#fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
#fig.show()

# update_geos(
#     resolution=50,
#     showcoastlines=False, coastlinecolor="RebeccaPurple",
#     showland=True, landcolor="LightGreen",
#     showocean=True, oceancolor="LightBlue",
#     showlakes=True, lakecolor="Blue",
#     showrivers=True, rivercolor="Blue"
# )

fig.update_geos(fitbounds="locations", visible=False)

app.layout = html.Div([
    dcc.Graph(figure = fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)