import re

data = input()
pattern = r"^>>(?P<furniture>[A-Za-z]+)<<(?P<price>[\d+\.?]+)!(?P<qty>\d+)$"
total_spend = 0
furniture_list = []

while not data == "Purchase":

    match = re.match(pattern, data)

    if match is not None:
        furniture = match.group("furniture")
        price = float(match.group("price"))
        qty = int(match.group("qty"))

        total_spend += float(price) * int(qty)
        furniture_list.append(furniture)

    data = input()

print("Bought furniture:")
for furniture in furniture_list:
    print(furniture)
print(f"Total money spend: {total_spend:.2f}")
