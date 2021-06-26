from re import DEBUG
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd


df = pd.read_csv("data.csv")


app = dash.Dash()
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Hello Dash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.Div(children='Dash: A web application framework for Python.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    dcc.Graph(
        id='Graph1',
        figure={
            'data': [
                {'x': df['Name'], 'y': df['Old Grade'], 'type': 'bar', 'name': 'Nairobi'},
                {'x': df['Name'], 'y': df['New Grade'], 'type': 'bar', 'name': 'Mombasa'},
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