def even_parameters(func):
    def wrapper(*args):
        all_even = all([True if isinstance(n, int) and n % 2 == 0 else False for n in args])
        if all_even:
            return func(*args)
        return 'Please use only even numbers!'
    return wrapper


@even_parameters
def add(a, b):
    return a + b

print(add(2, 4))
print(add('Peter', 1))


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result

print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))