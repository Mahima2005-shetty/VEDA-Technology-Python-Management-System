from data_manager import load_data, save_data, next_id
from utils import print_header, required_text, pause

FILE = "customers.json"


def customer_menu():
    while True:
        print_header("CUSTOMER MANAGEMENT")
        print("1. Add customer")
        print("2. View customers")
        print("3. Search customers")
        print("0. Back")

        choice = input("\nEnter choice: ").strip()

        if choice == "1":
            add_customer()
        elif choice == "2":
            view_customers()
        elif choice == "3":
            search_customers()
        elif choice == "0":
            break
        else:
            print("Invalid choice.")
            pause()


def add_customer():
    customers = load_data(FILE)
    customer = {
        "id": next_id(customers),
        "name": required_text("Customer name: "),
        "email": required_text("Email: "),
        "phone": required_text("Phone: "),
        "organization": required_text("Organization: "),
    }
    customers.append(customer)
    save_data(FILE, customers)
    print("Customer added successfully.")
    pause()


def view_customers():
    customers = load_data(FILE)
    print_header("ALL CUSTOMERS")

    if not customers:
        print("No customers found.")
    for item in customers:
        print(
            f'ID: {item["id"]} | {item["name"]} | '
            f'{item["email"]} | {item["phone"]} | {item["organization"]}'
        )
    pause()


def search_customers():
    customers = load_data(FILE)
    keyword = input("Search by name/email/organization: ").strip().lower()
    results = [
        item for item in customers
        if keyword in item["name"].lower()
        or keyword in item["email"].lower()
        or keyword in item["organization"].lower()
    ]

    print_header("CUSTOMER SEARCH RESULTS")
    if not results:
        print("No matching customers.")
    for item in results:
        print(f'{item["id"]}. {item["name"]} - {item["email"]} - {item["organization"]}')
    pause()
