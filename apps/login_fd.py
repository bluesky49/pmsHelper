# Dash configuration
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app

# Create app layout
layout = html.Div(children=[
    dcc.Location(id='url_login_df', refresh=True),
    # html.Div(
    #     className="container",
    #     children=[
    #         html.Div(
    #             html.Div(
    #                 className="row",
    #                 children=[
    #                     html.Div(
    #                         className="ten columns",
    #                         children=[
    #                             html.Br(),
    #                             html.Div('User non authenticated - Please login to view the success screen'),
    #                         ]
    #                     ),
    #                     html.Div(
    #                         className="two columns",
    #                         # children=html.A(html.Button('LogOut'), href='/')
    #                         children=[
    #                             html.Br(),
    #                             html.Button(id='back-button', children='Go back', n_clicks=0)
    #                         ]
    #                     )
    #                 ]
    #             )
    #         )
    #     ]
    # )
    dbc.Container([
        dbc.Row([
            dbc.Col([
                html.Br(),
                html.Div('User non authenticated - Please login to view the success screen'),
            ])
        ]),
        dbc.Row([
            dbc.Col([
                html.Br(),
                html.Button(id='back-button', children='Go back', n_clicks=0)
            ])
        ])
    ])
])


# Create callbacks
@app.callback(Output('url_login_df', 'pathname'),
              [Input('back-button', 'n_clicks')])
def logout_dashboard(n_clicks):
    if n_clicks > 0:
        return '/login'
