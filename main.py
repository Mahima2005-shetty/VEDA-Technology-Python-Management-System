from services import service_menu
from programs import program_menu
from customers import customer_menu
from inquiries import inquiry_menu
from reports import reports_menu
from utils import pause, print_header


def main():
    while True:
        print_header("VEDA TECHNOLOGY - MANAGEMENT SYSTEM")
        print("1. Service Management")
        print("2. Program Management")
        print("3. Customer Management")
        print("4. Service Inquiry Management")
        print("5. Search & Filtering")
        print("6. Business Reports")
        print("0. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            service_menu()
        elif choice == "2":
            program_menu()
        elif choice == "3":
            customer_menu()
        elif choice == "4":
            inquiry_menu()
        elif choice == "5":
            # Search is available inside each management module.
            print("\nSearch/filtering is available in Services, Programs, Customers, and Inquiries.")
            pause()
        elif choice == "6":
            reports_menu()
        elif choice == "0":
            print("\nThank you for using Veda Technology Management System.")
            break
        else:
            print("\nInvalid choice. Please enter a number from the menu.")
            pause()


if __name__ == "__main__":
    main()
