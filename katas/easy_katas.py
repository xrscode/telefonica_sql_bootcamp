from src.utility_functions import query_database

"""
Connect to SSMS to examine the tables and data.
The first kata has been completed for you. 
Type the query and uncomment the corresponding test in the test file to test 
your solution.

Remember that you will need to deploy the project first!

If the tests are not running due to 'module not found' errors, try setting the
python path with this command entered into the terminal:

$env:PYTHONPATH = "$PWD"
"""

def kata_1():
    """
    Write a query that shows the CategoryName and Description
    from the Categories table.  Sort by CateogryName."""
    

    query = """
    SELECT CategoryName, Description
    FROM Categories
    ORDER BY CategoryName
    """

    result = query_database(query)
    return result





def kata_2():
    """
    From the customers table; show the ConcatctName, Address, City Which are 
    not from 'Germany', 'Mexico' or 'Spain'.
    """

    # Write query here:
    query = """
    
    """

    result = query_database(query)
    return result




def kata_3():
    """
    From the Orders table; show the OrderDate, ShippedDate, CustomerID and
    Freight for all orders placed on the 14th of August 1996.
    """   

    # Write query here:
    query = """
      
    """
    result = query_database(query)
    return result




def kata_4():
    """
    Show the EmployeeID, OrderID, CustomerID, RequiredDate, ShippedDate
    From the Orders table.  Only show the orders where the order arrived
    after it was required!
    """   

    # Write query here:
    query = """
    
    """
    result = query_database(query)
    return result




def kata_5():
    """
    Show only even numbered OrderID's from the Orders table.
    """   

    # Write query here:
    query = """
     
    """
    result = query_database(query)
    return result




def kata_6():
    """
    Show the City, CompanyName, ContactName From the Customers table. 
    Only display cities that contain the letter 'L'.
    Sort by alphabetically by ContactName.
    """   

    # Write query here:
    query = """
    
    """
    result = query_database(query)
    return result




def kata_7():
    """
    Show the CompanyName, ContactName, FaxNumber for all customers
    that have a fax number.
    """   

    # Write query here:
    query = """
    
    """
    result = query_database(query)
    return result




def kata_8():
    """
    Show the FirstName, LastName, HireDate of the most recently hired employee.
    """   

    # Write query here:
    query = """
    
    """
    result = query_database(query)
    return result




def kata_9():
    """
    Show the averate unit price rounded to 2 decimal places,
    the total units in stock, total discontinued products form the products
    table.

    HINT: The Discontinued table are of type BIT.  Look at trying to CAST to a
    useful data type!
    """   

    # Write query here:
    query = """

    """
    result = query_database(query)
    return result

