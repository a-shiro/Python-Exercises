first_employee_max = int(input())
second_employee_max = int(input())
third_employee_max = int(input())
total_questions = int(input())


max_questions_per_hour = first_employee_max + second_employee_max + third_employee_max
hours = 0

while not total_questions == 0:
    hours += 1
    if hours % 4 == 0 and not hours == 0:
        continue
    if total_questions >= max_questions_per_hour:
        total_questions -= max_questions_per_hour
    else:
        total_questions -= total_questions

print(f"Time needed: {hours}h.")

