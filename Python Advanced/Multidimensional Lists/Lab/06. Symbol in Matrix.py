def read_matrix():
    matrix_size = int(input())

    matrix = []

    for _ in range(matrix_size):
        matrix.append(input().split())

    return matrix


matrix = read_matrix()
symbol = input()
is_found = False

for col in range(len(matrix)):
    if symbol in matrix[col][0]:
        index, column = matrix[col][0].index(symbol), col
        print(f"{column, index}")
        is_found = True
        break

if not is_found:
    print(f'{symbol} does not occur in the matrix')