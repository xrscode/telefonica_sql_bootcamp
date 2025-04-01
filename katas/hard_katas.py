from src.utility_functions import query_database

def kata_1():
    """
    Show the employee's FirstName and LastName, a 'num_orders' column with a 
    count of the orders taken, and a column called 'shipped' that displays; 
    'On Time' if the order ShippedDate is less or equal to the RequiredDate,
    'Late' if the order ShippedDate is greater than the RequiredDate,
    'Not Shipped' if the order ShippedDate is NULL.
    """
    

    query = """
    

    """

    result = query_database(query)
    return result