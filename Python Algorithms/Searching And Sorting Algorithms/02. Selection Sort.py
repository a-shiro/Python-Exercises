numbers = [int(n) for n in input().split()]

for idx, n in enumerate(numbers):
    min_number = min(numbers[idx:])
    min_number_idx = numbers.index(min_number, idx)

    if min_number < n:
        numbers[idx], numbers[min_number_idx] = numbers[min_number_idx], numbers[idx]

print(*numbers)
