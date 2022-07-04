price_for_1_page = float(input())
price_for_1_cover = float(input())
percent_discount = int(input())
designer_fee = float(input())
team_discount = int(input())

raw_sum = price_for_1_page * 899 + price_for_1_cover * 2
discount = percent_discount / 100
sum_with_discount = raw_sum - (raw_sum * discount)
sum_after_designer_fee = sum_with_discount + designer_fee
total_after_team_discount = sum_after_designer_fee - (sum_after_designer_fee * team_discount /100)

print(f"Avtonom should pay {total_after_team_discount:.2f} BGN.")
