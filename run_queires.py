import sqlite3 
# Connect to the database
conn = sqlite3.connect("grocery_store.db")
cursor = conn.cursor()
# List of queries to run 
queires =[
    "SELECT * FROM Customers;",
    "SELECT * FROM  Products;",
    "SELECT * FROM Orders WHERE TotalAmount> 6;",
    "SELECT Name, Category, Price * FROM Products WHERE Stock > 50;" 
    "SELECT * FROM Suppliers;",
    """
    "SELECT C.Name AS Customer, O.OrderDate, O.TotalAmount
    FROM Customers C 
    INNER JOIN Orders O ON C.CustomerID = O.CustomerID
    WHERE O.TotalAmount > 5;
    """
]



