from brain_games.cli import welcome_user
from random import randint


def main_game_even():
    user_name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter = 0

    while counter < 3:
        question = randint(1, 1000)
        print(f"Question: {question}")
        user_answer = input("Your answer: ").lower()

        if question % 2 == 0:
            correct_answer = "yes"
        else:
            correct_answer = "no"

        if user_answer == correct_answer:
            print("Correct!")
            counter += 1
        else:
            print(
                f"'{user_answer}' is the wrong answer ;(. "
                f"The correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {user_name}!")
            break
    if counter == 3:
        print(f"Congratulation, {user_name}!")
