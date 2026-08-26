from pathlib import Path
from typing import Optional
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form, status
from sqlmodel.ext.asyncio.session import AsyncSession
from app.core.config import MEDIA_POSTS_DIR
from app.core.deps import get_current_user
from app.db.session import get_db
from app.models.talk import Talk
from app.models.user import User
from app.schemas.talk import TalkRead, TalkContentType, TalkType

router = APIRouter(prefix="/new_post", tags=["talks"])

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".webp"}
VIDEO_EXTENSIONS = {".mp4", ".mov", ".webm", ".mkv"}


@router.post("", response_model=TalkRead)
async def create_talk(
    content_type: TalkContentType = Form(...),
    post_type: TalkType = Form(...),
    parent_post_id: Optional[str] = Form(None),  
    content: Optional[str] = Form(None),
    caption: Optional[str] = Form(None),
    mediafile: Optional[UploadFile] = File(None),
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    post_type = post_type.lower()

    if parent_post_id is not None and post_type == "main":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="post_type cannot be 'main' when parent_post_id is given",
        )

    ext = None
    if mediafile and mediafile.filename:
        ext = Path(mediafile.filename).suffix.lower()
        if content_type == "image" and ext not in IMAGE_EXTENSIONS:
            raise HTTPException(status_code=400, detail="Invalid image file type")
        if content_type == "video" and ext not in VIDEO_EXTENSIONS:
            raise HTTPException(status_code=400, detail="Invalid video file type")

    post = Talk(
        user_id=current_user.user_id,
        username=current_user.username,
        parent_post_id=parent_post_id,
        content_type=content_type,
        content=content,
        caption=caption,
        post_type=post_type,
        interests=list(current_user.interests),
    )
    db.add(post)
    await db.flush()

    if mediafile and ext:
        MEDIA_POSTS_DIR.mkdir(parents=True, exist_ok=True)
        stored_name = f"post_{post.post_id}_1{ext}"
        file_bytes = await mediafile.read()
        (MEDIA_POSTS_DIR / stored_name).write_bytes(file_bytes)
        post.media_url = f"media_posts/{stored_name}"

    await db.commit()
    await db.refresh(post)
    return post