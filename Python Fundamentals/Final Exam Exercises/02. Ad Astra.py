import re

products = input()
pattern = r"(#|\|)(?P<product>[A-Za-z\s]+)(\1)(?P<exp_date>[0-9]{2}\/[0-9]{2}\/[0-9]{2})(\1)(?P<calories>[0-9]+)(\1)"
total_calories = 0

calorie_match = re.finditer(pattern, products)

for match in calorie_match:

    calories = int(match.group("calories"))
    total_calories += calories

print(f"You have food to last you for: {total_calories // 2000} days!")
data_match = re.finditer(pattern, products)
for data in data_match:
    print(f"Item: {data[2]}, Best before: {data[4]}, Nutrition: {data[6]}")

