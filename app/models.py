"""
This module contains the SQLAlchemy model for the User entity.

Classes:
    User: Represents a user in the application's database.

Attributes:
    id (int): The unique identifier for the user.
    username (str): The unique username for the user.
    email (str): The unique email address for the user.
"""
from sqlalchemy.orm import  mapped_column, Mapped
from app import db

class User(db.Model):
    """
    Represents a user in the application's database.

    Attributes:
        id (int): The unique identifier for the user. Primary key.
        username (str): The unique username for the user. Cannot be null.
        email (str): The unique email address for the user. Cannot be null.
    """
    __tablename__ = "users"

    id: Mapped[int] = mapped_column( primary_key=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
