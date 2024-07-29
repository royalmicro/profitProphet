from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict
from app.domain.model.entity.dto_interface import EntityDtoInterface


@dataclass()
class DataPriceDto(EntityDtoInterface):
    """
    A Data Transfer Object (DTO) for transferring price data information.

    Attributes:
        id (Any): The unique identifier for the price data entry.
        stock_id (Any): The identifier for the associated stock.
        register_date (Any): The date the price data was recorded.
        open_price (Any): The opening price of the stock on the register date.
        close_price (Any): The closing price of the stock on the register date.
        highest_price (Any): The highest price of the stock on the register date.
        lowest_price (Any): The lowest price of the stock on the register date.
        transaction_volume (Any): The transaction volume of the stock on the register date.
    """

    id: int
    stock_id: int
    register_date: datetime
    open_price: float
    close_price: float
    highest_price: float
    lowest_price: float
    transaction_volume: int

    def to_string(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "stock_id": self.stock_id,
            "register_date": self.register_date.strftime("%Y-%m-%d"),
            "open_price": self.open_price,
            "close_price": self.close_price,
            "highest_price": self.highest_price,
            "lowest_price": self.lowest_price,
            "transaction_volume": self.transaction_volume,
        }
