from brain_games.utils import get_random_for_progression
from brain_games.consts import RULES_PROGRESSION
from brain_games.engine import play_game


def get_question_and_answer_progression():
    start, step, closed_number_index = get_random_for_progression()
    progression = [str(start + step * i) for i in range(10)]
    correct_answer = int(progression[closed_number_index])
    progression[closed_number_index] = ".."
    question = " ".join(progression)

    return question, correct_answer


def play_game_progression():
    play_game(get_question_and_answer_progression, RULES_PROGRESSION)
