def find_fib(n):
    if n <= 1:
        return 1
    return find_fib(n - 1) + find_fib(n - 2)


n = int(input())
print(find_fib(n))