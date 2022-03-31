def read_matrix():
    rows_count = int(input())

    matrix = []

    for _ in range(rows_count):
        row = [int(r) for r in input().split(', ')]
        matrix.append(row)

    return matrix


matrix = read_matrix()

result = {
    'primary_diagonal': {'values': [], 'sum': 0},
    'secondary_diagonal': {'values': [], 'sum': 0}
}

primary_diagonal_sum = 0
secondary_diagonal_sum = 0

for i in range(len(matrix)):
    primary_diagonal_sum += matrix[i][i]
    result['primary_diagonal']['values'].append(matrix[i][i])

result['primary_diagonal']['sum'] = primary_diagonal_sum

for i in range(len(matrix)):
    secondary_diagonal_sum += matrix[i][len(matrix) - i - 1]
    result['secondary_diagonal']['values'].append(matrix[i][len(matrix) - i - 1])

result['secondary_diagonal']['sum'] = secondary_diagonal_sum

p_d_sum = result['primary_diagonal']['sum']
p_d_values = ', '.join(map(str, result['primary_diagonal']['values']))
print(f'Primary diagonal: {p_d_values}. Sum: {p_d_sum}')

s_d_sum = result['secondary_diagonal']['sum']
s_d_values = ', '.join(map(str, result['secondary_diagonal']['values']))
print(f'Secondary diagonal: {s_d_values}. Sum: {s_d_sum}')