from data_manager import load_data
from utils import print_header, pause


def reports_menu():
    services = load_data("services.json")
    programs = load_data("programs.json")
    customers = load_data("customers.json")
    inquiries = load_data("inquiries.json")

    print_header("BASIC BUSINESS REPORT")

    active_services = sum(1 for x in services if x.get("status") == "Active")
    open_programs = sum(1 for x in programs if x.get("status") == "Open")
    new_inquiries = sum(1 for x in inquiries if x.get("status") == "New")
    resolved_inquiries = sum(
        1 for x in inquiries if x.get("status") in {"Resolved", "Closed"}
    )
    total_service_value = sum(float(x.get("price", 0)) for x in services)
    total_program_fees = sum(float(x.get("fee", 0)) for x in programs)

    print(f"Total services           : {len(services)}")
    print(f"Active services          : {active_services}")
    print(f"Total programs           : {len(programs)}")
    print(f"Open programs            : {open_programs}")
    print(f"Total customers          : {len(customers)}")
    print(f"Total inquiries          : {len(inquiries)}")
    print(f"New inquiries            : {new_inquiries}")
    print(f"Resolved/closed inquiries: {resolved_inquiries}")
    print(f"Service value total      : {total_service_value:.2f}")
    print(f"Program fee total        : {total_program_fees:.2f}")

    print("\nReport generated from local JSON files only.")
    pause()
