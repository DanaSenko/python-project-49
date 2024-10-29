from brain_games.utils import get_random_number
from brain_games.consts import RULES_PRIME
from brain_games.engine import run_game


def is_prime(question):
    if question < 2:
        return False

    for i in range(2, int(question**0.5) + 1):
        if question % i == 0:
            return False
    return True


def get_question_and_answer_prime():
    question = get_random_number()
    answer = "yes" if is_prime(question) else "no"

    return question, answer


def run_game_prime():
    run_game(get_question_and_answer_prime, RULES_PRIME)
