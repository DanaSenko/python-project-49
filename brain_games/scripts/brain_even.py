import prompt
from random import randint


def greet():
    global user_name
    print("Welcome to the Brain Games!")
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')


def rules_even():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def main_game_even():
    counter = 0

    while counter < 3:
        question = randint(1, 1000)
        print(f'Question: {question}')
        user_answer = input('Your answer: ').lower()

        if question % 2 == 0:
            correct_answer = "yes"
        else:
            correct_answer = 'no'

        if user_answer == correct_answer:
            print('Correct!')
            counter += 1
        else:
            print(f"'{user_answer}' is the wrong answer ;(. "
            f"The correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            break
    if counter == 3:
        print(f'Congratulation, {user_name}!')


def main():
    greet()
    rules_even()
    main_game_even()


# if __name__ == "__main__":  
#     main()
