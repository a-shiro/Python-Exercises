def find_intersection(first_pair, second_pair):

    first_pair_range = set([n_1 for n_1 in range(first_pair[0], first_pair[-1] + 1)])
    second_pair_range = set([n_2 for n_2 in range(second_pair[0], second_pair[-1] + 1)])

    return first_pair_range.intersection(second_pair_range)


n = int(input())

longest_intersection = []

for _ in range(n):

    pair = input().split("-")

    first_pair = [int(x) for x in pair[0].split(",")]
    second_pair = [int(x) for x in pair[1].split(",")]

    intersection = find_intersection(first_pair, second_pair)

    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

print(f"Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}")
