from collections import deque
from sys import maxsize


def calculate_pureness(numbers_list):
    total = sum([i * el for i, el in enumerate(numbers_list)])
    return total


def best_list_pureness(numbers_list, rotations):
    numbers_list = deque(numbers_list)
    purest = -maxsize
    purest_rotation = None

    for rotation in range(rotations + 1):
        pureness = calculate_pureness(numbers_list)
        if pureness > purest:
            purest = pureness
            purest_rotation = rotation
        numbers_list.appendleft(numbers_list.pop())

    return f'Best pureness {purest} after {purest_rotation} rotations'


test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)

