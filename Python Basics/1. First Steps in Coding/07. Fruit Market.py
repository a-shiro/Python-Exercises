cost_strawberries = float(input())
amount_bananas = float(input())
amount_oranges = float(input())
amount_raspberries = float(input())
amount_strawberries = float(input())


cost_raspberries_for_1kg = cost_strawberries * 0.5
cost_oranges_for_1kg = cost_raspberries_for_1kg - (0.4 * cost_raspberries_for_1kg)
cost_bananas_for_1kg = cost_raspberries_for_1kg - (0.8 * cost_raspberries_for_1kg)


raspberries_cost = amount_raspberries * cost_raspberries_for_1kg
oranges_cost = amount_oranges * cost_oranges_for_1kg
bananas_cost = amount_bananas * cost_bananas_for_1kg
strawberries_cost = amount_strawberries * cost_strawberries

total_spent = raspberries_cost + oranges_cost + bananas_cost + strawberries_cost

print(total_spent)