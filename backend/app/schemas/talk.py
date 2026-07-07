from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class TalkBase(BaseModel):
    user_id: int
    subject: str
    media_url: Optional[str] = None
    sockets: List[str] = []


class TalkCreate(TalkBase):
    pass


class TalkUpdate(TalkBase):
    pass


class Talk(TalkBase):
    id: int
    created_at: datetime
    updated_at: datetime