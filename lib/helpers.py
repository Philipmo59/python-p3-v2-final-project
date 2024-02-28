from models.customer import Customer
from models.shipping_orders import Order

Customer.create_table()
Order.create_table()

customer_index_set = {}

def list_customers():
    counter = 1
    print("The Customer names are:")
    print("-------------------------------------")
    Customer.get_all()
    for customer in Customer.list_of_customers.values():
        print(f"{counter}. {customer.name}")
        customer_index_set[counter] = [customer.name, customer.id]
        counter += 1
    print("-------------------------------------")

def find_by_name():
    list_customers()    
    try:
        customer_number = int(input("What customer do you want to know more about? Please enter their respective number: "))
        list_of_customers = Customer.find_all_by_name(customer_index_set[customer_number][0]) 
        if list_of_customers != None:
            if len(list_of_customers) > 1:
                print(f"We found {len(list_of_customers)} customers that match your choice.")
                for customer in list_of_customers:
                    print(f"\nCustomer Name: {customer.name}\nAddress: {customer.address}\nOrders: {', ' .join(customer.shipping_orders)}")
            else:
                for customer in list_of_customers:
                    print(f"\nCustomer Name: {customer.name}\nAddress: {customer.address}\nOrders: {', ' .join(customer.shipping_orders)}")
        else:
            print("Sorry, this name does not exist in the database")
    except ValueError:
        print("\nSorry I do not understand. Please enter a number.\n")
        find_by_name()
    except KeyError:
        print("\nPlease pick a number from the list.")
        find_by_name()


def add_customer():
    customer_name = input("What is the Customer's name?: ")
    customer_age = validate_integer_input((input("What is the Customer's age?: ")))
    while not customer_age:
        customer_age = validate_integer_input((input("What is the Customer's age?: ")))
    customer_address = input("What is the Customer's address?: ")
    new_customer = Customer.create(customer_name,customer_age,customer_address)
    print(f"Customer Name: {new_customer.name}\nAddress: {new_customer.address}\nOrders: {', ' .join(new_customer.shipping_orders)}")
    print("A Customer was born")

def delete_customer():
    list_customers()
    try:
        customer_number = int(input("Which Customer do you want to delete? Please submit their respective number:"))
        customer = Customer.find_by_name(customer_index_set[customer_number])
        print(f"\nCustomer's Name: {customer.name}\nCustomer's Age: {customer.age}\nCustomer's Address: {customer.address}\nOrders: {', '.join(customer.shipping_orders)}\n")
        user_response = input("Is this the customer you want to delete? Please respond Yes or No or Cancel: ").lower()
        if user_response == "yes":
            customer.delete()
        elif user_response == "no":
            delete_customer()
        elif user_response == "cancel":
            return
        else:
            print("Sorry I do not understand. Please try again")
            delete_customer()
    except ValueError:
        print("Please choose a number on the list.\n")
        delete_customer()
    except KeyError:
        print("Please choose a number on the list.\n")
        delete_customer()
    
def validate_integer_input(user_input:str):
    try:
        customer_age = int(user_input)
        return customer_age
    except ValueError:
        print("You did not enter a number. Please try again.")
        return False

def update_customer():
    try:
        list_customers()
        customer_number = int(input("Which customer do you want to update? Please enter their respective number: "))
        customer_object = Customer.find_by_id(customer_index_set[customer_number][1])
        print(f"\nCustomer's Name: {customer_object.name}\nCustomer's Age: {customer_object.age}\nCustomer's Address: {customer_object.address}\nOrders: {', '.join(customer_object.shipping_orders)}\n")
        user_response = input("Is this the customer you want to update? Please respond Yes or No or Cancel: ").lower()
        if user_response == "yes":
            print("\nPlease fill out the following: ")
            customer_name = input("Name: ")
            customer_age = validate_integer_input((input("Age: ")))
            while not customer_age:
                customer_age = validate_integer_input((input("Age: ")))
            customer_address = input("Address: ")
            print("\n")
            customer_object.update(customer_name,customer_age,customer_address)
            print("Update is Complete")
        elif user_response == "no":
            update_customer()
        elif user_response == "cancel":
            return
        else:
            print("Sorry I do not understand, Please try again.")
    except ValueError:
        print("Invalid input.Please submit a number from the list") 
    except KeyError:
        print("Invalid input.Please submit a number from the list") 
    

def add_order():
    list_customers()
    try:
        chosen_customer = int(input("Which customer is purchasing? Please submit their respective number: "))
        customer_id = customer_index_set[chosen_customer][1]
        if customer := Customer.find_by_id(customer_id):
            # print(customer.name)
            new_order = input("What is the new order?")
            quantity = validate_integer_input((input("How many?")))
            while not quantity:
                quantity = validate_integer_input((input("How many?")))
            new_item = Order.create(new_order,quantity,customer.id)
            Order.add_order(new_item,customer_id)
            print(f"{customer.name} bought {new_item.quantity} {new_item.item_name}")

        else:
            print("This Customer does not exist")
    except KeyError:
        print("Please choose a number on the list")

def delete_order():
    order_list = {}
    try:
        counter = 1
        list_customers()
        customer_number = int(input("Which Customer name do you want to delete from? Please enter their resepective number: "))
        customer_object = Customer.find_by_id(customer_index_set[customer_number][1])
        if not customer_object.shipping_orders:
            print("This Customer has no Orders")
        else:
            for order in customer_object.shipping_orders:
                print(f"{counter}. {order}")
                order_list[counter] = order
                counter += 1
            user_selection = int(input("Which order do you want to delete? Please enter their resepective number: "))
            customer_order_list = Order.find_order_by_foreign_key(customer_object.id)
            for order in customer_order_list:
                if order[1] == order_list[user_selection]:
                    Order.delete_order(order[0])
                    print(f"{order[1]} has been deleted")

    
            
        # customer_orders_object = Order.find_by_id(customer_orders)
        # print(customer_orders_object)

    except KeyError:
        print("Please choose a number on the list")
    except ValueError:
        print("Please choose a number on the list")