from katas.medium_katas import *
from src.utility_functions import *
from katas.solutions.solutions_hard_katas import *


# Tests for hard Katas:
def test_kata_1():
    result = kata_1()
    assert kata_1() == hard_1, f'Expected {hard_1} but got {result}'