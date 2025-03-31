from katas.easy_katas import *
from src.utility_functions import *
from katas.solutions.solutions_easy_katas import *

def test_kata_one():
    result = kata_one()
    assert kata_one() == d_one, f'Expected {d_one} but got {result}'


def test_kata_two():
    result = kata_two()
    assert kata_two() == d_two, f'Expected {d_two} but got {result}'

