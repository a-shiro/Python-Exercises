products = input().split()
searched_products = input().split()

products_dict = {}
for i in range(0, len(products), 2):
    key = products[i]
    value = products[i + 1]

    products_dict[key] = int(value)

for searched_p in searched_products:
    if searched_p in products_dict.keys():
        print(f"We have {products_dict[searched_p]} of {searched_p} left")
    else:
        print(f"Sorry, we don't have {searched_p}")
