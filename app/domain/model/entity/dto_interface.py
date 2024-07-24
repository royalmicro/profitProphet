from typing import Any, Dict, Protocol


class EntityDtoInterface(Protocol):
    """
    Interface for converting an entity to a dictionary representation.

    Methods
    -------
    to_string() -> Dict[str, Any]:
        Converts the entity to a dictionary representation.
    """
    def to_string(self) -> Dict[str, Any]: ...
