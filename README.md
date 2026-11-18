# Grow.AI — backend

Grow.AI is an AI-powered personal growth OS. Users set goals, track habits and write daily check-ins.
An LLM pipeline turns those check-ins into reflection prompts and insights.

This repo is the backend: a FastAPI service with a relational data model, streak and scheduling
logic, and an LLM pipeline. The frontend is being designed in Figma and will be built in Next.js later.

> Status: early development (December 2026). See [docs/ROADMAP.md](docs/ROADMAP.md).

## Stack

- **Python 3.12+**, **FastAPI**, **Pydantic v2**
- **SQLAlchemy 2.0** + **Alembic** (SQLite locally, Postgres in production)
- **Anthropic API** for reflection prompts and check-in analysis
- **pytest**, **ruff**, GitHub Actions CI, **uv** for dependencies

## Getting started

```bash
uv sync                       # install dependencies
cp .env.example .env          # configure
uv run uvicorn growai.main:app --reload
uv run pytest                 # run tests
```

API docs are served at http://localhost:8000/docs.

## Project layout

```
src/growai/
  api/routes/   HTTP endpoints
  core/         settings and shared config
  db/           engine, sessions, ORM base
  models/       SQLAlchemy models
  schemas/      Pydantic request/response models
  services/     domain logic (streaks, scheduling)
  llm/          prompt templates and LLM pipeline
tests/
```

## Built with AI assistance

This project is built in the terminal with an AI coding assistant. I design, review, test and
commit every change myself.
