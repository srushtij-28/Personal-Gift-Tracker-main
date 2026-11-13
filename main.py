from storage import initialize_storage

from gift_manager import (
    add_gift,
    view_gifts,
    search_gifts,
    filter_gifts_by_status,
    update_gift,
    delete_gift,
    show_statistics
)

from utils import (
    get_valid_date,
    get_valid_amount,
    get_valid_id,
    get_gift_status
)


def display_menu():
    print("\n========== PERSONAL GIFT TRACKER ==========")
    print("1. Add Gift")
    print("2. View All Gifts")
    print("3. Search Gift")
    print("4. Filter Gifts by Status")
    print("5. Update Gift")
    print("6. Delete Gift")
    print("7. Gift Statistics")
    print("8. Exit")
    print("===========================================")


def get_gift_details():
    person = input("Enter person's name: ").strip()
    occasion = input("Enter occasion: ").strip()
    gift_name = input("Enter gift name: ").strip()

    gift_date = get_valid_date(
        "Enter occasion date (YYYY-MM-DD): "
    )

    budget = get_valid_amount(
        "Enter planned budget (₹): "
    )

    actual_cost = get_valid_amount(
        "Enter actual gift cost (₹): "
    )

    status = get_gift_status()

    notes = input("Enter additional notes: ").strip()

    if not person or not occasion or not gift_name:
        print("Person, occasion, and gift name are required.")
        return None

    return (
        person,
        occasion,
        gift_name,
        gift_date,
        budget,
        actual_cost,
        status,
        notes
    )


def main():
    initialize_storage()

    while True:
        display_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            details = get_gift_details()

            if details:
                add_gift(*details)

        elif choice == "2":
            view_gifts()

        elif choice == "3":
            keyword = input(
                "Enter person, occasion, or gift name: "
            ).strip()

            search_gifts(keyword)

        elif choice == "4":
            status = get_gift_status()
            filter_gifts_by_status(status)

        elif choice == "5":
            gift_id = get_valid_id(
                "Enter gift ID to update: "
            )

            details = get_gift_details()

            if details:
                update_gift(gift_id, *details)

        elif choice == "6":
            gift_id = get_valid_id(
                "Enter gift ID to delete: "
            )

            delete_gift(gift_id)

        elif choice == "7":
            show_statistics()

        elif choice == "8":
            print("Thank you for using Personal Gift Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
