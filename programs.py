from data_manager import load_data, save_data, next_id
from utils import print_header, required_text, positive_number, choose_status, pause

FILE = "programs.json"
STATUSES = ["Open", "Closed", "Upcoming"]


def program_menu():
    while True:
        print_header("PROGRAM MANAGEMENT")
        print("1. Add program")
        print("2. View programs")
        print("3. Search programs")
        print("4. Update program status")
        print("0. Back")

        choice = input("\nEnter choice: ").strip()

        if choice == "1":
            add_program()
        elif choice == "2":
            view_programs()
        elif choice == "3":
            search_programs()
        elif choice == "4":
            update_program_status()
        elif choice == "0":
            break
        else:
            print("Invalid choice.")
            pause()


def add_program():
    programs = load_data(FILE)
    program = {
        "id": next_id(programs),
        "name": required_text("Program name: "),
        "category": required_text("Category: "),
        "duration": required_text("Duration: "),
        "fee": positive_number("Program fee: "),
        "status": "Upcoming",
    }
    programs.append(program)
    save_data(FILE, programs)
    print("Program added successfully.")
    pause()


def view_programs():
    programs = load_data(FILE)
    print_header("ALL PROGRAMS")

    if not programs:
        print("No programs found.")
    for item in programs:
        print(
            f'ID: {item["id"]} | {item["name"]} | '
            f'{item["category"]} | {item["duration"]} | '
            f'Fee: {item["fee"]:.2f} | {item["status"]}'
        )
    pause()


def search_programs():
    programs = load_data(FILE)
    keyword = input("Search by name/category/status: ").strip().lower()
    results = [
        item for item in programs
        if keyword in item["name"].lower()
        or keyword in item["category"].lower()
        or keyword in item["status"].lower()
    ]

    print_header("PROGRAM SEARCH RESULTS")
    if not results:
        print("No matching programs.")
    for item in results:
        print(f'{item["id"]}. {item["name"]} - {item["category"]} - {item["status"]}')
    pause()


def update_program_status():
    programs = load_data(FILE)
    try:
        program_id = int(input("Enter program ID: ").strip())
    except ValueError:
        print("Invalid ID.")
        pause()
        return

    for item in programs:
        if item["id"] == program_id:
            item["status"] = choose_status(
                "New status (Open/Closed/Upcoming): ", STATUSES
            )
            save_data(FILE, programs)
            print("Program status updated.")
            pause()
            return

    print("Program not found.")
    pause()
