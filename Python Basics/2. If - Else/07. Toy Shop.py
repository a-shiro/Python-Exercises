puzzle = 2.60
doll = 3
bear = 4.10
minion = 8.20
truck = 2

price_holiday = float(input())
num_puzzles = int(input())
num_dolls = int(input())
num_bears = int(input())
num_minions = int(input())
num_trucks = int(input())

total_toys = num_puzzles + num_dolls + num_bears + num_minions + num_trucks
total_money = (num_puzzles * puzzle) + (num_dolls * doll) + (num_bears * bear) + (num_minions * minion) + (num_trucks * truck)

if total_toys >= 50:
    total_money = total_money - (total_money * 0.25)
    total_money = total_money - (total_money * 0.10)

elif total_toys < 50:
    total_money = total_money - (total_money * 0.10)

if total_money >= price_holiday:
    print(f"Yes! {(total_money - price_holiday):.2f} lv left.")

elif total_money < price_holiday:
    print(f"Not enough money! {(price_holiday - total_money):.2f} lv needed.")




