import sqlite3

# Connect to SQlite database
conn = sqlite3.connect("grocery_store.db")
cursor = conn.cursor()

#Populate Suppliers
suppliers =[
("Fresh Farms","123-456-7890")
("Dairy World","234-567-8901")
("Grain Suppliers","345-678-9012")
("Bakery Suppliers","456-789-0123")
]
cursor.executemany("""
INSERT INTO Suppliers(SupplierName, ContactIfo) VALUES(?,?)                   
 """,suppliers)

 # Populate Products
products =[
    ("Apple,""Fruits",0.5,100,1),
    ("Banana","Fruits",0.2,150,1),
    ("Milk","Dairy",1.5,50,2),
    ("Bread","Bakery",2.0,30,4),
    ("Eggs","Dairy",3.0,20,2)
 ]
cursor.executemany("""
INSERT INTO Products(ProductName,Category,Price, StockQuanity,SupplierID) VALUES(?,?,?,?,?)                    
""",products)

    #Populate Customers
customers= [
("John","Doe","johndoe@example.com",50),
("James","Smith","jamesmith@example.com",100),
("Alice","Johnson","alicejohnson@example.com",200)

]
cursor.executemany("""
INSERT INTO Customers (FirstName,LastName,Email,LoyaltyPoints) VALUE(?,?,?,?)
""",customers)