gifts = input().split()

command = input().split()

while not command[0] == "No": # Splits NO | MONEY

    if command[0] == "OutOfStock":
        gift = command[1]
        if gift in gifts:
            for i in range(len(gifts)):
                if gifts[i] == gift:
                    gifts[i] = "None"

    elif command[0] == "Required":
        gift, index = command[1], int(command[2])

        if index in range(len(gifts)):
            gifts[index] = gift

    elif command[0] == "JustInCase":
        gift = command[1]
        gifts[len(gifts) - 1] = gift

    command = input().split()

while "None" in gifts:
    gifts.remove("None")

print(*gifts)

