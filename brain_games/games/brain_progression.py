import random

from brain_games.utils import get_random_number
from brain_games.consts import (
    RULES_PROGRESSION,
    MIN_PROGRESSION_LENGTH,
    MAX_PROGRESSION_LENGTH,
    HIDDEN_SIMBOL,
)
from brain_games.engine import run_game


def get_progression_and_missed_num():
    start, step = get_random_number(), random.randint(1, 10)
    progr_length = random.randint(MIN_PROGRESSION_LENGTH, MAX_PROGRESSION_LENGTH)

    missed_index = random.randint(0, progr_length - 1)

    progression_with_missed_num = " ".join(
        [
            ".." if i == missed_index else str(start + step * i)
            for i in range(progr_length)
        ]
    )

    missed_num = start + step * missed_index

    return progression_with_missed_num, missed_num


def run_game_progression():
    run_game(get_progression_and_missed_num, RULES_PROGRESSION)
