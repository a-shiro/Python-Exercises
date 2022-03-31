from collections import deque


def read_matrix(dimensions):
    mtrx = []

    for row in range(dimensions):
        col = [n for n in input().split(' ')]
        mtrx.append(col)

    return mtrx


def get_miner_position(matrix, dimensions):
    miner_pos, miner_row = None, None

    for row in range(dimensions):
        if 's' in matrix[row]:
            miner_pos, miner_row = matrix[row].index('s'), row
            return miner_row, miner_pos


def check_for_coal(matrix, dimensions):
    coal = 0

    for row in range(dimensions):
        if 'c' in matrix[row]:
            coal += matrix[row].count('c')

    return coal


dimensions = int(input())
commands = deque(input().split(' '))

matrix = read_matrix(dimensions)
miner_row, miner_pos = get_miner_position(matrix, dimensions)

found_e = False

while commands:

    current_command = commands.popleft()

    if current_command == 'up' and miner_row - 1 >= 0:
        if matrix[miner_row - 1][miner_pos] == 'c':
            matrix[miner_row - 1][miner_pos], matrix[miner_row][miner_pos] = \
                matrix[miner_row][miner_pos], '*'
        elif matrix[miner_row - 1][miner_pos] == 'e':
            matrix[miner_row - 1][miner_pos], matrix[miner_row][miner_pos] = \
                matrix[miner_row][miner_pos], '*'
            found_e = True
        else:
            matrix[miner_row - 1][miner_pos], matrix[miner_row][miner_pos] = \
                matrix[miner_row][miner_pos], matrix[miner_row - 1][miner_pos]
        miner_row -= 1

    elif current_command == 'down' and miner_row + 1 < dimensions:
        if matrix[miner_row + 1][miner_pos] == 'c':
            matrix[miner_row + 1][miner_pos], matrix[miner_row][miner_pos] = \
                matrix[miner_row][miner_pos], '*'
        elif matrix[miner_row + 1][miner_pos] == 'e':
            matrix[miner_row - 1][miner_pos], matrix[miner_row][miner_pos] = \
                matrix[miner_row][miner_pos], '*'
            found_e = True
        else:
            matrix[miner_row + 1][miner_pos], matrix[miner_row][miner_pos] = \
                matrix[miner_row][miner_pos], matrix[miner_row + 1][miner_pos]
        miner_row += 1

    elif current_command == 'left' and miner_pos - 1 >= 0:
        if matrix[miner_row][miner_pos - 1] == 'c':
            matrix[miner_row][miner_pos - 1], matrix[miner_row][miner_pos] = \
                matrix[miner_row][miner_pos], '*'
        elif matrix[miner_row][miner_pos - 1] == 'e':
            matrix[miner_row - 1][miner_pos], matrix[miner_row][miner_pos] = \
                matrix[miner_row][miner_pos], '*'
            found_e = True
        else:
            matrix[miner_row][miner_pos - 1], matrix[miner_row][miner_pos] = \
                matrix[miner_row][miner_pos], matrix[miner_row][miner_pos - 1]
        miner_pos -= 1

    elif current_command == 'right' and miner_pos + 1 < dimensions:
        if matrix[miner_row][miner_pos + 1] == 'c':
            matrix[miner_row][miner_pos + 1], matrix[miner_row][miner_pos] = \
                matrix[miner_row][miner_pos], '*'
        elif matrix[miner_row][miner_pos + 1] == 'e':
            matrix[miner_row - 1][miner_pos], matrix[miner_row][miner_pos] = \
                matrix[miner_row][miner_pos], '*'
            found_e = True
        else:
            matrix[miner_row][miner_pos + 1], matrix[miner_row][miner_pos] = \
                matrix[miner_row][miner_pos], matrix[miner_row][miner_pos + 1]
        miner_pos += 1

    if found_e:
        break

coal = check_for_coal(matrix, dimensions)

if found_e:
    print(f'Game over! ({miner_row}, {miner_pos})')
elif coal > 0:
    print(f'{coal} pieces of coal left. ({miner_row}, {miner_pos})')
elif coal == 0:
    print(f'You collected all coal! ({miner_row}, {miner_pos})')
