#import sys
#print(sys.executable)
#used to import libraries that

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Output, Input
import dash_table
#import mysql.connector as mysql
import time
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px
#from datetime import datetime, date as date
from datetime import datetime as dt
import dash_auth





# needed only if running this as a single page app
external_stylesheets = [dbc.themes.BOOTSTRAP]
main = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = main.server

auth = dash_auth.BasicAuth(
    main,
    {'chima': 'business-intelligence',
     'tom': 'mantom'}
)


while True:
    time.sleep(30)
    #HOST = "63.250.45.202"  # or "domain.com"
# database name, if you want just to connect to MySQL server, leave it empty
    #DATABASE = "getfit"
# this is the user you create
    #USER = "_rchim"
# user password
    #PASSWORD = "_FadeBle$$$007"
# connect to MySQL server
    #db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
    #print("Connected to:", db_connection.get_server_info())

# while True:
# sleep(60 - time() % 60)


    #cursor = db_connection.cursor()
# get database information
    #cursor.execute("select database();")
    #database_name = cursor.fetchone()
    #print("[+] You are connected to the database:", database_name)
# fetch the database
    #df = cursor.execute("select * from customers")
# get all selected rows
    #rows = cursor.fetchall()
    #df = pd.read_sql("select * from customers", db_connection)

    df = pd.read_csv('data/customers.csv')
    df100 = df[['id', 'name', 'phone', 'email', 'state', 'country', 'created_at', 'updated_at']]

    df6 = df[df.country == 'nigeria']
    #df9 = df[(df['country'] != 'Nigeria')]
    df9 = df[~df['country'].isin(['Nigeria'])]
    #df10 = df9['country']

    #df10.count()

    print("done importing customers")


    df1 = pd.read_csv('data/orders.csv')
    #df1 = cursor.execute("select * from orders")
    #df1 = pd.read_sql("select * from orders", db_connection)

    #limo = df1[df1['note']].isin(['Limo dennis', 'Limo dennis(influencer)'])
    #nysc = df1[df1['note']].isin(['NYSC sales'])

    #limo = df1[df1['note']].isin(['Limo dennis', 'Limo dennis(influencer)'])
    #nysc = df1[df1['note']].isin(['NYSC sales', 'NYSC SALES', 'NYSC Sales', 'nysc sales'])




    df1['created_at'] = pd.to_datetime(df1['created_at']).dt.date
    df1['updated_at'] = pd.to_datetime(df1['updated_at']).dt.date

    df1['updated_at'] = pd.to_datetime(df1['updated_at']).dt.strftime('%Y-%m-%d')
    df1['created_at'] = pd.to_datetime(df1['created_at']).dt.strftime('%Y-%m-%d')


    #print(df1)
    df7 = pd.read_csv('data/orderproducts.csv')
    print("finished importing orders")

    #df7 = cursor.execute("select * from orderproducts")
    #df7 = pd.read_sql("select * from order_products", db_connection)
    df14 = pd.read_csv('data/employees.csv')

    #df14 = cursor.execute("select * from employees")
    #df14 = pd.read_sql("select * from employees", db_connection)
    df20 = pd.read_csv('data/products.csv')

    #df20 = cursor.execute("select * from products")
    #df20 = pd.read_sql("select * from products", db_connection)
    #df2 = df6.groupby('country').size().reset_index(name='counts')
    #df5 = df[(df.country =="nigeria")]

    print("done")

    df8 = df7[['id', 'product_id', 'order_id', 'status', 'created_at']]

    #print("csv imported")

    #df400 = pd.read_sql("select * from customer_reviews", db_connection)
    df400 = pd.read_csv('data/customer_reviews.csv')

    df407 = pd.merge(df400, df14, left_on="customer_id", right_on="id")




    #df402 = df401[['id', 'name', 'phone', 'email', 'state', 'country', 'created_at_', 'updated_at']]





    df0 = df[df['country'].isin(['Nigeria', 'Ghana'])]
    df10 = df[df['country'].isin(['Nigeria'])]
    df2 = df10.groupby('state').size().reset_index(name='counts')
    df11 = df9[df9['country'].isin(['Ghana', 'USA', 'United Kingdom', 'United States', 'Russia', 'Sweden', 'Turkey', 'Germany',
    'France', 'Algeria', 'Belgium', 'Qatar', 'Benin', 'China', 'Italy', 'Spain', 'Ireland', 'Liberia', 'Switzerland',
    'Zambia', 'Canada', 'Botswana', 'New Zealand', 'Australia', 'Cameroon', 'Bulgaria', 'South Africa', 'Bahrain', 'Scotland',
    'Netherlands', 'Botswana'])]
    df12 = df11.groupby('country').size().reset_index(name='counts')

    #matching total getfit product sales
    df15 = df7[df7['status'].isin([1])]

    print(df15)
    for col in df15.columns:
        print(col)


    print(df20)
    for col in df20.columns:
        print(col)

    df21 = pd.merge(df15, df20, left_on="product_id", right_on="product_id")

    df401 = pd.merge(df400, df14, left_on="staff_id", right_on="id")
    # for col in df401.columns:
    # print(col)

    df405 = pd.merge(df15, df1, left_on="order_id", right_on="id")
    # for col in df405.columns:
    # print(col)

    df406 = pd.merge(df405, df, left_on="customer_id", right_on="id")
    for col in df406.columns:
        print(col)


    for col in df20.columns:
        print(col)

    df407 = pd.merge(df406, df20, left_on="product_id", right_on="product_id")
    for col in df407.columns:
        print(col)

    print(407)

    df408 = df407[["product_id", "updated_at_x", "delivery_address", "state", "name_x", "note", "name_y", "phone"]]

    #print(df21)

    df22 = df21.groupby('name').size().reset_index(name='products sold')
    #print(df22)
    #df22.count()

    #df410 = df21.groupby('name', 'amount')
    #for col in df410.columns:
        #print(col)


    #number of sales as per getfit employee
    #print(df14.shape)
    df200 = df14[~df14['name'].isin(['PROMO', 'Real Oviawe'])]
    df16 = pd.merge(df1, df14, left_on="employee_id", right_on="id")

    df300 = pd.merge(df1, df200, left_on="employee_id", right_on="id")




    #dfc = df300[["created_at_x", "name"]]

    #dfc2 = pd.pivot_table(dfc, index=['created_at_x'], columns='name')

    #print(dfc)
    #print(df200.shape)


    df17 = df16.groupby('name').size().reset_index(name='number of sales')

    dfc3 = df300.copy()
    dfc3['created_at_x'] = pd.to_datetime(dfc3['created_at_x'])
    dfc3.set_index('created_at_x', inplace=True)
    print(dfc3)






    #print(df16)
    #for col in df16.columns:
        #print(col)

    #print(df25)

    #break;

    df3 = df.groupby(["state"]).size().reset_index(name='counts')

    #df1['created_at_y'] = pd.to_datetime(df21['created_at_y']).dt.date
    #df21['updated_at_y'] = pd.to_datetime(df21['updated_at_y']).dt.date

    #df['date'] = pd.to_datetime(df['date']).dt.date

    available_employee = df14['name']
    available_dates = df7['created_at']


    #print(available_employee)





    fig = px.bar(
        df2,  # dataframe
        x="state",  # x
        y="counts",  # y
        labels={"x": "state", "y": "counts"},  # define label
        color="counts",
        #color=df2.groupby("country")["counts"].agg(sum),
        #color_continuous_scale=px.colors.sequential.RdBu,  # color
        text="counts",
        #color_continuous_scale=px.colors.sequential.RdBu,
        #text=df2.groupby("country")["counts"].agg(sum),  # text
        title="Nigerian Customers Count",  # title
        orientation="v",# horizonal bar chart
        height=600

    )

    fig3 = px.bar(
        df12,  # dataframe
        x="country",  # x
        y="counts",  # y
        labels={"x": "country", "y": "counts"},  # define label
        color="counts",
        # color=df2.groupby("country")["counts"].agg(sum),
        # color_continuous_scale=px.colors.sequential.RdBu,  # color
        text="counts",

        # text=df2.groupby("country")["counts"].agg(sum),  # text
        title="International Customers Count",  # title
        orientation="v",  # horizonal bar chart
        height=350

    )

    fig4 = px.bar(
        df17,  # dataframe
        x="number of sales",  # x
        y="name",  # y
        labels={"x": "number of sales", "y": "name"},  # define label
        color="number of sales",
        # color=df2.groupby("country")["counts"].agg(sum),
        # color_continuous_scale=px.colors.sequential.RdBu,  # color
        text="number of sales",

        # text=df2.groupby("country")["counts"].agg(sum),  # text
        title="Total Historical Orders By Customer Rep",  # title
        orientation="h",  # horizonal bar chart
        height=550

    )

    fig5 = px.bar(
        df22,  # dataframe
        x="products sold",  # x
        y="name",  # y
        labels={"x": "products sold", "y": "name"},  # define label
        color="products sold",
        # color=df2.groupby("country")["counts"].agg(sum),
        color_continuous_scale=px.colors.sequential.RdBu,  # color
        text="products sold",

        # text=df2.groupby("country")["counts"].agg(sum),  # text
        title="Total Historical Getfit Products Sold",  # title
        orientation="h",  # horizonal bar chart
        height=650

    )

    fig2 = dbc.Col(html.Div(children=[dash_table.DataTable(
        id='table1',
        columns=[{"id": i, "order_id": i} for i in df8.columns],

        data=df.to_dict('records'),
        # data=df1.to_dict('records'),
        page_size=5,
        filter_action='native',
        export_format='xlsx',
        export_headers='display',
        merge_duplicate_headers=True,
        # style_table={'margin:2px'},
        # style_header={'backgroundColor': 'rgb(30, 30, 30)'},
        style_cell={
            # 'backgroundColor': 'rgb(50, 50, 50)',
            'color': 'black'

        },

    ),
    ],
    ),
    ),



    #columns = ["id", "name", "phone", "email", "instagram", "state", "country", "customer_ser_id", "created_at",
           #"updated_at"]
    #df1 = pd.DataFrame(columns=columns)

    #state = df1['state']
    #state

    df.rename(columns={'id': 'id',
                       'name': 'name',
                       'phone': 'phone',
                       'email': 'email',
                       'instagram': 'instagram',
                       'state': 'state',
                       'country': 'country',
                       'ser_id': 'ser_id',
                       'created_at': 'created_at',
                       'updated_at': 'updated_at'
                       },
              inplace=True)

    #print("all imported data")
    #print("looping again")

    #app = dash.Dash(__name__)




    main.layout = html.Div([






        #dbc.Container([
            dbc.Row([
            dbc.Col(html.H4('Getfit Analytics Dashboard', className="header-title", style={'text-align': 'center', 'color': 'blue'}))]),

        dbc.Row([
            dbc.Col(html.H4('', className="header-title",
                            style={'text-align': 'center', 'color': 'blue'}))]),
        dbc.Row([
            dbc.Col(html.H4('', className="header-title", style={'text-align': 'center', 'color': 'blue'}))]),

            dbc.Row([
                dbc.Col(dbc.Card(html.H6(children='Customers Latest Update',
                                         className="text-center text-light sm-dark"), body=True, color="dark")
                        , className="mb-2"
                )
            ]),



                dash_table.DataTable(
                id='table',
                columns=[{"id": i, "name": i} for i in df100.columns],
                data=df100.to_dict('records'),
                # data=df1.to_dict('records'),
                page_size=5,
                filter_action='native',
                export_format='xlsx',
                export_headers='display',
                merge_duplicate_headers=True,
                #style_table={'margin:2px'},
                    #style_header={'backgroundColor': 'rgb(30, 30, 30)'},
                    style_cell={
                        #'backgroundColor': 'rgb(50, 50, 50)',
                        'color': 'black',
                        'left-padding': '10%'


                    },

                ),

        dcc.Markdown(id='test_cell'),

        dbc.Row([
            dbc.Col(html.H4('Customers Orders', className="header-title",
                            style={'text-align': 'left', 'color': 'red'}))]),

        dash_table.DataTable(
            id='table2',
            columns=[{"id": i, "name": i} for i in df408.columns],
            data=df408.to_dict('records'),
            # data=df1.to_dict('records'),
            page_size=5,
            filter_action='native',
            export_format='xlsx',
            export_headers='display',
            merge_duplicate_headers=True,
            # style_table={'margin:2px'},
            # style_header={'backgroundColor': 'rgb(30, 30, 30)'},
            style_cell={
                # 'backgroundColor': 'rgb(50, 50, 50)',
                'color': 'black',
                'left-padding': '10%'

            },

        ),







        dcc.Markdown(id='test_cell1'),

        dbc.Row([
            dbc.Col(html.H4('Customer Reviews', className="header-title",
                            style={'text-align': 'left', 'color': 'red'}))]),

        dash_table.DataTable(
            id='table3',
            columns=[{"id": i, "name": i} for i in df400.columns],
            data=df400.to_dict('records'),
            # data=df1.to_dict('records'),
            page_size=5,
            filter_action='native',
            export_format='xlsx',
            export_headers='display',
            merge_duplicate_headers=True,
            # style_table={'margin:2px'},
            # style_header={'backgroundColor': 'rgb(30, 30, 30)'},
            style_cell={
                # 'backgroundColor': 'rgb(50, 50, 50)',
                'color': 'black',
                'left-padding': '10%'

            },

        ),

        dcc.Markdown(id='test_cell3'),

            dbc.Row([
                dbc.Col(html.H5(children='--------------------------------------------------', className="text-center"),
                        className="mt-4"),


            ]),

            dbc.Row([
                dbc.Col(
                    dcc.Graph(figure=fig)),
            ], style={"height": "120%", "width": "100%"}),

            dbc.Row([
                dbc.Col(
                    dcc.Graph(figure=fig3)),
            ], style={"height": "120%", "width": "100%"}),

            dbc.Row([
                dbc.Col(
                    dcc.Graph(figure=fig4)),
                dbc.Col(
                    dcc.Graph(figure=fig5)),
            ], style={"height": "220%", "width": "100%"}),



            #dcc.Dropdown(
               # id='choose_hospital_situation',
                #options=[
                   # {'label': 'Amaka', 'value': 'Amaka Obi'},
                    #{'label': 'General wards', 'value': 'General wards'},
                   # {'label': 'Isolation', 'value': 'In Isolation'},
                   # {'label': 'Total completed isolation', 'value': 'Total completed isolation'},
                   # {'label': 'Total discharged from hospital', 'value': 'Total discharged from hospital'},
              #  ],
               # value=['Amaka Obi', 'General wards'],
              #  multi=True,
            #    style={'width': '70%', 'margin-left': '5px'}
           # ),

        #]),
        #dbc.Row([
            #dcc.Graph(id='situation_graph_by_period')]),

            #dbc.Row([
               # dbc.Col(html.H5(children='Situation in local hospitals', className="text-center"),
                        #className="mt-4")
           # ]),







            dbc.Row([
                #dbc.Col(html.H5(children='Daily COVID-19 cases in Singapore', className="text-center"),
                       # className="mt-4"),




            #dbc.Row([
                #dbc.Col(
                   # dcc.Graph(id='local and imported'), width=6),



                #dcc.Markdown(id='test_cell1'),

                #dbc.Col(
                #dcc.Graph(figure=fig)),
            #], style={"height": "120%", "width": "100%"}),







            dbc.Row([
                #dbc.Col(html.H5(children="Breakdown of sales:(LOCATION)")),






             #dbc.Col(html.H5(children='Breakdown of cases: whether residing in dorms', className="text-center")),
            ]),


               #graphical


                #graphical



           # dbc.Row(
               # [
                        #dbc.Col(html.Div(children="One of three columns")),
                        #   dash_table.DataTable(
                        # id='table2',
                        #columns=[{"name": i, "id": i} for i in df8.columns],

                        # data=df8.to_dict('records'),
                        # data=df1.to_dict('records'),
                        # page_size=5,
                        # filter_action='native',
                        # export_format='xlsx',
                        #  export_headers='display',
                        # merge_duplicate_headers=True,
                        # style_table={'margin:2px'},
                        # style_header={'backgroundColor': 'rgb(30, 30, 30)'},
                        # style_cell={
                        # 'backgroundColor': 'rgb(50, 50, 50)',
                        #   'color': 'black',
                        # 'left-padding': '10%'

                        #},

                        # ),

                    #dcc.Markdown(id='test_cell1'),



                    #dbc.Col(html.Div(children="One of three columns")),
                    #dbc.Col(html.Div(children="One of three columns")),
               # ]
            #),
            #dcc.Markdown(id='test_cell1'),




        ]),


        dbc.Row([
            dbc.Col(dbc.Card(html.H3(children='Daily Getfit Conversions ( line graph per employee)',
                                     className="text-center text-light bg-dark"), body=True, color="dark")
                    , className="mb-4")
        ]),

        dbc.Row([


        dcc.Dropdown(
            id='emp_name',
            options=[{'label': i, 'value': i} for i in available_employee],
            value=['Rita'],
            multi=True,
            style={'width': '70%', 'margin-left': '5px'}
            ),

        #dcc.Dropdown(
               # id='date_name',
               # options=[{'label': i, 'value': i} for i in available_dates],
               # value=['2020-10-01 09:55:37'],
                #multi=True,
                #style={'width': '70%', 'margin-left': '5px'}
           # ),

            #dcc.DatePickerRange(
                #id='date_range',
                #day_size=50,
                #reopen_calendar_on_clear=True,
               # clearable=True,
               # min_date_allowed=date(2021, 1, 1),
               # max_date_allowed=date(2021, 12, 31),
                # initial_visible_month = date(2020, 7, 1),
               # start_date=date(2021, 6, 1),
                #end_date=date(2021, 6, 30),
                #minimum_nights=0,
                #updatemode='singledate'
            #),




        ]),

        #dcc.DatePickerRange(
            #id='my-date-picker-range',
            #min_date_allowed=date(1995, 8, 5),
            #max_date_allowed=date(2017, 9, 19),
            #initial_visible_month=date(2017, 8, 5),
            #end_date=date(2017, 8, 25)
        #),
        #html.Div(id='output-container-date-picker-range'),

        dbc.Row([
            dbc.Col(html.H5(children='Daily Conversions figures', className="text-center"),
                    className="mt-4"),
        ]),

        dcc.Graph(id='cases_or_deaths_country'),

        dbc.Row([
            dbc.Col(html.H5(children='Cumulative Conversions figures', className="text-center"),
                    className="mt-4"),
        ]),

        dcc.Graph(id='total_cases_or_deaths_country'),

        dbc.Row([
            dbc.Col(html.H5(children='Daily date Conversions figures', className="text-center"),
                    className="mt-4"),
        ]),

        dcc.DatePickerRange(
            id='my-date-picker-range',  # ID to be used for callback
            calendar_orientation='horizontal',  # vertical or horizontal
            day_size=39,  # size of calendar image. Default is 39
            end_date_placeholder_text="Return",  # text that appears when no end date chosen
            with_portal=False,  # if True calendar will open in a full screen overlay portal
            reopen_calendar_on_clear=True,
            is_RTL=False,  # True or False for direction of calendar
            clearable=True,  # whether or not the user can clear the dropdown
            number_of_months_shown=1,  # number of months shown when calendar is open
            min_date_allowed=dt(2020, 10, 1),  # minimum date allowed on the DatePickerRange component
            max_date_allowed=dt(2022, 6, 20),  # maximum date allowed on the DatePickerRange component
            initial_visible_month=dt(2021, 1, 1),  # the month initially presented when the user opens the calendar
            start_date=dt(2020, 10, 1).date(),
            end_date=dt(2022, 5, 15).date(),
            display_format='MMM Do, YY',  # how selected dates are displayed in the DatePickerRange component.
            month_format='MMMM, YYYY',  # how calendar headers are displayed when the calendar is opened.
            minimum_nights=2,  # minimum number of days between start and end date

            persistence=True,
            persisted_props=['start_date'],
            persistence_type='session',  # session, local, or memory. Default is 'local'

            updatemode='singledate'  # singledate or bothdates. Determines when callback is triggered
        ),

        dcc.Graph(id='date'),

        dbc.Row([
            dbc.Col(dbc.Card(html.H3(children='Offline Sales',
                                     className="text-center text-light bg-dark"), body=True, color="dark")
                    , className="mb-4"),
        ]),

        dbc.Row([
            dbc.Col(html.H5(children='NYSC', className="text-center"),
                    className="mt-4"),

            dbc.Col(html.H5(children='Limo Dennis', className="text-center"),
                    className="mt-4"),



        ]),

        dbc.Row([
            dbc.Col(html.H5(children='Wuse', className="text-center"),
                    className="mt-4"),

            dbc.Col(html.H5(children='Garki', className="text-center"),
                    className="mt-4"),

        ]),





    ])



    @main.callback(
        Output('test_cell', 'children'),
        Input('table', 'active_cell'))
    def return_cell_info(active_cell):
        return str(active_cell)


    @main.callback(
        Output('test_cell1', 'children'),
        Input('table2', 'active_cell'))
    def return_cell_info(active_cell):
        return str(active_cell)

    @main.callback(
        Output('test_cell3', 'children'),
        Input('table3', 'active_cell'))
    def return_cell_info(active_cell):
        return str(active_cell)

    #@app.callback(
       # Output('test_cell1', 'children'),
       #  Input('table2', 'active_cell'))
       # def return_cell_info(active_cell):
       #  return str(active_cell)



    #def update_graph(cases_or_deaths_country, total_cases_or_deaths_country):

        #dfc = df16.copy()
        #dfc = dfc[dfc.name.isin(['Rita', 'Amaka Obi'])]

        #dfc = pd.pivot_table(dfc, values=employee, index=['updated_at_x'], columns='name')

       # dfc2 = df16.copy()
        #dfc2 = dfc2[dfc2.name.isin(['Rita', 'Amaka Obi'])]

        #dfc2 = dfc2.groupby(['name', 'created_at_y']).sum()
        #dfc2 = dfc2.reset_index()
        #dfc2['crea'] = dfc2.groupby(['name'])['cases per 1 mil'].apply(
           # lambda x: x.cumsum())
        #dfc2['deaths per 1 mil'] = dfc2.groupby(['name'])['deaths per 1 mil'].apply(
           # lambda x: x.cumsum())

        #dfc2 = pd.pivot_table(dfc2, values=employee, index=['order_id'], columns='name')

    @main.callback(
        [dash.dependencies.Output('cases_or_deaths_country', 'figure'),
         dash.dependencies.Output('total_cases_or_deaths_country', 'figure'),
         #Output('cases_or_deaths_country', 'figure')
         ],
        [dash.dependencies.Input('emp_name', 'value'),
         #dash.dependencies.Input('my-date-picker-range', 'start_date'),
         #dash.dependencies.Input('my-date-picker-range', 'end_date')
         #dash.dependencies.Input('my-date-picker-range', 'start_date'),
         #dash.dependencies.Input('my-date-picker-range', 'end_date')
         #dash.dependencies.Input('date_name', 'value')
         ])


    def update_graph(emp_name1):

        #f_df = df300[df300['name'] == name]

        #dfc = df16[df16['name'].isin(['emp_name'])]
        #dfc = df16[(df16['name'].isin(['emp_name']))]

        #filtered_data1 = df16[df16["name"] == name]
        #filtered_data2 = df[df25["name"] == name]

        #dfc = pd.pivot_table(df300, values=emp_name1, index=['created_at_x'], columns='name')

        #print(dfc)

        dfc1 = df300.copy()
        #dfc1 = dfc1[(dfc1['name'] == emp_name1)]
        dfc1 = dfc1[dfc1.name.isin(emp_name1)]
        dfc1 = dfc1.groupby(['created_at_x', 'name']).size().unstack(fill_value=0)

        dfc2 = df300.copy()
        #dfc2 = dfc2[(dfc2['name'] == emp_name1) & (dfc2['created_at_x'].between(start_date, end_date))]
        dfc2 = dfc2[dfc2.name.isin(emp_name1)]
        dfc2 = dfc2.groupby(['created_at_x', 'name']).size().unstack(fill_value=0).apply(lambda x: x.cumsum())

        #dfc3 = df300.copy()
        #dfc3 = df300.loc[start_date:end_date]





        fig5 = go.Figure()
        for col in dfc1.columns:
            fig5.add_trace(go.Scatter(x=dfc1.index, y=dfc1[col].values, name=col, mode='markers+lines'))

        fig5.update_layout(yaxis_title='Sale Per Customer Rep',
                           paper_bgcolor='rgba(0,0,0,0)',
                           plot_bgcolor='rgba(0,0,0,0)',
                           template="seaborn",
                           #color="df27[col].values",
                           #style={"height": "50%", "width": "40%"},
                           margin=dict(t=0),
                           width=1400,
                           height=300
                           )


        fig6 = go.Figure()
        for col in dfc2.columns:
            fig6.add_trace(go.Scatter(x=dfc2.index, y=dfc2[col].values,
                                      name=col,
                                      mode='markers+lines'))

            fig6.update_layout(yaxis_title='Cumulative sale per Customer Rep',
                               paper_bgcolor='rgba(0,0,0,0)',
                               plot_bgcolor='rgba(0,0,0,0)',
                               template="seaborn",
                               #color="df27[col].values",
                               margin=dict(t=0),
                               width=1400,
                               height=300
                               )

        return fig5, fig6


    @main.callback(
        [dash.dependencies.Output('date', 'figure'),
         #dash.dependencies.Output('total_cases_or_deaths_country', 'figure'),
         #Output('cases_or_deaths_country', 'figure')
         ],
        [#dash.dependencies.Input('date_dt', 'value'),
         dash.dependencies.Input('my-date-picker-range', 'start_date'),
         dash.dependencies.Input('my-date-picker-range', 'end_date')
         #dash.dependencies.Input('my-date-picker-range', 'start_date'),
         #dash.dependencies.Input('my-date-picker-range', 'end_date')
         #dash.dependencies.Input('date_name', 'value')
         ])




    def update_graph(start_date, end_date):


        #dfc3['created_at_x'] = pd.to_datetime(dfc3['created_at_x'])
        #dfc3.set_index('created_at_x', inplace=True)

        #dfc3 = dfc3.loc[start_date:end_date]

        dff = dfc3.loc[start_date:end_date]
        dff = dff.groupby(["name"]).size().reset_index(name='counts')

        fig7 = px.bar(
            dff,  # dataframe
            x="counts",  # x
            y="name",  # y
            labels={"x": "state", "y": "counts"},  # define label
            color="counts",
            # color=df2.groupby("country")["counts"].agg(sum),
            # color_continuous_scale=px.colors.sequential.RdBu,  # color
            text="counts",
            # color_continuous_scale=px.colors.sequential.RdBu,
            # text=df2.groupby("country")["counts"].agg(sum),  # text
            title="Nigerian Customers Count",  # title
            orientation="v",  # horizonal bar chart
            height=600

        )

        return fig7


    #@main.callback(
        #Output('cases_or_deaths_country', 'figure'),
        #[Input('my-date-picker-range', 'start_date'),
         #Input('my-date-picker-range', 'end_date')]
    #)
    #def update_output(start_date, end_date):
        # print("Start date: " + start_date)
        # print("End date: " + end_date)
        #dff = df.loc[start_date:end_date]
        # print(dff[:5])


    if __name__ == '__main__':
        main.run_server(debug=True)