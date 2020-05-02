import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from apps.navbar import navbar
import dash_extra_ui_components as educ

from app import app

myGirl = dbc.Card(
    style={"height": "100px", "width":"400px"},
    className="girlCard"
)

layout = html.Div([
    navbar,
    dbc.Container([
        html.H4("Welcome to demo page", className="text-center mt-5 mb-4", style={"color":"white"}),
        dbc.Row([
            dbc.Col(myGirl),
        ]),
        dbc.Row([
            dbc.Col(myGirl),
        ],),
        dbc.Row([
            dbc.Col(myGirl),
        ]),
    ])
])
