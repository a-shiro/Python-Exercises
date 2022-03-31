from errors import InvalidSignError, PositionTakenError


def check_for_a_winner(board, player_sign):

    board_size = len(board)

    for row in board:  # horizontal
        if all([True if el == player_sign else False for el in row]):
            return True

    for row in range(board_size):  # vertical
        if all([True if board[col][row] == player_sign else False for col in range(3)]):
            return True

    if all([True if board[row][row] == player_sign else False for row in range(board_size)]):  # primary diagonal
        return True

    if all([True if board[row][board_size - row - 1] == player_sign else False for row in range(board_size)]):  # secondary diagonal
        return True


def place_choice_on_board(board, player_choice, player_sign):
    if player_choice == 1 and board[0][0] == ' ':
        board[0][0] = player_sign
        return board
    elif player_choice == 2 and board[0][1] == ' ':
        board[0][1] = player_sign
        return board
    elif player_choice == 3 and board[0][2] == ' ':
        board[0][2] = player_sign
        return board
    elif player_choice == 4 and board[1][0] == ' ':
        board[1][0] = player_sign
        return board
    elif player_choice == 5 and board[1][1] == ' ':
        board[1][1] = player_sign
        return board
    elif player_choice == 6 and board[1][2] == ' ':
        board[1][2] = player_sign
        return board
    elif player_choice == 7 and board[2][0] == ' ':
        board[2][0] = player_sign
        return board
    elif player_choice == 8 and board[2][1] == ' ':
        board[2][1] = player_sign
        return board
    elif player_choice == 9 and board[2][2] == ' ':
        board[2][2] = player_sign
        return board

    raise PositionTakenError


def display_board(board):
    for row in board:
        print('| ', end='')
        print(' | '.join(row), end='')
        print(' |')


def play(board, player_1, player_2):
    player_1_name, player_1_sign = player_1
    player_2_name, player_2_sign = player_2

    turn = 1
    current_player = {1: player_1_name, 0: player_2_name}

    while True:
        try:
            player_choice = int(input(
                f'{current_player[turn % 2]} choose a free position [1-9]:'))  # swap players and make them choose free position
            if player_choice < 1 or player_choice > 9:
                raise ValueError

            player_sign = player_1_sign if turn % 2 == 1 else player_2_sign

            place_choice_on_board(board, player_choice, player_sign)  # place player choice if free if
            display_board(board)  # print the board after choice
            if check_for_a_winner(board, player_sign):  # create the logic for vertical, horizontal, diagonal and secondary diagonal win condition
                print(f'{current_player[turn % 2]} won!')
                break

            if turn == 9:  # If the is no winner at turn 9 - its a draw
                print('Draw!')
                break

            turn += 1
        except ValueError:
            print('Please enter a valid number between 1 and 9 ')
        except PositionTakenError:
            print('Position already taken! Please choose a free position.')


def display_board_numeration():
    print('This is the numeration of the board:')
    print('|  1  |  2  |  3  |')
    print('|  4  |  5  |  6  |')
    print('|  7  |  8  |  9  |')


def get_players_info():
    player1_name = input('Player one name: ')
    player2_name = input('Player two name: ')

    while True:
        try:
            player1_sign = input(f'{player1_name} would you like to play with "X" or "O"?').upper()
            if player1_sign not in ['X', 'O']:
                raise InvalidSignError

            player2_sign = 'O' if player1_sign == 'X' else 'X'

            player1 = [player1_name, player1_sign]
            player2 = [player2_name, player2_sign]
            return player1, player2
        except InvalidSignError:
            print(f'Please choose a valid sign - "X" or "O"')


player_1, player_2 = get_players_info()  # read player info - player names and sign they play with

display_board_numeration()  # display the numeration of the board

print(f'{player_1[0]} starts first!')  # print who starts first

board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

play(board, player_1, player_2)  # play logic
