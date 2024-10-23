from brain_games.utils import get_random_for_even
from brain_games.consts import RULES_EVEN
from brain_games.engine import run_game


def is_even(question):
    return question % 2 == 0


def get_num_and_even_answer():
    question = get_random_for_even()
    correct_answer = "yes" if is_even(question) else "no"

    return question, correct_answer


def run_game_even():
    run_game(get_num_and_even_answer, RULES_EVEN)
