budget = 0

age = int(input())
money_needed = float(input())
toy_price = int(input())

money_income = 10

for i in range(1, age + 1):
    if i % 2 != 0:
        budget += toy_price
    else:
        money_stolen = 1

        budget += money_income
        budget -= money_stolen

        money_income += 10

if budget >= money_needed:
    money_left = budget - money_needed

    print(f'Yes! {money_left:.2f}')

else:
    money_needed = money_needed - budget

    print(f'No! {money_needed:.2f}')
