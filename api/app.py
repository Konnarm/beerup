from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from routes import *

#@app.route('/')
#@app.route('/index')
#def index():
#    return 'Hello'

if __name__ == '__main__':
    app.run()
