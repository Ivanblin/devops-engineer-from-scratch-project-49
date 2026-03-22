import math

from brain_games.game_utils import get_random_int

GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def generate_round() -> tuple[int, str]:
    question = get_random_int(2, 100)
    correct_answer = "yes" if is_prime(question) else "no"
    return question, correct_answer
