def pos_out_of_range(next_p_row, next_p_col, size):
    return 0 > next_p_row or next_p_row >= size or 0 > next_p_col or next_p_col >= size


def get_next_pos(p_row, p_col, command):
    if command == 'up':
        return p_row - 1, p_col
    elif command == 'down':
        return p_row + 1, p_col
    elif command == 'left':
        return p_row, p_col - 1
    elif command == 'right':
        return p_row, p_col + 1


def start_collecting(player_position, field):
    global initial_str
    p_row, p_col = player_position

    n = int(input())
    for _ in range(n):
        command = input()

        next_p_row, next_p_col = get_next_pos(p_row, p_col, command)
        if pos_out_of_range(next_p_row, next_p_col, size):
            initial_str = initial_str[:-1]
        elif not field[next_p_row][next_p_col] == '-':
            initial_str += field[next_p_row][next_p_col]
            field[next_p_row][next_p_col], field[p_row][p_col] = 'P', '-'
            p_row, p_col = next_p_row, next_p_col
        else:
            field[next_p_row][next_p_col], field[p_row][p_col] = 'P', '-'
            p_row, p_col = next_p_row, next_p_col


def get_starting_position(field):
    for row in field:
        if 'P' in row:
            return field.index(row), row.index('P')


def create_field(size):
    field = []

    for row in range(size):
        col = input()
        field.append([])
        for el in col:
            field[row].append(el)

    return field


initial_str = input()
size = int(input())

field = create_field(size)  # create field
player_position = get_starting_position(field)  # get player position
start_collecting(player_position, field)  # make a for loop and start accepting direction
# if next pos is letter
# if next pos is out of field
print(initial_str)
[print(''.join(row)) for row in field]
