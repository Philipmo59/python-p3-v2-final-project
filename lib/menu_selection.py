from models.customer import Customer
from helpers import (
    list_customers,
    find_by_name,
    add_customer,
    update_customer,
    add_order
)

def main():
    menu()
    choice = input("> ")
    if choice == "1":
        list_customers()
    if choice == "2":
        find_by_name()
    if choice == "3":
        add_customer()
    if choice == "4":
        update_customer()
    if choice == "5":
        add_order()

def menu():
    list_of_options = ["Exit the Program", "List all Customers","Find Customer by name","Add a Customer","Update a Customer","Add Order"]
    for count, value in enumerate(list_of_options):
        print(f"{count}. {value}")

if __name__ == "__main__":
    main()