from collections import deque

green_light_duration = int(input())
free_window_duration = int(input())
command = input()

cars_passed = 0
crash = False
queue = deque()

while not command == "END":

    if command == "green":

        seconds_left = green_light_duration
        exit_window = free_window_duration

        while queue:
            car = queue.popleft()

            for ch in car:
                if seconds_left == 0:
                    exit_window -= 1
                    if exit_window < 0:
                        print(f"A crash happened!")
                        print(f"{car} was hit at {ch}.")
                        crash = True
                        break
                else:
                    seconds_left -= 1

            cars_passed += 1

            if seconds_left <= 0:
                break
    else:
        queue.append(command)

    if crash:
        break

    command = input()

if not crash:
    print("Everyone is safe.")
    print(f"{cars_passed} total cars passed the crossroads.")

