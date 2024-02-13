from models.customer import Customer
from models.shipping_orders import Order

def list_customers():
    counter = 1
    print("The Customer names are:")
    print("-------------------------------------")
    Customer.get_all()
    for customer in Customer.list_of_customers.values():
        print(f"{counter}. {customer.name}")
        counter += 1
    print("-------------------------------------")

def find_by_name():
    customer_name = input("What is the name you are looking for?: ")
    list_of_customers = Customer.find_by_name(customer_name) 
    if list_of_customers != None:
        for customer in list_of_customers:
            print(f"Customer Name: {customer.name}\nAddress: {customer.address}\nOrders: {', ' .join(customer.shipping_orders)}")
    else:
        print("Sorry, this name does not exist in the database")

def add_customer():
    customer_name = input("What is the Customer's name?: ")
    customer_age = int(input("What is the Customer's age?: "))
    customer_address = input("What is the Customer's address?: ")
    new_customer = Customer.create(customer_name,customer_age,customer_address)
    print(f"Customer Name: {new_customer.name}\nAddress: {new_customer.address}\nOrders: {', ' .join(new_customer.shipping_orders)}")
    print("A Customer was born")

def update_customer():
    customer_name = input("What is the Customer name that you want to change?: ")
    if list_of_customers := Customer.find_by_name(customer_name):
        if len(list_of_customers) > 1:
            for count,customer in enumerate(list_of_customers):
                print(f"{count + 1}. {customer.name}: Address: {customer.address} Orders: {', '.join(customer.shipping_orders)}")
            selected_customer = int(input(f"Which {customer.name} do you want to update? Please input the number corresponding"))
            print("Please fill out the following: ")
            customer_name = input("Name: ")
            customer_age = input("Age: ")
            customer_address = input("Address: ")
            print("\n")
            list_of_customers[selected_customer - 1].update(customer_name,customer_age,customer_address)
            print(f"{customer.name}'s Age: {customer.age} Address:{customer_address}")
            print("Update is Complete")
        else:
            print("Please update the following: ")
            customer_name = input("Name: ")
            customer_age = input("Age: ")
            customer_address = input("Address: ")
            customer.update(customer_name,customer_age,customer_address)
            print("\n")
            print(f"{customer.name}'s Age: {customer.age} Address: {customer_address}")
            print("Update is Complete")
    else:
        print("Customer ID does not exist")
    

def add_order():
    customer_id = int(input("Which customer is purchasing? Please submit your id: "))
    if customer := Customer.find_by_id(customer_id):
        print(customer.name)
        new_order = input("What is the new order?")
        quantity = int(input("How many?"))
        new_item = Order.create(new_order,quantity,customer.id)
        customer.add_order(new_item)
        print(f"{customer.name} bought {new_item.quantity} {new_item.item_name}")

    else:
        print("This Customer does not exist")

def delete_order():
    customer = input("Which Customer name do you want to delete from?: ")
    possible_customers = Customer.find_by_name(customer)
    if len(possible_customers) > 1:
        for count,customer in enumerate(possible_customers):
            print(f"{count + 1}. {customer.name}: Address: {customer.address} Orders: {', '.join(customer.shipping_orders)}")
        selected_customer = int(input(f"Which {customer.name} do you want to delete from? Please input the number corresponding"))
        selected_order = input(f"Which of {possible_customers[0].name}'s order do you want to delete?")
        possible_customers[selected_customer - 1].delete_order(selected_order)

    else:
        print(f"{possible_customers[0].name}'s Orders: {', '.join(possible_customers[0].shipping_orders)}")
        selected_order = input(f"Which of {possible_customers[0].name}'s order do you want to delete?")
        possible_customers[0].delete_order(selected_order)
    # Customer.delete_order(customer)