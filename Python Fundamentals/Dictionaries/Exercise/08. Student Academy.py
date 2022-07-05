number_inputs = int(input())

students = {}
students_average = {}

for ipt in range(number_inputs):

    name = input()
    grade = float(input())

    if name not in students:
        students[name] = []
    students[name].append(grade)

for student, grades in students.items():

    average_grade = sum(grades) / len(grades)
    if not average_grade < 4.5:
        students_average[student] = average_grade

sorted_student_average = sorted(students_average.items(), key=lambda s: -s[1])

for tup in sorted_student_average:

    student, grade = tup
    print(f"{student} -> {grade:.2f}")
