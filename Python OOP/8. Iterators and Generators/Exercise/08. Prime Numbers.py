def get_primes(integers):
    for num in integers:
        if num > 1:
            for divider in range(2, num):
                if num % divider == 0:
                    break
            else:
                yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print(list(get_primes([-2, 0, 0, 1, 1, 0])))