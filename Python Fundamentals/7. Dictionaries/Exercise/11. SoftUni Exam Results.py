def is_banned(students_info):

    if students_info[1] == "banned":
        del results[students_info[0]]
        return True


students_info = input().split("-")

submissions = {}
results = {}

while not students_info[0] == "exam finished":

    if is_banned(students_info):
        students_info = input().split("-")
        continue

    if students_info[0] not in results:
        results[students_info[0]] = int(students_info[2])
    else:
        if results[students_info[0]] < int(students_info[2]):
            results[students_info[0]] = int(students_info[2])

    if students_info[1] not in submissions:
        submissions[students_info[1]] = 1
    else:
        submissions[students_info[1]] += 1

    students_info = input().split("-")

sorted_results = sorted(results.items(), key=lambda x: (-int(x[1]), x[0]))
sorted_submissions = sorted(submissions.items(), key=lambda x: (-int(x[1]), x[0]))

print("Results:")
for pair in sorted_results:
    print(f"{pair[0]} | {pair[1]}")

print("Submissions:")
for pair in sorted_submissions:
    print(f"{pair[0]} - {pair[1]}")