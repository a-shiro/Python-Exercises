price_above_20_kg = float(input())
luggage_kg = float(input())
days_until_trip = int(input())
luggage_count = int(input())

fee = 0

if 1 <= luggage_kg < 10:
    fee = price_above_20_kg * 0.20

elif 10 <= luggage_kg <= 20:
    fee = price_above_20_kg * 0.50

elif luggage_kg > 20:
    fee = price_above_20_kg


if days_until_trip > 30:
    fee *= 1.10
    total = fee * luggage_count
    print(f"The total price of bags is: {total:.2f} lv.")

elif 7 <= days_until_trip <= 30:
    fee *= 1.15
    total = fee * luggage_count
    print(f"The total price of bags is: {total:.2f} lv.")
elif days_until_trip < 7:
    fee *= 1.40
    total = fee * luggage_count
    print(f"The total price of bags is: {total:.2f} lv.")


