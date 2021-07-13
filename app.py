import os

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import time

import mysql.connector as mysql

# enter your server IP address/domain name
while True:
    time.sleep(5)

    # enter your server IP address/domain name
    HOST = "sql5.freemysqlhosting.net"  # or "domain.com"
    # database name, if you want just to connect to MySQL server, leave it empty
    DATABASE = "sql5424622"
    # this is the user you create
    USER = "sql5424622"
    # user password
    PASSWORD = "wMwKZ98X7u"
    # connect to MySQL server
    db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
    print("Connected to:", db_connection.get_server_info())

    # while True:
    # sleep(60 - time() % 60)

    cursor = db_connection.cursor()
    # get database information
    cursor.execute("select database();")
    database_name = cursor.fetchone()
    print("[+] You are connected to the database:", database_name)
    # fetch the database
    df = cursor.execute("select * from tblfood")
    # get all selected rows
    rows = cursor.fetchall()
    columns = ["ID", "CategoryName", "ItemName", "ItemPrice", "ItemDes", "Image", "ItemQty"]
    df = pd.DataFrame(rows, columns=columns)

    print("all imported data")
    print("looping again")

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Mangoes", "Oranges", "Bananas", "Mangoes", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)



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
        id='example-graph-2',
        figure=fig
    )
])

@app.callback(dash.dependencies.Output('display-value', 'children'),
              [dash.dependencies.Input('dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)

if __name__ == '__main__':
    app.run_server(debug=True)