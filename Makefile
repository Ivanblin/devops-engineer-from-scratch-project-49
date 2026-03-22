install:
	uv sync

brain-games:
	uv run brain-games

brain-even:
	uv run brain-even

brain-calc:
	uv run brain-calc

brain-gcd:
	uv run brain-gcd

brain-progression:
	uv run brain-progression

brain-prime:
	uv run brain-prime

lint:
	uv run ruff check brain_games

build:
	uv build

publish:
	uv build && uv publish --dry-run

.PHONY: install brain-games brain-even brain-calc brain-gcd brain-progression brain-prime lint build publish
