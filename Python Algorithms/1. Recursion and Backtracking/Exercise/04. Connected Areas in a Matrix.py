class Area:
    def __init__(self, row, col, size):
        self.starting_row = row
        self.starting_col = col
        self.size = size


def find_area_count(row, col, matrix):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return 0

    if matrix[row][col] != '-':
        return 0

    matrix[row][col] = 'v'
    result = 1

    result += find_area_count(row - 1, col, matrix)
    result += find_area_count(row + 1, col, matrix)
    result += find_area_count(row, col - 1, matrix)
    result += find_area_count(row, col + 1, matrix)

    return result


rows = int(input())
cols = int(input())

matrix = [list(input()) for _ in range(rows)]

areas = []

for row in range(rows):
    for col in range(cols):
        size = find_area_count(row, col, matrix)
        if size == 0:
            continue

        area = Area(row, col, size)
        areas.append(area)

print(f'Total areas found: {len(areas)}')
for idx, area in enumerate(sorted(areas, key=lambda x: -x.size)):
    print(f'Area #{idx + 1} at {area.starting_row, area.starting_col}, size: {area.size}')

# 4
# 9
# ---*---*-
# ---*---*-
# ---*---*-
# ----*-*--

# 5
# 10
# *--*---*--
# *--*---*--
# *--*****--
# *--*---*--
# *--*---*--
