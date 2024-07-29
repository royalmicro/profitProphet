from typing import Any, Dict
from app.domain.model.entity_interface import EntityInterface
from app.domain.model.stock.stock_dto import StockDto


class Stock(EntityInterface):
    """
    Represents a stock entity with its associated data.

    Attributes:
        id (int | None): The unique identifier for the stock.
        symbol (str): The stock symbol.
        name (str): The name of the stock.
        historical_data (Dict[str, Any] | None): The historical data for the stock.

    Methods:
        get_symbol() -> str:
            Returns the stock symbol.

        get_name() -> str:
            Returns the stock name.

        get_historical_data() -> Dict[str, Any] | None:
            Returns the historical data for the stock.

        set_historical_data(historical_data: Dict[str, Any]) -> None:
            Sets the historical data for the stock.

        entity_to_dto() -> StockDto:
            Converts the stock entity to a data transfer object (DTO).
    """

    def __init__(
        self,
        stockId: int | None,
        symbol: str,
        name: str,
        historical_data: Dict[str, any] | None,
    ) -> None:
        self.id = stockId
        self.symbol = symbol
        self.name = name
        self.historical_data = historical_data

    def get_symbol(self):
        return self.symbol

    def get_name(self):
        return self.name

    def get_historical_data(self):
        return self.historical_data

    def set_historical_data(self, historical_data: Dict[str, Any]):
        self.historical_data = historical_data

    def entity_to_dto(self) -> StockDto:
        return StockDto(
            id=self.id,
            symbol=self.symbol,
            name=self.name,
            historical_data=self.historical_data or {},
        )
