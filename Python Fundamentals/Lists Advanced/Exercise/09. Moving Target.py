targets = [int(num) for num in input().split()]
command = input()

while not command == "End":
    command_name, index, value = command.split()
    index = int(index)
    value = int(value)

    if command_name == "Shoot":
        if index < 0 or index > len(targets) - 1:
            command = input()
            continue
        targets[index] -= value
        if targets[index] <= 0:
            targets.remove(targets[index])

    elif command_name == "Add":
        if 0 <= index <= len(targets) - 1:
            targets.insert(index, value)
        else:
            print("Invalid placement!")

    elif command_name == "Strike":
        if_missed = [num for num in targets]
        missed = False
        starting_num = targets[index]
        before_index = index - value
        for radius in range(index - 1, before_index -1, -1):
            if radius < 0:
                missed = True
                break
            targets.remove(targets[radius])

        starting_index = targets.index(starting_num)
        after_index = starting_index + value
        for radius in range(after_index, starting_index, -1):
            if radius < 0 or missed == True:
                missed = True
                break
            targets.remove(targets[radius])
        targets.remove(starting_num)
        if missed:
            print("Strike missed!")
            targets = if_missed

    command = input()

print("|".join([str(el) for el in targets]))