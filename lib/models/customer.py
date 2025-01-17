import sqlite3
from models.shipping_orders import Order

CONN = sqlite3.connect('tracking_order.db')
CURSOR = CONN.cursor()


class Customer:
    list_of_customers = {}
    
    def __init__(self,name,age,address,id = None) -> None:
        self.id = id
        self.name = name
        self.age = age
        self.address = address
        self.shipping_orders = []
    #Keep the format to the front end
    # def __repr__(self):
    #     #Look through the Order's Table and with the foreign key, return all the orders that belong to that foreign key
    #     self.get_order_list()
    #     return f"Customer {self.id}: {self.name}, Age: {self.age}, Address: {self.address}, Shipping Orders: {self.shipping_orders} "   

    def get_order_list(self)->None:
        sql = """
            SELECT * FROM orders WHERE foreign_key = ?;
        """
        rows = CURSOR.execute(sql,(self.id,)).fetchall()

        updated_orders = []
        for row in rows:
            order_object = Order.instance_from_db(row)
            updated_orders.append(order_object.item_name)
        self.shipping_orders = updated_orders
    
    @property
    def name(self):
        #Getter Method 
        # print("Retrieving Name")
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-empty string"
            )
        
    def get_age(self):
        # print("Retrieving Age")
        return self._age

    def set_age(self, age):
        if isinstance(age, int):
            # print("Setting Age")
            self._age = age
        else:
            raise ValueError(
                "Age must be an number"
            )
        
    age = property(get_age,set_age)

    @property
    def address(self):
        # print("Retrieving Address")
        return self._address
    @address.setter
    def address (self,address):
        if isinstance(address,str) and len(address):
            # print("Setting Address")
            self._address = address
        else:
            raise ValueError("Address can not be an empty line")
    
        

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Customer instances """
        sql = """
            CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            address TEXT
            );
        """
        CURSOR.execute(sql)
        CONN.commit()
        # print("Table has been created")


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
                VALUES (?, ?, ?);
        """

        CURSOR.execute(sql, (self.name, self.age, self.address,))
        CONN.commit()

        self.id = CURSOR.lastrowid

    @classmethod
    def create(cls, name, age, address):
        """ Initialize a new Customer instance and save the object to the database """
        customer = cls(name, age, address)
        customer.save()
        return customer
    
    def delete(self):
        """Delete the table row corresponding to the current Customer instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM customers
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        print(f"{self.name} has been deleted")
    

    def delete_order(self,selected_order):
        sql = """
            DELETE FROM orders WHERE item_name = ? and foreign_key = ?
        """
        CURSOR.execute(sql,(selected_order,self.id))
        CONN.commit()
        print("Done")
        
        
    @classmethod
    def instance_from_db(cls, row):
        """Return a Customer object having the attribute values from the table row."""

        # Check the dictionary for  existing instance using the row's primary key
        customer = cls.list_of_customers.get(row[0])
        if customer:
            #Only activates if customer already exists (updates customer based on the database table)
            customer.name = row[1]
            customer.age = row[2]
            customer.address = row[3]
            customer.get_order_list()
        else:
            # if not in dictionary, create new instance and add to dictionary
            customer = cls(row[1], row[2], row[3])
            customer.id = row[0]
            cls.list_of_customers[customer.id] = customer
            customer.get_order_list()
        return customer

    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM customers
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows] 
        

    def update(self,name,age,address):
        """Update the table row corresponding to the current Customer instance."""
        sql = """
            UPDATE customers
            SET name = ?, age = ?, address = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (name,age,address,self.id))
        CONN.commit()


    # def add_order(self,order:Order)->None:
    #     '''Takes in an instance of an Order and appends it to the customer database'''
    #     sql = '''
    #         INSERT INTO orders (item_name, quantity, foreign_key)
    #         VALUES (?, ? , ?)
    #     '''
    #     CURSOR.execute(sql, (order.item_name,order.quantity, self.id))
    #     CONN.commit()

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
    def find_by_name(cls, name) -> list:
        """Return Customer object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM customers
            WHERE name = ?
        """

        customer_object = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(customer_object)
    @classmethod
    def find_all_by_name(cls,name) -> list:
        """Returns an array of Customer objects corresponding to specificed name"""
        sql = """
            SELECT * FROM customers WHERE name = ?
        """
        customer_objects = CURSOR.execute(sql,(name,)).fetchall()
        return [cls.instance_from_db(object) for object in customer_objects]

        
