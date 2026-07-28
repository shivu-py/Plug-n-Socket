from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class TalkBase(BaseModel):
    user_id: int
    subject: str
    media_url: Optional[str] = None
    pulg_n_socket: List[str] = []
    lables: List[str] = []


class TalkCreate(TalkBase):
    subject: str
    media_url: Optional[str]
    pulg_n_socket: List[str] = []
    lables: List[str] = []

class TalkUpdate(TalkBase):
    pass


class Talk(TalkBase):
    id: int
    created_at: datetime
    updated_at: datetime