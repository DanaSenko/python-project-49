from brain_games.utils import get_random_for_calc
from brain_games.consts import RULES_CALC, MATH_SIGNES
from random import choice
from brain_games.engine import play_game


def get_math_expression_and_answer():
    number1, number2 = get_random_for_calc()
    operation = choice(MATH_SIGNES)
    math_expression = f"{number1} {operation} {number2}"
    answer = eval(math_expression)

    return math_expression, answer


def play_game_calc():
    play_game(get_math_expression_and_answer, RULES_CALC)
