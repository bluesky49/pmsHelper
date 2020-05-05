import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app, login_manager, User
from app import server, Pms
from apps import home, login, login_fd, signup, unconfrimed, dataset

from apps.signup import confirm_email, resend_email, show_users
from flask_login import logout_user, current_user
import os
from flask import session, redirect, url_for

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

def micro_router(conf_layout):
    if current_user.is_authenticated:
        # user = session.get('user')
        try:
            # if user.confirmed:
            if current_user.confirmed:
                return conf_layout
            else:
                return dcc.Location(pathname='/unconfirmed', id='unconfirmed_redirect')
        except:
            return login_fd.layout
    else:
        return login_fd.layout

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):

    if pathname == '/home':
        return micro_router(home.layout)
    elif pathname =='/dataset':
        return dataset.layout
    elif pathname == "/login":
        return login.layout
    elif pathname == "/signup":
        return signup.layout
    elif pathname == '/':
        if current_user.is_authenticated:
            return dcc.Location(pathname='/home', id="home_url")
        else:
            return dcc.Location(pathname='/login', id='login_redirect')
    elif pathname == '/logout':
        if current_user.is_authenticated:
            logout_user()
            return dcc.Location(pathname='/login', id='login_redirect')
        else:
            return dcc.Location(pathname='/login', id='login_redirect')
    elif str(pathname).startswith('/confirm'):
        if pathname.startswith('/confirm/'):
            token = pathname.split('/')[-1]
            if confirm_email(token) == '/home':
                return dcc.Location(pathname='/home', id="home_url")
            else:
                return dcc.Location(pathname='/login', id='login_redirect')
    elif str(pathname).startswith('/unconfirmed'):
        return unconfrimed.layout
    elif pathname == "/resend":
        if resend_email() == '/unconfirmed':
            return dcc.Location(pathname='/unconfirmed', id='unconfirmed_redirect')
        else:
            return dcc.Location(pathname='/login', id='login_redirect')
    else:
        return '404'

# callback to reload the user object
@login_manager.user_loader
def load_user(user_id):
    try:
        return User.query.get(int(user_id))
        #return session['user']
    except:
        return None


if __name__ == '__main__':
    app.run_server(host="0.0.0.0", port=int("8080"), debug=True,dev_tools_ui=True, dev_tools_props_check=True)