def calc_fib(n, memoization):
    if n in memoization:
        return memoization[n]

    if n <= 2:
        return 1

    result = calc_fib(n - 1, memoization) + calc_fib(n - 2, memoization)
    memoization[n] = result

    return result


n = int(input())
memoization = []

print(calc_fib(n, {}))
