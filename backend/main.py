from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlalchemy import text
from sqlmodel import SQLModel

from app.core.config import settings
from app.db.session import engine
from app.middleware.cors import setup_cors
from app.routes.auth import router as auth_router
from app.routes.health import router as health_router
    
@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        async with engine.begin() as conn:
            await conn.execute(text("SELECT 1"))
            await conn.run_sync(SQLModel.metadata.create_all)
    except Exception as e:
        print(f"DB connection error: {e}")

    yield
    await engine.dispose()
    print("engine disposed app shutting down.")

app = FastAPI(
    title="Plug-n-Socket API",
    version="0.1.0",
    lifespan=lifespan,
    docs_url="/docs" if settings.environment == "development" else None,
    redoc_url="/redoc" if settings.environment == "development" else None,
)

setup_cors(app)
app.include_router(health_router, prefix="/api")
app.include_router(auth_router, prefix="/api")
