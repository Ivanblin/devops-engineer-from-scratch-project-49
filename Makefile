install:
	uv sync

brain-games:
	uv run brain-games

brain-even:
	uv run brain-even

lint:
	uv run ruff check brain_games

.PHONY: install brain-games brain-even lint
