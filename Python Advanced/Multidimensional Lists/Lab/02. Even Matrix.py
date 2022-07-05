def read_matrix():
    r = int(input())

    matrix = []

    for _ in range(r):
        row = [int(n) for n in input().split(', ') if int(n) % 2 == 0]
        matrix.append(row)

    return matrix


matrix = read_matrix()

print(matrix)