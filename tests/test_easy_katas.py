import pytest
from katas.easy_katas import *
from src.utility_functions import *

def test_kata_two():
    expected_output = [('Beverages', 'Soft drinks, coffees, teas, beers, and ales'), ('Condiments', 'Sweet and savory sauces, relishes, spreads, and seasonings'), ('Confections', 'Desserts, candies, and sweet breads'), ('Dairy Products', 'Cheeses'), ('Grains/Cereals', 'Breads, crackers, pasta, and cereal'), ('Meat/Poultry', 'Prepared meats'), ('Produce', 'Dried fruit and bean curd'), ('Seafood', 'Seaweed and fish')]
    actual_output   = kata_one()

    for i, x in enumerate(actual_output  ):
        assert expected_output[i] == actual_output[i], f"Expected {expected_output[i]} but got {actual_output  [i]}"
    
    ('Beverages', 'Soft drinks, coffees, teas, beers, and ales')
    ('Beverages', 'Soft drinks, coffees, teas, beers, and ales')