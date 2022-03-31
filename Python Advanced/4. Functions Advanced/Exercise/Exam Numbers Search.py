def numbers_searching(*args):
    result = []
    unique_sequence = set(args)

    for n in range(min(unique_sequence), max(unique_sequence) + 1):
        if n not in unique_sequence:
            result.append(n)
            break

    duplicates = []
    for n in unique_sequence:
        if args.count(n) > 1:
            duplicates.append(n)

    result.append(sorted(duplicates))

    return result


print(numbers_searching(0, 0, 2, 4, 2, 5, 4, 100))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
