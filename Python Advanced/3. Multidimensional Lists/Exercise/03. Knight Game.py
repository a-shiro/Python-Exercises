class Knight:
    def __init__(self, row, col):
        self.row = row
        self.col = col


def get_knight_positions(board):
    all_knights = []

    for row_idx, row in enumerate(board):
        for col_idx, col in enumerate(row):
            if col == 'K':
                all_knights.append(Knight(row_idx, col_idx))

    return all_knights


def knight_placed(row, col, board):
    board_size = len(board)

    if row < 0 or col < 0 or row >= board_size or col >= board_size:
        return False
    return board[row][col] == 'K'


def get_enemies_count(knight, board):
    enemies_count = 0

    knight_moves = [
        (knight.row - 1, knight.col - 2),
        (knight.row - 2, knight.col - 1),
        (knight.row - 1, knight.col + 2),
        (knight.row - 2, knight.col + 1),
        (knight.row + 1, knight.col - 2),
        (knight.row + 2, knight.col - 1),
        (knight.row + 1, knight.col + 2),
        (knight.row + 2, knight.col + 1)
    ]

    for move in knight_moves:
        row, col = move

        if knight_placed(row, col, board):
            enemies_count += 1

    return enemies_count


def remove_knights():
    removed = 0

    while True:
        most_enemies = 0
        biggest_threat = ''

        for knight in all_knights:
            enemies_count = get_enemies_count(knight, board)

            if enemies_count > most_enemies:
                most_enemies = enemies_count
                biggest_threat = knight

        if most_enemies == 0:
            break

        board[biggest_threat.row][biggest_threat.col] = '0'
        all_knights.remove(biggest_threat)
        removed += 1

    return removed


board_size = int(input())
board = [list(input()) for _ in range(board_size)]

all_knights = get_knight_positions(board)

removed_knights = remove_knights()
print(removed_knights)

# 5
# 0K0K0
# K000K
# 00K00
# K000K
# 0K0K0

# 2
# KK
# KK

# 8
# 0K0KKK00
# 0K00KKKK
# 00K0000K
# KKKKKK0K
# K0K0000K
# KK00000K
# 00K0K000
# 000K00KK
