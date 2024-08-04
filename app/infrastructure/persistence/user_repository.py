from werkzeug.security import generate_password_hash
from app.domain.model.user.user_repository_interface import UserRepositoryInterface
from app.domain.model.user.user import User
from app.infrastructure.persistence.sql_alchemy.user.user_mapped import UserMapped
from app.configuration.extensions.db_extension import db


class UserRepository(UserRepositoryInterface):
    """
    Repository class for managing user data persistence using SQLAlchemy.

    This class implements the UserRepositoryInterface and provides methods
    to add new users and retrieve users by their username from the database.
    """

    def __init__(self) -> None:
        self.db = db
        super().__init__()

    def add_entity(self, user: User) -> User | None:
        user: UserMapped = UserMapped(
            username=user.get_username(),
            password_hash=generate_password_hash(user.get_password()),
        )
        self.db.session.add(user)
        self.db.session.commit()

        last_updated = (
            self.db.session.query(UserMapped).order_by(UserMapped.id.desc()).first()
        )

        if last_updated is None:
            return None

        return User(**last_updated)

    def get_by_username(self, username: str) -> User:
        user: UserMapped = UserMapped.query.filter_by(username=username).first()
        user_attrs = user.get_model_attributes()
        return User(**user_attrs)
