from pydantic import BaseModel, field_validator
from typing import Optional, List, Literal
from datetime import datetime
from uuid import UUID


TalkContentType = Literal["image", "video", "text"]
TalkType = Literal["main", "subpost", "reply"]


# class TalkCreate(BaseModel):
#     parent_post_id: Optional[UUID] = None
#     content_type: TalkContentType
#     content: Optional[str] = None
#     caption: Optional[str] = None
#     post_type: TalkType
#     file_name: Optional[str] = None
#     file_base64: Optional[str] = None

#     @field_validator("post_type", mode="before")
#     @classmethod
#     def normalize_post_type(cls, v: str) -> str:
#         return v.lower() if isinstance(v, str) else v


class TalkRead(BaseModel):
    post_id: UUID
    username: str
    parent_post_id: Optional[UUID] = None
    content_type: str
    content: Optional[str] = None
    caption: Optional[str] = None
    media_url: Optional[str] = None
    post_type: Optional[str] = None
    posted_date: datetime
    interests: List[str] = []

    model_config = {"from_attributes": True}
