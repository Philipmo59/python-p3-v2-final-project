import sqlite3

CONN = sqlite3.connect("shopping_list.db")
CURSOR = CONN.cursor()

class Supermarket():
    def __init__(self,name,price,id = None) -> None:
        self.id = id
        self.name = name
        self.price = price
    def create_table():
        sql = """
            CREATE TABLE IF NOT EXISTS supermarkets(
            id INTEGER PRIMARY KEY,
            name TEXT,
            quantity INTEGER
            );
        """
    
