from fastapi import APIRouter
from sqlalchemy import text
from db.session import async_session_maker

router = APIRouter(tags=["health"])

@router.get("/health")
async def health_check():
    try:
        async with async_session_maker() as session:
            await session.execute(text("SELECT 1"))
        return {"status": "ok", "db": "connected"}
    except Exception as e:
        return {"status": "error", "db": f"{e}"}
