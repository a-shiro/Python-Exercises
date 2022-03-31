flower_type = input()
flower_count = int(input())
budget = int(input())

flower_price = 0

if flower_type == "Roses":
    flower_price = 5
elif flower_type == "Dahlias":
    flower_price = 3.8
elif flower_type == "Tulips":
    flower_price = 2.8
elif flower_type == "Narcissus":
    flower_price = 3
elif flower_type == "Gladiolus":
    flower_price = 2.5

flower_price = flower_price * flower_count

if flower_count > 80 and flower_type == "Roses":
    flower_price = flower_price * 0.90
elif flower_count > 90 and flower_type == "Dahlias":
    flower_price = flower_price * 0.85
elif flower_count > 80 and flower_type == "Tulips":
    flower_price = flower_price * 0.85
elif flower_count < 120 and flower_type == "Narcissus":
    flower_price = flower_price * 1.15
elif flower_count < 80 and flower_type == "Gladiolus":
    flower_price = flower_price * 1.20

if budget >= flower_price:
    left = budget - flower_price
    print(f"Hey, you have a great garden with {flower_count} {flower_type} and {left:.2f} leva left.")
else:
    print(f"Not enough money, you need {flower_price - budget:.2f} leva more.")