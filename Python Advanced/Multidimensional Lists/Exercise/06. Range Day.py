def out_of_range(r, c, size):
    if r < 0 or c < 0 or r >= size or c >= size:
        return True
    return False


def get_position(direction, my_row, my_col, steps):
    if direction == 'up':
        return my_row - steps, my_col
    elif direction == 'down':
        return my_row + steps, my_col
    elif direction == 'left':
        return my_row, my_col - steps
    elif direction == 'right':
        return my_row, my_col + steps


def read_matrix_and_get_my_pos(size):
    matrix , my_row, my_col, total_targets = [], 0, 0 , 0

    for _ in range(size):
        row = input().split()
        matrix.append(row)
        if 'A' in row:
            my_row, my_col = matrix.index(row), row.index('A')
        if 'x' in row:
            total_targets += row.count('x')

    return matrix, my_row, my_col, total_targets


size = 5

matrix, my_row, my_col, total_targets = read_matrix_and_get_my_pos(size)
command_count = int(input())

hit_targets = []


for _ in range(command_count):

    current_command = input().split(' ')

    name = current_command[0]
    direction = current_command[1]

    if name == 'move':
        steps = int(current_command[2])

        my_next_row, my_next_col = get_position(direction, my_row, my_col, steps)

        if out_of_range(my_next_row, my_next_col, size):
            continue
        if matrix[my_next_row][my_next_col] != '.':
            continue

        matrix[my_row][my_col] = '.'
        matrix[my_next_row][my_next_col] = 'A'
        my_row, my_col = my_next_row, my_next_col
    else:
        bullet_row, bullet_col = get_position(direction, my_row, my_col, 1)
        while True:
            if out_of_range(bullet_row, bullet_col, size):
                break

            if matrix[bullet_row][bullet_col] == 'x':
                hit_targets.append([bullet_row, bullet_col])
                matrix[bullet_row][bullet_col] = '.'
                break

            bullet_row, bullet_col = get_position(direction, bullet_row, bullet_col, 1)

        if len(hit_targets) == total_targets:
            break

if len(hit_targets) == total_targets:
    print(f'Training completed! All {total_targets} targets hit.')
else:
    print(f'Training not completed! {total_targets - len(hit_targets)} targets left.')

for target in hit_targets:
    print(target)
