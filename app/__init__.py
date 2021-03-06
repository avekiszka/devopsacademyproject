from flask import Flask

from .home import home as home_blueprint

from .config import Config

app = Flask(__name__)
app.secret_key = 'sdjh23jkhKGHWe2'
app.config.from_object(Config)

def create_app():
    app.register_blueprint(home_blueprint)

    return app