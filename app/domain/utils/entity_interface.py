from typing import Any, Protocol

from app.domain.utils.dto_interface import EntityDtoInterface


class EntityInterface(Protocol):
    """
    Interface for converting an entity to its corresponding DTO (Data Transfer Object).

    Methods
    -------
    entity_to_dto() -> EntityDtoInterface:
        Converts the entity to its corresponding Data Transfer Object (DTO).
    """

    def entity_to_dto(self) -> EntityDtoInterface: ...

    def has_changed(self, mapped_file: Any, attr: str) -> bool: ...
