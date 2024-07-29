from flask import Flask
from flask_marshmallow import Marshmallow
from flask_restx import Api

from app.configuration.extensions.db_extension import db
from app.configuration.extensions.migration_extension import Migration


# Initialize extensions
api = Api()
migration = Migration()
marshmallow = Marshmallow()


def init(app: Flask):

    db.init_app(app)
    migration.init_migration(app, db)
    marshmallow.init_app(app)

    configuration = {
        "title": "Profit Prophet",
        "description": "Profit Prophet api documentation",
    }
    api.init_app(app, **configuration)
