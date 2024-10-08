from brain_games.cli import welcome_user
from math import gcd
from random import randint


def main_game_gcd():
    user_name = welcome_user()
    print("Find the greatest common divisor of given numbers.")
    counter = 0

    while counter < 3:
        number1 = randint(1, 10)
        number2 = randint(1, 10)
        print(f"Question: {number1} {number2} ")
        user_answer = input("Your answer: ").lower()

        correct_answer = gcd(number1, number2)

        if int(user_answer) == correct_answer:
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
            print(f"Congratulations, {user_name}!")
