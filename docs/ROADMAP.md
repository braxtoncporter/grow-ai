# Roadmap — December 2026

Sessions are short (about 45 minutes) and scheduled around exams. Commit at the end of every session.

## M0 — Foundation (by Nov 30)
- [x] Scaffold: FastAPI app, config, DB session, health check, CI
- [ ] First run locally, tests green, pushed to GitHub

## M1 — Data model (Dec 1–7)
- [ ] Models: User, Goal, Habit, HabitLog, CheckIn (with relationships)
- [ ] Alembic set up with first migration
- [ ] Pydantic schemas

## M2 — Core API (Dec 8–14)
- [ ] CRUD endpoints for goals, habits and check-ins
- [ ] Endpoint to log a habit as done
- [ ] API tests using a test database

## M3 — Domain logic (Dec 15–21)
- [ ] Streak service: current and longest streak, handles missed days and timezones
- [ ] Scheduling: which habits are due today (daily, weekdays, N-times-per-week)
- [ ] Unit tests for edge cases

## M4 — LLM pipeline (Dec 22–31)
- [ ] LLM client wrapper with retries and a fake client for tests
- [ ] Check-in processing: mood, themes and linked goals as structured JSON
- [ ] Reflection prompt generation based on recent check-ins and streaks
- [ ] Store outputs and expose them through endpoints

## Later
- Auth (JWT), Postgres/Supabase deployment, Docker, Next.js frontend
