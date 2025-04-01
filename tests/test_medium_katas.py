from katas.medium_katas import *
from src.utility_functions import *
from katas.solutions.solutions_medium_katas import *


# Tests for medium Katas:
def test_kata_1():
    result = kata_1()
    assert kata_1() == medium_1, f'Expected {medium_1} but got {result}'