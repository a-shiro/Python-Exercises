month = input()
nights_count = int(input())

studio = 0
apartment = 0

if month == "May" or month == "October":
    studio = 50
    apartment = 65

elif month == "June" or month == "September":
    studio = 75.20
    apartment = 68.70

elif month == "July" or month == "August":
    studio = 76
    apartment = 77

total_price_studio = studio * nights_count
total_price_apartment = apartment * nights_count


if 14 > nights_count > 7 and (month == "May" or month == "October"):
    total_price_studio = total_price_studio * 0.95

elif nights_count > 14 and (month == "May" or month == "October"):
    total_price_studio = total_price_studio * 0.70

elif nights_count > 14 and (month == "June" or month == "September"):
    total_price_studio = total_price_studio * 0.80


if nights_count > 14:
    total_price_apartment = total_price_apartment * 0.90

print(f"Apartment: {total_price_apartment:.2f} lv.")
print(f"Studio: {total_price_studio:.2f} lv.")