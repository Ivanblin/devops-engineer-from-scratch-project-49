import random

GAME_RULES = "What is the result of the expression?"


def calculate(num1: int, num2: int, operator: str) -> int:
    if operator == "+":
        return num1 + num2
    if operator == "-":
        return num1 - num2
    if operator == "*":
        return num1 * num2
    msg = f"invalid operator - {operator}"
    raise ValueError(msg)


def generate_round() -> tuple[str, str]:
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    operator = random.choice(["+", "-", "*"])
    question = f"{num1} {operator} {num2}"
    correct_answer = str(calculate(num1, num2, operator))
    return question, correct_answer
