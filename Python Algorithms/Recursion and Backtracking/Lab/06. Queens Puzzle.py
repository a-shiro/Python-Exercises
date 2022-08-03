def find_all_solutions(row, board, unavailable_positions):
    if row == 8:
        for row in board:
            print(*row)
        print()
        return

    for col in range(8):
        if col in unavailable_positions['cols']:
            continue

        if col - row in unavailable_positions['left_diagonal']:
            continue

        if row + col in unavailable_positions['right_diagonal']:
            continue

        board[row][col] = '*'
        unavailable_positions['cols'].append(col)
        unavailable_positions['left_diagonal'].append(col - row)
        unavailable_positions['right_diagonal'].append(row + col)

        find_all_solutions(row + 1, board, unavailable_positions)

        board[row][col] = '-'
        unavailable_positions['cols'].pop()
        unavailable_positions['left_diagonal'].pop()
        unavailable_positions['right_diagonal'].pop()


board = [list('-' * 8) for _ in range(8)]

unavailable_positions = {
    'cols': [],
    'left_diagonal': [],
    'right_diagonal': [],
}

find_all_solutions(0, board, unavailable_positions)
