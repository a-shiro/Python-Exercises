class Bunny:
    def __init__(self, row, col):
        self.row = row
        self.col = col


def get_player_position(matrix):
    for row_idx, row in enumerate(matrix):
        for col_idx, element in enumerate(row):
            if element == 'P':
                return row_idx, col_idx


def get_bunnies_positions(matrix):
    result = []
    for row_idx, row in enumerate(matrix):
        for col_idx, element in enumerate(row):
            if element == 'B':
                result.append(Bunny(row_idx, col_idx))

    return result


row_size, col_size = [int(n) for n in input().split(' ')]
matrix = [list(input()) for _ in range(row_size)]
player_moves = list(input())

row, col = get_player_position(matrix)
bunnies = get_bunnies_positions(matrix)

escaped = False

for move in player_moves:
    matrix[row][col] = '.'

    result = []
    for bunny in bunnies:
        if not bunny.row - 1 < 0:
            if not matrix[bunny.row - 1][bunny.col] == 'B':
                matrix[bunny.row - 1][bunny.col] = 'B'
                result.append(Bunny(bunny.row - 1, bunny.col))

        if not bunny.row + 1 >= row_size:
            if not matrix[bunny.row + 1][bunny.col] == 'B':
                matrix[bunny.row + 1][bunny.col] = 'B'
                result.append(Bunny(bunny.row + 1, bunny.col))

        if not bunny.col - 1 < 0:
            if not matrix[bunny.row][bunny.col - 1] == 'B':
                matrix[bunny.row][bunny.col - 1] = 'B'
                result.append(Bunny(bunny.row, bunny.col - 1))

        if not bunny.col + 1 >= col_size:
            if not matrix[bunny.row][bunny.col + 1] == 'B':
                matrix[bunny.row][bunny.col + 1] = 'B'
                result.append(Bunny(bunny.row, bunny.col + 1))

    bunnies.clear()
    bunnies += result

    if move == 'U':
        row -= 1

    if move == 'D':
        row += 1

    if move == 'L':
        col -= 1

    if move == 'R':
        col += 1

    if row < 0 or col < 0 or row >= row_size or col >= col_size:
        if row < 0:
            row = 0

        if col < 0:
            col = 0

        if row >= row_size:
            row = row_size - 1

        if col >= col_size:
            col = col_size - 1

        escaped = True
        break

    elif matrix[row][col] == 'B':
        break

for matrix_row in matrix:
    print(''.join(matrix_row))

if escaped:
    print(f'won: {row} {col}')
else:
    print(f'dead: {row} {col}')

# 5 6
# .....P
# ......
# ...B..
# ......
# ......
# ULDDDR

# 4 5
# .....
# .....
# .B...
# ...P.
# LLLLLLLL


# 5 8
# .......B
# ...B....
# ....B..B
# ........
# ..P.....
# ULLL
