from injector import Binder, singleton

from app.infrastructure.persistence.stock_repository import StockRepository
from app.infrastructure.services.http.http_response import HttpResponse


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

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(Services, cls).__new__(cls)
        return cls.instance

    def include_modules(self, binder: Binder):
        binder.bind(StockRepository, to=StockRepository, scope=singleton)
        binder.bind(HttpResponse, to=HttpResponse, scope=singleton)
