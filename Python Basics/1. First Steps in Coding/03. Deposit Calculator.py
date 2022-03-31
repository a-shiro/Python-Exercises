deposited_sum = float(input())
time_of_deposit = int(input())
yearly_percentage = float(input())

interest_amount = deposited_sum * yearly_percentage /100
interest_amount_1month = interest_amount / 12
total_sum = deposited_sum + time_of_deposit * interest_amount_1month

print(total_sum)