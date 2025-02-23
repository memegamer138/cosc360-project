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

        self.cursor.execute("INSERT INTO Products (productName, categoryID, productDesc, price, imagePath) VALUES ('Last of Us', 1, 'RPG/Action/Sci-Fi by Naughty Dog', 28.00, 'images/1.jpg')")
        self.cursor.execute("INSERT INTO Products (productName, categoryID, productDesc, price, imagePath) VALUES ('Uncharted Bundle', 1, 'RPG/Action by Naughty Dog', 69.00, 'images/2.jpg')")
        self.cursor.execute("INSERT INTO Products (productName, categoryID, productDesc, price, imagePath) VALUES ('GTA 6', 3, 'Crime/PG by Rockstar Games', 30.00, 'images/3.jpg')")
        self.cursor.execute("INSERT INTO Products (productName, categoryID, productDesc, price, imagePath) VALUES ('Spider-Man Miles Morales', 1, 'Action/Superhero by Insomniac', 22.00, 'images/4.jpg')")
        self.cursor.execute("INSERT INTO Products (productName, categoryID, productDesc, price, imagePath) VALUES ('Mario Bros Kart', 4, 'Racing by Nintendo', 21.35, 'images/5.jpg')")
        self.cursor.execute("INSERT INTO Products (productName, categoryID, productDesc, price, imagePath) VALUES ('PS5 Controller', 1, 'Controller', 25.00, 'images/6.jpg')")
        self.cursor.execute("INSERT INTO Products (productName, categoryID, productDesc, price, imagePath) VALUES ('Five Nights at Freddys', 3, 'Horror/Indie by Scott Cawthon', 30.00, 'images/7.jpg')")
        self.cursor.execute("INSERT INTO Products (productName, categoryID, productDesc, price, imagePath) VALUES ('Freddy Plushie', 5, 'Plushie', 40.00, 'images/8.jpg')")
        self.cursor.execute("INSERT INTO Products (productName, categoryID, productDesc, price, imagePath) VALUES ('Valorant', 3, 'FPS/Shooting by Riot Games', 7.00, 'images/9.jpg')")
        self.cursor.execute("INSERT INTO Products (productName, categoryID, productDesc, price, imagePath) VALUES ('Ghost of Tsushima', 1, 'RPG/Fighting by Sucker Punch Productions', 31.00, 'images/10.jpg')")
        self.cursor.execute("INSERT INTO Products (productName, categoryID, productDesc, price, imagePath) VALUES ('Dead by Daylight', 3, 'Horror/Online by Behaviour Interactive', 21.00, 'images/11.jpg')")
        self.cursor.execute("INSERT INTO Products (productName, categoryID, productDesc, price, imagePath) VALUES ('Forza Horizon 4', 2, 'Racing by Microsoft', 38.00, 'images/12.jpg')")
        self.cursor.execute("INSERT INTO Products (productName, categoryID, productDesc, price, imagePath) VALUES ('Midtown Madness', 4, 'Racing by Angel Studios', 23.25, 'images/13.jpg')")
        self.cursor.execute("INSERT INTO Products (productName, categoryID, productDesc, price, imagePath) VALUES ('Shadow of the Colossus', 1, 'Action/Adventure by Japan Studio', 15.50, 'images/14.jpg')")
        self.cursor.execute("INSERT INTO Products (productName, categoryID, productDesc, price, imagePath) VALUES ('Mario Smash Bros', 4, 'Fighting by Nintendo', 17.45, 'images/15.jpg')")
        self.cursor.execute("INSERT INTO Products (productName, categoryID, productDesc, price, imagePath) VALUES ('Subnautica', 1, 'Survival/Adventure by Unknown Worlds Entertainment', 19.00, 'images/16.jpg')")
        self.cursor.execute("INSERT INTO Products (productName, categoryID, productDesc, price, imagePath) VALUES ('Halo', 2, 'Online/Shooter by Microsoft', 62.50, 'images/17.jpg')")
        self.cursor.execute("INSERT INTO Products (productName, categoryID, productDesc, price, imagePath) VALUES ('Need For Speed Poster', 5, 'Poster', 9.20, 'images/18.jpg')")
        self.cursor.execute("INSERT INTO Products (productName, categoryID, productDesc, price, imagePath) VALUES ('Captain Claw', 3, 'Platform by Monolith Productions', 81.00, 'images/19.jpg')")
        self.cursor.execute("INSERT INTO Products (productName, categoryID, productDesc, price, imagePath) VALUES ('Monopoly for Nintendo', 4, 'Family by Nintendo', 10.00, 'images/20.jpg')")
        self.cursor.execute("INSERT INTO Products (productName, categoryID, productDesc, price, imagePath) VALUES ('Switch Controller (Blue)', 5, 'Controller', 21.00, 'images/21.jpg')")
        self.cursor.execute("INSERT INTO Products (productName, categoryID, productDesc, price, imagePath) VALUES ('Vegeta Action Figure', 5, 'Dragon Ball Action Figure', 14.00, 'images/22.jpg')")
        self.cursor.execute("INSERT INTO Products (productName, categoryID, productDesc, price, imagePath) VALUES ('Luigis Mansion', 4, 'Horror/Family by Nintendo', 18.00, 'images/23.jpg')")
        self.cursor.execute("INSERT INTO Products (productName, categoryID, productDesc, price, imagePath) VALUES ('RGB Keyboard', 3, 'Keyboard', 99.00, 'images/24.jpg')")
        self.cursor.execute("INSERT INTO Products (productName, categoryID, productDesc, price, imagePath) VALUES ('Final Fantasy X1V', 3, 'Online/RPG by Square Enix', 18.40, 'images/25.jpg')")
        self.cursor.execute("INSERT INTO Products (productName, categoryID, productDesc, price, imagePath) VALUES ('Donkey Kong', 4, 'Platform by Nintendo', 89.65, 'images/26.jpg')")
        self.cursor.execute("INSERT INTO Products (productName, categoryID, productDesc, price, imagePath) VALUES ('Blair Witch', 3, 'Horror/RPG by Bloober Team', 14.00, 'images/27.jpg')")
        self.cursor.execute("INSERT INTO Products (productName, categoryID, productDesc, price, imagePath) VALUES ('Xbox Controller (Camo)', 5, 'Controller', 21.05, 'images/28.jpg')")
        self.cursor.execute("INSERT INTO Products (productName, categoryID, productDesc, price, imagePath) VALUES ('Apex Legends', 1, 'FPS/Online by Respawn Entertainment', 14.00, 'images/29.jpg')")
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

        self.cursor.execute("INSERT INTO Categories(categoryName) VALUES ('PlayStation')")
        self.cursor.execute("INSERT INTO Categories(categoryName) VALUES ('Xbox')")
        self.cursor.execute("INSERT INTO Categories(categoryName) VALUES ('PC')")
        self.cursor.execute("INSERT INTO Categories(categoryName) VALUES ('Nintendo Switch')")
        self.cursor.execute("INSERT INTO Categories(categoryName) VALUES ('Accessories')")

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