numbers = [float(n) for n in input().split()]

numbers_count = {}

for n in numbers:

    if n not in numbers_count:
        numbers_count[n] = 0

    numbers_count[n] += 1

[print(f"{n} - {count} times") for n, count in numbers_count.items()]