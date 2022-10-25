def read_matrix():
    r, c = [int(n) for n in input().split(', ')]

    matrix = []

    for _ in range(r):
        row = [int(n) for n in input().split(' ')]
        matrix.append(row)

    return matrix


matrix = read_matrix()
result = [el * 0 for el in range(len(matrix[0]))]

for r in matrix:
    i = 0
    for d in r:
        result[i] += d
        i += 1

[print(n) for n in result]
