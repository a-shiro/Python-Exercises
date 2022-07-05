location_count = int(input())

for location in range(location_count):
    expected_average_income_per_day = float(input())
    days_count_for_location = int(input())
    income = 0
    for days in range(days_count_for_location):
        income_per_day = float(input())
        income += income_per_day

    average_income = income / days_count_for_location
    if average_income >= expected_average_income_per_day:
        print(f"Good job! Average gold per day: {average_income:.2f}.")

    else:
        print(f"You need {expected_average_income_per_day - average_income:.2f} gold.")
