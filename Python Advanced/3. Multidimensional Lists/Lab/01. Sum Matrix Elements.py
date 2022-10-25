def read_matrix():
    r, c = [int(n) for n in input().split(', ')]

    matrix = []

    for _ in range(r):
        row = [int(n) for n in input().split(', ')]
        matrix.append(row)

    return matrix

matrix = read_matrix()
total_sum = 0

for el in matrix:
    total_sum += sum(el)

print(total_sum)
print(matrix)