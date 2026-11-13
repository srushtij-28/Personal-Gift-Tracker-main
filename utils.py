from datetime import datetime


def get_valid_date(prompt):
    while True:
        value = input(prompt).strip()

        try:
            parsed_date = datetime.strptime(value, "%Y-%m-%d")
            return parsed_date.strftime("%Y-%m-%d")

        except ValueError:
            print("Invalid date. Use YYYY-MM-DD format.")


def get_valid_amount(prompt):
    while True:
        try:
            amount = float(input(prompt))

            if amount < 0:
                print("Amount cannot be negative.")
                continue

            return round(amount, 2)

        except ValueError:
            print("Please enter a valid amount.")


def get_valid_id(prompt):
    while True:
        try:
            gift_id = int(input(prompt))

            if gift_id > 0:
                return gift_id

            print("ID must be greater than zero.")

        except ValueError:
            print("Please enter a valid numeric ID.")


def get_gift_status():
    print("\nSelect Gift Status:")
    print("1. Planned")
    print("2. Purchased")
    print("3. Given")

    statuses = {
        "1": "Planned",
        "2": "Purchased",
        "3": "Given"
    }

    while True:
        choice = input("Enter choice: ").strip()

        if choice in statuses:
            return statuses[choice]

        print("Invalid status choice.")
