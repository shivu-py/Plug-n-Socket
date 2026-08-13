from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .talk import Talk
    from .user import User

class Response(SQLModel,table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    content: str = Field()
    talk_id: int = Field(foreign_key="talk.id")
    user_id: int = Field(foreign_key="user.id")
    created_at: datetime = Field(default=datetime.utcnow())
    updated_at: datetime = Field(default=datetime.utcnow())

    user: Optional["User"] = Relationship(back_populates="responses")
    talk: Optional["Talk"] = Relationship(back_populates="responses")