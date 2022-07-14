def find_all_paths(row, col, end_row, end_col, unique_paths, grid):
    if row == end_row and col == end_col:
        unique_paths.append(1)
        return

    if row == len(grid) or col == len(grid[0]):
        return

    if grid[row][col] == 'v':
        return

    else:
        grid[row][col] = 'v'

        find_all_paths(row + 1, col, end_row, end_col, unique_paths, grid)  # Down
        find_all_paths(row, col + 1, end_row, end_col, unique_paths, grid)  # Right

        grid[row][col] = '-'

    return unique_paths


def create_grid(rows, cols):
    return [['-' for _ in range(cols)] for _ in range(rows)]


rows = int(input())
cols = int(input())

grid = create_grid(rows, cols)

starting_row, starting_col = 0, 0
end_row, end_col = rows - 1, cols - 1
unique_paths = []

result = find_all_paths(starting_row, starting_col, end_row, end_col, unique_paths, grid)

print(sum(result))
