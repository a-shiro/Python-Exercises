value = input()

parts_price = 0
taxes = 0
total_price = 0

while not value == "regular" and not value == "special":
    value = float(value)
    if value < 0:
        print("Invalid price!")
        value = input()
        continue

    parts_price += value
    taxes += value * 0.2

    value = input()

if value == "special":
    total_price = parts_price + taxes
    total_price -= total_price * 0.1
else:
    total_price = parts_price + taxes

if total_price == 0:
    print("Invalid order!")
else:
    print(f"""Congratulations you've just bought a new computer!
Price without taxes: {parts_price:.2f}$
Taxes: {taxes:.2f}$
-----------
Total price: {total_price:.2f}$""")