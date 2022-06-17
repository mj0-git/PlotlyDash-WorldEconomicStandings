import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

# Load CSV and Format
df = pd.read_csv("happiness/world-happiness.csv")
df = df.rename(columns={"Happiness score": "Happiness", 
                   "Explained by: Social support":"Social Support",
                   "Explained by: Healthy life expectancy": "Life Expectancy", 
                   "Explained by: Freedom to make life choices":"Freedom to make Life Choices",
                   "Explained by: Generosity": "Generosity", 
                   "Explained by: Perceptions of corruption": "Perceptions of Corruption" })

# Dropdown filter list
filter_list = ['Happiness', 'Social Support', 'Life Expectancy', 'Freedom to make Life Choices', 'Generosity', 'Perceptions of Corruption']

# Dash web app
app = Dash(__name__)

# Configure UI 
app.layout = html.Div([
    html.Div([
            html.Pre(children= "World Happiness Report (2022)",
            style={"text-align": "center", 'margin-bottom':0, 'font-family':'sans-serif', "font-size":"30px", "color":"black"}),
            html.P("*Ranking of Happiness based on a three-year-average 2019-2021",
            style={"text-align": "center", 'font-family':'sans-serif', "font-size":"12px", "color":"black"})
        ]),
    html.Div([html.Pre(children= "Measure by:",
            style={"text-align": "left", 'font-family':'sans-serif', "font-size":"20px", "color":"black"}),
        dcc.Dropdown(id="level",
                       options=filter_list, 
                       value=filter_list[0])
    ], style={'margin': 25, "width": 350, "text-align": "center"}),
    dcc.Graph(
        id='the_graph'
    )
])

@app.callback(
    Output('the_graph','figure'),
    [Input('level','value')]
)

# Configure input logic
def update_graph(level):
    fig = px.choropleth(df, locations=df['Country'],
                    locationmode="country names",
                    color=level, # lifeExp is a column of gapminder
                    hover_name="Country", # column to add to hover information
                    color_continuous_scale=px.colors.sequential.Plasma)
    fig.update_geos(projection_type="natural earth")
    fig.update_layout(height=700, margin={"r":0,"t":20,"l":0,"b":0})
    return (fig)


if __name__ == '__main__':
    app.run_server(debug=True)

