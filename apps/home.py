import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from apps.navbar import navbar
import dash_extra_ui_components as deuc
from flask_login import logout_user, current_user
from pms_mgt import db, Pms as base, add_girl_pms_data, delete_girl_pms_data, update_user, get_girl_pms

from app import app

data = [('Anna', '2020-04-07', 30, 7, 15), ('Anna', '2020-04-07', 28, 5, 14)]

layout = html.Div([
    navbar,
    dbc.Container([
        html.H4("Welcome to demo page", className="text-center mt-5 mb-4", style={"color":"white"}),
        deuc.PMSComponent(id = 'pms', value = data),
        dbc.Row([
            html.Button('Get', id='get', n_clicks=0, style={'visible':True}),
            html.Button('Add', id='add', n_clicks=0),
        ]),
        
        dbc.Row([
            # educ.PMSComponent(id = 'pms')
        ], id='getOut'),
         dbc.Row([
            # educ.PMSComponent(id = 'pms')
        ], id='addOut'),
    ])
])

# @app.callback(Output('getOut', 'children'),
#             [Input('get', 'n_clicks')]
#             )
# def get(n_clicks):
#     global myGirl
#     children = []
#     result = get_girl_pms(current_user.id)
#     row = result.fetchall()
#     print(row)
#     result.close()

# @app.callback(Output('addOut', 'children'),
#             [Input('add', 'n_clicks')]
#             )
# def add(n_clicks):
#     print("asdfasdfasdfasdfasdfasdf")
#     add_girl_pms_data(current_user.id, 'Anna', '2020-04-07', 30, 7, 14,)