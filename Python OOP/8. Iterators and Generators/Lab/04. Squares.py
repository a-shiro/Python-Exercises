def squares(n):
    index = 1
    while index <= n:
        yield index ** 2
        index += 1


print(list(squares(5)))