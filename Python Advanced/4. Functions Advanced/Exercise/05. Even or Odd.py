def even_odd(*args):
    command = args[-1]
    sequence = args[:-1]

    even_or_odd = 0 if command == 'even' else 1
    result = []

    for x in sequence:
        if x % 2 == even_or_odd:
            result.append(x)
    return result


print(even_odd(1, 2, 3, 4, 5, 6, 'even'))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'odd'))
