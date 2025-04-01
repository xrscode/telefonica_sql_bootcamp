from src.utility_functions import query_database

def kata_1():
    """
    Write a query that shows the CategoryName and Description
    from the dbo.Categories table.  Sort by CateogryName."""
    

    query = """
    SELECT CategoryName, Description
    FROM Categories
    ORDER BY CategoryName
    """

    result = query_database(query)
    return result