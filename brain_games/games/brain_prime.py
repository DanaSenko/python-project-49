from brain_games.cli import welcome_user
from random import randint


def is_prime(question):
    if question < 2:
        return False

    for i in range(2, int(question**0.5) + 1):
        if question % i == 0:
            return False
    return True


def main_game_prime():
    user_name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    counter = 0

    while counter < 3:
        question = randint(1, 100)
        print(f"Question: {question}")
        user_answer = input("Your answer: ").lower()

        correct_answer = "yes" if is_prime(question) else "no"

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
        print(f"Congratulations, {user_name}!")
