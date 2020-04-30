from sqlalchemy import Table
from sqlalchemy.sql import select
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from config import engine
from flask_login import UserMixin
# 

db = SQLAlchemy()


class User(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    # username = db.Column(db.String(15), unique=True)
    # email = db.Column(db.String(50), unique=True)
    # password = db.Column(db.String(80))
    id = db.Column(db.Integer,
                   primary_key=True)
    username = db.Column(db.String(15),
                     nullable=False,
                     unique=False)
    email = db.Column(db.String(40),
                      unique=True,
                      nullable=False)
    password = db.Column(db.String(200),
                         primary_key=False,
                         unique=False,
                         nullable=False)
    created_on = db.Column(db.DateTime,
                           index=False,
                           unique=False,
                           nullable=True)
    user_role = db.Column(db.Integer,nullable=False, default=0)
    last_login = db.Column(db.DateTime,
                           index=False,
                           unique=False,
                           nullable=True)
    confirmed = db.Column(db.Boolean, nullable=False, default=False)
    confirmed_on = db.Column(db.DateTime, nullable=True)

User_tbl = Table('user', User.metadata)


def create_user_table():
    User.metadata.create_all(engine)


def add_user(username, password, email, user_role=0):
    hashed_password = generate_password_hash(password, method='sha256')

    ins = User_tbl.insert().values(
        username=username, email=email, password=hashed_password, confirmed=False, user_role=user_role)
#    try:
    conn = engine.connect()
    conn.execute(ins)
    conn.close()
#    except:
#        print('error')
def change_pwd(password):
    hashed_password = generate_password_hash(password, method='sha256')
    return hashed_password

def del_user(username, id):
    delete = None
    if username is not None:
        delete = User_tbl.delete().where(User_tbl.c.username == username)
    if id is not None:
        delete = User_tbl.delete().where(User_tbl.c.id == id)

    conn = engine.connect()
    conn.execute(delete)
    conn.close()

def update_user(stmp):
    conn = engine.connect()
    conn.execute(stmp)
    conn.close()


def show_users():
    select_st = select([ User_tbl.c.id, User_tbl.c.username, User_tbl.c.email, User_tbl.c.confirmed, User_tbl.c.user_role ])

    conn = engine.connect()
    rs = conn.execute(select_st)
    
    conn.close()
    return rs