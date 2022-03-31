def total_price(product, quantity):

    if product == "coffee":
        return 1.5 * quantity
    elif product == "water":
        return 1 * quantity
    elif product == "coke":
        return 1.4 * quantity
    elif product == "snacks":
        return 2 * quantity

product = input()
quantity = int(input())
total = total_price(product,quantity)

print(f"{total:.2f}")