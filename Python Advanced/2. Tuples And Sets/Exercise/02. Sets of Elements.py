n, m = map(int, input().split())

first_set = set()
second_set = set()

counter = 0

for _ in range(n + m):

    number = int(input())
    counter += 1

    if counter <= n:
        first_set.add(number)
    else:
        second_set.add(number)

[print(x) for x in first_set.intersection(second_set)]