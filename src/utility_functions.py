import pyodbc
import os
from dotenv import load_dotenv

# Ensure override set to true to refresh latest .env variables.
load_dotenv(override=True)

sql_server = os.getenv('server_name')
sql_user = os.getenv('server_user')
sql_password = os.getenv('server_password')
connection_string = os.getenv('connection_string')

def query_database(query):
    """
    
    """
    # Establish connection:
    conn = conn = pyodbc.connect(connection_string, autocommit=True) 
    
    # Create a cursor object:
    cursor = conn.cursor()
    
    # Execute the query:
    cursor.execute(query)

    # Save results to variable:
    data = cursor.fetchall()
    
    # Close the cursor adn connection:
    cursor.close()
    conn.close()

    # Return the data:
    return data