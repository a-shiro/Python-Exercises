items_bought = []
sales_list = []
profit = 0

item_collection = input().split("|")
budget = float(input())

for item in item_collection:

    item_type, item_price = item.split("->")
    item_price = float(item_price)

    if item_type == "Clothes" and item_price <= 50 and budget >= item_price:
        budget -= item_price
        items_bought.append(item_price)

    elif item_type == "Shoes" and item_price <= 35 and budget >= item_price:
        budget -= item_price
        items_bought.append(item_price)

    elif item_type == "Accessories" and item_price <= 20.50 and budget >= item_price:
        budget -= item_price
        items_bought.append(item_price)

for item in items_bought:

    sell_price = item * 1.4
    profit += sell_price - item

    budget += sell_price

    sell_price = (f"{sell_price:.2f}")
    sales_list.append(str(sell_price))

print(" ".join(sales_list))
print(f"Profit: {profit:.2f}")
if budget >= 150:
    print("Hello, France!")
else:
    print("Time to go.")
