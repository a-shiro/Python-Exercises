budget = int(input())
season = input()
fisherman_count = int(input())

ship_rent = 0

if season == "Spring":
    ship_rent = 3000
elif season == "Summer" or season == "Autumn":
    ship_rent = 4200
elif season == "Winter":
    ship_rent = 2600

if 11 >= fisherman_count > 6:
    ship_rent = ship_rent * 0.85
elif fisherman_count <= 6:
    ship_rent = ship_rent * 0.90
else:
    ship_rent = ship_rent * 0.75

if fisherman_count % 2 == 0 and season != "Autumn":
    ship_rent = ship_rent * 0.95

if budget >= ship_rent:
    money_left = budget - ship_rent
    print(f"Yes! You have {money_left:.2f} leva left. ")
else:
    money_needed = ship_rent - budget
    print(f"Not enough money! You need {money_needed:.2f} leva.")