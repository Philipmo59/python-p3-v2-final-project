from models.customer import Customer
from models.shipping_orders import Order

def list_customers():
    for customer in Customer.get_all():
        print(customer)
            
        

def find_by_name():
    customer_name = input("What is the name you are looking for?: ").lower()
    customer_object = Customer.find_by_name(customer_name) 

    if customer_object != None:
        print(customer_object)
    else:
        print("Sorry, this name does not exist in the database")

def add_customer():
    customer_name = input("What is the Customer's name?: ")
    customer_age = input("What is the Customer's age?: ")
    customer_address = input("What is the Customer's address?: ")
    Customer.create_table()
    Customer.create(customer_name,customer_age,customer_address)
    print("A Customer was born")

def update_customer():
    customer_id = int(input("What is the Customer ID you want to change?: "))
    if Customer.find_by_id(customer_id):
        print("Please update the following: ")
        customer_name = input("Name: ")
        customer_age = input("Age: ")
        customer_address = input("Address: ")
        Customer.update(customer_name,customer_age,customer_address)
        print("done")
    else:
        print("Error Occurred")

def add_order():
    customer_id = int(input("Which customer is purchasing? Please submit your id: "))
    Order.create_table()
    if customer := Customer.find_by_id(customer_id):
        print(customer)
        new_order = input("What is the new order?")
        quantity = int(input("How many?"))
        new_item = Order.create(new_order,quantity,customer.id)
        customer.add_order(new_item)
        print(f"Item: {new_item.item_name} Quantity: {new_item.quantity}")
        print(customer)

    else:
        print("This Customer does not exist")