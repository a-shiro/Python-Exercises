from collections import deque

queue = deque()
water_quantity = int(input())

while True:

    command = input()

    if command == "Start":
        break

    queue.append(command)

while True:

    command_1 = input()

    if command_1 == "End":
        break

    elif "refill" in command_1:
        refill = int(command_1.split()[1])
        water_quantity += refill

    else:
        person = queue.popleft()

        if water_quantity - int(command_1) >= 0:
            print(f"{person} got water")
            water_quantity -= int(command_1)
        else:
            print(f"{person} must wait")

print(f"{water_quantity} liters left")