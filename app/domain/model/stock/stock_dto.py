from dataclasses import dataclass
from typing import Any, Dict

from app.domain.utils.dto_interface import EntityDtoInterface


@dataclass()
class StockDto(EntityDtoInterface):
    """
    Represents a Data Transfer Object for the stock.

    Attributes:
        id (int): The unique identifier for the stock.
        symbol (str): The symbol for the stock.
        name (str): The name of the company.
        historical_data (dict): Historical price and volume data.
    """

    id: int
    symbol: str
    name: str
    historical_data: Dict[str, Any]

    def to_string(self) -> Dict[str, Any]:
        if self.id:
            return {
                "id": self.id,
                "symbol": self.symbol,
                "name": self.name,
                "historical_data": self.historical_data,
            }

        return {
            "symbol": self.symbol,
            "name": self.name,
            "historical_data": self.historical_data,
        }
