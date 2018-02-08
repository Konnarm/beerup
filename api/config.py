from flask.ext.dotenv import DotEnv
class Config(object):
    SECRET_KEY = 'testing'

    @classmethod
    def init_app(self, app)
        env = DotEnv()
        env.init_app(app)
