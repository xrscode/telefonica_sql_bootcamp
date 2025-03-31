from src.utility_functions import query_database

d_one = query_database("""SELECT CategoryName, Description
                       FROM dbo.Categories
                       ORDER BY CategoryName""")

d_two = query_database("""
    SELECT ContactName, Address, City
    FROM Customers
    WHERE Country NOT IN ('Germany', 'Mexico', 'Spain')
    """)