from math import gcd

from brain_games.utils import get_random_number
from brain_games.consts import RULES_GCD
from brain_games.engine import run_game


def get_question_and_answer_gcd():
    number1, number2 = get_random_number(), get_random_number()
    question = f"{number1} {number2}"
    answer = gcd(number1, number2)

    return question, answer


def run_game_gcd():
    run_game(get_question_and_answer_gcd, RULES_GCD)
