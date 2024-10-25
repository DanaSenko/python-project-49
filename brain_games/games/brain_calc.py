import random

from brain_games.engine import run_game
from brain_games.consts import RULES_CALC
from brain_games.utils import get_random_number


def get_random_math_sign_and_result(number1, number2):
    operations = {
        "+": number1 + number2,
        "-": number1 - number2,
        "*": number1 * number2,
    }
    sign = random.choice(list(operations.keys()))
    result = operations[sign]

    return sign, result


def get_math_expression_and_answer():
    number1, number2 = get_random_number(), get_random_number()
    sign, answer = get_random_math_sign_and_result(number1, number2)
    math_expression = f"{number1} {sign} {number2}"

    return math_expression, answer


def play_game_calc():
    run_game(get_math_expression_and_answer, RULES_CALC)
