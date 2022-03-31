def func_executor(*args):
    result = []
    for func_tuple in args:
        func_name, func_params = func_tuple
        result.append(func_name(*func_params))
    return result


def sum_numbers(x, y):
    return x + y


def multiply_numbers(x, y):
    return x * y


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))

