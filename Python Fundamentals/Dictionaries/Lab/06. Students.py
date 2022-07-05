command = input()

courses_dict = {}
while ":" in command:

    name, student_id, course = command.split(":")
    if course not in courses_dict:
        courses_dict[course] = []
    student = (name, student_id)
    courses_dict[course].append(student)

    command = input()

if "_" in command:
    command = command.split("_")
    command = " ".join(command)

    for value in courses_dict[command]:
        name, student_id = value
        print(f"{name} - {student_id}")

else:

    for value in courses_dict[command]:
        name, student_id = value
        print(f"{name} - {student_id}")
