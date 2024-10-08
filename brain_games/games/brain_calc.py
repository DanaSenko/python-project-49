from brain_games.cli import welcome_user
from random import randint, choice


def main_game_calc():
    user_name = welcome_user()
    print("What is the result of the expression?")
    counter = 0

    while counter < 3:
        number1 = randint(1, 10)
        number2 = randint(1, 10)
        operations = ["+", "-", "*"]
        operation = choice(operations)
        print(f"Question: {number1} {operation} {number2}")
        user_answer = input("Your answer: ").lower()

        if operation == "+":
            correct_answer = number1 + number2
        elif operation == "-":
            correct_answer = number1 - number2
        else:
            correct_answer = number1 * number2

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
