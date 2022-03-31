class ValueCannotBeNegative(Exception):
    pass


for _ in range(5):
    n = float(input())

    if n < 0:
        raise ValueCannotBeNegative



