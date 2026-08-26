import uuid
from uuid import UUID
from sqlmodel import SQLModel, Field, Relationship, Column, JSON
from datetime import datetime
from typing import Optional, List, TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User


class Talk(SQLModel, table=True):
    post_id: str = Field(default_factory=lambda: uuid.uuid4().hex, primary_key=True)
    user_id: UUID = Field(foreign_key="user.user_id", index=True)
    username: str = Field(index=True)
    parent_post_id: Optional[str] = Field(default=None, foreign_key="talk.post_id", index=True)
    content_type: str = Field(index=True)
    content: Optional[str] = None
    caption: Optional[str] = None
    media_url: Optional[str] = None
    post_type: Optional[str] = Field(default=None, index=True)
    posted_date: datetime = Field(default_factory=datetime.utcnow)
    interests: List[str] = Field(default=[], sa_column=Column(JSON))

    user: Optional["User"] = Relationship(back_populates="talks")
