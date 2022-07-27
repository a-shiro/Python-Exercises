numbers = [int(n) for n in input().split()]

is_sorted = False
counter = 0

while not is_sorted:
    is_sorted = True

    for idx in range(1, len(numbers) - counter):
        if numbers[idx] < numbers[idx - 1]:
            numbers[idx], numbers[idx - 1] = numbers[idx - 1], numbers[idx]
            is_sorted = False

    counter += 1

print(*numbers)