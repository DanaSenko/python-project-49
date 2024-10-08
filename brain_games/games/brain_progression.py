from brain_games.cli import welcome_user
from random import randint


def main_game_progression():
    user_name = welcome_user()
    print("What number is missing in the progression?")
    counter = 0

    while counter < 3:
        start = randint(1, 100)
        step = randint(1, 10)
        progression = [start + step * i for i in range(10)]
        closed_number_index = randint(0, 9)
        correct_answer = progression[closed_number_index]
        progression[closed_number_index] = ".."

        print(f"Question: {progression}")
        user_answer = input("Your answer: ").lower()

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
        print(f"Congratulation, {user_name}!")
