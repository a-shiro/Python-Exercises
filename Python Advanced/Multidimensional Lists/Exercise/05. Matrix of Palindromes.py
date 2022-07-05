r, c = (map(int, input().split(' ')))

for row in range(r):
    for col in range(c):
        print(f'{chr(97 + row)}{chr(97 + row + col)}{chr(97 + row)}', end=' ')
    print()