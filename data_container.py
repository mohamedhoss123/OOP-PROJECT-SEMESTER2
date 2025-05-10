import sqlite3
class DataContainer:
    def __init__(self):
        self.conn = sqlite3.connect("database.sqlite")

    def exec(self,query,fetch=False):
        cursor = self.conn.cursor()
        cursor.execute(query)

        self.conn.commit()
        if fetch:
            return cursor.fetchall()

    def __del__(self):
        self.conn.close()
