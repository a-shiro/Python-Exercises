def solution():
    def integers():
        n = 1
        while True:
            yield n
            n += 1

    def halves():
        for n in integers():
            yield n / 2

    def take(n, seq):
        result = []
        for _ in range(n):
            result.append(next(seq))
        return result

    return (take, halves, integers)


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))