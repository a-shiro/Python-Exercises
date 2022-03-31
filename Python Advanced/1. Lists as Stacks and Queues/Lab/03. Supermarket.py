from collections import deque

waiting = deque()

while True:

    command = input()

    if command == "Paid":
        while waiting:
            print(waiting.popleft())
    elif command == "End":
        print(f"{len(waiting)} people remaining.")
        break
    else:
        waiting.append(command)





