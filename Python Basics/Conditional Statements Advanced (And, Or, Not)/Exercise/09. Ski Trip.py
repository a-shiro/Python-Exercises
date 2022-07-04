days = int(input())
room_type = input()
review = input()

room_for_one_person = 0
apartment_price = 0
president_apartment_price = 0

if room_type == "room for one files_01_Wild_Cat_Zoo":
    room_for_one_person = 18 * (days - 1)

elif room_type == "apartment":
    apartment_price = 25 * (days - 1)

    if (days - 1) < 10:
        apartment_price = apartment_price - (apartment_price * 0.30)
    elif 10 <= (days - 1) < 15:
        apartment_price = apartment_price - (apartment_price * 0.35)
    else:
        apartment_price = apartment_price - (apartment_price * 0.50)

elif room_type == "president apartment":
    president_apartment_price = 35 * (days - 1)

    if (days - 1) < 10:
        president_apartment_price = president_apartment_price - (president_apartment_price * 0.10)
    elif 10 <= (days - 1) < 15:
        president_apartment_price = president_apartment_price - (president_apartment_price * 0.15)
    else:
        president_apartment_price = president_apartment_price - (president_apartment_price * 0.20)


if review == "positive":
    if room_type == "room for one files_01_Wild_Cat_Zoo":
        total_price = room_for_one_person + (room_for_one_person * 0.25)
        print(f"{total_price:.2f}")
    elif room_type == "apartment":
        total_price = apartment_price + (apartment_price * 0.25)
        print(f"{total_price:.2f}")
    elif room_type == "president apartment":
        total_price = president_apartment_price + (president_apartment_price * 0.25)
        print(f"{total_price:.2f}")

elif review == "negative":
    if room_type == "room for one files_01_Wild_Cat_Zoo":
        total_price = room_for_one_person - (room_for_one_person * 0.10)
        print(f"{total_price:.2f}")
    elif room_type == "apartment":
        total_price = apartment_price - (apartment_price * 0.10)
        print(f"{total_price:.2f}")
    elif room_type == "president apartment":
        total_price = president_apartment_price - (president_apartment_price * 0.10)
        print(f"{total_price:.2f}")



