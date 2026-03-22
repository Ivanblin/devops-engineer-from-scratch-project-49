import prompt

from brain_games.cli import welcome_user
from brain_games.constants import ROUNDS_COUNT


def run_engine(description: str, generate_round) -> None:
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print(description)
    for _ in range(ROUNDS_COUNT):
        question, correct_answer = generate_round()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(
                f"{user_answer} is wrong answer ;(. "
                f"Correct answer was {correct_answer}.\n"
                f"Let's try again, {name}!"
            )
            return
    print(f"Congratulations, {name}!")
