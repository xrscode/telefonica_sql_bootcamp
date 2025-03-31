from src.utility_functions import query_database

def kata_one():
    """
    Write a query that shows the CategoryName and Description
    from the dbo.Categories table.  Sort by CateogryName."""
    

    query = """
    SELECT CategoryName, Description
    FROM dbo.Categories
    ORDER BY CategoryName
    """
    data = query_database(query)
    return data




def kata_two():
    """
    Show the ConcatctName, Address, City Which are not from 'Germany', 'Mexico',
    'Spain'.
    """

    query = """
    SELECT ContactName, Address, City
    FROM Customers
    WHERE Country NOT IN ('Germany', 'Mexico', 'Spain')
    """
    data = query_database(query)
    return data

def kata_three():
    

