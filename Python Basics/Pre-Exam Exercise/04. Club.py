wanted_income = float(input())
total_income = 0

cocktail = input()

while cocktail != "Party!":

    order = int(input())

    cocktail_price = len(cocktail)
    cocktail_price = order * cocktail_price

    if cocktail_price % 2 != 0:

        discount = cocktail_price - (cocktail_price * 0.25)
        total_income += discount
    else:
        total_income += cocktail_price

    if total_income >= wanted_income:
        break
    cocktail = input()

if cocktail == "Party!":
    print(f"We need {wanted_income - total_income:.2f} leva more.")

elif total_income >= wanted_income:
    print("Target acquired.")

print(f"Club income - {total_income:.2f} leva.")


