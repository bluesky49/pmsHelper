import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from apps.navbar import navbar
from flask_login import logout_user, current_user
from pms_mgt import db, Pms as base, add_girl_pms_data, delete_girl_pms_data, update_girl_pms_data, get_girl_pms
import json
from app import app
import datetime
from datetime import timedelta
import math
import  dash_bootstrap_components as dbc
# import ast
# teststr = "['aaa','bbb','ccc']"
# testarray = ast.literal_eval(teststr)
PMSData = '[]'

list_group = []

title = "PMS APPLICATION FOR MAN",
layout = html.Div([
    navbar,
    html.Div([
        html.H4(title, id = "title", className="text-center mt-5 mb-4", style={"color":"white"}),
        dbc.Button("Add Girl",id="open"),
        dbc.Modal(
            [
               dbc.ModalHeader("Header"),
                dbc.ModalBody("This is the content of the modal"),
                dbc.ModalFooter(
                    dbc.Button("Close", id="close", className="ml-auto")
                ), 
            ],
            id = "modal"
        ),
        
        dbc.Row(
            dbc.Col([
                dbc.Row(
                    [
                        dbc.Col(html.Div([
                            dbc.Row([
                                html.Div([
                                    html.H4("Girl List")
                                ], className="itemTitle listTitle"),
                                html.Div(id="getGirlList", className="girlListGroup")
                            ])
                        ], className="girlList girlCard"), width=2),
                        dbc.Col(html.Div([
                            dbc.Row([
                                html.Div([
                                    dbc.Row([
                                        dbc.Col([
                                            html.H5("Name : "),
                                            html.H5(id="name")
                                        ], width=8),
                                        dbc.Col([
                                            html.H5("startDate : "),
                                            html.H5(id="startDate")
                                        ], width=4)
                                    ]),
                                    dbc.Row([
                                        dbc.Col([
                                            html.H5("Menstration : "),
                                            html.H5(id="menstration")
                                        ], width=3),
                                        dbc.Col([
                                            html.H5("Ovulation : "),
                                            html.H5(id="name")
                                        ], width=3),
                                        dbc.Col([
                                            html.H5("Name : "),
                                            html.H5(id="name")
                                        ], width=3),
                                        dbc.Col([html.H5("Cycle : "),
                                            html.H5(id="cycle")], width=3),
                                    ]),
                                    dbc.Row([
                                        dbc.Col([
                                            dcc.Graph(id='pms',config={"displayModeBar": False})
                                        ])
                                    ])
                                ], className="itemTitle dataTitle"),
                                html.Div(id="getGirlList")
                            ])
                        ], className="girlData girlCard"), width=10),
                    ]
                ),                    
            ], width={"size": 8, "offset":2},)
        ),

        html.Div([
            html.Button('Get', id='get', n_clicks=0),
            dcc.Input(type = "text", id = "addList"),
            dcc.Input(type = "text", id = "updateList")
        ], style = {"visibility": "hidden"}
        ),
        
        dbc.Row([
            # educ.PMSComponent(id = 'pms')
        ], id='getOut', style = {'height': '300px'}),
    ], )
])

@app.callback(
    Output("modal","is_open"),
    [Input("open", "n_clicks"), Input("close", "n_clicks")],
    [State("modal", "is_open")],
)

def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open



@app.callback([Output('pms', 'figure'),
               Output('name', 'children'),
               Output('menstration', 'children'),
               Output('startDate', 'children'),
               Output('cycle', 'children')],
            [Input('get', 'n_clicks')])
def get(n_clicks):
    array = get_girl_pms(current_user.id)
    
    start = datetime.datetime.strptime(array[0]['startDate'],"%Y-%m-%d").date()
    xdata = [start + timedelta(days=i) for i in range(0,array[0]['cycle']*3)]
    
    pmsData,colors = [],[]
    for i in range(array[0]['menstruation']):
        step = 100/array[0]['menstruation']
        pmsData.append(round(100-i*step))
        colorstep = 205/array[0]['menstruation']
        colorred = round(255 - colorstep * i)
        colors.append('rgb('+str(colorred)+',0,0)')
    
    for i in range(array[0]['menstruation'], array[0]['cycle']-5-array[0]['ovulation']):
        pmsData.append(0)
        colors.append('rgb(255,255,255)')
    
    fertility,colorGreen = 0,0
    for i in range(array[0]['cycle']-array[0]['ovulation']-5, array[0]['cycle']-array[0]['ovulation']):
        fertility += 20
        pmsData.append(fertility)
        colorGreen += 41
        colors.append('rgb(0,'+str(colorGreen)+',0)')
    
    pmsData.append(75)
    colors.append('rgb(0, 164, 0)')
    pmsData.append(50)
    colors.append('rgb(0, 153, 0)')
    
    for i in range(array[0]['cycle'] - array[0]['ovulation'] + 2, array[0]['cycle'] - 7):
        pmsData.append(0)
        colors.append('rgb(255,255,255)')
   
    pms,colorBlue = 0,0
    for i in range(array[0]['cycle'] - 7, array[0]['cycle']):
        pms += round(100/7)
        pmsData.append(pms)
        
        colorBlueStep = math.floor((255 - 50) / 7)
        colorBlue += colorBlueStep
        colors.append('rgb(0,0,'+ str(colorBlue) +')')
    
    colors += colors + colors
    pmsData += pmsData + pmsData
     
    return {
        'data':[
            dict(
                x=xdata,
                y=pmsData,
                type='bar',
                marker={'color': colors}
            )
        ],
        'layout': {
            'plot_bgcolor': '#EEEEEE',
            'paper_bgcolor': '#EEEEEE',
            'title': 'PMS Data',
            'xaxis':{"title": "Date",
                           'rangeselector': {},
                           'rangeslider': {'visible': True}, 
                    },
            'yaxis':{"title": " "},
        }
    },array[0]['girlName'], array[0]['menstruation'], array[0]['startDate'], array[0]['cycle']
