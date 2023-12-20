from models.customer import Customer
from helpers import (
    list_customers,
    find_by_name,
    find_by_id,
    add_customer,
    update_customer
)

def main():
    Customer.drop_table()
    Customer.create_table()
    menu()
    choice = input("> ")
    if choice == "1":
        list_customers()
    if choice == "2":
        find_by_name()
    if choice == "3":
        find_by_id()
    if choice == "4":
        add_customer()
    if choice == "5":
        update_customer()

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all Customers")
    print("2. Find Customer by name")
    print("3. Find Customer by id")
    print("4: Add a Customer")
    print("5: Update Customer")
    # print("6: Delete department")
    # print("7. List all employees")
    # print("8. Find employee by name")
    # print("9. Find employee by id")
    # print("10: Create employee")
    # print("11: Update employee")
    # print("12: Delete employee")
    # print("13: List all employees in a department")

if __name__ == "__main__":
    main()