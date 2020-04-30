import configparser
from urllib.parse import quote_plus as urlquote
from sqlalchemy import create_engine
import os

config = configparser.ConfigParser()

connectionstring = "mysql://develop:%s@34.66.242.13/pmshelper" % urlquote('as34Chpl')
# connectionstring = "mysql://root1:%s@34.66.242.13/dash_login" % urlquote('uChplX1o2')1
engine = create_engine(connectionstring)

