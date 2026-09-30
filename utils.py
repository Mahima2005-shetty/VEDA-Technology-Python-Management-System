def print_header(title):
    print("\n" + "=" * 60)
    print(title.center(60))
    print("=" * 60)


def pause():
    input("\nPress Enter to continue...")


def required_text(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")


def positive_number(prompt):
    while True:
        try:
            value = float(input(prompt).strip())
            if value >= 0:
                return value
            print("Enter a value greater than or equal to 0.")
        except ValueError:
            print("Please enter a valid number.")


def choose_status(prompt, statuses):
    while True:
        value = input(prompt).strip()
        if value in statuses:
            return value
        print("Invalid status. Choose:", ", ".join(statuses))
