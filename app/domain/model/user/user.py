from app.domain.model.entity_interface import EntityInterface


class User(EntityInterface):
    """
    User entity class representing a user in the domain model.

    This class implements the EntityInterface and provides methods
    to access the user's username and hashed password.
    """

    def __init__(self, **kwargs) -> None:
        self.__username = kwargs.get("username")
        self.__password_hash = kwargs.get("password_hash")

    def get_username(self) -> str:
        return self.__username

    def get_password_hash(self) -> str:
        return self.__password_hash
