import sqlite3

CONN = sqlite3.connect('tracking_order.db')
CURSOR = CONN.cursor()

class Order:
    all = {}

    def __init__(self,item_name,quantity,foreign_key = None,id = None):
        self.id = id
        self.item_name = item_name
        self.quantity = quantity
        self.foreign_key = foreign_key

    def __str__(self) -> str:
        return f"{self.item_name}, Quantity: {self.quantity}"
    
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Order instances """
        sql = """
            CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY,
            item_name TEXT,
            quantity INTEGER,
            foreign_key INTEGER
            );
        """
        print("Orders table made")
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def delete_table(cls):
        sql = """
            DROP TABLE IF EXISTS orders
        """
        CURSOR.execute(sql)
        CONN.commit()

    
    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Order instances """
        sql = """
            DROP TABLE IF EXISTS orders;
        """
        CURSOR.execute(sql)
        CONN.commit()

    
    @classmethod
    def create(cls, item_name, quantity,foreign_key):
        """ Initialize a new Order instance and save the object to the database """
        order = cls(item_name, quantity,foreign_key)
        return order
    
    
    @classmethod
    def get_all(cls):
        
        sql = """
            SELECT * FROM orders
        """
        CURSOR.execute(sql).fetchall()
    
    @classmethod
    def find_by_id(cls,id):
        sql = """
            SELECT * FROM ORDERS WHERE id = ?
        """
        found_order = CURSOR.execute(sql,(id,)).fetchone()
        CONN.commit()
        return found_order
    

    




