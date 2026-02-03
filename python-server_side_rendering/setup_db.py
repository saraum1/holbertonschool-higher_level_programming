import sqlite3
conn = sqlite3.connect('products.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS Products (id INTEGER PRIMARY KEY, name TEXT, category TEXT, price REAL)')
cursor.execute('INSERT OR REPLACE INTO Products VALUES (1, "Laptop", "Electronics", 799.99)')
cursor.execute('INSERT OR REPLACE INTO Products VALUES (2, "Coffee Mug", "Home Goods", 15.99)')
conn.commit()
conn.close()
