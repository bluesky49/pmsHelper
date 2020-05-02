import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from apps.navbar import navbar
import dash_extra_ui_components as educ

from app import app

dataset_card = dbc.Card(
    [
        html.A([
            dbc.CardImg(src="/assets/acoin-xjoz2.svg", top=True),
            dbc.CardFooter("Dataset Preparation", className="text-center")
        ], href='/dataset'),
    ],
    # style={"width": "18rem"}
)

layout = html.Div([
    navbar,
    dbc.Container([
        html.H4("Welcome to demo page", className="text-center mt-5 mb-4"),
        dbc.Row([
            dbc.Col(dataset_card),
            dbc.Col(dataset_card),
            dbc.Col(dataset_card),
        ], className="mb-4"),
        dbc.Row([
            dbc.Col(dataset_card),
            dbc.Col(dataset_card),
            dbc.Col(dataset_card),
        ], className="mb-4"),
        dbc.Row([
            dbc.Col(dataset_card),
            dbc.Col(dataset_card),
            dbc.Col(dataset_card),
        ], className="mb-4"),
    ])
])
