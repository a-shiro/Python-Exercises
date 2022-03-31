def create_individual_statistics(participants_dict):

    individual_statistics = {}

    for v in participants_dict.values():
        for u, p in v.items():
            if u not in individual_statistics:
                individual_statistics[u] = p
            else:
                individual_statistics[u] += p

    return individual_statistics


participants_dict = {}

participants_data = input().split(" -> ")

while not participants_data[0] == "no more time":

    username, contest_name, points = participants_data[0], participants_data[1], int(participants_data[2])

    if contest_name not in participants_dict:
        participants_dict[contest_name] = {username: points}

    elif username not in participants_dict[contest_name]:
        participants_dict[contest_name].update({username: points})

    elif participants_dict[contest_name][username] < points:
        participants_dict[contest_name][username] = points

    participants_data = input().split(" -> ")


individual_statistics = create_individual_statistics(participants_dict)


for k, v in participants_dict.items():
    print(f"{k}: {len(participants_dict[k])} participants")
    pos = 1
    for u, p in sorted(v.items(), key=lambda x: (-x[1], x[0])):
        print(f"{pos}. {u} <::> {p}")
        pos += 1

print("Individual standings:")
pos = 1
for u, p in sorted(individual_statistics.items(), key=lambda x: (-x[1], x[0])):
    print(f"{pos}. {u} -> {p}")
    pos += 1
