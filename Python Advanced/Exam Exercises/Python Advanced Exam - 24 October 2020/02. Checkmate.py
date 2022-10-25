def king_is_targeted(king_position, board):

    king_row, king_col = king_position
    while not king_row == 0:  # up
        king_row -= 1
        if board[king_row][king_col] == 'Q':
            king_threats.append([king_row, king_col])
            break

    king_row, king_col = king_position
    while not king_row == len(board) - 1:  # down
        king_row += 1
        if board[king_row][king_col] == 'Q':
            king_threats.append([king_row, king_col])
            break

    king_row, king_col = king_position
    while not king_col == 0:  # left
        king_col -= 1
        if board[king_row][king_col] == 'Q':
            king_threats.append([king_row, king_col])
            break

    king_row, king_col = king_position
    while not king_col == len(board) - 1:  # right
        king_col += 1
        if board[king_row][king_col] == 'Q':
            king_threats.append([king_row, king_col])
            break

    king_row, king_col = king_position
    while not king_row == 0 and not king_col == 0:  # primary diagonal up left
        king_row -= 1
        king_col -= 1
        if board[king_row][king_col] == 'Q':
            king_threats.append([king_row, king_col])
            break

    king_row, king_col = king_position
    while not king_row == 0 and not king_col == len(board) - 1:  # secondary diagonal up right
        king_row -= 1
        king_col += 1
        if board[king_row][king_col] == 'Q':
            king_threats.append([king_row, king_col])
            break

    king_row, king_col = king_position
    while not king_row == len(board) - 1 and not king_col == 0:  # secondary diagonal down left
        king_row += 1
        king_col -= 1
        if board[king_row][king_col] == 'Q':
            king_threats.append([king_row, king_col])
            break

    king_row, king_col = king_position
    while not king_row == len(board) - 1 and not king_col == len(board) - 1:  # primary diagonal down right
        king_row += 1
        king_col += 1
        if board[king_row][king_col] == 'Q':
            king_threats.append([king_row, king_col])
            break

    if king_threats:
        return True
    return False


def find_king(board):
    for row in board:
        if 'K' in row:
            return board.index(row), row.index('K')


def create_board():
    board = []
    for _ in range(8):
        board.append(input().split(' '))

    return board


board = create_board()
king_threats = []
king_position = find_king(board)

if king_is_targeted(king_position, board):
    [print(q) for q in king_threats]
else:
    print('The king is safe!')