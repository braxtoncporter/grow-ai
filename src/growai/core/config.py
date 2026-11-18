"""Application settings, loaded from environment variables or a local .env file."""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_prefix="GROWAI_", extra="ignore")

    app_name: str = "Grow.AI"
    environment: str = "development"
    debug: bool = False

    # SQLite for local dev; swap for a Postgres URL in production.
    database_url: str = "sqlite:///./growai.db"

    # LLM pipeline (wired up in a later milestone).
    anthropic_api_key: str | None = None
    llm_model: str = "claude-sonnet-4-5"


@lru_cache
def get_settings() -> Settings:
    return Settings()
