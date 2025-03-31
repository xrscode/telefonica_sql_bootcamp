import pyodbc
import os
from dotenv import load_dotenv
import re

load_dotenv()

sql_server = os.getenv('server_name')
sql_user = os.getenv('server_user')
sql_password = os.getenv('server_password')
connection_string = os.getenv('connection_string')

def read_sql_script(path):
    """
    Args: 
        path (str): Path to the SQL script file.
    Returns:
        str: The content of the SQL script.
    Raises:
        FileNotFoundError: If the file does not exist.
        IOError: If there is an error reading the file.
    
    Description:
    Reads the SQL script from the specified file path.
    """
    
    # Check if the file exists and is readable
    if not os.path.isfile(path):
        raise FileNotFoundError(f"File not found: {path}")

    with open(path, 'r') as sql:
        sql_script = sql.read()

    return sql_script

# Set location for instnwnd:
instwnd = './src/instnwnd.sql'

# Save sql script to variable:
sql_script = read_sql_script(instwnd)

# Query database with pydobc:
def query_database(query, connection_string):
    """
    
    """
    # Establish connection:
    conn = conn = pyodbc.connect(connection_string, autocommit=True) 
    
    # Create a cursor object:
    cursor = conn.cursor()

    print('Executing query: ', query)
    
    cursor.execute(query)

    data = cursor.fetchall()

    # Close the cursor and connection:
    cursor.close()
    conn.close()
    
    return data



parts = re.split(r"(?i)\bGO\b", sql_script)

for part in parts:
    query_database(part, connection_string)

