import sqlite3

CONN = sqlite3.connect('tracking_order.db')
CURSOR = CONN.cursor()

class Order:
    all_orders = {}

    def __init__(self,item_name,quantity,foreign_key = None,id = None):
        self.id = id
        self.item_name = item_name
        self.quantity = quantity
        self.foreign_key = foreign_key

    # def __repr__(self) -> str:
    #     return f"{self.item_name}, Quantity: {self.quantity}"
    
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
        # print("Orders table made")
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
    def delete_order(cls,id):
        sql = """
            DELETE FROM orders WHERE id = ?
        """
        CURSOR.execute(sql,(id,))
        CONN.commit()

    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM orders
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows] 

    @classmethod
    def find_by_id(cls,id):
        sql = """
            SELECT * FROM ORDERS WHERE id = ?
        """
        results = CURSOR.execute(sql,(id,)).fetchone()
        return results
    
    @classmethod
    def find_order_by_foreign_key(cls,foreign_key):
        sql = """
            SELECT * FROM ORDERS WHERE foreign_key = ?
        """
        results = CURSOR.execute(sql,(foreign_key,)).fetchall()
        return results
    
    @classmethod
    def add_order(cls,order,foreign_key)->None:
        '''Takes in an instance of an Order and appends it to the customer database'''
        sql = '''
            INSERT INTO orders (item_name, quantity, foreign_key)
            VALUES (?, ? , ?)
        '''
        CURSOR.execute(sql, (order.item_name,order.quantity, foreign_key))
        CONN.commit()

    @classmethod
    def instance_from_db(cls, row):
        """Return an Orders object having the attribute values from the table row."""

        # Check the dictionary for  existing instance using the row's primary key
        order = cls.all_orders.get(row[0])
        if order:
            #Only activates if order already exists (updates order based on the database table)
            order.item_name = row[1]
            order.quantity = row[2]
            order.foreign_key = row[3]
        else:
            # if not in dictionary, create new instance and add to dictionary
            order = cls(row[1], row[2], row[3])
            order.id = row[0]
            cls.all_orders[order.id] = order
        return order
