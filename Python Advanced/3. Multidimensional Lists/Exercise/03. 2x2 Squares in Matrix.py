def read_matrix(c, r):
    matrix = []

    for _ in range(c):
        row = input().split(' ')
        matrix.append(row)

    return matrix


c, r = [int(n) for n in input().split(' ')]
matrix = read_matrix(c, r)
matches = 0

for col in range(c - 1):
    for row in range(r - 1):
        if matrix[col][row] == matrix[col][row + 1] == matrix[col + 1][row] == matrix[col + 1][row + 1]:
            matches += 1

print(matches)