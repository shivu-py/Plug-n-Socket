from sqlmodel import SQLModel, Field, Relationship, Column, JSON
from datetime import datetime
from typing import Optional, List, TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User


class Talk(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    subject: str = Field(index=True)
    talk: str = Field()
    media_url: Optional[str] = None
    pns: List[str] = Field(default=[], sa_column=Column(JSON))
    created_at: datetime = Field(default=datetime.utcnow())
    updated_at: datetime = Field(default=datetime.utcnow())

    user: Optional["User"] = Relationship(back_populates="talks")
