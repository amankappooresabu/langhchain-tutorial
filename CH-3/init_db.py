import sqlite3
import os
import sys

conn = sqlite3.connect("SalesDB/sales.db")

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT NOT NULL,
    product_name TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    price REAL NOT NULL,
    total REAL NOT NULL
    )
""")

cursor.execute("""
INSERT INTO orders (customer_name, product_name, quantity, price, total) VALUES
('Alice', 'Laptop', 2, 10.0, 20.0),
('Bob', 'SmartPhone', 1, 15.0, 15.0),
('Charlie', 'Tablet', 3, 10.0, 30.0),
('Dave', 'Laptop', 1, 20.0, 20.0)
""")

conn.commit()
conn.close()

