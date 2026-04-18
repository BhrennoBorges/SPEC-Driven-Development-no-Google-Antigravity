import enum
from datetime import datetime
from app import db
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, Integer, Text, Enum, ForeignKey, DateTime
from typing import Optional

class TaskStatus(enum.Enum):
    PENDING = 'pendente'
    IN_PROGRESS = 'em_progresso'
    COMPLETED = 'concluído'

class Task(db.Model):
    """
    Representa uma tarefa (todo) criada por um usuário.
    """
    __tablename__ = 'tasks'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(128), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text)
    status: Mapped[TaskStatus] = mapped_column(Enum(TaskStatus), default=TaskStatus.PENDING, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)
    
    # Referência reversa para User
    author = relationship("User", back_populates="tasks")

    def __repr__(self):
        return f'<Task {self.title}>'
