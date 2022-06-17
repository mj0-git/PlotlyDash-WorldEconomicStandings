import pandas as pd
import numpy as np
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

# Load CSV 
df = pd.read_csv("migrants/world_population.csv")

# Dash web app
app = Dash(__name__)

# Configure UI 
app.layout = html.Div([
    html.Div([
        html.Pre(children= "Worldwide Net Migrations (2022)",
        style={"text-align": "center", 'margin-bottom':0, 'font-family':'sans-serif', "font-size":"30px", "color":"black"}),
    ]),
    html.Div([
        dcc.RadioItems(id="continent",
                       options=['All','North America', 'South America','Asia', 'Australia', 'Africa', 'Europe'], 
                       value='All')
    ], style={'margin': 25,'font-family':'sans-serif', "font-size":"20px", "width": "auto"}),
    dcc.Graph(
        id='the_graph'
    )
    
])

@app.callback(
    Output('the_graph','figure'),
    [Input('continent','value')]
)

# Configure input logic
def update_graph(continent):
    if(continent == "All"):
        dff = df
        fig = px.scatter(dff, 
                             x="Migrants (net)", y="Urban Pop %", 
                             color="Continent", hover_data=['Country/Other'], size="Population (2020)", size_max = 50,
                             labels={
                                        "Migrants (net)": "Net Migrations",
                                        "Urban Pop %": "Urban Population %"
                                    }, )
    else:  
        dff=df[df.Continent == continent]
        fig = px.scatter(dff, 
                             x="Migrants (net)", y="Urban Pop %", 
                             color="Country/Other", hover_data=['Country/Other'], size="Population (2020)", size_max = 50,
                             labels={
                                        "Migrants (net)": "Net Migrations",
                                        "Urban Pop %": "Urban Population %"
                                    }, )
    
    fig.update_layout(
        height=800, 
        margin={"r":20,"t":20,"l":20,"b":0},
        font_family = 'sans-serif', 
        font_size = 20
        )
    fig.update_traces(marker=dict(line=dict(color='DarkSlateGrey')),
                  selector=dict(mode='markers'))
    
    return (fig)


if __name__ == '__main__':
    app.run_server(debug=True)
