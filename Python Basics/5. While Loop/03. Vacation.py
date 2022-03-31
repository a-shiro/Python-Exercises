holiday_money = float(input())
current_money_saved = float(input())

days = 0
spending_counter = 0

while holiday_money > current_money_saved and spending_counter < 5:
    spend_or_saved = input()
    spent_or_saved_money = float(input())

    days += 1

    if spend_or_saved == "spend":
        current_money_saved -= spent_or_saved_money
        spending_counter += 1
        if current_money_saved < 0:
            current_money_saved = 0

    elif spend_or_saved == "save":
        current_money_saved += spent_or_saved_money
        spending_counter = 0


if spending_counter == 5:
   print("You can't save the money.")
   print(days)

elif current_money_saved >= holiday_money:
    print(f"You saved the money for {days} days.")
