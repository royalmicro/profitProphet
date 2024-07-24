from app.infrastructure.persistence.base_repository import RepositoryAbstract


class StockRepository(RepositoryAbstract):
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
