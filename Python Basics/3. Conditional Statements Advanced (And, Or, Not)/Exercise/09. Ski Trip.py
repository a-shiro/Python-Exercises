one_person_room_price = 18
apartment_price = 25
presidential_apartment = 35

days = int(input()) - 1
type_of_place = input()
review = input()

holiday_cost = 0

if type_of_place == 'room for one person':
    holiday_cost = days * one_person_room_price

elif type_of_place == 'apartment':
    holiday_cost = days * apartment_price
    discount = 0

    if 0 < days < 10:
        discount = holiday_cost * .3

    elif 10 <= days <= 15:
        discount = holiday_cost * .35

    elif days > 15:
        discount = holiday_cost * .5

    holiday_cost -= discount

else:
    holiday_cost = days * presidential_apartment
    discount = 0

    if 0 < days < 10:
        discount = holiday_cost * .1

    elif 10 <= days <= 15:
        discount = holiday_cost * .15

    elif days > 15:
        discount = holiday_cost * .2

    holiday_cost -= discount

if review == 'positive':
    holiday_cost += holiday_cost * .25

else:
    holiday_cost -= holiday_cost * .1

print(f'{holiday_cost:.2f}')
