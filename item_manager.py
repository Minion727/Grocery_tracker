def add_item(shopping_list):
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


def update_item(shopping_list):
    if len(shopping_list) == 0:
        print("Shopping list is empty.")
        return

    for i in range(len(shopping_list)):
        print(i + 1, ".", shopping_list[i]["name"])

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


def remove_item(shopping_list):
    if len(shopping_list) == 0:
        print("Shopping list is empty.")
        return

    for i in range(len(shopping_list)):
        print(i + 1, ".", shopping_list[i]["name"])

    number = int(input("Enter item number to remove: "))

    if number >= 1 and number <= len(shopping_list):
        removed = shopping_list.pop(number - 1)
        print(removed["name"], "removed successfully.")

    else:
        print("Invalid item number.")


def mark_purchased(shopping_list):
    if len(shopping_list) == 0:
        print("Shopping list is empty.")
        return

    for i in range(len(shopping_list)):
        print(i + 1, ".", shopping_list[i]["name"])

    number = int(input("Enter item number: "))

    if number >= 1 and number <= len(shopping_list):
        shopping_list[number - 1]["purchased"] = True
        print("Item marked as purchased!")

    else:
        print("Invalid item number.")
