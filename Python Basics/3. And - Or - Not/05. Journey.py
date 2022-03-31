budget = float(input())
season = input()

destination = ""
type = ""
money_spent = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        type = "Camp"
        money_spent = budget * 0.30
    elif season == "winter":
        type = "Hotel"
        money_spent = budget * 0.70

elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        type = "Camp"
        money_spent = budget * 0.40
    elif season == "winter":
        type = "Hotel"
        money_spent = budget * 0.80

else:
    destination = "Europe"
    type = "Hotel"
    money_spent = budget * 0.90

print(f"Somewhere in {destination}")
print(f"{type} - {money_spent:.2f}")
