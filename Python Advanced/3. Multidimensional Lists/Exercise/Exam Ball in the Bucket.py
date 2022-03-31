def outside(row, col):
    return 0 > row or row > 5 or 0 > col or col > 5


def collect_points(row, col, board):
    points = 0

    next_row = row - 1
    while next_row >= 0:
        if not board[next_row][col] == 'B' and not board[next_row][col] == 'X':
            points += int(board[next_row][col])
        next_row -= 1

    next_row = row + 1
    while next_row < 6:
        if not board[next_row][col] == 'B' and not board[next_row][col] == 'X':
            points += int(board[next_row][col])
        next_row += 1
    return points


def start_throwing(board):
    total_points = 0

    for throw in range(3):
        row, col = [int(n) for n in input().lstrip('(').rstrip(')').split(', ')]

        if outside(row, col):
            continue
        if board[row][col] == 'B':
            board[row][col] = 'X'
            total_points += collect_points(row, col, board)

    if total_points < 100:
        return False, total_points
    return True, total_points


def create_board():
    board = []

    for _ in range(6):
        board.append(input().split(' '))

    return board


board = create_board()

win, points = start_throwing(board)

if win:
    if 100 <= points <= 199:
        prize = 'Football'
    elif 200 <= points <= 299:
        prize = 'Teddy Bear'
    else:
        prize = 'Lego Construction Set'

    print(f"Good job! You scored {points} points, and you've won {prize}.")
else:
    print(f'Sorry! You need {100 - points} points more to win a prize.')