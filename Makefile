install:
	uv sync

brain-games:
	uv run brain-games

lint:
	uv run ruff check brain_games

.PHONY: install brain-games lint
