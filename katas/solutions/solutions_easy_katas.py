from src.utility_functions import query_database

solution_1 = query_database("""
SELECT CategoryName, Description
FROM Categories
ORDER BY CategoryName""")

solution_2 = query_database("""
SELECT ContactName, Address, City
FROM Customers
WHERE Country NOT IN ('Germany', 'Mexico', 'Spain')
""")

solution_3 = query_database("""
SELECT OrderDate, ShippedDate, CustomerID, Freight
FROM Orders
WHERE OrderDate = '1996-08-14'  
""")

solution_4 = query_database("""
SELECT EmployeeID, OrderID, CustomerID, RequiredDate, ShippedDate
FROM Orders
WHERE ShippedDate > RequiredDate  
""")

solution_5 = query_database("""
SELECT EmployeeID, OrderID, CustomerID, RequiredDate, ShippedDate
FROM Orders
WHERE ShippedDate > RequiredDate  
""")


solution_6 = query_database("""
SELECT City, CompanyName, ContactName
FROM Customers
WHERE City LIKE '%L%'
ORDER BY ContactName;
""") 


solution_7 = query_database("""
SELECT CompanyName, ContactName, Fax
FROM Customers
WHERE FAX IS NOT NULL
""") 


solution_8 = query_database("""
SELECT TOP (1) FirstName, LastName, HireDate
FROM Employees
ORDER BY HireDate DESC;
""") 


solution_9 = query_database("""
SELECT  ROUND(AVG(UnitPrice), 2) AS average_price
	   ,SUM(UnitsInStock) AS total_stock
	   ,SUM(CAST(Discontinued AS INT)) AS total_discontinued
FROM Products
""") 

