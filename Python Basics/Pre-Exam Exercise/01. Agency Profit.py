name = input()
number_adult_tickets = int(input())
number_kid_tickets = int(input())
adult_ticket_price = float(input())
service_fee = float(input())

kid_ticket_price = adult_ticket_price - (adult_ticket_price * 0.7)

adult_ticket_after_fee = adult_ticket_price + service_fee
kid_ticket_after_fee = kid_ticket_price + service_fee

total_sum = number_adult_tickets * adult_ticket_after_fee + number_kid_tickets * kid_ticket_after_fee
profit = total_sum * 0.20

print(f"The profit of your agency from {name} tickets is {profit:.2f} lv.")