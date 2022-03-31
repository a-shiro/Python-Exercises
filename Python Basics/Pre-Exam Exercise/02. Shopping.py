budget = float(input())

videocard = int(input())
processor = int(input())
ram = int(input())

price_videocard = videocard * 250
price_processor = price_videocard * 0.35
price_ram = price_videocard * 0.10

total_price = price_videocard + (processor * price_processor) + (ram * price_ram)

if videocard > processor:
    total_price *= 0.85

if budget >= total_price:
    print(f"You have {budget - total_price:.2f} leva left!")
else:
    print(f"Not enough money! You need {total_price - budget:.2f} leva more!")