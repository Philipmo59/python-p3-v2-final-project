from lib.__init__ import CURSOR, CONN

class Customer:

    def __init__(self,name,age,address,id = None) -> None:
        self.id = id
        self.name = name
        self.age = age
        self.address = address

    def __repr__(self):
        return (
            f"<Customer {self.id}: {self.name}, {self.age}, {self.address} " 
        )
    
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Employee instances """
        sql = """
            CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            address TEXT,
            FOREIGN KEY (department_id) REFERENCES departments(id))
        """
        CURSOR.execute(sql)
        CONN.commit()


    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Employee instances """
        sql = """
            DROP TABLE IF EXISTS customers;
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    def save(self):
        """ Insert a new row with the name, job title, and department id values of the current Employee object.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
                INSERT INTO customers (name, age, address)
                VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.name, self.address))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """Update the table row corresponding to the current Employee instance."""
        sql = """
            UPDATE employees
            SET name = ?, age = ?, address = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.age,
                             self.address, self.id))
        CONN.commit()




susan = Customer ("susan","10","apple st")
print(repr(susan))
