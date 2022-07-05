command = input().split(": ")

products_dict = {}
while not command[0] == "statistics":
    key = command[0]
    value = int(command[1])

    if key not in products_dict.keys():
        products_dict[key] = value
    else:
        products_dict[key] += value

    command = input().split(": ")

print("Products in stock:")
for key in products_dict.keys():
    print(f"- {key}: {products_dict[key]}")

print(f"Total Products: {len(products_dict.keys())}")
print(f"Total Quantity: {sum(products_dict.values())}")