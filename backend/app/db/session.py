from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel.ext.asyncio import create_async_engine, async_sessionmaker
from core.config import settings

engine = create_async_engine(
    settings.database_url,
    echo=settings.environment=="development",
    pool_size=5,
    max_overflow=10,
    pool_pre_ping=True,
)
async_session_maker = async_sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

async def get_db():
    async with async_session_maker() as session:
        yield session