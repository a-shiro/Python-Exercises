def read_matrix(r, c):
    mtrx = []

    for _ in range(r):
        row = [int(n) for n in input().split(' ')]
        mtrx.append(row)

    return mtrx


r, c = [int(n) for n in input().split(' ')]
matrix = read_matrix(r, c)
biggest_sum, start_r, start_c = 0, 0, 0

for row in range(r - 2):
    for col in range(c - 2):
        current_sum = matrix[row][col] + matrix[row][col + 1] + matrix[row][col + 2] + \
                      matrix[row + 1][col] + matrix[row + 1][col + 1] + matrix[row + 1][col + 2] + \
                      matrix[row + 2][col] + matrix[row + 2][col + 1] + matrix[row + 2][col + 2]

        if current_sum > biggest_sum:
            biggest_sum, start_r, start_c = current_sum, row, col

print(f'Sum = {biggest_sum}')
print(f'{matrix[start_r][start_c]} {matrix[start_r][start_c + 1]} {matrix[start_r][start_c + 2]} \n'
      f'{matrix[start_r + 1][start_c]} {matrix[start_r + 1][start_c + 1]} {matrix[start_r + 1][start_c + 2]} \n'
      f'{matrix[start_r + 2][start_c]} {matrix[start_r + 2][start_c + 1]} {matrix[start_r + 2][start_c + 2]}')

