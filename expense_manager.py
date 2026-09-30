def total_expense(shopping_list, budget):

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

    return total
