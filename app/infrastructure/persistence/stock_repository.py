from dataclasses import dataclass
from typing import List

from app.configuration.extensions.db_extension import db
from app.domain.model.stock.stock import Stock
from app.infrastructure.persistence.sql_alchemy.stock.stock_mapped import StockMapped
from app.domain.model.stock.stock_repository_interface import (
    StockRepositoryInterface,
)


@dataclass
class StockRepository(StockRepositoryInterface):
    """
    Repository class for performing CRUD operations on StockEntity.

    This class inherits from RepositoryAbstract and implements methods
    for adding, retrieving, updating, and deleting stock entities from the database.

    Methods:
        get(id: int) -> Optional[StockEntity]: Retrieves a stock entity by its ID.
        add(stock: StockEntity) -> None: Adds a new stock entity to the database.
        update(stock: StockEntity) -> None: Updates an existing stock entity in the database.
        delete(id: int) -> None: Deletes a stock entity from the database by its ID.
        list() -> List[StockEntity]: Lists all stock entities in the database.
    """

    def __init__(self) -> None:
        self.db = db

    def add(self, entity: Stock) -> None:
        mapped_stock = StockMapped(name=entity.get_name(), symbol=entity.get_symbol())
        self.db.session.add(mapped_stock)
        self.db.session.commit()

    def get_all(self) -> None:
        stocks_mapped = StockMapped.query.all()
        stocks: List[StockMapped] = []
        for stock in stocks_mapped:
            stocks.append(
                Stock(
                    stockId=stock.id,
                    name=stock.name,
                    symbol=stock.symbol,
                    historical_data=stock.historical_data,
                )
            )
        return stocks
