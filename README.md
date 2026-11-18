# Grow.AI

A personal growth OS that turns goals, habits and daily reflections into an adaptive, AI driven plan.

## Overview

Most goal and habit apps are passive trackers. You log things, and the app shows you charts. Grow.AI is built around a feedback loop instead:

1. You set a small number of meaningful goals in a focus area (Health, Career, Mind, Money).
2. You attach daily habits to those goals and track them as streaks.
3. You write a short daily check in, guided by an AI generated reflection question.
4. An LLM pipeline reads your check ins and habit history, picks up patterns, and adjusts the next questions and suggestions to where you actually are.

This repository is the backend: a FastAPI service with a relational data model, the domain logic for streaks and scheduling, and the LLM pipeline. The mobile frontend is being designed in Figma and will be built in Next.js / React against this API.

## Tech stack

* **Python 3.12**, **FastAPI**, **Pydantic v2** with pydantic settings for configuration
* **SQLAlchemy 2.0** (typed `Mapped` models) with **Alembic** for migrations
* **SQLite** for local development, **PostgreSQL** planned for production
* **Anthropic API** for reflection prompts and check in analysis
* **pytest** for tests, **ruff** for linting, **GitHub Actions** for CI
* **uv** for dependency management and reproducible installs (`uv.lock`)

## Project structure

```
src/growai/
  main.py         App factory and router registration
  core/config.py  Typed settings loaded from environment / .env
  db/session.py   Engine, session factory, declarative Base, FastAPI DB dependency
  models/         SQLAlchemy models (User, Goal so far)
  schemas/        Pydantic request and response models
  api/routes/     HTTP endpoints (health check so far)
  services/       Domain logic: streaks, habit scheduling
  llm/            Prompt templates and the LLM pipeline
tests/            pytest suite
docs/ROADMAP.md   Milestones and progress
```

Design choices worth noting:

* **Layered structure.** Routes stay thin. Business rules (streaks, scheduling) live in `services/` so they can be unit tested without HTTP or a database.
* **Timezone aware from the start.** Each user stores a timezone, because "did you do it today" and streak boundaries depend on when the user's day ends, not on server time.
* **LLM behind an interface.** The pipeline will sit behind a small client wrapper, so tests can run against a fake client with no API calls or cost.

## Data model

| Model | Purpose | Key fields |
|---|---|---|
| `User` | Account and preferences | `email` (unique), `display_name`, `timezone`, `created_at` |
| `Goal` | A meaningful outcome a user works toward | `user_id` → users, `title`, `focus_area`, `description`, `target_date`, `status` |

Planned next: `Habit`, `HabitLog` (one row per completion, the source of truth for streaks) and `CheckIn` (daily reflection text, mood, and the AI prompt it answered).

## Getting started

Requirements: Python 3.12+ and [uv](https://docs.astral.sh/uv/).

```bash
git clone https://github.com/braxtoncporter/grow-ai.git
cd grow-ai
uv sync                      # install dependencies from uv.lock
cp .env.example .env         # local configuration
uv run uvicorn growai.main:app --reload
```

The API runs at http://localhost:8000 and interactive docs at http://localhost:8000/docs.

Run the checks that CI runs:

```bash
uv run ruff check .
uv run pytest
```

## Configuration

Settings are read from environment variables with the `GROWAI_` prefix (see `.env.example`):

| Variable | Default | Purpose |
|---|---|---|
| `GROWAI_DATABASE_URL` | `sqlite:///./growai.db` | Database connection |
| `GROWAI_DEBUG` | `false` | FastAPI debug mode |
| `GROWAI_ANTHROPIC_API_KEY` | none | Key for the LLM pipeline |

## Status

Early, active development (started November 2026).

**Working now:** app skeleton and settings, database session layer, health endpoint with a passing test, CI on every push, `User` and `Goal` models.

## Roadmap

Full detail in [docs/ROADMAP.md](docs/ROADMAP.md).

1. **Data model.** Habit, HabitLog and CheckIn models, relationships, first Alembic migration.
2. **Core API.** Endpoints for goals, habits, habit completions and check ins, with tests against a test database.
3. **Domain logic.** Streak calculation (current and longest, missed days, user timezones) and scheduling for daily, weekday and "N times per week" habits.
4. **LLM pipeline.** Check in analysis into structured output (mood, themes, linked goals) and reflection prompts generated from recent check ins and streaks.
5. **Later.** Authentication, PostgreSQL deployment, Docker, and the Next.js frontend.

## How this is built

I build this in the terminal with an AI coding assistant. I design the features, write and review the code, run the tests and make every commit myself.
