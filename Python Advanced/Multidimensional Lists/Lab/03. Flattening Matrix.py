def read_matrix():
    r = int(input())

    matrix = []

    for _ in range(r):
        row = [int(n) for n in input().split(', ')]
        matrix.extend(row)

    return matrix


matrix = read_matrix()

print(matrix)

