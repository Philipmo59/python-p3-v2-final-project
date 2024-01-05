import sqlite3

CONN = sqlite3.connect('tracking_order.db')
CURSOR = CONN.cursor()


class Customer:
    all = {}
    
    def __init__(self,name,age,address,id = None) -> None:
        self.id = id
        self.name = name
        self.age = age
        self.address = address
        self.shipping_orders = []

    def __str__(self):
        return (
            f"<Customer {self.id}: {self.name}, Age: {self.age}, Address: {self.address}, Shipping Orders: {self.shipping_orders} " 
        )
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-empty string"
            )

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Customer instances """
        sql = """
            CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            address TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()
        print("Table has been created")


    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Customer instances """
        sql = """
            DROP TABLE IF EXISTS customers;
        """
        CURSOR.execute(sql)
        CONN.commit()
        print("Table has been Dropped")
    
    def save(self):
        sql = """
                INSERT INTO customers (name, age, address)
                VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.age, self.address))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, age, address):
        """ Initialize a new Customer instance and save the object to the database """
        customer = cls(name, age, address)
        customer.save()
        return customer
    
    @classmethod
    def delete(self):
        """Delete the table row corresponding to the current Customer instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM customers
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        
    @classmethod
    def instance_from_db(cls, row):
        """Return a Customer object having the attribute values from the table row."""

        # Check the dictionary for  existing instance using the row's primary key
        customer = cls.all.get(row[0])
        if customer:
            # ensure attributes match row values in case local instance was modified
            customer.name = row[1]
            customer.age = row[2]
            customer.address = row[3]
        else:
            # not in dictionary, create new instance and add to dictionary
            customer = cls(row[1], row[2], row[3])
            customer.id = row[0]
            cls.all[customer.id] = customer
        return customer

    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM customers
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]


    def update(self):
        """Update the table row corresponding to the current Customer instance."""
        sql = """
            UPDATE employees
            SET name = ?, age = ?, address = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.age,
                             self.address, self.id))
        CONN.commit()


    @classmethod
    def find_by_id(cls, id):
        """Return Customer object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM customers
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """Return Customer object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM customers
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
