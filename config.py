import os
from sqlalchemy import create_engine

import urllib
class config(object):
    SECRET_KEY='Clave nueva'
    SESION_COOKIE_SECURE=False



class DevelopmentConfig(config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/bdAplicacionesWeb'
    SQLALCHEMY_TRACK_MODIFICATIONS=False