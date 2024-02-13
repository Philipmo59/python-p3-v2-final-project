from models.customer import Customer
from helpers import (
    list_customers,
    find_by_name,
    add_customer,
    update_customer,
    add_order,
    delete_order
)

def main():
    flag = True
    while flag:
        menu()
        choice = input("> ")
        if choice == "0":
            flag = False
            print("Menu End")
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
        if choice == "6":
            delete_order()


def menu():
    list_of_options = ["Exit the Program", "List all Customers","Find Customer by name","Add a Customer","Update a Customer","Add Order","Delete Order"]
    print("\n")
    print("-------------------------------------")

    for count, value in enumerate(list_of_options):
        print(f"{count}. {value}")
    print("-------------------------------------")

if __name__ == "__main__":
    main()