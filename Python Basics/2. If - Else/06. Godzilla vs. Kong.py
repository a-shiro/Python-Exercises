budget = float(input())
people = int(input())
outfit_per_person = float(input())

outfit_cost = people * outfit_per_person
decor_cost = budget * 0.10
decor_and_outfit_price = decor_cost + outfit_cost

if people > 150:
 outfit_discount = outfit_cost * 0.1
 outfit_cost = outfit_cost - outfit_discount
 decor_and_outfit_price = decor_cost + outfit_cost

if decor_and_outfit_price > budget:
    money = decor_and_outfit_price - budget
    print(f"Not enough money!")
    print(f"Wingard needs {money:.2f} leva more.")

elif decor_and_outfit_price <= budget:
    money = budget - decor_and_outfit_price
    print(f"Action!")
    print(f"Wingard starts filming with {money:.2f} leva left.")