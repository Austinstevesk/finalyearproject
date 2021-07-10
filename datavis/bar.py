from re import DEBUG
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# styling for the dash app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']



mydf = pd.read_csv("data.csv")


app = dash.Dash(external_stylesheets=external_stylesheets,
                meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}])
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Hello.. Welcome Data Analyst',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.Div(children='Gas leakage cases within Nairobi', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    dcc.Graph(
        id='Graph1',
        figure={
            'data': [
                {'x': mydf['Name'], 'y': mydf['Old Grade'], 'type': 'bar', 'name': 'Nairobi'},
                {'x': mydf['Name'], 'y': mydf['New Grade'], 'type': 'bar', 'name': 'Nairobi'},
            ],
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
    )
])

# @app.callback(
#     Output("bar-chart", "figure"), 
#     [Input("dropdown", "value")])
# def update_bar_chart():
#     #mask = df["day"] == day
#     fig = px.bar(df[mask], x="sex", y="total_bill", 
#                  color="smoker", barmode="group")
#     return fig

if __name__ == "__main__":
    app.run_server(debug=True)