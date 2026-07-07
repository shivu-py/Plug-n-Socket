from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class ThoughtBase(BaseModel):
    thought: str
    media_url: Optional[str] = None
    sockets: List[str] = []


class ThoughtCreate(ThoughtBase):
    pass


class ThoughtUpdate(ThoughtBase):
    pass


class Thought(ThoughtBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime
