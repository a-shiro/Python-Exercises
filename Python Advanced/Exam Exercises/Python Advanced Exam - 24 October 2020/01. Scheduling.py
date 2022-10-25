from collections import deque


def find_needed_clock_cycles(searched_speed, clock_cycle):
    clock_cycle = deque(sorted(clock_cycle))
    total = 0

    while clock_cycle:
        current_speed = clock_cycle[0]

        if current_speed > searched_speed:
            break

        speed = clock_cycle.popleft()
        total += speed

    return total


clock_cycle = deque([int(n) for n in input().split(', ')])
searched_speed = clock_cycle[int(input())]

total_clock_cycles = find_needed_clock_cycles(searched_speed, clock_cycle)
print(total_clock_cycles)


