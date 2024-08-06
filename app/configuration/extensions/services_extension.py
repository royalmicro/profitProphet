import importlib
import os
import fnmatch
from injector import Binder, singleton
from flask import Flask
from app.application.services.alpha_vantage.query import Query


class Services:
    """
    A singleton class that configures dependency injection bindings for services in the application.

    This class ensures that only one instance of Services exists and provides a method to include
    and bind service modules using the Injector library.

    Methods:
        __new__(cls):
            Ensures a single instance of the Services class is created.

        include_modules(self, binder: Binder):
            Binds service classes to their respective implementations in the singleton scope.

            Parameters:
                binder (Binder): The Binder instance from the Injector library used to bind
                                 service classes to their implementations.
    """

    root_path: str
    interface_files_name: list[str] = []
    binders: list = []
    repository_modules: list[dict[str, any]] = []
    repository_interface_modules: list[dict[str, any]] = []

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(Services, cls).__new__(cls)
        return cls.instance

    def init_app(self, app: Flask):
        self.root_path = app.config["ROOT_PATH"]
        self.__import_repository_modules()
        self.__include_repository_interface_names()
        for file_path in self.interface_files_name:
            self.__import_repository_interface_modules(file_path)

    def __include_repository_interface_names(self):
        domain_services_path = f"{self.root_path}/domain/model"
        for root, _, files in os.walk(domain_services_path):
            for file in files:
                if fnmatch.fnmatch(file, "*_interface.py"):
                    self.interface_files_name.append(os.path.join(root, file))

    def __import_repository_interface_modules(self, filepath: str):
        module_name = os.path.splitext(os.path.basename(filepath))[0]
        module_name = self.__split_and_capitalize(module_name)

        full_module_name = self.__convert_path_to_module(filepath)
        module = importlib.import_module(full_module_name)
        self.repository_interface_modules.append({module_name: module})

    def __import_repository_modules(self):
        repositories_services_path = f"{self.root_path}/infrastructure/persistence"

        # Get a list of all files in the controllers directory
        for file in os.listdir(repositories_services_path):
            if file.endswith(".py") and file != "__init__.py":
                module_name = file[:-3]
                full_module_name = f"app.infrastructure.persistence.{module_name}"
                module_name = self.__split_and_capitalize(module_name)
                module = importlib.import_module(full_module_name)
                self.repository_modules.append({module_name: module})

    def __convert_path_to_module(self, path: str):
        path = path.replace("/", ".").replace(".py", "")
        cleaned_path = path.lstrip(".")
        return cleaned_path

    def __split_and_capitalize(self, input_string, split_by: str = "_"):
        substrings = input_string.split(split_by)
        capitalized_substrings = [substring.capitalize() for substring in substrings]
        return "".join(capitalized_substrings)

    def include_modules(self, binder: Binder):
        for repository in self.repository_modules:
            repository_key = next(iter(repository))
            repository_value = repository[repository_key]

            for interface in self.repository_interface_modules:
                interface_key = next(iter(interface))
                interface_value = interface[interface_key]

                if repository_key in interface_key:
                    repository_class = getattr(repository_value, repository_key)
                    interface_class = getattr(interface_value, interface_key)
                    binder.bind(
                        interface=interface_class, to=repository_class, scope=singleton
                    )
        self.__specific_binders(binder)

    def __specific_binders(self, binder: Binder):
        binder.bind(interface=Query, to=Query, scope=singleton)
