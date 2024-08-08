from typing import Protocol


class ApplicationServiceInterface(Protocol):
    """
    An interface that defines the contract for an application service.

    This interface specifies that any class implementing it must define an `execute` method
    that takes a `symbol` as a string parameter.

    Methods:
    --------
    execute(symbol: str) -> None:
        Execute a service action based on the provided symbol.

        Parameters:
        -----------
        symbol : str
            A string representing a symbol (e.g., a stock ticker) that the service will act upon.
    """

    def execute(self, symbol: str): ...
