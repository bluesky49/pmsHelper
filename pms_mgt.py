from sqlalchemy import Table
from sqlalchemy.sql import select
from flask_sqlalchemy import SQLAlchemy
from config import engine
import json
db = SQLAlchemy()

class Pms(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    # girlName = db.Column(db.String)
    # user_id = db.Column(db.Integer)
    # cycle = db.Column(db.Integer)
    # ovulation = db.Column(db.Integer)
    # menstruation = db.Column(db.Integer)
    id = db.Column(db.Integer,
                   primary_key=True)
    girlName = db.Column(db.String(30),
                    nullable=False)
    startDate = db.Column(db.String(30),
                    nullable=False)
    cycle = db.Column(db.Integer,
                      nullable=False)
    menstruation = db.Column(db.Integer,
                        nullable=False
                        )
    ovulation = db.Column(db.Integer,
                         nullable=False)
    user_id = db.Column(db.Integer,
                    nullable=False)

Pms_tbl = Table('pms', Pms.metadata)

def create_pms_table():
    Pms.metadata.create_all(engine)


def add_girl_pms_data(user_id, girlName, startDate, cycle, menstruation, ovulation):
    insertString = Pms_tbl.insert().values(
        user_id=user_id, girlName=girlName, startDate=startDate, cycle=cycle, menstruation=menstruation, ovulation=ovulation )
#    try:
    print(insertString)
    conn = engine.connect()
    conn.execute(insertString)
    conn.close()
#    except:
#        print('error')

def delete_girl_pms_data(girlName, id):
    delete = None
    if girlName is not None:
        delete = Pms_tbl.delete().where(Pms_tbl.c.girlName == girlName)
    if id is not None:
        delete = Pms_tbl.delete().where(User_tbl.c.id == id)

    conn = engine.connect()
    conn.execute(delete)
    conn.close()

def update_girl_pms_data(user_id, updateData):
    updateString = users.update()\
        .where(Pms_tbl.c.id==user_id)\
        .values(girlName=updateData['girlName'], 
                startDate=updateData['startDate'],
                cycle=updateData['cycle'],
                ovulation=updateData['ovulation'],
                menstruation=updateData['menstruation']
                )
    conn = engine.connect()
    conn.execute(updateString)
    conn.close()


def get_girl_pms(user_id):
    select_st = select([Pms_tbl.c.id, Pms_tbl.c.girlName, Pms_tbl.c.startDate , Pms_tbl.c.cycle, Pms_tbl.c.menstruation, Pms_tbl.c.ovulation ]).where(user_id==user_id)
    conn = engine.connect()
    res = conn.execute(select_st)
    conn.close()
    return json.dumps([dict(r) for r in res])