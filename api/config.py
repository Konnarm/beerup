import os
class Config(object):
    SECRET_KEY = 'testing'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
