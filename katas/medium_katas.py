from src.utility_functions import query_database

def kata_1():
    """
    Show the ProductName, CompanyName, CategoryName from the products,
    suppliers and categories table.
    """
    

    query = """
    

    """

    result = query_database(query)
    return result




def kata_2():
    """
    Show the CategoryName and the average_unit_price
    for each category rounded to 2 decimal places.
    """
    

    query = """
    

    """

    result = query_database(query)
    return result




def kata_3():
    """
    Show the City, CompanyName, ContactName from the Customers and Suppliers
    table merged together.  Create a column called 'Relationship' which 
    contains 'Customers' or 'Suppliers' depending on which table it came
    from.
    """
    

    query = """
    

    """

    result = query_database(query)
    return result




def kata_4():
    """
    Show the total amount of orders for each year/month.
    """
    

    query = """
    

    """

    result = query_database(query)
    return result