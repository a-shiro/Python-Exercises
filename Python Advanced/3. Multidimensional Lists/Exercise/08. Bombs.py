from collections import deque


def read_matrix(dimensions):

    mtrx = []

    for _ in range(dimensions):
        col = [int(n) for n in input().split(' ')]
        mtrx.append(col)

    return mtrx


def get_cells(matrix):

    cells_alive = 0
    cells_sum = 0

    for r in matrix:
        for c in r:
            if c > 0:
                cells_alive += 1
                cells_sum += c

    return cells_alive, cells_sum


dimensions = int(input())
matrix = read_matrix(dimensions)

bombs = deque([[int(y) for y in x.split(",")] for x in input().split(' ')])

for b in range(len(bombs)):

    bomb_row, bomb_col = bombs.popleft()
    damage = matrix[bomb_row][bomb_col]

    if matrix[bomb_row][bomb_col] > 0:
        for row in range(3):
            for col in range(3):
                if 0 <= bomb_row - 1 + row < len(matrix) and 0 <= bomb_col - 1 + col < len(matrix):
                    if matrix[bomb_row - 1 + row][bomb_col - 1 + col] > 0:
                        matrix[bomb_row - 1 + row][bomb_col - 1 + col] -= damage

alive, sum = get_cells(matrix)

print(f'Alive cells: {alive}')
print(f'Sum: {sum}')

for el in matrix:
    print(' '.join(str(x) for x in el))
