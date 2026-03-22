#!/usr/bin/env python3

from brain_games.engine import run_engine
from brain_games.games.gcd import GAME_RULES, generate_round


def main() -> None:
    run_engine(GAME_RULES, generate_round)


if __name__ == "__main__":
    main()
