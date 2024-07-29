from flask import Flask
from flask_marshmallow import Marshmallow

from app.configuration.extensions.db_extension import db
from app.configuration.extensions.migration_extension import Migration
from app.configuration.extensions.api_extension import ProfitProphetApi

# Initialize extensions
migration = Migration()
marshmallow = Marshmallow()


def init(app: Flask, package_name: str, package_path: str):

    db.init_app(app)
    migration.init_migration(app, db)
    marshmallow.init_app(app)

    configuration = {
        "title": "Profit Prophet",
        "description": "Profit Prophet api documentation",
    }
    restx_api = ProfitProphetApi(package_name, package_path)
    restx_api.init_app(app, configuration)
