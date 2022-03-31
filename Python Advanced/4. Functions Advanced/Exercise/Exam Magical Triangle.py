def calculate_triangle_indices(n, magic_triangle):
    for row in range(n):
        for col in range(row + 1):
            if col == 0 or col == row:
                magic_triangle[row][col] = magic_triangle[row - 1][0]
            else:
                magic_triangle[row][col] = magic_triangle[row - 1][col - 1] + magic_triangle[row - 1][col]


def create_triangle_rows(n, magic_triangle):
    for row in range(1, n + 1):
        magic_triangle.append([1 for x in range(row)])


def get_magic_triangle(n):
    magic_triangle = []

    create_triangle_rows(n, magic_triangle)
    calculate_triangle_indices(n, magic_triangle)

    return magic_triangle


magic_triangle = get_magic_triangle(6)
for row in magic_triangle:
    print(row)