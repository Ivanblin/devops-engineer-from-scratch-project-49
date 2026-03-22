from brain_games.game_utils import get_random_int

GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number: int) -> bool:
    return number % 2 == 0


def generate_round() -> tuple[int, str]:
    question = get_random_int()
    correct_answer = "yes" if is_even(question) else "no"
    return question, correct_answer
