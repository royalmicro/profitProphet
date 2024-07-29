import importlib
import pkgutil
from typing import Any, Dict
from flask import Flask
from flask_restx import Api, Namespace


class ProfitProphetApi:
    """
    Singleton for managing and initializing a Flask-RESTX API with dynamic controller registration.

    This class ensures that only one instance of the API is created. It provides methods to
    initializethe API with a Flask application and dynamically register controllers (namespaces)
    from a specified package.

    Attributes
    ----------
        package_name (str): The name of the package containing the controllers.
        package_path (str): The path to the package containing the controllers.
        api_instance (Api): The Flask-RESTX API instance.

    Methods
    -------
        get_api_instance() -> Api:
            Returns the current instance of the Flask-RESTX API.

        init_app(app: Flask, config: Dict[str, Any]) -> None:
            Initializes the Flask-RESTX API with the given Flask app and configuration.

        register_controllers() -> None:
            Dynamically registers namespaces in the specified package with the Flask-RESTX API.
    """

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "instance"):
            cls.instance = super(ProfitProphetApi, cls).__new__(cls)
        return cls.instance

    def __init__(self, package_name: str = None, package_path: str = None):
        self.package_name = package_name
        self.package_path = package_path
        self.api_instance = Api()

        if self.package_name is not None and self.package_path is not None:
            self.register_controllers()

    def get_api_instance(self) -> Api:
        """
        Returns the current instance of the Flask-RESTX API.

        Returns:
            Api: The Flask-RESTX API instance.
        """
        return self.api_instance

    def init_app(self, app: Flask, config: Dict[str, Any]) -> None:
        """
        Initializes the Flask-RESTX API with the given Flask app and configuration.

        Args:
            app (Flask): The Flask application instance.
            config (Dict[str, Any]): Configuration settings for the Flask-RESTX API.
        """
        self.api_instance.init_app(app, **config)

    def register_controllers(
        self,
    ) -> None:
        """
        Dynamically registers namespaces in the specified package with the Flask-RESTX API.

        This method imports all modules in the given package path and registers any found namespaces
        with the Flask-RESTX API instance.

        Raises:
            ImportError: If there is an issue importing the modules.
        """
        for _, module_name, _ in pkgutil.walk_packages(
            self.package_path, f"{self.package_name}."
        ):
            module = importlib.import_module(module_name)
        for attr in dir(module):
            obj = getattr(module, attr)
            if isinstance(obj, Namespace):
                self.api_instance.add_namespace(obj)
