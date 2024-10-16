from random import randint


def get_random_for_calc():
    number1, number2 = randint(1, 10), randint(1, 10)
    return number1, number2


def get_random_for_even():
    question = randint(1, 1000)
    return question


def get_random_for_gcd():
    number1, number2 = randint(1, 10), randint(1, 10)
    return number1, number2


def get_random_for_prime():
    question = randint(1, 100)
    return question


def get_random_for_progression():
    start, step, closed_number_index = randint(1, 100), randint(1, 10), randint(0, 9)
    return start, step, closed_number_index
