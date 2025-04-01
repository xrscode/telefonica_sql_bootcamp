from src.utility_functions import query_database


medium_1 = query_database("""
SELECT CategoryName, Description
FROM Categories
ORDER BY CategoryName""")