budget = float(input())

graphic_cards_count = int(input())
cpus_count = int(input())
ram_count = int(input())

graphic_card_price = 250
cpu_price = .35 * (graphic_cards_count * graphic_card_price)
ram_price = .1 * (graphic_cards_count * graphic_card_price)

graphic_cards_total = graphic_cards_count * graphic_card_price
cpu_total = cpus_count * cpu_price
ram_total = ram_count * ram_price

total_cost = graphic_cards_total + cpu_total + ram_total

if graphic_cards_count > cpus_count:
    total_cost -= total_cost * 0.15


if total_cost <= budget:
    money_left = budget - total_cost

    print(f"You have {money_left:.2f} leva left!")

else:
    money_needed = total_cost - budget

    print(f"Not enough money! You need {money_needed:.2f} leva more!")
