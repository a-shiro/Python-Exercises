def find_all_exits(current_row, current_col, labyrinth, direction, path):
    if current_row < 0 or current_col < 0 or current_row >= len(labyrinth) or current_col >= len(labyrinth[0]):
        return

    if labyrinth[current_row][current_col] == '*' or labyrinth[current_row][current_col] == 'v':
        return

    if labyrinth[current_row][current_col] == 'e':
        path.append(direction)

        print(*path, sep='')
    else:
        labyrinth[current_row][current_col] = 'v'
        path.append(direction)

        find_all_exits(current_row - 1, current_col, labyrinth, 'U', path)  # up
        find_all_exits(current_row + 1, current_col, labyrinth, 'D', path)  # down
        find_all_exits(current_row, current_col - 1, labyrinth, 'L', path)  # left
        find_all_exits(current_row, current_col + 1, labyrinth, 'R', path)  # right

        labyrinth[current_row][current_col] = '-'

    path.pop()


def create_labyrinth(rows):
    labyrinth = []

    for _ in range(rows):
        labyrinth.append(list(input()))

    return labyrinth


rows = int(input())
cols = int(input())

labyrinth = create_labyrinth(rows)

find_all_exits(0, 0, labyrinth, '', [])

