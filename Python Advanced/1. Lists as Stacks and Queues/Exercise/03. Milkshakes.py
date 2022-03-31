from collections import deque

chocolates = [int(c) for c in input().split(', ')]
cups_of_milk = deque(int(m) for m in input().split(', '))

shakes_made = 0

while shakes_made < 5 and len(chocolates) > 0 and len(cups_of_milk) > 0:

    last_chocolate = chocolates[-1]
    first_cup = cups_of_milk[0]

    if not last_chocolate == first_cup:
        if last_chocolate <= 0 or first_cup <= 0:
            if last_chocolate <= 0:
                chocolates.pop()
            if first_cup <= 0:
                cups_of_milk.popleft()
        else:
            cups_of_milk.append(cups_of_milk.popleft())
            chocolates[-1] -= 5

    else:
        chocolates.pop()
        cups_of_milk.popleft()
        shakes_made += 1

if shakes_made == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join(map(str, chocolates))}")
else:
    print("Chocolate: empty")

if cups_of_milk:
    print(f"Milk: {', '.join(map(str, cups_of_milk))}")
else:
    print("Milk: empty")