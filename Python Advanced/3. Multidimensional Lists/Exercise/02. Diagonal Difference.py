def read_matrix():
    rows_count = int(input())

    matrix = []

    for _ in range(rows_count):
        row = [int(r) for r in input().split(' ')]
        matrix.append(row)

    return matrix


def get_primary_diagonal_sum(matrix):
    p_d_sum = 0

    for i in range(len(matrix)):
        p_d_sum += matrix[i][i]


    return p_d_sum


def get_secondary_diagonal_sum(matrix):
    s_d_sum = 0

    for i in range(len(matrix)):
        s_d_sum += matrix[i][len(matrix) - i - 1]

    return s_d_sum


matrix = read_matrix()

primary_diagonal_sum = get_primary_diagonal_sum(matrix)
secondary_diagonal_sum = get_secondary_diagonal_sum(matrix)

print(abs(primary_diagonal_sum - secondary_diagonal_sum))

