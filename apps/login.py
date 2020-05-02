import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from flask import session

from app import app, User
from flask_login import login_user, current_user
from werkzeug.security import check_password_hash

# error = ''
# if 'error' in session:
#     error = session.get('error')

layout = dbc.Container([
    dcc.Location(id='url_login', refresh=True),
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.Img(
                        src='/assets/dash-logo-stripe.svg',
                        className='brand_logo'
                    ),
                ], className="brand_logo_container")
            ], className="d-flex justify-content-center"),
            html.Div([
                html.Form([
                    html.Div(id="error", className="error-message mb-2"),
                    html.Div([
                        html.Div([
                            html.Span([
                                html.I(className="fas fa-user")
                            ], className="input-group-text")
                        ], className="input-group-append"),
                        dcc.Input(type="text", className="form-control input_user", placeholder="User name", id="uname-box")
                    ], className="input-group mb-3"),
                    html.Div([
                        html.Div([
                            html.Span([
                                html.I(className="fas fa-key")
                            ], className="input-group-text")
                            # dbc.Span
                        ], className="input-group-append"),
                        dcc.Input(type="password", className="form-control input_pass", placeholder="Password", id="pwd-box")
                    ], className="input-group mb-2"),
                    html.Div(className="form-group", children=[
                        dcc.Checklist(
                            options=[
                                {'label': "Remember me", 'value': 'me'}
                            ]
                        )
                    ]),
                    html.Div(className="d-flex justify-content-center mt-3 login_container", children=[
                        html.Button(type="button", className="btn login_btn", children=["Login"], id="login-button")
                    ])
                ])
            ], className="d-flex justify-content-center form_container"),
            html.Div(className="mt-4", children=[
                html.Div(className="d-flex justify-content-center links", children=[
                    "Don't have an account?",
                    html.A("Sign Up", className="ml-2", href="/signup")##31fd0c
                ])
            ])
        ], className="user_card")
    ], className="d-flex justify-content-center h-100")
], className="h-100 login-form-padding")

@app.callback([Output('url_login', 'pathname'), Output('error', 'children')],
              [Input('login-button', 'n_clicks')],
              [State('uname-box', 'value'),
               State('pwd-box', 'value')])
def sucess(n_clicks, input1, input2):
    try:
        user = User.query.filter_by(username=input1).first()
        if user:
            if check_password_hash(user.password, input2):
                if user.confirmed:
                    login_user(user, remember=True)
                    session['username'] = input1
                    session['user'] = user
                    if user.user_role > 0:
                        return '/admin/dashboard', ""
                    return '/home', ""
                else:
                    session['username'] = input1
                    session['user'] = user
                    return '/unconfirmed', ""
            else:
                return None, "Incorrect Password"
        else:
            return None, "Incorrect Username"
    except:
        return None, 'Internal Server Error'

# @app.callback(Output('error', 'children'), [Input()])