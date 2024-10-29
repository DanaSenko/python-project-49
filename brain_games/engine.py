import prompt
from brain_games.consts import GAME_ROUNDS


def parse_user_input(user_answer):
    """Преобразует ввод пользователя к числу.
    Если ошибка т.е 'yes' or 'no'
    -> возвращает неизмененный ввод"""

    try:
        return int(user_answer)
    except ValueError:
        return user_answer


def run_game(get_question_and_answer, instruction):
    user_name = prompt.string(
        "Welcome to the Brain Games!\nMay I have your name? "
    )
    print(f"Hello, {user_name}!\n{instruction}")

    for _ in range(GAME_ROUNDS):
        question, correct_answer = get_question_and_answer()
        print(f"Question: {question}")
        user_answer = parse_user_input(prompt.string("Your answer: "))

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
