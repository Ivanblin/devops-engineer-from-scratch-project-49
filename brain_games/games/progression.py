from brain_games.game_utils import get_random_int

GAME_RULES = "What number is missing in the progression?"
PROGRESSION_LENGTH = 10


def generate_progression(start: int, step: int, hidden_index: int) -> tuple[str, str]:
    numbers = [start + i * step for i in range(PROGRESSION_LENGTH)]
    missing = numbers[hidden_index]
    numbers[hidden_index] = ".."
    question = " ".join(str(n) for n in numbers)
    return question, str(missing)


def generate_round() -> tuple[str, str]:
    start = get_random_int()
    step = get_random_int(2, 10)
    hidden_index = get_random_int(0, PROGRESSION_LENGTH - 1)
    return generate_progression(start, step, hidden_index)
