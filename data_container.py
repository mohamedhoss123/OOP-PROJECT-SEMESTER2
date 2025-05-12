import sqlite3
class DataContainer:
    def __init__(self):
        self.conn = sqlite3.connect("database.sqlite")
        self.migrate()

    def exec(self,query,fetch=False):
        cursor = self.conn.cursor()
        cursor.execute(query)

        self.conn.commit()
        if fetch:
            return cursor.fetchall()

    def __del__(self):
        self.conn.close()
    def migrate(self):
        self.conn.executescript("""
CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    category_id INTEGER NOT NULL,
    FOREIGN KEY (category_id) REFERENCES categories(id)
);

CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY,
    created_at DATETIME NOT NULL
);

CREATE TABLE IF NOT EXISTS order_items (
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    total REAL NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (product_id) REFERENCES products(id),
);

""")
        self.conn.commit()