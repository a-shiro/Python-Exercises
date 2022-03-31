max_bad_grades = int(input())

last_exercise = ""
bad_grades_count = 0

grade_total = 0
exercise_total = 0


name_exercise = input()
grade = int(input())
while bad_grades_count < max_bad_grades:

    exercise_total += 1
    grade_total += grade

    if grade <= 4:
        bad_grades_count += 1
        if bad_grades_count == max_bad_grades:
            break
        last_exercise = name_exercise
        name_exercise = input()
        if name_exercise == "Enough":
            break
        grade = int(input())

    else:
        last_exercise = name_exercise
        name_exercise = input()
        if name_exercise == "Enough":
            break
        grade = int(input())


average_grade = grade_total / exercise_total

if name_exercise == "Enough":
   print(f"Average score: {average_grade:.2f}")
   print(f"Number of problems: {exercise_total}")
   print(f"Last problem: {last_exercise}")

else:
   print(f"You need a break, {bad_grades_count} poor grades.")


