def read_matrix(r, c):
    mtrx = []

    for _ in range(r):
        row = [n for n in input().split(' ')]
        mtrx.append(row)

    return mtrx


r, c = [int(n) for n in input().split(' ')]
matrix = read_matrix(r, c)

command = input().split()

while not command[0] == 'END':

    if command[0] != 'swap' or len(command) != 5:
        print('Invalid input!')
        command = input().split(' ')
        continue

    row_1, col_1, row_2, col_2 = [int(n) for n in command[1:]]

    if (0 <= row_1 <= r and 0 <= col_1 <= c) and (0 <= row_2 <= r and 0 <= col_2 <= c):
        matrix[row_1][col_1], matrix[row_2][col_2] = matrix[row_2][col_2], matrix[row_1][col_1]
        for rows in range(r):
            print(' '.join(str(x) for x in matrix[rows]))
    else:
        print('Invalid input!')

    command = input().split(' ')