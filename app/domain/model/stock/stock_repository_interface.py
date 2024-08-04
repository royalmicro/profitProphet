from app.domain.model.repository_interface import RepositoryInterface


class StockRepositoryInterface(RepositoryInterface):
    """
    Interface for converting an entity to its corresponding DTO (Data Transfer Object).

    Methods
    -------
    entity_to_dto() -> EntityDtoInterface:
        Converts the entity to its corresponding Data Transfer Object (DTO).
    """
