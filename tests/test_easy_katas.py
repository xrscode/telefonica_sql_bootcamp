from katas.easy_katas import *
from src.utility_functions import *

def test_kata_one():
    query = """
    SELECT CategoryName, Description
    FROM dbo.Categories
    ORDER BY CategoryName
    """
    data = query_database(query)
    assert kata_one() == data, f'Expected {kata_one()} but got {data}'


def test_kata_two():
    query = """
    SELECT ContactName, Address, City
    FROM Customers
    WHERE Country NOT IN ('Germany', 'Mexico', 'Spain')
    """
    data = query_database(query)
    assert kata_two() == data, f'Expected {kata_two()} but got {data}'

