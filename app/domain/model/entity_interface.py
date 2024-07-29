from typing import Protocol

from app.domain.model.dto_interface import EntityDtoInterface


class EntityInterface(Protocol):
    """
    Interface for converting an entity to its corresponding DTO (Data Transfer Object).

    Methods
    -------
    entity_to_dto() -> EntityDtoInterface:
        Converts the entity to its corresponding Data Transfer Object (DTO).
    """

    def entity_to_dto(self) -> EntityDtoInterface: ...
