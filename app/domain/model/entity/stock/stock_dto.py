from typing import Any, Dict
from app.domain.model.entity.dto_interface import EntityDtoInterface

class StockDTO(EntityDtoInterface):
    """
    Represents a Data Transfer Object for the stock.

    Attributes:
        id (int): The unique identifier for the stock.
        symbol (str): The symbol for the stock.
        name (str): The name of the company.
        historical_data (dict): Historical price and volume data.
    """
    def __init__(self, stockId: int, symbol: str, name: str, historical_data: Dict[str, Any]):
        self.id = stockId
        self.symbol = symbol
        self.name = name
        self.historical_data = historical_data

    def __repr__(self):
        return (f"<StockDTO(id={self.id}, symbol={self.symbol}, "
                f"name={self.name}, historical_data={self.historical_data})>")


    def to_string(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "symbol": self.symbol,
            "name" : self.name,
            "historical_data": self.historical_data
        }
