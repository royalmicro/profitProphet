from dataclasses import dataclass
from typing import Any, Dict, Optional

from sqlalchemy import JSON, String
from sqlalchemy.orm import Mapped, mapped_column
from app.configuration.extensions.db_extension import db


@dataclass
class StockMapped(db.Model):
    """
    Represents a stock entity in the application's database.

    Attributes:
        id (int): The unique identifier for the stock. Primary key.
        symbol (str): The symbol for the stock (e.g., AAPL for Apple). Cannot be null.
        name (str): The name of the company. Cannot be null.
        historical_data (Optional[Dict[str, Any]]): Historical price and volume data,
            stored as JSON.
    """

    __tablename__ = "stocks"

    id: Mapped[int] = mapped_column(primary_key=True)
    symbol: Mapped[str] = mapped_column(String(8), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    historical_data: Mapped[Optional[Dict[str, Any]]] = mapped_column(
        type_=JSON, nullable=True
    )

    def has_changed(self, attr, new_value):
        current_value = getattr(self, attr)
        return current_value != new_value

    def to_str(self) -> Dict[str, any]:
        response = {}

        if self.id:
            response.update({"id": self.id})

        response.update(
            {
                "name": self.name,
                "symbol": self.symbol,
                "historical_data": self.historical_data,
            }
        )

        return response
