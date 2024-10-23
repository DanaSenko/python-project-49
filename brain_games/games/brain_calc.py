from random import choice

from brain_games.engine import run_game
from brain_games.consts import RULES_CALC, MATH_SIGNES
from brain_games.utils import get_random_for_calc


def generate_math_expression():
    number1, number2 = get_random_for_calc()
    operation = choice(MATH_SIGNES)
    math_expression = f"{number1} {operation} {number2}"
    return math_expression


def get_math_expression_and_answer():
    math_expression = generate_math_expression()
    answer = eval(math_expression)

    return math_expression, answer


def play_game_calc():
    run_game(get_math_expression_and_answer, RULES_CALC)
