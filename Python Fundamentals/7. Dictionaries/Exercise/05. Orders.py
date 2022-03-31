product_info = input().split()

product_info_dict = {}
while not product_info[0] == "buy":

    name, price, qty = product_info

    if name not in product_info_dict:
        product_info_dict[name] = [float(price), int(qty)]

    else:
        product_info_dict[name][1] += int(qty)
        product_info_dict[name][0] = price

    product_info = input().split()

for key, value in product_info_dict.items():
    print(f"{key} -> {float(value[0]) * int(value[1]):.2f}")
