# Dash app initialization
import dash
# User management initialization
import os
from flask_login import LoginManager, UserMixin
from users_mgt import db, User as base, create_user_table
from pms_mgt import db, Pms as pms_base, create_pms_table
from config import config, connectionstring
import dash_bootstrap_components as dbc
from flask_session import Session
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

FONT_AWESOME = "https://use.fontawesome.com/releases/v5.7.2/css/all.css"
# BOOTSTRAP_CSS = "https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
external_stylesheets=[dbc.themes.BOOTSTRAP, FONT_AWESOME]
# external_stylesheets=[FONT_AWESOME, BOOTSTRAP_CSS]
external_scripts = ["https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.min.js", "https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"]

create_pms_table()
create_user_table()

app = dash.Dash(
    __name__,
    meta_tags=[
        {
            'charset': 'utf-8',
        },
        {
            'name': 'viewport',
            'content': 'width=device-width, initial-scale=1, shrink-to-fit=no'
        }
    ],
    external_stylesheets=external_stylesheets,
    external_scripts=external_scripts
)
app.title = 'Demo'
server = app.server

################################
###    server config  ##########
################################
app.config.suppress_callback_exceptions = True
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

server.config['SESSION_PERMANENT'] = True
server.config['SESSION_TYPE'] = 'filesystem'
server.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=5)
server.config['SESSION_FILE_THRESHOLD'] = 100  
server.config['SECURITY_PASSWORD_SALT'] = 'my_precious_two'

# mail settings
server.config['MAIL_SERVER'] = 'smtp.yandex.com'
server.config['MAIL_PORT'] = 587
server.config['MAIL_USE_TLS'] = True

# gmail authentication
server.config['MAIL_USERNAME'] = "*******@yandex.com"
server.config['MAIL_PASSWORD'] = "********"
# server.config['MAIL_USERNAME'] = os.environ['APP_MAIL_USERNAME']
# server.config['MAIL_PASSWORD'] = os.environ['APP_MAIL_PASSWORD']

# mail accounts
server.config['MAIL_DEFAULT_SENDER'] = '**********@yandex.com'

# The maximum number of items the session stores 
# before it starts deleting some, default 500
server.config['SESSION_FILE_THRESHOLD'] = 100 
# server.secret_key = os.urandom(24)
server.secret_key = "J057m7EYSDAd692XJfMcfEou1P3m8afS"
server.config.update(
    # SECRET_KEY=os.urandom(12),
    SQLALCHEMY_DATABASE_URI=connectionstring,
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)

######################################

sess = Session()
sess.init_app(server)

mail = Mail(server)

db = SQLAlchemy(server)
db.init_app(server)
    
login_manager = LoginManager()
login_manager.init_app(server)
login_manager.login_view = '/login'


# Create User class with UserMixin
class User(UserMixin, base):
    pass

class Pms(pms_base):
    pass

# callback to reload the user object
@login_manager.user_loader
def load_user(user_id):
    try:
        return User.query.get(int(user_id))
    except:
        return None
