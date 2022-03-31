students_count = int(input())
lectures_count = int(input())
additional_bonus = int(input())

maximum_bonus_student = 0
maximum_bonus_student_attendances = 0

for student in range(1, students_count + 1):
    attendance_count = int(input())

    total_bonus = attendance_count / lectures_count * (5 + additional_bonus)

    if total_bonus > maximum_bonus_student:
        maximum_bonus_student = total_bonus
        maximum_bonus_student_attendances = attendance_count

print(f"Max Bonus: {round(maximum_bonus_student)}.")
print(f"The student has attended {maximum_bonus_student_attendances} lectures.")
