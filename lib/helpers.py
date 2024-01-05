from models.customer import Customer
from models.shipping_orders import Order

def list_customers():
    list_of_customers = Customer.get_all()
    for customer in list_of_customers:
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
    try: 
        Customer.create_table()
        Customer.create(customer_name,customer_age,customer_address)
        print("A Customer was born")
    except:
        print("Error")

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
    customer_id = input("Which customer is purchasing? Please submit your id: ")
    if customer := Customer.find_by_id(customer_id):
        print(Customer.find_by_id(customer_id))
        new_order = input("What is the new order?")
        quantity = int(input("How many?"))
        new_item = Order(new_order,quantity)
        customer.shipping_orders.append(new_item)
        customer.add_order(new_item)#method to be created 
        for item in customer.shipping_orders:
            print(f"Item: {item.item_name} Quantity: {item.quantity}")
        print(customer)

    else:
        print("This Customer does not exist")