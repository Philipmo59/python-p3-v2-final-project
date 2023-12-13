# lib/models/department.py
from models.__init__ import CURSOR, CONN

class Order:

    def __init__(self,name,quantity,customer_id, id=None):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.customer_id = customer_id
    def save(self):
        sql = """
            INSERT INTO orders (name,quantity,customer_name)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.quantity, self.customer_id))

    def create(cls,name,quantity,customer_id):
        """Initializes a shipping order instance and save to database"""
        order = cls(name,quantity,customer_id)
        order.save()
        return order

    @classmethod
    def create_table(cls):
        """ Creates a new table to persist the Children Instances"""
        sql = """
            CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY,
            name TEXT,
            quantity INTEGER,
            customer_name TEXT,
            )
        """
        CURSOR.execute(sql)
        CONN.commit()










