import math

name = input()
budget = float(input())
beer_count = int(input())
chips_count = int(input())

beer = 1.20
beer_cost = beer_count * beer
b = beer_cost * 0.45
chips_cost = math.ceil(b * chips_count)

total_sum = beer_cost + chips_cost

if total_sum <= budget:
    print(f"{name} bought a snack and has {budget - total_sum:.2f} leva left.")

else:
    print(f"{name} needs {total_sum - budget:.2f} more leva!")

