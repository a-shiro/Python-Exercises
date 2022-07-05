from collections import deque

bees = deque(int(b) for b in input().split(' '))
nectar = [int(n) for n in input().split(' ')]
operations = deque(s for s in input().split(' '))

total_honey = 0

while len(bees) > 0 and len(nectar) > 0:

    current_bee = bees[0]
    current_nectar = nectar[-1]

    if current_nectar >= current_bee:
        symbol = operations.popleft()

        if symbol == "+":
            total_honey += abs(current_bee + current_nectar)
        elif symbol == "-":
            total_honey += abs(current_bee - current_nectar)
        elif symbol == "*":
            total_honey += abs(current_bee * current_nectar)
        elif symbol == "/":
            if current_bee > 0 and current_nectar > 0:
                total_honey += abs(current_bee / current_nectar)

        bees.popleft()
        nectar.pop()

    else:
        nectar.pop()

print(f"Total honey made: {total_honey}")

if len(bees) > 0:
    print(f"Bees left: {', '.join(map(str, bees))}")
elif len(nectar) > 0:
    print(f"Nectar left: {', '.join(map(str, nectar))}")