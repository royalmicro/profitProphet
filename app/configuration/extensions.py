from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

marshmallow = Marshmallow()
db = SQLAlchemy()
migration = Migrate()
api = Api()

def init(app: Flask):
    # Initialize extensions
    db.init_app(app)
    marshmallow.init_app(app)
    migration.init_app(app, db)

    configuration = {
        'title': 'Profit Prophet',  
        'description': 'Profit Prophet api documentation'
    }
    api.init_app(app, **configuration)
