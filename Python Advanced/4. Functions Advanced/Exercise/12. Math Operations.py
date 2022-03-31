def math_operations(*args, **kwargs):
    result = kwargs
    operation = 1

    for n in args:
        if operation == 1:
            result['a'] += n
        elif operation == 2:
            result['s'] -= n
        elif operation == 3:
            if n != 0:
                result['d'] /= n
        elif operation == 4:
            result['m'] *= n

        operation += 1
        if operation == 5:
            operation = 1

    return result


print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
print(math_operations(-1, 0, 1, 0, 6, -2, 80, a=0, s=0, d=0, m=0))
print(math_operations(6, a=0, s=0, d=0, m=0))
