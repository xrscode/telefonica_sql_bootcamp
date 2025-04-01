from src.utility_functions import query_database


hard_1 = query_database("""SELECT e.FirstName
, e.LastName
, COUNT(o.OrderID) AS num_orders
,(
CASE
	WHEN o.ShippedDate <= o.RequiredDate THEN 'On Time'
	WHEN o.ShippedDate > o.RequiredDate THEN 'Late'
	WHEN o.ShippedDate IS NULL THEN 'Not Shipped'
END 
) AS shipped
FROM Orders o
JOIN Employees e ON e.EmployeeID = o.EmployeeID
GROUP BY 
	e.FirstName
,   e.LastName
,   CASE
	WHEN o.ShippedDate <= o.RequiredDate THEN 'On Time'
	WHEN o.ShippedDate > o.RequiredDate THEN 'Late'
	WHEN o.ShippedDate IS NULL THEN 'Not Shipped'
END
ORDER BY 
	e.LastName,
	e.FirstName,
	num_orders DESC;""")


