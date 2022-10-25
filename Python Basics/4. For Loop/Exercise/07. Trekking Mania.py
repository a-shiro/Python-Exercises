total_groups_count = int(input())

total_people = 0

mountain_peak_1_people_count = 0
mountain_peak_2_people_count = 0
mountain_peak_3_people_count = 0
mountain_peak_4_people_count = 0
mountain_peak_5_people_count = 0

for _ in range(total_groups_count):

    current_group_count = int(input())
    total_people += current_group_count

    if 0 <= current_group_count <= 5:
        mountain_peak_1_people_count += current_group_count

    elif 6 <= current_group_count <= 12:
        mountain_peak_2_people_count += current_group_count

    elif 13 <= current_group_count <= 25:
        mountain_peak_3_people_count += current_group_count

    elif 26 <= current_group_count <= 40:
        mountain_peak_4_people_count += current_group_count

    else:
        mountain_peak_5_people_count += current_group_count

print(f'{(mountain_peak_1_people_count / total_people) * 100:.2f}%')
print(f'{(mountain_peak_2_people_count / total_people) * 100:.2f}%')
print(f'{(mountain_peak_3_people_count / total_people) * 100:.2f}%')
print(f'{(mountain_peak_4_people_count / total_people) * 100:.2f}%')
print(f'{(mountain_peak_5_people_count / total_people) * 100:.2f}%')
