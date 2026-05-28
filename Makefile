.PHONY: sync dev test lint format typecheck

sync:
	uv sync

dev:
	uv run python echo.py

test:
	uv run pytest

lint:
	uv run ruff check .

format:
	uv run ruff format .

typecheck:
	uv run pyright

