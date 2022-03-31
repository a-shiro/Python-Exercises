energy = int(input())
command = input()
battles_won = 0

while not command == "End of battle":
    command = int(command)

    if energy < command:
        print(f"Not enough energy! Game ends with {battles_won} won battles and {energy} energy")
        break
    else:
        energy -= command
        battles_won += 1
        if battles_won % 3 == 0:
            energy += battles_won

    command = input()

if command == "End of battle":
    print(f"Won battles: {battles_won}. Energy left: {energy}")