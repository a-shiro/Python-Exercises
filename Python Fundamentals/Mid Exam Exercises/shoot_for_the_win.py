targets = [int(target) for target in input().split()]
index = input()
shot_targets = 0

while not index == "End":
    index = int(index)

    if index in range(len(targets)):
        target_number = targets[index]
        targets[index] -= targets[index] + 1
        shot_targets += 1
        for target in range(len(targets)):
            if targets[target] > target_number:
                targets[target] -= target_number
            elif not targets[target] == -1:
                targets[target] += target_number

    index = input()

targets = " ".join([str(target) for target in targets])
print(f"Shot targets: {shot_targets} -> {targets}")
