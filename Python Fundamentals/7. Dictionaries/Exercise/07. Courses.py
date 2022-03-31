command = input().split(" : ")

courses_dict = {}

while not command[0] == "end":

    if command[0] not in courses_dict:
        courses_dict[command[0]] = []
    courses_dict[command[0]].append(command[1])

    command = input().split(" : ")

sorted_courses = sorted(courses_dict.items(), key=lambda c: -len(c[1]))
for el in sorted_courses:
    course, students = el

    print(f"{course}: {len(students)}")
    students.sort()
    for student in students:
        print(f"-- {student}")
