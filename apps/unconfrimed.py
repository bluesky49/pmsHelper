# Dash configuration
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app

# Create app layout
layout = html.Div(children=[
    dcc.Location(id='url_unconfirmed', refresh=True),
    dbc.Container([
        dbc.Row([
            dbc.Col([
                html.H1("Welcome!"),
                html.Br(),
                html.Div('You have not confirmed your account. Please check your inbox (and your spam folder) - you should have received an email with a confirmation link.'),
                html.Div([html.P("Didn't get the email?"), dcc.Link("Resend", href="/resend")])
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
@app.callback(Output('url_unconfirmed', 'pathname'),
              [Input('back-button', 'n_clicks')])
def logout_dashboard(n_clicks):
    if n_clicks > 0:
        return '/'
