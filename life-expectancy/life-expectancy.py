import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

# Load CSV 
df = pd.read_csv("life-expectancy/world_databank.csv")

# Dash web app
app = Dash(__name__)

fig = px.scatter(df, y="Life-Expectancy", x="GDP-PerCap", color="Continent",
                 animation_frame="Date",
                 animation_group="Country Name", 
                 size=df["Population (2020)"],
                 size_max=60, 
                 hover_name="Country Name",
                 labels={
                            "Life-Expectancy": "Life Expectancy at birth",
                            "GDP-PerCap": "GDP per capita"
                        }, )


fig.update_layout(
    height=1000, 
    margin={"r":0,"t":20,"l":0,"b":0},
    font_family = 'sans-serif', 
    font_size = 16
    )
fig.update_traces(marker=dict(line=dict(color='DarkSlateGrey')),
                  selector=dict(mode='markers'))

app.layout = html.Div([
    html.Div([
        html.Pre(children= "Life Expectancy vs GDP per capita",
        style={"text-align": "center", 'margin-bottom':0, 'font-family':'sans-serif', "font-size":"30px", "color":"black"}),
    ]),

    dcc.Graph(
        id='the_graph',
        figure = fig
    )
    
])

if __name__ == '__main__':
    app.run_server(debug=True)
