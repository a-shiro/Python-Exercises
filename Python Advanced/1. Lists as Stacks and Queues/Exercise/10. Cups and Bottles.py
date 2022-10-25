from collections import deque

cups = deque([int(c) for c in input().split()])
bottles = [int(b) for b in input().split()]

wasted_water = 0

while len(cups) > 0 and len(bottles) > 0:

    cup_capacity, bottle_capacity = cups[0], bottles[-1]

    if bottle_capacity >= cup_capacity:

        cups.popleft(), bottles.pop()
        wasted_water += bottle_capacity - cup_capacity
    else:
        while cup_capacity > 0:
            cup_capacity = cup_capacity - bottles.pop()
            if cup_capacity <= 0:
                wasted_water += abs(cup_capacity)
                cups.popleft()
                break

if cups:
    print(f"Cups: {' '.join(map(str, cups))}")
else:
    print(f"Bottles: {' '.join(map(str, bottles))}")

print(f"Wasted litters of water: {wasted_water}")