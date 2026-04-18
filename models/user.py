from flask_login import UserMixin
from typing import List
from app import db
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, Integer

class User(UserMixin, db.Model):
    """
    Representa um usuário no sistema.
    """
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(64), unique=True, index=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(256), nullable=False)

    # Relacionamento 1-N com Task
    tasks: Mapped[List["Task"]] = relationship("Task", back_populates="author", cascade="all, delete-orphan")

    def __repr__(self):
        return f'<User {self.username}>'
