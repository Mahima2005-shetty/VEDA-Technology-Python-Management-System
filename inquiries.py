from data_manager import load_data, save_data, next_id
from utils import print_header, required_text, choose_status, pause

FILE = "inquiries.json"
STATUSES = ["New", "In Progress", "Resolved", "Closed"]


def inquiry_menu():
    while True:
        print_header("SERVICE INQUIRY MANAGEMENT")
        print("1. Add inquiry")
        print("2. View inquiries")
        print("3. Search inquiries")
        print("4. Update inquiry status")
        print("0. Back")

        choice = input("\nEnter choice: ").strip()

        if choice == "1":
            add_inquiry()
        elif choice == "2":
            view_inquiries()
        elif choice == "3":
            search_inquiries()
        elif choice == "4":
            update_inquiry_status()
        elif choice == "0":
            break
        else:
            print("Invalid choice.")
            pause()


def add_inquiry():
    inquiries = load_data(FILE)
    inquiry = {
        "id": next_id(inquiries),
        "customer_name": required_text("Customer name: "),
        "service": required_text("Requested service: "),
        "category": required_text("Inquiry category: "),
        "message": required_text("Inquiry message: "),
        "status": "New",
    }
    inquiries.append(inquiry)
    save_data(FILE, inquiries)
    print("Inquiry added successfully.")
    pause()


def view_inquiries():
    inquiries = load_data(FILE)
    print_header("ALL INQUIRIES")

    if not inquiries:
        print("No inquiries found.")
    for item in inquiries:
        print(
            f'ID: {item["id"]} | {item["customer_name"]} | '
            f'{item["service"]} | {item["category"]} | {item["status"]}'
        )
    pause()


def search_inquiries():
    inquiries = load_data(FILE)
    keyword = input("Search by customer/service/category/status: ").strip().lower()
    results = [
        item for item in inquiries
        if keyword in item["customer_name"].lower()
        or keyword in item["service"].lower()
        or keyword in item["category"].lower()
        or keyword in item["status"].lower()
    ]

    print_header("INQUIRY SEARCH RESULTS")
    if not results:
        print("No matching inquiries.")
    for item in results:
        print(
            f'{item["id"]}. {item["customer_name"]} - '
            f'{item["service"]} - {item["status"]}'
        )
    pause()


def update_inquiry_status():
    inquiries = load_data(FILE)
    try:
        inquiry_id = int(input("Enter inquiry ID: ").strip())
    except ValueError:
        print("Invalid ID.")
        pause()
        return

    for item in inquiries:
        if item["id"] == inquiry_id:
            item["status"] = choose_status(
                "New status (New/In Progress/Resolved/Closed): ", STATUSES
            )
            save_data(FILE, inquiries)
            print("Inquiry status updated.")
            pause()
            return

    print("Inquiry not found.")
    pause()
