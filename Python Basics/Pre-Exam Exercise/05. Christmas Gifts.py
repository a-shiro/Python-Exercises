adults = 0
kids = 0
total_money_toys = 0
total_money_sweaters = 0

command = input()
while command != "Christmas":
    years_old = int(command)
    if years_old <= 16:
        kids += 1
        total_money_toys += 5

    elif years_old > 16:
        adults +=1
        total_money_sweaters += 15

    command = input()

print(f"Number of adults: {adults}")
print(f"Number of kids: {kids}")
print(f"Money for toys: {total_money_toys}")
print(f"Money for sweaters: {total_money_sweaters}")
