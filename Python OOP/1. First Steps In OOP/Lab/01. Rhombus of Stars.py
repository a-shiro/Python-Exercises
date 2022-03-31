def print_row(star_count):
    for _ in range(star_count, size - 1):
        print(' ', end='')

    for _ in range(star_count):
        print('*', end=' ')
    print('*')


size = int(input())

for star_count in range(size):
    print_row(star_count)

for star_count in range(size - 2, -1, -1):
    print_row(star_count)
