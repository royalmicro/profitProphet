from datetime import datetime

from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import Float, Integer

from app.configuration.extensions import db
from app.domain.model.entity.price_data.data_price_dto import DataPriceDto


class DataPriceEntity(db.Model):
    """
    A SQLAlchemy model representing the price data of a stock.

    Attributes:
        id (Mapped[int]): The primary key for the price data entry.
        stock_id (Mapped[int]): A foreign key linking to the ID of a stock in the stocks table.
        register_date (Mapped[Date]): The date the price data was recorded.
        open_price (Mapped[Float]): The opening price of the stock on the register date.
        close_price (Mapped[Float]): The closing price of the stock on the register date.
        highest_price (Mapped[Float]): The highest price of the stock on the register date.
        lowest_price (Mapped[Float]): The lowest price of the stock on the register date.
        transaction_volume (Mapped[Integer]): The transaction volume of the stock on
            the register date.
    """

    __tablename__ = "data_prices"

    id: Mapped[int] = mapped_column(primary_key=True)
    stock_id: Mapped[int] = mapped_column(ForeignKey("stocks.id"))
    register_date: Mapped[datetime] = mapped_column(DateTime(), nullable=True, unique=True)
    open_price: Mapped[float] = mapped_column(Float(), nullable=True)
    close_price: Mapped[float] = mapped_column(Float(), nullable=True)
    highest_price: Mapped[float] = mapped_column(Float(), nullable=True)
    lowest_price: Mapped[float] = mapped_column(Float(), nullable=True)
    transaction_volume: Mapped[int] = mapped_column(Integer(), nullable=True)

    def entity_to_dto(self) -> DataPriceDto:
        return DataPriceDto(
            self.id,
            self.stock_id,
            self.register_date,
            self.open_price,
            self.close_price,
            self.highest_price,
            self.lowest_price,
            self.transaction_volume,
        )
