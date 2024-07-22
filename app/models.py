from sqlalchemy import Integer, String
from sqlalchemy.orm import  mapped_column, Mapped
from app import db

class User(db.Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column( primary_key=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
