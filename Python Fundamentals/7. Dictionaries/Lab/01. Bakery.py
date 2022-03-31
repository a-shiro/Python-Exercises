products = input().split()

products_dict = {}
for i in range(0, len(products), 2):
    key = products[i]
    value = products[i + 1]

    products_dict[key] = int(value)

print(products_dict)

