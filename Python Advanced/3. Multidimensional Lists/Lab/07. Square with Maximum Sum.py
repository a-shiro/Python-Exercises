def read_matrix(r):
    matrix = []

    for _ in range(r):
        row = [int(n) for n in input().split(', ')]
        matrix.append(row)

    return matrix


r, c = [int(n) for n in input().split(', ')]
matrix = read_matrix(r)

biggest_square = {
    'first_row': [0, 0],
    'second_row': [0, 0],
    'sum': 0
}

for row in range(len(matrix)):
    if row == len(matrix) - 1:
        break
    for n in range(len(matrix[row]) - 1):
        total_sum = matrix[row][n] + matrix[row][n + 1] + matrix[row + 1][n] + matrix[row + 1][n + 1]
        if total_sum > biggest_square['sum']:
            biggest_square['sum'] = total_sum
            biggest_square['first_row'][0], biggest_square['first_row'][1] = matrix[row][n], matrix[row][n + 1]
            biggest_square['second_row'][0], biggest_square['second_row'][1] = matrix[row + 1][n], matrix[row + 1][
                n + 1]

print(' '.join(str(n) for n in biggest_square['first_row']))
print(' '.join(str(n) for n in biggest_square['second_row']))
print(biggest_square['sum'])