import dash
import os
import dash_auth
import flask
from flask import send_from_directory

from flask import Flask, redirect, url_for, session, request, jsonify

from requests_oauthlib import OAuth2Session
from flask_login import logout_user, current_user
import json
import dash_bootstrap_components as dbc

base_server = flask.Flask(__name__)

VALID_USERNAME_PASSWORD_PAIRS = {
    'test': 'test'
}

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
external_stylesheets=[dbc.themes.BOOTSTRAP]


app = dash.Dash(__name__, external_stylesheets=external_stylesheets,server=base_server,routes_pathname_prefix='/apps/',meta_tags=[{"name": "viewport", "content": "width=device-width"}])
app.title = 'Demo'
auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)
server = app.server
app.config.suppress_callback_exceptions = True

# app.css.config.serve_locally = True

# external_css = [
#     'https://codepen.io/chriddyp/pen/bWLwgP.css',
#     # '/static/base.css',
#     # '/static/style.css',
# ]

# for css in external_css:
#     app.css.append_css({"external_url": css})



client_id = "xxxxxxx"
client_secret = "xxxxx"
base_url="xxxxxxxx:8878"
redirect_uri = base_url+'/callback'
authorization_base_url = 'https:xxxxxxx/authorization.oauth2'
token_url = 'https:xxxxxxxx/token.oauth2'
scope = [
    "email",
    "profile",
    "openid",
    "phone"
]

def is_user_logged():
    # try:
    #     data=profile()
    #     if len(json.loads(data.data)['email']) > 3:
    #         return True
    #     else:
    #         return False
    # except:
    #     return False
    return True


@app.server.route('/static/<path:path>')
def static_file(path):
    static_folder = os.path.join(os.getcwd(), 'static')
    return send_from_directory(static_folder, path)
