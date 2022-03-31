def outside(r, c, size):
    if r < 0 or c < 0 or r >= size or c >= size:
        return True
    return False


def get_next_pos(r, c, command):
    if command == 'up':
        return r - 1, c
    elif command == 'down':
        return r + 1, c
    elif command == 'left':
        return r, c - 1
    elif command == 'right':
        return r, c + 1


def get_matrix(size):
    matrix, santa_row, santa_col = [], 0, 0
    unhappy_nice_kids = 0

    for _ in range(size):
        row = input().split()
        matrix.append(row)

        if 'S' in row:
            santa_row, santa_col = matrix.index(row), row.index('S')

    return matrix, santa_row, santa_col, unhappy_nice_kids


happy_kids = 0
presents = int(input())
n = int(input())

matrix, santa_row, santa_col, unhappy_nice_kids = get_matrix(n)

command = input()
while command != 'Christmas morning':

    santa_next_row, santa_next_col = get_next_pos(santa_row, santa_col, command)

    if outside(santa_next_row, santa_next_col, n):
        command = input()
        continue

    if matrix[santa_next_row][santa_next_col] == 'V':
        matrix[santa_row][santa_col] = '-'
        matrix[santa_next_row][santa_next_col] = 'S'
        presents -= 1
        happy_kids += 1
        if presents <= 0:
            break
    elif matrix[santa_next_row][santa_next_col] == 'C':
        matrix[santa_row][santa_col] = '-'
        matrix[santa_next_row][santa_next_col] = 'S'
        if matrix[santa_next_row - 1][santa_next_col] == 'V' or matrix[santa_next_row - 1][santa_next_col] == 'X':  # up
            if matrix[santa_next_row - 1][santa_next_col] == 'V':
                happy_kids += 1
            matrix[santa_next_row - 1][santa_next_col] = '-'
            presents -= 1
            if presents <= 0:
                break
        if matrix[santa_next_row + 1][santa_next_col] == 'V' or matrix[santa_next_row + 1][santa_next_col] == 'X': # down
            if matrix[santa_next_row + 1][santa_next_col] == 'V':
                happy_kids += 1
            matrix[santa_next_row + 1][santa_next_col] = '-'
            presents -= 1
            if presents <= 0:
                break
        if matrix[santa_next_row][santa_next_col - 1] == 'V' or matrix[santa_next_row][santa_next_col -1] == 'X': # left
            if matrix[santa_next_row][santa_next_col - 1] == 'V':
                happy_kids += 1
            matrix[santa_next_row][santa_next_col - 1] = '-'
            presents -= 1
            if presents <= 0:
                break
        if matrix[santa_next_row][santa_next_col + 1] == 'V' or matrix[santa_next_row][santa_next_col + 1] == 'X':
            if matrix[santa_next_row][santa_next_col + 1] == 'V':
                happy_kids += 1
            matrix[santa_next_row][santa_next_col + 1] = '-'
            presents -= 1
            if presents <= 0:
                break
    else:
        matrix[santa_row][santa_col] = '-'
        matrix[santa_next_row][santa_next_col] = 'S'

    santa_row, santa_col = santa_next_row, santa_next_col

    command = input()

if presents == 0:
    for row in matrix:
        if 'V' in row:
            print('Santa ran out of presents!')
            break
[print(' '.join(row)) for row in matrix]

nice_kids_left = 0
for row in matrix:
    if 'V' in row:
        nice_kids_left += row.count('V')

if nice_kids_left == 0:
    print(f'Good job, Santa! {happy_kids} happy nice kid/s.')
else:
    print(f'No presents for {nice_kids_left} nice kid/s.')
