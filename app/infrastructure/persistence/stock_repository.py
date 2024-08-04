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
        super().__init__(self)

    def add(self, **kwargs) -> None:
        mapped_stock = StockMapped(name=kwargs.get("name"), symbol=kwargs.get("symbol"))
        self.db.session.add(mapped_stock)
        self.db.session.commit()

        return (
            self.db.session.query(StockMapped).order_by(StockMapped.id.desc()).first()
        )

    def get_all(self) -> None:
        stocks_mapped: List[StockMapped] = StockMapped.query.all()
        stocks: List[Stock] = []
        for stock in stocks_mapped:
            stocks.append(Stock(**stock.to_str()))
        return stocks

    def get_by_symbol(self, symbol) -> StockMapped:
        stock_mapped: StockMapped = StockMapped.query.filter(
            (StockMapped.symbol == symbol)
        ).first()
        return stock_mapped

    def update(self, entity: Stock):
        stock_mapped = self.get_by_symbol(entity.symbol)

        if stock_mapped.has_changed("name", entity.name):
            stock_mapped.name = entity.name

        stock_mapped.historical_data = entity.historical_data

        self.db.session.commit()

    def delete_by_symbol(self, symbol: str):
        stock = self.get_by_symbol(symbol)
        self.db.session.delete(stock)
        db.session.commit()
