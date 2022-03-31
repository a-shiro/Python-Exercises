rented_place = int(input())

price_cake = rented_place * 0.2
price_drinks = price_cake - (price_cake * 0.45)
price_animator = rented_place / 3

total = price_cake + price_drinks + price_animator + rented_place

print(total)