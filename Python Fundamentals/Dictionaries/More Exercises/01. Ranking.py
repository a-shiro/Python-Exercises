def most_points_check(candidates_data):

    top_candidate = ""
    top_points = 0

    for key, value in candidates_data.items():
        total_points = 0
        for points in value:
            total_points += value[points]

        if total_points > top_points:

            top_candidate = key
            top_points = total_points

    return top_points, top_candidate


contests_data = {}
candidates_data = {}

contests_and_passwords = input().split(":")

while not contests_and_passwords[0] == "end of contests":

    name, pw = contests_and_passwords[0], contests_and_passwords[1]
    contests_data[name] = pw

    contests_and_passwords = input().split(":")

submissions = input().split("=>")

while not submissions[0] == "end of submissions":

    contest, password, username, points = submissions[0], submissions[1], submissions[2], int(submissions[3])

    if contest in contests_data and contests_data[contest] == password:
        if username not in candidates_data.keys():
            candidates_data[username] = {contest: points}

        elif contest not in candidates_data[username]:
            candidates_data[username].update({contest: points})

        elif candidates_data[username][contest] < points:
            candidates_data[username][contest] = points

    submissions = input().split("=>")

top_points, top_candidate = most_points_check(candidates_data)

print(f"Best candidate is {top_candidate} with total {top_points} points.")
print("Ranking:")

for name, crs_n_pts in sorted(candidates_data.items()):
    print(name)
    for course, points in sorted(crs_n_pts.items(), key=lambda x: -x[1]):
        print(f"#  {course} -> {points}")