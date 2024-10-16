import prompt
from brain_games.consts import GAME_ROUNDS


def parse_user_input(user_answer):

    ''' Преобразует ввод пользователя к числу.
    Если ошибка т.е 'yes' or 'no'
    -> возвращает неизмененный ввод '''

    try:
        return int(user_answer)
    except ValueError:
        return user_answer


def play_game(get_question_and_answer, instruction):
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}!\n" f"{instruction}")

    for _ in range(GAME_ROUNDS):
        question, correct_answer = get_question_and_answer()
        user_answer = prompt.string(f"Question: {question}\n" f"Your answer: ")
        user_answer = parse_user_input(user_answer)

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(
                f"'{user_answer}' is the wrong answer ;(. "
                f"The correct answer was '{correct_answer}'."
                f"Let's try again, {user_name}!"
            )
            return

    print(f"Congratulations, {user_name}!")
