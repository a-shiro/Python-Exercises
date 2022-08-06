def dfs(row, col, letter, matrix, visited, areas):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return

    if visited[row][col]:
        return

    if matrix[row][col] != letter:
        return

    visited[row][col] = True

    dfs(row - 1, col, letter, matrix, visited, areas)  # up
    dfs(row + 1, col, letter, matrix, visited, areas)  # down
    dfs(row, col - 1, letter, matrix, visited, areas)  # left
    dfs(row, col + 1, letter, matrix, visited, areas)  # right


rows = int(input())
cols = int(input())

matrix = [list(input()) for _ in range(rows)]
visited = [[False] * cols for _ in range(rows)]
areas = {}

for i, row in enumerate(matrix):
    for j, letter in enumerate(row):
        if visited[i][j]:
            continue

        if letter not in areas:
            areas[letter] = 0

        dfs(i, j, letter, matrix, visited, areas)

        areas[letter] += 1

total_areas = sum(areas.values())

print(f'Areas: {total_areas}')

for area, count in sorted(areas.items()):
    print(f"Letter '{area}' -> {count}")

# 6
# 8
# aacccaac
# baaaaccc
# baabaccc
# bbdaaccc
# ccdccccc
# ccdccccc

# 3
# 3
# aaa
# aaa
# aaa

# 5
# 9
# asssaadas
# adsdasdad
# sdsdadsas
# sdasdsdsa
# ssssasddd
