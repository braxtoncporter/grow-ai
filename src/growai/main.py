"""FastAPI application entrypoint. Run with: uv run uvicorn growai.main:app --reload"""

from fastapi import FastAPI

from growai.api.routes import health
from growai.core.config import get_settings


def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(title=settings.app_name, debug=settings.debug)
    app.include_router(health.router)
    return app


app = create_app()
