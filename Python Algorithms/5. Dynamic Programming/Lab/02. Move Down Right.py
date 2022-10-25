from collections import deque

rows = int(input())
cols = int(input())

matrix = []
dp = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])
    dp.append([0] * cols)

dp[0][0] = matrix[0][0]

for col in range(1, cols):
    dp[0][col] = dp[0][col - 1] + matrix[0][col]

for row in range(1, rows):
    dp[row][0] = dp[row - 1][0] + matrix[row][0]

for row in range(1, rows):
    for col in range(1, cols):
        dp[row][col] = max(dp[row - 1][col], dp[row][col - 1]) + matrix[row][col]

row = rows - 1
col = cols - 1

result = deque()
while row > 0 and col > 0:
    result.appendleft([row, col])

    if dp[row][col - 1] >= dp[row - 1][col]:
        col -= 1
    else:
        row -= 1

while row > 0:
    result.appendleft([row, col])
    row -= 1

while col > 0:
    result.appendleft([row, col])
    col -= 1

result.appendleft([0, 0])
print(*result)

# 3
# 3
# 1 1 1
# 1 1 1
# 1 1 1

# 3
# 3
# 1 0 6
# 8 3 7
# 2 4 9

# 8
# 7
# 2 6 1 8 9 4 2
# 1 8 0 3 5 6 7
# 3 4 8 7 2 1 8
# 0 9 2 8 1 7 9
# 2 7 1 9 7 8 2
# 4 5 6 1 2 5 6
# 9 3 5 2 8 1 9
# 2 3 4 1 7 2 8