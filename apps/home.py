import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from apps.navbar import navbar
import dash_extra_ui_components as deuc
from flask_login import logout_user, current_user
from pms_mgt import db, Pms as base, add_girl_pms_data, delete_girl_pms_data, update_girl_pms_data, get_girl_pms
import json
from app import app

PMSData = '[]'

title = "",
layout = html.Div([
    navbar,
    dbc.Container([
        html.H4(title, id = "title", className="text-center mt-5 mb-4", style={"color":"white"}),
        html.Div([
            deuc.PMSComponent(id = 'pms', value = PMSData),
        ], id="Pmswrapper"),
        
        html.Div([
            html.Button('Get', id='get', n_clicks=0, style={'visible':True}),
            dcc.Input(type = "text", id = "addList"),
            dcc.Input(type = "text", id = "updateList")
        ], style = {"visibility": "hidden"}),
        
        dbc.Row([
            # educ.PMSComponent(id = 'pms')
        ], id='getOut', style = {'height': '300px'}),
    ])
])

@app.callback(Output('pms', 'value'),
            [Input('get', 'n_clicks'),
            Input('addList', 'value'),
            Input('updateList', 'value')]
            )
def get(n_clicks, addList,updateList):
    result = get_girl_pms(current_user.id)
    return result

@app.callback(Output('addList', 'value'),
            [Input('pms', 'newGirl')]
            )
def add(newGirl):
    if(newGirl):
        add_girl_pms_data(current_user.id, newGirl['girlName'], "2020-05-04", newGirl['cycle'], newGirl['menstruation'], newGirl['obulation'])
        return "OK"

@app.callback(Output('updateList', 'value'),
                    [Input('pms','updateData')]
                    )
def update(updateData):
    print(updateData)
    if(updateData):
        update_girl_pms_data(updateData['id'],updateData)
