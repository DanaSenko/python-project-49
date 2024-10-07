from brain_games.cli import welcome_user
from random import randint


def main_game_prime():
    user_name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    counter = 0

    while counter < 3:
        question = randint(1, 100)
        print(f"Question: {question}")
        user_answer = input("Your answer: ").lower()
        num_of_divisions = 0

        for i in range(1, question + 1):
            if question % i == 0:
                num_of_divisions += 1

        if num_of_divisions == 2:
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


def main():
    main_game_prime()


if __name__ == "__main__":
    main()
