import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from users_mgt import add_user, User_tbl, update_user, show_users, change_pwd, del_user

from app import app, User
from flask_login import login_user
from werkzeug.security import generate_password_hash
from apps.utils.token import generate_confirmation_token, confirm_token
from apps.utils.email import send_email
from flask import flash, url_for, render_template
import flask
import datetime
from flask import session

layout = dbc.Container([
    dcc.Location(id='url_signup', refresh=True),
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.Img(
                        src='assets/dash-logo-stripe.svg',
                        className='brand_logo'
                    ),
                ], className="brand_logo_container")
            ], className="d-flex justify-content-center"),
            html.Div([
                html.Form([
                    html.Div(id="sign_error", className="error-message mb-2"),
                    html.Div([
                        html.Div([
                            html.Span([
                                html.I(className="fas fa-user")
                            ], className="input-group-text")
                            # dbc.Span
                        ], className="input-group-append"),
                        dcc.Input(type="text", className="form-control input_user", placeholder="User Name", id="uname-box")
                    ], className="input-group mb-3"),
                    html.Div([
                        html.Div([
                            html.Span([
                                html.I(className="fas fa-envelope")
                            ], className="input-group-text")
                            # dbc.Span
                        ], className="input-group-append"),
                        dcc.Input(type="text", className="form-control input_user", placeholder="Email address", id="email-box")
                    ], className="input-group mb-3"),
                    html.Div([
                        html.Div([
                            html.Span([
                                html.I(className="fas fa-lock")
                            ], className="input-group-text")
                            # dbc.Span
                        ], className="input-group-append"),
                        dcc.Input(type="password", className="form-control input_pass", placeholder="Create password", id="pwd-box")
                    ], className="input-group mb-3"),
                    html.Div([
                        html.Div([
                            html.Span([
                                html.I(className="fas fa-lock")
                            ], className="input-group-text")
                            # dbc.Span
                        ], className="input-group-append"),
                        dcc.Input(type="password", className="form-control input_pass", placeholder="Repeat password", id="confirm-box")
                    ], className="input-group mb-2"),
                    html.Div(className="form-group", children=[
                        html.Div(className="custom-control custom-checkbox", children=[
                            dbc.Input(type="checkbox", className="custom-control-input", id="customControlInline"),
                            # html.Label("Remember me", className="custom-control-label", htmlFor="customControlInline")
                        ])
                    ]),
                    html.Div(className="d-flex justify-content-center mt-3 login_container", children=[
                        html.Button(type="button", className="btn login_btn", children=["Create Account"], id="signup-button")
                    ])
                ])
            ], className="d-flex justify-content-center form_container"),
            html.Div(className="mt-4", children=[
                html.Div(className="d-flex justify-content-center links", children=[
                    "Have an account?",
                    html.A("Log In", className="ml-2", href="/login")
                ])
            ])
        ], className="user_card_signup")
    ], className="d-flex justify-content-center h-100")
], className="h-100 login-form-padding")

@app.callback([Output('url_signup', 'pathname'), Output('sign_error', 'children')],
              [Input('signup-button', 'n_clicks')],
              [State('uname-box', 'value'),
                State('email-box', 'value'),
                State('pwd-box', 'value'),
                State('confirm-box', 'value')])
def sucess(n_clicks, input1, input2, input3, input4):
    existing_user = User.query.filter_by(username=input1).first()
    if input3 != input4:
        return None, "Different Password."
    if existing_user is None:
        add_user(input1, input3, input2, 0)
        
        if tokenMake(input2):
            print('A confirmation email has been sent via email.', 'success')
            return '/login', None
        else:
            return None, "Internal Server Error {0}."
        return None, "A user already exists with that email address."
    else:
        return None, "Exist user!"

def tokenMake(email):
    try:
        token = generate_confirmation_token(email)
        host = flask.request.host_url if flask.has_request_context() else ''
        confirm_url = host + 'confirm/' + token
        html = render_template('email.html', confirm_url=confirm_url)
        subject = "Please confirm your email"
        send_email(email, subject, html)
        return True
    except:
        return False


def confirm_email(token):
    # print(token)
    try:
        email = confirm_token(token)
    except:
        print('The confirmation link is invalid or has expired.', 'danger')
        return "/resend"
    
    user = User.query.filter_by(email=email).first_or_404()
    if user.confirmed:
        login_user(user, remember=True)
        session['user'] = user
        print('Account already confirmed. Please login.', 'success')
        return "/home"
    else:
        stmt = User_tbl.update().where(User_tbl.c.username==user.username).values(confirmed=True,confirmed_on=datetime.datetime.now())
        update_user(stmt)
        login_user(user, remember=True)
        session['user'] = user
        print('You have confirmed your account. Thanks!', 'success')
        return "/home"
    return False

def resend_email():
    username = session.get('username')
    user = User.query.filter_by(username=username).first_or_404()
    if tokenMake(user.email):
        return '/login'
    else:
        return '/unconfirmed'
