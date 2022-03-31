number_of_pages = int(input())
pages_for_1_hour = int(input())
number_of_days = int(input())

time_needed_for_book = number_of_pages / pages_for_1_hour
hours_per_day = time_needed_for_book / number_of_days

print(hours_per_day)