from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from .config import config

db = SQLAlchemy()
cors = CORS()

def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    cors.init_app(app, resources={r"/*": {"origins": "*"}})

    from . import routes
    app.register_blueprint(routes.bp)

    return app