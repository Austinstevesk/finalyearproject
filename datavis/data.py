from re import DEBUG
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
import datetime
import database_connection
import mysql.connector
from mysql.connector import Error


# styling for the dash app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']




app = dash.Dash(__name__, external_stylesheets=external_stylesheets,
                meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}])
colors = {
    'background': '#111111',
    'background2': '#FF0',
    'text': '#7FDBFF'
}

# global color setting
app_color = {
    "graph_bg": "rgb(221, 236, 255)",
    "graph_line": "rgb(8, 70, 151)",
    "graph_font": "rgb(2, 29, 65)"
}

# colors for plots
chart_colors = [
    '#664DFF',
    '#893BFF',
    '#3CC5E8',
    '#2C93E8',
    '#0BEBDD',
    '#0073FF',
    '#00BDFF',
    '#A5E82C',
    '#FFBD42',
    '#FFCA30'
]

app.layout = html.Div(children=[
    # the dash application layout 
    html.Div(
        [
            dcc.Interval(
                id='query_update',
                interval=int(5000),
                n_intervals=0,

            ),
            html.Div(
                [html.H3("Hello, Welcome Data Analyst", className='graph_title')]
            ),
            dcc.Graph(
                id='example-graph',
                animate=False,
                figure=go.Figure(
                    layout=go.Layout(
                        plot_bgcolor=app_color["graph_bg"],
                        paper_bgcolor=app_color["graph_bg"],
                    )
                ),
            ),

        ],
        className='graph__container first'
    )

])


# callback for the data processing
@app.callback(
    Output('example-graph', 'figure'),
    [Input('query_update', 'n_intervals')])
def update_graph_bar(n_intervals):
    # setting time interval from which to fetch the tweets from db
    time_now = datetime.datetime.utcnow()
    time_10mins_before = datetime.timedelta(hours=0, minutes=10)
    time_interval = time_now - time_10mins_before

    # fetching tweets from db
    time_now = datetime.datetime.utcnow()

    time_1day_before = datetime.timedelta(hours=1, minutes=0)
    # print(time_10mins_before)
    day_interval = time_now - time_1day_before
    print(".......")
    print(day_interval)
    print("......")

    df = database_connection.datafr
  
    Y = df.count(leakagecase[1])

    
    return {
        'data': [
            {'x': "Nairobi", 'y': [Y], 'type': 'bar', 'name': 'Nairobi'},
            {'x': "Kenya", 'y': [Y], 'type': 'bar', 'name': 'Kenya'}
        ],
        'layout': {
            'title': 'Gas Leakage cases within Nairobi',
            # 'plot_bgcolor': colors['background'],
            # 'paper_bgcolor': colors['background']
        }
    }



if __name__ == '__main__':
    app.run_server(debug=True)