from math import floor


def is_outside(next_p_row, next_p_col, field):
    return 0 > next_p_row or next_p_row > len(field) - 1 or 0 > next_p_col or next_p_col > len(field) - 1


def get_next_position(p_row, p_col, command):
    if command == 'up':
        return p_row - 1, p_col
    elif command == 'down':
        return p_row + 1, p_col
    elif command == 'left':
        return p_row, p_col - 1
    elif command == 'right':
        return p_row, p_col + 1


def collect_coins(player, field):
    coins = 0
    player_path = []

    valid_command = {'up', 'down', 'left', 'right'}
    p_row, p_col = player

    while True:
        command = input()

        if command not in valid_command:
            command = input()
            continue

        next_p_row, next_p_col = get_next_position(p_row, p_col, command)

        if is_outside(next_p_row, next_p_col, field):
            coins = coins * 0.5
            return floor(coins), player_path

        elif field[next_p_row][next_p_col] == 'X':
            coins = coins * 0.5
            return floor(coins), player_path

        else:
            if field[next_p_row][next_p_col] != '-':
                coins += int(field[next_p_row][next_p_col])

            field[next_p_row][next_p_col], field[p_row][p_col] = 'P', '-'

        player_path.append([next_p_row, next_p_col])

        if coins >= 100:
            return floor(coins), player_path

        p_row, p_col = next_p_row, next_p_col


def find_player_position(field):
    for row in field:
        if 'P' in row:
            return field.index(row), row.index('P')


def create_field():
    size = int(input())
    field = []

    for _ in range(size):
        field.append(input().split())

    return field


field = create_field()
player = find_player_position(field)
coins, player_path = collect_coins(player, field)

if coins >= 100:
    print(f"You won! You've collected {coins} coins.")
else:
    print(f"Game over! You've collected {coins} coins.")

print('Your path:')
for path in player_path:
    print(path)

