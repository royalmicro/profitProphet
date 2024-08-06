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

import importlib
import os
from flask import Flask
from flask_injector import FlaskInjector

from app.configuration import extensions
from app.configuration.extensions import services
from .configuration.config import DevelopmentConfig


def import_controllers():
    # Path to the controllers directory
    controllers_path = os.path.join(
        os.path.dirname(__file__), "application", "controller"
    )

    # Get a list of all files in the controllers directory
    for file in os.listdir(controllers_path):
        if file.endswith(".py") and file != "__init__.py":
            # Module name is the file name without the .py extension
            module_name = file[:-3]
            # Full module name includes the package path
            full_module_name = f"app.application.controller.{module_name}"
            # Import the module dynamically
            importlib.import_module(full_module_name)


app = Flask(__name__)
# Load configuration
app.config.from_object(DevelopmentConfig)
extensions.init(app)
import_controllers()

FlaskInjector(app=app, modules=[services.include_modules])


if __name__ == "__main__":
    app.run()
