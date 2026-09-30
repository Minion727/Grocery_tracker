shopping_list = []
budget = 0


def add_item():
    name = input("Enter item name: ")
    category = input("Enter category: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per item: "))

    item = {
        "name": name,
        "category": category,
        "quantity": quantity,
        "price": price,
        "purchased": False
    }

    shopping_list.append(item)
    print("Item added successfully!")


def view_list():
    if len(shopping_list) == 0:
        print("Shopping list is empty.")
        return

    print("\n----------- SHOPPING LIST -----------")
    
    for i in range(len(shopping_list)):
        item = shopping_list[i]

        total_price = item["quantity"] * item["price"]

        if item["purchased"]:
            status = "Purchased"
        else:
            status = "Pending"

        print("\nItem Number:", i + 1)
        print("Name:", item["name"])
        print("Category:", item["category"])
        print("Quantity:", item["quantity"])
        print("Price per item: ₹", item["price"])
        print("Total Price: ₹", total_price)
        print("Status:", status)

    print("------------------------------------")


def update_item():
    view_list()

    if len(shopping_list) == 0:
        return

    number = int(input("Enter item number to update: "))

    if number >= 1 and number <= len(shopping_list):
        item = shopping_list[number - 1]

        print("\n1. Update Name")
        print("2. Update Category")
        print("3. Update Quantity")
        print("4. Update Price")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            item["name"] = input("Enter new name: ")

        elif choice == 2:
            item["category"] = input("Enter new category: ")

        elif choice == 3:
            item["quantity"] = int(input("Enter new quantity: "))

        elif choice == 4:
            item["price"] = float(input("Enter new price: "))

        else:
            print("Invalid choice.")
            return

        print("Item updated successfully!")

    else:
        print("Invalid item number.")


def remove_item():
    view_list()

    if len(shopping_list) == 0:
        return

    number = int(input("Enter item number to remove: "))

    if number >= 1 and number <= len(shopping_list):
        removed_item = shopping_list.pop(number - 1)
        print(removed_item["name"], "removed successfully.")

    else:
        print("Invalid item number.")


def mark_purchased():
    view_list()

    if len(shopping_list) == 0:
        return

    number = int(input("Enter item number: "))

    if number >= 1 and number <= len(shopping_list):
        shopping_list[number - 1]["purchased"] = True
        print("Item marked as purchased!")

    else:
        print("Invalid item number.")


def purchased_items():
    found = False

    print("\n--------- PURCHASED ITEMS ---------")

    for item in shopping_list:
        if item["purchased"]:
            total_price = item["quantity"] * item["price"]

            print("Name:", item["name"])
            print("Category:", item["category"])
            print("Quantity:", item["quantity"])
            print("Total Price: ₹", total_price)
            print("--------------------------------")

            found = True

    if found == False:
        print("No purchased items.")


def category_items():
    category = input("Enter category: ")
    found = False

    print("\n--------- CATEGORY ITEMS ---------")

    for item in shopping_list:
        if item["category"].lower() == category.lower():
            print("Name:", item["name"])
            print("Quantity:", item["quantity"])
            print("Price: ₹", item["price"])
            print("--------------------------------")

            found = True

    if found == False:
        print("No items found in this category.")


def total_expense():
    total = 0

    for item in shopping_list:
        total = total + item["quantity"] * item["price"]

    print("\nTotal Shopping Expense: ₹", total)

    if budget > 0:
        remaining = budget - total

        if remaining >= 0:
            print("Remaining Budget: ₹", remaining)
        else:
            print("Budget exceeded by: ₹", -remaining)


def set_budget():
    global budget

    budget = float(input("Enter your shopping budget: ₹"))

    print("Budget set successfully!")
    print("Your Budget: ₹", budget)


def main():
    while True:

        print("===================================")
        print("       GROCERY MANAGER             ")
        print("===================================")
        print("1. Add Item")
        print("2. View Shopping List")
        print("3. Update Item")
        print("4. Remove Item")
        print("5. Mark Item as Purchased")
        print("6. View Purchased Items")
        print("7. View Items by Category")
        print("8. View Total Expense")
        print("9. Set Budget")
        print("10. Exit")
        print("===================================")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_item()

        elif choice == 2:
            view_list()

        elif choice == 3:
            update_item()

        elif choice == 4:
            remove_item()

        elif choice == 5:
            mark_purchased()

        elif choice == 6:
            purchased_items()

        elif choice == 7:
            category_items()

        elif choice == 8:
            total_expense()

        elif choice == 9:
            set_budget()

        elif choice == 10:
            print("Thank you for using Grocery Manager!")
            break

        else:
            print("Invalid choice. Please try again.")


main()
