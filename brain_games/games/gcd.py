import random

GAME_RULES = "Find the greatest common divisor of given numbers."


def get_gcd(num1: int, num2: int) -> int:
    if num1 == 0:
        return num2
    return get_gcd(num2 % num1, num1)


def generate_round() -> tuple[str, str]:
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    question = f"{num1} {num2}"
    correct_answer = str(get_gcd(num1, num2))
    return question, correct_answer
