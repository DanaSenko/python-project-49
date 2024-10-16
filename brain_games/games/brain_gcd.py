from brain_games.utils import get_random_for_gcd
from brain_games.consts import RULES_GCD
from brain_games.engine import play_game
from math import gcd


def get_question_and_answer_gcd():
    number1, number2 = get_random_for_gcd()
    question = f"{number1} {number2}"
    answer = gcd(number1, number2)

    return question, answer


def play_game_gcd():
    play_game(get_question_and_answer_gcd, RULES_GCD)
