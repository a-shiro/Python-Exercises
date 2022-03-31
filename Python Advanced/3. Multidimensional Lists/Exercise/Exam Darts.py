def get_all_directions_values(row, col, board):
    total = 0

    total += int(board[0][col])
    total += int(board[-1][col])
    total += int(board[row][0])
    total += int(board[row][-1])

    return total


def outside_board(shoot):
    row, col = shoot
    return 0 > row or row > 6 or 0 > col or col > 6


def bullseye(shoot, board):
    row, col = shoot

    if board[row][col] == 'B':
        return True
    return False


def other_hit_conditions(shoot, current_player, board):
    row, col = shoot

    if board[row][col].isdigit():
        current_player[1] -= int(board[row][col])

    elif board[row][col] == 'D':
        total = get_all_directions_values(row, col, board)
        current_player[1] -= total * 2

    elif board[row][col] == 'T':
        total = get_all_directions_values(row, col, board)
        current_player[1] -= total * 3


def play(player_names, board):
    player_1 = [player_names[0], 501, 0]
    player_2 = [player_names[1], 501, 0]
    turn = 1

    while True:
        current_player = player_2 if turn % 2 == 0 else player_1
        shoot = [int(n) for n in input().lstrip('(').rstrip(')').split(', ')]

        current_player[2] += 1

        if outside_board(shoot):
            turn += 1
            continue

        elif bullseye(shoot, board):
            return current_player[2], current_player[0]

        else:
            other_hit_conditions(shoot, current_player, board)

        if current_player[1] <= 0:
            return current_player[2], current_player[0]

        turn += 1


def create_board():
    board = []

    for _ in range(7):
        board.append(input().split(' '))

    return board


player_names = input().split(', ')

board = create_board()
winner = play(player_names, board)

print(f'{winner[1]} won the game with {winner[0]} throws!')

