from models.customer import Customer
from helpers import (
    list_customers,
    find_by_name,
    add_customer,
    delete_customer,
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
        elif choice == "1":
            list_customers()
        elif choice == "2":
            find_by_name()
        elif choice == "3":
            add_customer()
        elif choice == "4":
            delete_customer()
        elif choice == "5":
            update_customer()
        elif choice == "6":
            add_order()
        elif choice == "7":
            delete_order()
        else:
            print("Sorry I do not understand. Please pick a number from the list.")



def menu():
    list_of_options = ["Exit the Program", "List all Customers","Find Customer by name","Add a Customer","Delete a Customer","Update a Customer","Add Order","Delete Order"]
    print("\n")
    print("-------------------------------------")

    for count, value in enumerate(list_of_options):
        print(f"{count}. {value}")
    print("-------------------------------------")

if __name__ == "__main__":
    main()