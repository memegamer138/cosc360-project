import sqlite3
import os

class projectDB:
    def __init__(self, db_path = 'projectDB.db'):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        # Create the Products table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Products (
                productID INTEGER PRIMARY KEY AUTOINCREMENT,
                imagePath VARCHAR(255) NOT NULL,
                productName TEXT NOT NULL,
                productDesc TEXT NOT NULL,
                categoryID TEXT NOT NULL,
                stock INTEGER,
                price INTEGER,
                FOREIGN KEY (categoryID) REFERENCES Categories(categoryID) ON DELETE SET NULL
                     
            )
        """)
        # Create the User table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS User (
                userEmail TEXT NOT NULL UNIQUE PRIMARY KEY,
                userPassword VARCHAR(255) NOT NULL
            )
        """)
        # Create the admin table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Admin (
                adminEmail TEXT NOT NULL UNIQUE PRIMARY KEY,
                adminPassword VARCHAR(255) NOT NULL
            )
        """)
        # Create the Categories table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Categories (
                categoryID INTEGER PRIMARY KEY AUTOINCREMENT,
                categoryName TEXT NOT NULL,
                description TEXT
            )
        """)
        # Create the Orders table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Orders (
                orderID INTEGER PRIMARY KEY AUTOINCREMENT,
                userEmail TEXT NOT NULL,
                createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                status TEXT NOT NULL CHECK(status IN ('pending', 'shipped', 'delivered', 'cancelled')) DEFAULT 'pending',
                FOREIGN KEY (userEmail) REFERENCES User(userEmail) ON DELETE CASCADE
            )
        """)
        # Create the cart table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Cart (
                cartID INTEGER PRIMARY KEY AUTOINCREMENT,
                userEmail TEXT NOT NULL,
                productID INTEGER NOT NULL,
                quantity INTEGER NOT NULL,
                FOREIGN KEY (userEmail) REFERENCES User(userEmail) ON DELETE CASCADE,
                FOREIGN KEY (productID) REFERENCES Products(productID) ON DELETE CASCADE
            )
        """)
        # Create the reviews table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Reviews (
                reviewID INTEGER PRIMARY KEY AUTOINCREMENT,
                userEmail TEXT NOT NULL,
                productID INTEGER NOT NULL,
                review TEXT NOT NULL,
                rating INTEGER NOT NULL,
                FOREIGN KEY (userEmail) REFERENCES User(userEmail) ON DELETE CASCADE,
                FOREIGN KEY (productID) REFERENCES Products(productID) ON DELETE CASCADE
            )
        """)

        self.conn.commit()

    def close(self):
        self.conn.close()

if __name__ == '__main__':
    print("Creating the database")
    db = projectDB()
    print("Database created")
    db.close()