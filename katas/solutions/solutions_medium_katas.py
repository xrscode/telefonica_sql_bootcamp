from src.utility_functions import query_database


medium_1 = query_database("""
SELECT p.ProductName, s.CompanyName, c.CategoryName
FROM Products p
JOIN Categories c ON c.CategoryID = p.CategoryID
JOIN Suppliers s ON s.SupplierID = p.SupplierID""")

medium_2 = query_database("""
SELECT c.CategoryName, ROUND(AVG(p.UnitPrice), 2) AS average_unit_price
FROM Categories c
JOIN Products p ON p.CategoryID = c.CategoryID
GROUP BY c.CategoryName""")

medium_3 = query_database("""
SELECT City, CompanyName, ContactName, 'Customers' AS Relationship
FROM Customers
UNION
SELECT City, CompanyName, ContactName, 'Suppliers' AS Relationship
FROM Suppliers;
""")

medium_4 = query_database("""
SELECT YEAR(OrderDate) AS order_year
       , MONTH(OrderDate) AS order_month
       , COUNT(*) AS no_of_orders
FROM Orders
GROUP BY YEAR(OrderDate), MONTH(OrderDate)
""")
