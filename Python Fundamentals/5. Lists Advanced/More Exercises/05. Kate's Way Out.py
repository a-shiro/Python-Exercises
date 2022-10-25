def find_way_out(row, col, maze, steps, exits):
    if row < 0 or col < 0 or row >= len(maze) or col >= len(maze[0]):
        exits.append(steps)
        return

    if maze[row][col] == '#' or maze[row][col] == 'v':
        return

    else:
        maze[row][col] = 'v'

        find_way_out(row - 1, col, maze, steps + 1, exits)  # UP
        find_way_out(row + 1, col, maze, steps + 1, exits)  # DOWN
        find_way_out(row, col - 1, maze, steps + 1, exits)  # LEFT
        find_way_out(row, col + 1, maze, steps + 1, exits)  # RIGHT

    return exits


def get_starting_position(maze):
    for row_idx, row in enumerate(maze):
        if 'k' in row:
            col = row.index('k')
            row = row_idx

            return row, col


rows = int(input())
maze = [list(input()) for _ in range(rows)]

starting_row, starting_col = get_starting_position(maze)
exits = find_way_out(starting_row, starting_col, maze, 0, [])


if exits:
    print(f'Kate got out in {exits[0]} moves')
else:
    print('Kate cannot get out')
