from data_manager import load_data, save_data, next_id
from utils import print_header, required_text, positive_number, choose_status, pause

FILE = "services.json"
STATUSES = ["Active", "Inactive"]


def service_menu():
    while True:
        print_header("SERVICE MANAGEMENT")
        print("1. Add service")
        print("2. View services")
        print("3. Search services")
        print("4. Update service status")
        print("0. Back")

        choice = input("\nEnter choice: ").strip()

        if choice == "1":
            add_service()
        elif choice == "2":
            view_services()
        elif choice == "3":
            search_services()
        elif choice == "4":
            update_service_status()
        elif choice == "0":
            break
        else:
            print("Invalid choice.")
            pause()


def add_service():
    services = load_data(FILE)
    service = {
        "id": next_id(services),
        "name": required_text("Service name: "),
        "category": required_text("Category: "),
        "description": required_text("Description: "),
        "price": positive_number("Estimated price: "),
        "status": "Active",
    }
    services.append(service)
    save_data(FILE, services)
    print("Service added successfully.")
    pause()


def view_services():
    services = load_data(FILE)
    print_header("ALL SERVICES")

    if not services:
        print("No services found.")
    for item in services:
        print(
            f'ID: {item["id"]} | {item["name"]} | '
            f'Category: {item["category"]} | Price: {item["price"]:.2f} | '
            f'Status: {item["status"]}'
        )
    pause()


def search_services():
    services = load_data(FILE)
    keyword = input("Search by name/category/status: ").strip().lower()
    results = [
        item for item in services
        if keyword in item["name"].lower()
        or keyword in item["category"].lower()
        or keyword in item["status"].lower()
    ]

    print_header("SERVICE SEARCH RESULTS")
    if not results:
        print("No matching services.")
    for item in results:
        print(f'{item["id"]}. {item["name"]} - {item["category"]} - {item["status"]}')
    pause()


def update_service_status():
    services = load_data(FILE)
    try:
        service_id = int(input("Enter service ID: ").strip())
    except ValueError:
        print("Invalid ID.")
        pause()
        return

    for item in services:
        if item["id"] == service_id:
            item["status"] = choose_status("New status (Active/Inactive): ", STATUSES)
            save_data(FILE, services)
            print("Service status updated.")
            pause()
            return

    print("Service not found.")
    pause()
