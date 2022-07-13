def recursive_loops(n, result):
    if len(result) == n:
        print(*result)

        return

    for number in range(1, n + 1):
        result.append(number)

        recursive_loops(n, result)

        result.pop()


n = int(input())
recursive_loops(n, [])