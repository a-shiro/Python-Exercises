def read_matrix(dimensions):

    mtrx = []

    for _ in range(dimensions):
        col = [int(n) for n in input().split(' ')]
        mtrx.append(col)

    return mtrx


dimensions = int(input())
matrix = read_matrix(dimensions)

command = input().split(' ')

while not command[0] == 'END':

    r, c, value = [int(x) for x in command[1:]]

    if 0 <= r < dimensions and 0 <= c < dimensions:
        if command[0] == 'Add':
            matrix[r][c] += value
        elif command[0] == 'Subtract':
            matrix[r][c] -= value
    else:
        print('Invalid coordinates')

    command = input().split(' ')

for row in matrix:
    print(' '.join([str(x) for x in row]))

