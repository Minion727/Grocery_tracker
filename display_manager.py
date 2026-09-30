def view_list(shopping_list):

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


def purchased_items(shopping_list):

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


def category_items(shopping_list):

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
