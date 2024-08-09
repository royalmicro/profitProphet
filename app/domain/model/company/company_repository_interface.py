from app.domain.utils.repository_interface import RepositoryInterface


class CompanyRepositoryInterface(RepositoryInterface):
    """
    Interface for converting an entity to its corresponding DTO (Data Transfer Object).

    Methods
    -------
    entity_to_dto() -> EntityDtoInterface:
        Converts the entity to its corresponding Data Transfer Object (DTO).
    """
