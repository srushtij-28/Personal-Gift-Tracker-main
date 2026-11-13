from storage import load_gifts, save_gifts


def add_gift(person, occasion, gift_name, gift_date,
             budget, actual_cost, status, notes):

    gifts = load_gifts()

    gift_id = max(
        [gift["id"] for gift in gifts],
        default=0
    ) + 1

    gift = {
        "id": gift_id,
        "person": person,
        "occasion": occasion,
        "gift_name": gift_name,
        "gift_date": gift_date,
        "budget": budget,
        "actual_cost": actual_cost,
        "status": status,
        "notes": notes
    }

    gifts.append(gift)
    save_gifts(gifts)

    print("\nGift added successfully!")


def view_gifts():
    gifts = load_gifts()

    if not gifts:
        print("\nNo gift records found.")
        return

    print("\n" + "-" * 110)
    print(
        f"{'ID':<5} {'Person':<18} {'Occasion':<18} "
        f"{'Gift':<20} {'Budget':<12} {'Status':<12}"
    )
    print("-" * 110)

    for gift in gifts:
        print(
            f"{gift['id']:<5} "
            f"{gift['person'][:17]:<18} "
            f"{gift['occasion'][:17]:<18} "
            f"{gift['gift_name'][:19]:<20} "
            f"₹{gift['budget']:<11.2f} "
            f"{gift['status']:<12}"
        )

    print("-" * 110)


def display_gift_details(gifts):
    if not gifts:
        print("\nNo matching gifts found.")
        return

    for gift in gifts:
        print("\n" + "=" * 45)
        print(f"Gift ID: {gift['id']}")
        print(f"Person: {gift['person']}")
        print(f"Occasion: {gift['occasion']}")
        print(f"Gift Name: {gift['gift_name']}")
        print(f"Gift Date: {gift['gift_date']}")
        print(f"Budget: ₹{gift['budget']:.2f}")
        print(f"Actual Cost: ₹{gift['actual_cost']:.2f}")
        print(f"Status: {gift['status']}")
        print(f"Notes: {gift['notes'] or 'N/A'}")
        print("=" * 45)


def search_gifts(keyword):
    gifts = load_gifts()
    keyword = keyword.lower()

    results = [
        gift for gift in gifts
        if keyword in gift["person"].lower()
        or keyword in gift["occasion"].lower()
        or keyword in gift["gift_name"].lower()
    ]

    display_gift_details(results)


def filter_gifts_by_status(status):
    gifts = load_gifts()

    results = [
        gift for gift in gifts
        if gift["status"] == status
    ]

    display_gift_details(results)


def update_gift(gift_id, person, occasion, gift_name,
                gift_date, budget, actual_cost, status, notes):

    gifts = load_gifts()

    for gift in gifts:
        if gift["id"] == gift_id:
            gift["person"] = person
            gift["occasion"] = occasion
            gift["gift_name"] = gift_name
            gift["gift_date"] = gift_date
            gift["budget"] = budget
            gift["actual_cost"] = actual_cost
            gift["status"] = status
            gift["notes"] = notes

            save_gifts(gifts)

            print("\nGift updated successfully!")
            return

    print("\nGift ID not found.")


def delete_gift(gift_id):
    gifts = load_gifts()

    updated_gifts = [
        gift for gift in gifts
        if gift["id"] != gift_id
    ]

    if len(updated_gifts) == len(gifts):
        print("\nGift ID not found.")
        return

    save_gifts(updated_gifts)
    print("\nGift deleted successfully.")


def show_statistics():
    gifts = load_gifts()

    if not gifts:
        print("\nNo gift statistics available.")
        return

    total_gifts = len(gifts)

    planned = sum(
        1 for gift in gifts
        if gift["status"] == "Planned"
    )

    purchased = sum(
        1 for gift in gifts
        if gift["status"] == "Purchased"
    )

    given = sum(
        1 for gift in gifts
        if gift["status"] == "Given"
    )

    total_budget = sum(
        gift["budget"] for gift in gifts
    )

    total_spent = sum(
        gift["actual_cost"] for gift in gifts
    )

    remaining_budget = total_budget - total_spent

    print("\n========== GIFT STATISTICS ==========")
    print(f"Total Gifts: {total_gifts}")
    print(f"Planned Gifts: {planned}")
    print(f"Purchased Gifts: {purchased}")
    print(f"Given Gifts: {given}")
    print(f"Total Budget: ₹{total_budget:.2f}")
    print(f"Total Spent: ₹{total_spent:.2f}")
    print(f"Budget Remaining: ₹{remaining_budget:.2f}")
    print("=====================================")
