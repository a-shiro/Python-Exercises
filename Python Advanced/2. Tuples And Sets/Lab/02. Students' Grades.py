def get_average(g):
    return sum(g) / len(g)


n = int(input())

students_record = {}

for _ in range(n):

    student, grade = input().split()

    if student not in students_record:
        students_record[student] = []
    students_record[student].append(float(grade))

for s, g in students_record.items():

    average = get_average(g)
    grades = ' '.join(f"{x:.2f}" for x in g)

    print(f"{s} -> {grades} (avg: {average:.2f})")
