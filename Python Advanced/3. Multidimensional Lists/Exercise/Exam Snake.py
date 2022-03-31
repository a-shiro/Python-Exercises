def output_data(food_eaten, territory):
    print(f'Food eaten: {food_eaten}')
    [print(''.join(row)) for row in territory]


def exited_territory(next_s_row, next_s_col):
    return 0 > next_s_row or next_s_row > len(territory) - 1 or 0 > next_s_col or next_s_col > len(territory) - 1


def get_next_position(s_row, s_col, command):
    if command == 'up':
        return s_row - 1, s_col
    elif command == 'down':
        return s_row + 1, s_col
    elif command == 'left':
        return s_row, s_col - 1
    elif command == 'right':
        return s_row, s_col + 1


def start_traversing(snake_row, snake_col, territory):

    food_eaten = 0

    while True:
        command = input()
        next_snake_row, next_snake_col = get_next_position(snake_row, snake_col, command)
        if exited_territory(next_snake_row, next_snake_col):
            print('Game over!')
            territory[snake_row][snake_col] = '.'
            output_data(food_eaten, territory)
            return

        if territory[next_snake_row][next_snake_col] == '*':
            food_eaten += 1
            territory[next_snake_row][next_snake_col], territory[snake_row][snake_col] = 'S', '.'
            snake_row, snake_col = next_snake_row, next_snake_col
        elif territory[next_snake_row][next_snake_col] == 'B':
            if (next_snake_row, next_snake_col) == burrow_1:
                territory[next_snake_row][next_snake_col], territory[snake_row][snake_col] = '.', '.'
                next_snake_row, next_snake_col = burrow_1[0], burrow_1[1]
                territory[burrow_2[0]][burrow_2[1]] = 'S'
                snake_row, snake_col = burrow_2[0], burrow_2[1]
            else:
                territory[next_snake_row][next_snake_col], territory[snake_row][snake_col] = '.', '.'
                next_snake_row, next_snake_col = burrow_2[0], burrow_2[1]
                territory[burrow_1[0]][burrow_1[1]] = 'S'
                snake_row, snake_col = burrow_1[0], burrow_1[1]
        else:
            territory[next_snake_row][next_snake_col], territory[snake_row][snake_col] = 'S', '.'
            snake_row, snake_col = next_snake_row, next_snake_col

        if food_eaten == 10:
            print('You won! You fed the snake.')
            output_data(food_eaten, territory)
            return


def get_burrow_positions(territory):
    b_1, b_2 = (None, None), (None, None)

    for row in territory:
        if 'B' in row:
            if b_1[0] is None:
                b_1 = (territory.index(row), row.index('B'))
            else:
                b_2 = (territory.index(row), row.index('B'))
    return b_1, b_2


def get_snake_position(territory):
    for row in territory:
        if 'S' in row:
            snake_row, snake_col = territory.index(row), row.index('S')
            return snake_row, snake_col


def create_snake_territory():
    size = int(input())
    territory = []
    burrows = False

    for row in range(size):
        col = input()
        territory.append([])
        for el in col:
            territory[row].append(el)
        if 'B' in col:
            burrows = True
    return territory, burrows


territory, burrows = create_snake_territory()
if burrows:
    burrow_1, burrow_2 = get_burrow_positions(territory)
snake_row, snake_col = get_snake_position(territory)
start_traversing(snake_row, snake_col, territory)

