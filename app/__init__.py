"""
This module initializes and configures the Flask application with SQLAlchemy, Marshmallow,
and Flask-Migrate. It also registers the application's blueprints for user and base routes.

Modules imported:
    - Flask: The core Flask application object.
    - Migrate: Flask-Migrate extension for SQLAlchemy database migrations.
    - SQLAlchemy: SQLAlchemy database extension for Flask.
    - Marshmallow: Marshmallow serialization/deserialization and validation library for Flask.
    - user_bp: Blueprint for user-related routes from `app.routes.user_route`.
    - base_bp: Blueprint for base routes from `app.routes.base_route`.

Functions:
    - create_app(config_filename=None): Initializes the Flask app with the given configuration 
      file, sets up database migrations, initializes extensions, and registers blueprints.

Usage:
    To create an instance of the Flask application, call `create_app` with an optional 
    configuration filename:
        app = create_app('path/to/config.py')
"""
from flask import Flask
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from .configuration.extensions import db
from . import configuration
from . import domain
from . import infrastructure
from .routes.stock_routes import stock_bp

__all__ = ['configuration', 'domain', 'infrastructure']

ma = Marshmallow()


def create_app(config_filename=None):
    """
    Initialize and configure the Flask application.

    Args:
        config_filename (str, optional): Path to a configuration file. If provided, the 
                                         configuration will be loaded from this file.

    Returns:
        Flask: Configured Flask application instance.
    """
    app = Flask(__name__)
    migrate = Migrate(app, db)  # noqa: F841
    # Load configuration
    app.config.from_object('app.configuration.config.DevelopmentConfig')
    if config_filename:
        app.config.from_pyfile(config_filename)

    # Initialize extensions
    db.init_app(app)
    ma.init_app(app)

    app.register_blueprint(stock_bp)

    return app
