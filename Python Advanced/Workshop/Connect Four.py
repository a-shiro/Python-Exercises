from errors import ColumnIsFullError


def display_board(board):
    [print(row) for row in board]


def outside_board(choice, board):
    return 1 > choice or choice > len(board)


def current_player(turn):
    return 2 if turn % 2 == 0 else 1


def col_is_full(choice, board):
    size, col = len(board) - 1, choice - 1

    for row in range(size, -1, -1):
        if board[row][col] == 0:
            return False
    return True


def won(win):
    return all(win) and len(win) == 4


def draw(board):
    for row in board:
        if 0 in row:
            return False
    return True


def player_won(placed_choice, player, board):
    row, col = placed_choice
    win = []

    while True:  # up
        if board[row][col] != player:
            win.append(False)
        else:
            win.append(True)
        row -= 1

        if row < 0:
            if won(win):
                return True
            win.clear()
            row = placed_choice[0]
            break
        if len(win) == 4:
            if won(win):
                return True
            win.clear()
            row = placed_choice[0]
            break

    while True:  # down
        if board[row][col] != player:
            win.append(False)
        else:
            win.append(True)
        row += 1

        if row > len(board) - 1:
            if won(win):
                return True
            win.clear()
            row = placed_choice[0]
            break
        if len(win) == 4:
            if won(win):
                return True
            win.clear()
            row = placed_choice[0]
            break

    while True:  # left
        if board[row][col] != player:
            win.append(False)
        else:
            win.append(True)
        col -= 1

        if col < 0:
            if won(win):
                return True
            win.clear()
            col = placed_choice[1]
            break
        if len(win) == 4:
            if won(win):
                return True
            win.clear()
            col = placed_choice[1]
            break

    while True:  # right
        if board[row][col] != player:
            win.append(False)
        else:
            win.append(True)
        col += 1

        if col > len(board) - 1:
            if won(win):
                return True
            win.clear()
            col = placed_choice[1]
            break
        if len(win) == 4:
            if won(win):
                return True
            win.clear()
            col = placed_choice[1]
            break

    while True:  # up left
        if board[row][col] != player:
            win.append(False)
        else:
            win.append(True)

        row -= 1
        col -= 1

        if row < 0 or col < 0:
            if won(win):
                return True
            win.clear()
            row, col = placed_choice
            break
        if len(win) == 4:
            if won(win):
                return True
            win.clear()
            row, col = placed_choice
            break

    while True:  # up right
        if board[row][col] != player:
            win.append(False)
        else:
            win.append(True)

        row -= 1
        col += 1

        if row < 0 or col > len(board) - 1:
            if won(win):
                return True
            win.clear()
            row, col = placed_choice
            break
        if len(win) == 4:
            if won(win):
                return True
            win.clear()
            row, col = placed_choice
            break

    while True:  # down left
        if board[row][col] != player:
            win.append(False)
        else:
            win.append(True)

        row += 1
        col -= 1

        if row > len(board) - 1 or col < 0:
            if won(win):
                return True
            win.clear()
            row, col = placed_choice
            break
        if len(win) == 4:
            if won(win):
                return True
            win.clear()
            row, col = placed_choice
            break

    while True:  # down right
        if board[row][col] != player:
            win.append(False)
        else:
            win.append(True)

        row += 1
        col += 1

        if row > len(board) - 1 or col > len(board) - 1:
            if won(win):
                return True
            win.clear()
            row, col = placed_choice
            break
        if len(win) == 4:
            if won(win):
                return True
            win.clear()
            row, col = placed_choice
            break


def place_choice(choice, player, board):
    size, col = len(board) - 1, choice - 1

    for row in range(size, -1, -1):
        if board[row][col] == 0:
            board[row][col] = player
            return [row, col]


def play(board):
    turn = 1

    while True:
        try:
            player_choice = int(input(f'Player {current_player(turn)}, please choose a column:'))

            if outside_board(player_choice, board):
                raise IndexError

            if col_is_full(player_choice, board):
                raise ColumnIsFullError

            placed_choice = place_choice(player_choice, current_player(turn), board)
            display_board(board)

            if player_won(placed_choice, current_player(turn), board):  # check if player won
                print(f'Winner is player {current_player(turn)}!')
                return

            if draw(board):
                print('Draw!')
                return

            turn += 1

        except ValueError:
            print('Please choose a valid column number!')

        except IndexError:
            print('Choose a valid position on the board!')

        except ColumnIsFullError:
            print('Column is full! Please choose a free column.')


def create_board():
    while True:
        try:
            size = int(input('Choose a board size from 4 to N:'))
            if size < 4:
                raise ValueError

            board = []

            for i in range(size):
                board.append([])
                for _ in range(size):
                    board[i].append(0)

            return board

        except ValueError:
            print('Please choose a valid number from 4 to N!')


board = create_board()
play(board)
