n = int(input())

chemicals = set()

for _ in range(n):
    [chemicals.add(x) for x in input().split(" ")]

[print(y) for y in chemicals]
