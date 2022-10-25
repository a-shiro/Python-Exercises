def sum_numbers(numbers, idx):
    if len(numbers) - 1 == idx:
        return numbers[idx]

    return numbers[idx] + sum_numbers(numbers, idx + 1)


numbers = [int(n) for n in input().split()]

print(sum_numbers(numbers, 0))
