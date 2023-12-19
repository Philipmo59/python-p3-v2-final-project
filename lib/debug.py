from lib/models.py/customer.py import Customer

def reset_database():
    Customer.create_table()