from backend.app.main import app
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings

def setup_cors(app):
    origins = [
        "http://localhost:5173",
        "http://localhost:3000",
    ]

    if settings.environment == "production":
        origins = [settings.frontend_url]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
