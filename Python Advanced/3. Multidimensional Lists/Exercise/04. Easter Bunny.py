from collections import deque


def read_matrix(dimensions):
    mtrx = []

    for row in range(dimensions):
        col = [n for n in input().split(' ')]
        mtrx.append(col)

    return mtrx


def get_bunny_coordinates(matrix):
    for row in matrix:
        if 'B' in row:
            bunny_row, bunny_col = matrix.index(row), row.index('B')
            return bunny_row, bunny_col


def get_biggest_sum(matrix, bunny_row, bunny_col):
    directions = deque(['up', 'down', 'left', 'right'])

    coordinates = {'up': [],
                   'down': [],
                   'left': [],
                   'right': []
                   }
    biggest_sum, direction_of_biggest = 0, ''

    while directions:

        current_direction = directions.popleft()
        sum_of_row = 0

        if current_direction == 'up' and bunny_row - 1 >= 0 and matrix[bunny_row - 1][bunny_col] != 'X':
            row = 1
            while not bunny_row - row < 0 and not matrix[bunny_row - row][bunny_col] == 'X':
                sum_of_row += int(matrix[bunny_row - row][bunny_col])
                coordinates['up'].append([bunny_row - row, bunny_col])
                row += 1

        elif current_direction == 'down' and bunny_row + 1 < dimensions and matrix[bunny_row + 1][bunny_col] != 'X':
            row = 1
            while not bunny_row + row == dimensions and not matrix[bunny_row + row][bunny_col] == 'X':
                sum_of_row += int(matrix[bunny_row + row][bunny_col])
                coordinates['down'].append([bunny_row + row, bunny_col])
                row += 1

        elif current_direction == 'left' and bunny_col - 1 >= 0 and matrix[bunny_row][bunny_col - 1] != 'X':
            col = 1
            while not bunny_col - col < 0 and not matrix[bunny_row][bunny_col - col] == 'X':
                sum_of_row += int(matrix[bunny_row][bunny_col - col])
                coordinates['left'].append([bunny_row, bunny_col - col])
                col += 1

        elif current_direction == 'right' and bunny_col + 1 < dimensions and matrix[bunny_row][bunny_col + 1] != 'X':
            col = 1
            while not bunny_col + col == dimensions and not matrix[bunny_row][bunny_col + col] == 'X':
                sum_of_row += int(matrix[bunny_row][bunny_col + col])
                coordinates['right'].append([bunny_row, bunny_col + col])
                col += 1

        if sum_of_row > biggest_sum:
            biggest_sum = sum_of_row
            direction_of_biggest = current_direction

    return biggest_sum, direction_of_biggest, coordinates


dimensions = int(input())
matrix = read_matrix(dimensions)
bunny_row, bunny_col = get_bunny_coordinates(matrix)

biggest_sum, direction_of_biggest, coordinates = get_biggest_sum(matrix, bunny_row, bunny_col)

if direction_of_biggest == '':
    print('right')
    print(*coordinates['right'], sep='\n')
    print(biggest_sum)
else:
    print(direction_of_biggest)
    print(*coordinates[direction_of_biggest], sep='\n')
    print(biggest_sum)
