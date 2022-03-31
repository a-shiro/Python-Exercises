def read_matrix():
    matrix = []

    for row in range(dimensions):
        col = [n for n in input().split(' ')]
        matrix.append(col)

    return matrix


def get_alice_coordinates():
    for row in matrix:
        if 'A' in row:
            alice_row, alice_col = matrix.index(row), row.index('A')
            return alice_row, alice_col


def get_rabbit_hole_coordinates():
    for row in matrix:
        if 'R' in row:
            rabbit_row, rabbit_col = matrix.index(row), row.index('R')
            return rabbit_row, rabbit_col


dimensions = int(input())
matrix = read_matrix()

alice_row, alice_col = get_alice_coordinates()
rabbit_row, rabbit_col = get_rabbit_hole_coordinates()
tea_bags = 0
in_wonderland = True

while in_wonderland and tea_bags < 10:

    direction = input()

    if direction == 'up':
        if 0 > alice_row - 1:
            in_wonderland = False
        elif matrix[alice_row - 1][alice_col] == 'R':
            matrix[rabbit_row][rabbit_col] = '*'
            in_wonderland = False
        else:
            if matrix[alice_row - 1][alice_col] != '.' and matrix[alice_row - 1][alice_col] != '*':
                tea_bags += int(matrix[alice_row - 1][alice_col])
            matrix[alice_row - 1][alice_col] = 'A'
        matrix[alice_row][alice_col] = '*'

    elif direction == 'down':
        if dimensions == alice_row + 1:
            in_wonderland = False
        elif matrix[alice_row + 1][alice_col] == 'R':
            matrix[rabbit_row][rabbit_col] = '*'
            in_wonderland = False
        else:
            if matrix[alice_row + 1][alice_col] != '.' and matrix[alice_row + 1][alice_col] != '*':
                tea_bags += int(matrix[alice_row + 1][alice_col])
            matrix[alice_row + 1][alice_col] = 'A'
        matrix[alice_row][alice_col] = '*'

    elif direction == 'left':
        if 0 > alice_col - 1:
            in_wonderland = False
        elif matrix[alice_row][alice_col - 1] == 'R':
            matrix[rabbit_row][rabbit_col] = '*'
            in_wonderland = False
        else:
            if matrix[alice_row][alice_col - 1] != '.' and matrix[alice_row][alice_col - 1] != '*':
                tea_bags += int(matrix[alice_row][alice_col - 1])
            matrix[alice_row][alice_col - 1] = 'A'
        matrix[alice_row][alice_col] = '*'

    elif direction == 'right':
        if dimensions == alice_col + 1:
            in_wonderland = False
        elif matrix[alice_row][alice_col + 1] == 'R':
            matrix[rabbit_row][rabbit_col] = '*'
            in_wonderland = False
        else:
            if matrix[alice_row][alice_col + 1] != '.' and matrix[alice_row][alice_col + 1] != '*':
                tea_bags += int(matrix[alice_row][alice_col + 1])
            matrix[alice_row][alice_col + 1] = 'A'
        matrix[alice_row][alice_col] = '*'

    if tea_bags >= 10:
        alice_row, alice_col = get_alice_coordinates()
        matrix[alice_row][alice_col] = '*'
    elif in_wonderland:
        alice_row, alice_col = get_alice_coordinates()

if not in_wonderland:
    print("Alice didn't make it to the tea party.")
else:
    print('She did it! She went to the party.')
[print(' '.join(row)) for row in matrix]