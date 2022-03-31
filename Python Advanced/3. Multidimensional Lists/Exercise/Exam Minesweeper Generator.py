def outside_of_board(mine_row, mine_col):
    return 0 > mine_row or mine_row > len(board) - 1 or 0 > mine_col or mine_col > len(board) - 1


def place_bombs_and_values(mine_row, mine_col, board):
    board[mine_row][mine_col] = '*'

    if not outside_of_board(mine_row - 1, mine_col - 1) and not board[mine_row - 1][mine_col - 1] == '*':
        board[mine_row - 1][mine_col - 1] += 1

    if not outside_of_board(mine_row - 1, mine_col) and not board[mine_row - 1][mine_col] == '*':
        board[mine_row - 1][mine_col] += 1

    if not outside_of_board(mine_row - 1, mine_col + 1) and not board[mine_row - 1][mine_col + 1] == '*':
        board[mine_row - 1][mine_col + 1] += 1

    if not outside_of_board(mine_row, mine_col - 1) and not board[mine_row][mine_col - 1] == '*':
        board[mine_row][mine_col - 1] += 1

    if not outside_of_board(mine_row, mine_col + 1) and not board[mine_row][mine_col + 1] == '*':
        board[mine_row][mine_col + 1] += 1

    if not outside_of_board(mine_row + 1, mine_col - 1) and not board[mine_row + 1][mine_col - 1] == '*':
        board[mine_row + 1][mine_col - 1] += 1

    if not outside_of_board(mine_row + 1, mine_col) and not board[mine_row + 1][mine_col] == '*':
        board[mine_row + 1][mine_col] += 1

    if not outside_of_board(mine_row + 1, mine_col + 1) and not board[mine_row + 1][mine_col + 1] == '*':
        board[mine_row + 1][mine_col + 1] += 1


def generate_bombs(board):
    for _ in range(int(input())):
        mine = input().lstrip('(').rstrip(')')
        mine_row, mine_col = [int(n) for n in mine.split(', ')]

        if outside_of_board(mine_row, mine_col):
            continue

        place_bombs_and_values(mine_row, mine_col, board)

    return board


def create_board():
    size = int(input())
    board = []

    for _ in range(size):
        board.append([0 for zero in range(size)])
    return board


board = create_board()
result = generate_bombs(board)
[print(' '.join(map(str, row))) for row in result]


