def find_all_solutions(row, col, board, unavailable_positions):
    if row == 8:
        for row in board:
            print(*row)
        print()
        return

    for col in range(8):
        if col in unavailable_positions['cols']:
            continue

        if col - 1 >= 0 and row - 1 >= 0:
            if board[row - 1][col - 1] == '*':
                continue

        if col + 1 <= 7 and row - 1 >= 0:
            if board[row - 1][col + 1] == '*':
                continue

        board[row][col] = '*'
        unavailable_positions['cols'].append(col)

        find_all_solutions(row + 1, col, board, unavailable_positions)

        unavailable_positions['cols'].pop()
        board[row][col] = '-'


board = [list('-' * 8) for _ in range(8)]

unavailable_positions = {
    'cols': [],
}

find_all_solutions(0, 0, board, unavailable_positions)
