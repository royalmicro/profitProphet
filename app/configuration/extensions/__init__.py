from flask import Flask
from flask_marshmallow import Marshmallow

from app.configuration.extensions.db_extension import db
from app.configuration.extensions.migration_extension import Migration
from app.configuration.extensions.api_extension import api
from app.configuration.extensions.jwt_extension import jwt_manager
from app.configuration.extensions.services_extension import Services

# Initialize extensions
migration = Migration()
marshmallow = Marshmallow()
services = Services()


def init(app: Flask):

    db.init_app(app)
    migration.init_migration(app, db)
    marshmallow.init_app(app)
    jwt_manager.init_app(app)
    services.init_app(app)

    from app.configuration.api.namespaces import profitProphet_ns
    from app.configuration.api.namespaces import auth_ns
    from app.configuration.api.models import stock_model
    from app.configuration.api.models import auth_model

    api.add_namespace(auth_ns, path="/auth")
    api.add_namespace(profitProphet_ns, path="/")

    api.add_model("Stock", stock_model)
    api.add_model("Auth", auth_model)

    api.init_app(app)
