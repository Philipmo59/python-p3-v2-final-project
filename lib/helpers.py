from models.customer import Customer

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
def find_by_id():
    customer_id = input("What is the id you are looking for?: ")
    customer_object= Customer.find_by_id(customer_id) 
    if customer_object:
        print(customer_object)
    else:
        print("Sorry this id does not exist in the database")

def add_customer():
    customer_name = input("What is the Customer's name?: ")
    customer_age = input("What is the Customer's age?: ")
    customer_address = input("What is the Customer's address?: ")
    try: 
        Customer.create(customer_name,customer_age,customer_address)
        print("A Customer was born")
    except:
        print("Error")

def update_customer():
    customer_id = input("What is the Customer ID you want to change?: ")
    print("Please update the following: ")
    customer_name = input("Name: ")
    customer_age = input("Age: ")
    customer_address = input("Address: ")
    if customer_id:
        Customer.update(customer_name,customer_age,customer_address)
        print("done")
    else:
        print("Error Occurred")
    