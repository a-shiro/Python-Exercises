size = int(input())

matrix = []
for c in range(size):
    col = [int(n) for n in input().split(' ')]
    matrix.append(col)

primary_diagonal_sum = 0

for i in range(size):
    primary_diagonal_sum += matrix[i][i]

print(primary_diagonal_sum)

