number_days = int(input())
number_pastry_cooks = int(input())
number_cakes = int(input())
number_waffles = int(input())
number_pancakes = int(input())

cake_cost = 45
waffle_cost = 5.8
pancake_cost = 3.2

cakes_made = number_cakes * cake_cost
waffles_made = number_waffles * waffle_cost
pancake_made = number_pancakes * pancake_cost

total_sweets = (cakes_made + waffles_made + pancake_made) * number_pastry_cooks
total_money_collected = total_sweets * number_days
fees = total_money_collected * 1/8
total_money_after_fees = total_money_collected - fees

print(total_money_after_fees)