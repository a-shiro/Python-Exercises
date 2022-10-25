from collections import deque


def read_matrix(r, c):
    mtrx = []

    for _ in range(r):
        mtrx.append([None for _ in range(c)])

    return mtrx


def get_snake_parts(word):
    return [e for e in word]


r, c = [int(n) for n in input().split(' ')]
snake = input()

matrix = read_matrix(r, c)
snake_parts = deque(get_snake_parts(snake))

for row in range(r):
    result = deque()

    if row % 2 == 0:
        for _ in range(c):
            if not snake_parts:
                snake_parts = deque(get_snake_parts(snake))
            result.append(snake_parts.popleft())
    else:
        for _ in range(c):
            if not snake_parts:
                snake_parts = deque(get_snake_parts(snake))
            result.appendleft(snake_parts.popleft())

    print(''.join(result))



