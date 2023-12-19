import sqlite3

CONN = sqlite3.connect('tracking_order.db')
CURSOR = CONN.cursor()


class Orders:
    all = {}

    def __init__(self,item_name,quantity,customer_id,id = None):
        self.id = id
        self.item_name = item_name
        self.quantity = quantity
        self.customer_id = customer_id

    def __str__(self) -> str:
        return f"Order {self.id}: {self.item_name}, Quantity: {self.quantity}, Customer ID: {self.customer_id}"
    
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of ORder instances """
        sql = """
            CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY,
            item_name TEXT,
            quantity INTEGER,
            customer_id INTEGER)
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

    def save(self):
        sql = """
                INSERT INTO orders (item_name, quantity, customer_id)
                VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.item_name, self.quantity, self.customer_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
    
    @classmethod
    def create(cls, item_name, quantity, customer_id):
        """ Initialize a new Order instance and save the object to the database """
        customer = cls(item_name, quantity, customer_id)
        customer.save()
        return customer
    @classmethod
    def delete(self):
        """Delete the table row corresponding to the current Orders instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM orders
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM orders
        """
        CURSOR.execute(sql).fetchall()
    
    def update(self):
        """Update the table row corresponding to the current Order instance."""
        sql = """
            UPDATE orders
            SET item_name = ?, quantity = ?, customer_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.item_name, self.quantity,
                             self.customer_id, self.id))
        CONN.commit()


    @classmethod
    def instance_from_db(cls, row):
        """Return a Order object having the attribute values from the table row."""

        # Check the dictionary for  existing instance using the row's primary key
        order = cls.all.get(row[0])
        if order:
            # ensure attributes match row values in case local instance was modified
            order.item_name = row[1]
            order.quantity = row[2]
            order.customer_id = row[3]
        else:
            # not in dictionary, create new instance and add to dictionary
            order = cls(row[1], row[2], row[3])
            order.id = row[0]
            cls.all[order.id] = order
        return order
    

    @classmethod
    def find_by_id(cls, id):
        """Return Order object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM orders
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """Return Order object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM orders
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None



    
Orders.create_table()
ps5 = Orders("ps5",3,1)
ps5.save()
