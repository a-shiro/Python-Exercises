n = int(input())
k = int(input())


def calc_binom(n, k, cache):
    key = f'{n} {k}'

    if key in cache:
        return cache[key]

    if n == 0 or k == 0 or n == k:
        return 1

    result = calc_binom(n - 1, k - 1, cache) + calc_binom(n - 1, k, cache)
    cache[key] = result

    return result


print(calc_binom(n, k, {}))

# 3
# 2

# 4
# 0

# 49
# 10
