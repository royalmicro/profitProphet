from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

def create_app(config_filename=None):
    app = Flask(__name__)

    # Load configuration
    app.config.from_object('app.config.Config')
    if config_filename:
        app.config.from_pyfile(config_filename)

    # Initialize extensions
    db.init_app(app)
    ma.init_app(app)

    # Register blueprints
    from app.routes.user_route import user_bp
    from app.routes.base_route import base_bp

    app.register_blueprint(base_bp)
    app.register_blueprint(user_bp)

    return app
