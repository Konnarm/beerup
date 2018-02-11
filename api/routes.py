from flask import render_template
from flask_restful import Resource, Api
from app import app

from models import User

api = Api(app)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Meet UP beer UP!')

class GetMatchingUser(Resource):
    def get(self):
        user = User.query.first()
        return user.name
        
api.add_resource(GetMatchingUser, '/api/v1/matching_user')
