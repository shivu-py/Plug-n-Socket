from contextlib import asynccontextmanager

from fastapi import FastAPI
from middleware.cors import setup_cors
from routes.health import router as health_router
from sqlalchemy import text

from core.config import settings
from db.session import engine

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.connect() as conn:
        try:
            await conn.execute(text("SELECT 1"))
            print(f"[{settings.environment}] DB connection verified. App starting up...")
        except Exception as e:
            print(f"DB connection error: {e}")

        yield

        await engine.dispose()
        print("engine disposed app shutting down.")


app = FastAPI(
    title="Dogmatic Judge API",
    version="0.1.0",
    lifespan=lifespan,
    docs_url="/docs" if settings.environment == "development" else None,
    redoc_url="/redoc" if settings.environment == "development" else None,
)

setup_cors(app)
app.include_router(health_router,prefix="/api")
