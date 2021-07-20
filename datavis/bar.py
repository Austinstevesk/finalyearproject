from re import DEBUG
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import datetime
import mysql.connector as connection
from mysql.connector import Error
import plotly.graph_objs as go

# styling for the dash app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


class DbConnect():
    def __init__(self) -> None:
        pass
    def connect():
        try:
            conn = connection.connect(host='204.11.59.250',
                                                database='austinst_gasmonitor',
                                                user='austinst_root',
                                                password='0797277217Sk')
            if conn.is_connected():
                db_Info = conn.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                cursor = conn.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                print("You're connected to database: ", record)

        except Error as e:
            print("Error while connecting to MySQL", e)
        return conn


    
# query = "SELECT residence, gasValue, leakagecase FROM gaslevel where leakagecase=1";
# df = pd.read_sql(query, conn)
# print(df)

# mydf = pd.read_csv("data.csv")

# #newdf = df.groupby('residence').residence.value_counts()

# value_counts = df['residence'].value_counts()

# # converting to df and assigning new names to the columns
# df_value_counts = pd.DataFrame(value_counts)
# df_value_counts = df_value_counts.reset_index()
# df_value_counts.columns = ['residence', 'counts'] # change column names
# print(df_value_counts)  


app = dash.Dash(external_stylesheets=external_stylesheets,
                meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}])
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
# app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
#     html.H1(
#         children='Hello.. Welcome Data Analyst',
#         style={
#             'textAlign': 'center',
#             'color': colors['text']
#         }
#     ),
#     html.Div(children='Gas leakage cases within Nairobi', style={
#         'textAlign': 'center',
#         'color': colors['text']
#     }
#             [
#             dcc.Interval(
#                 id='query_update',
#                 interval=int(5000),
#                 n_intervals=0,

#             ),
#             ],
#             ),
#     dcc.Graph(
#         id='Graph1',
#         figure={
#             'data': [
#                 {'x': df_value_counts['residence'], 'y': df_value_counts['counts'], 'type': 'bar', 'name': 'Nairobi'},
#                 #{'x': mydf['Name'], 'y': mydf['New Grade'], 'type': 'bar', 'name': 'Nairobi'},
#             ],
#             'layout': {
#                 'plot_bgcolor': colors['background'],
#                 'paper_bgcolor': colors['background'],
#                 'font': {
#                     'color': colors['text']
#                 }
#             }
#         }
#     )
# ])
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

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
        html.H1(
        children='Hello.. Welcome Data Analyst',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    # the dash application layout 
    html.Div(
        [
            dcc.Interval(
                id='query_update',
                interval=1*10000,
                n_intervals=0,

            ),
            html.Div(children='Gas Leakage Cases within Nairobi',
                    style={
                    'textAlign': 'center',
                    'color': chart_colors[3]
        }
                
            ),
            dcc.Graph(
                id='bar-chart',
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




@app.callback(
    Output("bar-chart", "figure"), 
    [Input('query_update', 'n_intervals')])     
 

def update_bar_chart(n_intervals):
    conn = DbConnect.connect()
    query = "SELECT residence, gasValue, leakagecase FROM gaslevel where leakagecase=1";
    df = pd.read_sql(query, conn)
    print(df)

    #newdf = df.groupby('residence').residence.value_counts()

    value_counts = df['residence'].value_counts()

    # converting to df and assigning new names to the columns
    df_value_counts = pd.DataFrame(value_counts)
    df_value_counts = df_value_counts.reset_index()
    df_value_counts.columns = ['residence', 'counts'] # change column names
    print(df_value_counts) 
    return {
            'data': [
                {'x': df_value_counts['residence'], 'y': df_value_counts['counts'], 'type': 'bar', 'name': 'Nairobi'},
                #{'x': mydf['Name'], 'y': mydf['New Grade'], 'type': 'bar', 'name': 'Nairobi'},
            ],
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }


if __name__ == "__main__":
    app.run_server(debug=True)