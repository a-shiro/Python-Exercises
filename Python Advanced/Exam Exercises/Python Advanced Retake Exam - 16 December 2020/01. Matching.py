from collections import deque


def start_matching(males, females):
    matches = 0

    while True:
        male, female = males[-1], females[0]

        if male <= 0 or female <= 0:
            if female <= 0:
                females.popleft()
            if male <= 0:
                males.pop()

        elif male % 25 == 0 or female % 25 == 0:
            if female % 25 == 0:
                for _ in range(2):
                    females.popleft()
            if male % 25 == 0:
                for _ in range(2):
                    males.pop()
        else:
            if not male == female:
                females.popleft()
                males[-1] -= 2
            else:
                males.pop()
                females.popleft()
                matches += 1

        if not males or not females:
            break
    return matches


males = [int(m) for m in input().split(' ')]
females = deque([int(f) for f in input().split(' ')])

matches = start_matching(males, females)

print(f'Matches: {matches}')
if males:
    print(f"Males left: {', '.join(map(str, males[::-1]))}")
else:
    print('Males left: none')
if females:
    print(f"Females left: {', '.join(map(str, females))}")
else:
    print('Females left: none')
