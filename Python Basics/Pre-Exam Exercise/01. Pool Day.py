import math

people = int(input())
entry_fee = float(input())
sunbed_price = float(input())
umbrella = float(input())


people_with_sunbed = math.ceil(people * 0.75)
umbrellas_needed = math.ceil(people * 0.50)

entry_fee_total = people * entry_fee
umbrellas_total = umbrella * umbrellas_needed
sunbed_total = people_with_sunbed * sunbed_price

total = entry_fee_total + umbrellas_total + sunbed_total

print(f"{total:.2f} lv.")
