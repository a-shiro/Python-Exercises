destination = input()

while destination != "End":
    budget = float(input())
    holiday_money = 0

    while budget > holiday_money:
        saving = float(input())
        holiday_money += saving

    print(f"Going to {destination}!")

    destination = input()