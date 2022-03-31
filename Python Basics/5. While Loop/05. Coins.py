coins = float(input())

change = 0

coins *= 100

while coins > 0:
    if coins >= 200:
        coins -= 200
        change += 1
        continue

    elif coins >= 100:
        coins -= 100
        change += 1
        continue

    elif coins >= 50:
        coins -= 50
        change += 1
        continue

    elif coins >= 20:
        coins -= 20
        change += 1
        continue

    elif coins >= 10:
        coins -= 10
        change += 1
        continue

    elif coins >= 5:
        coins -= 5
        change += 1
        continue

    elif coins >= 2:
        coins -= 2
        change += 1
        continue

    elif coins >= 1:
        coins -= 1
        change += 1
        continue

    if coins < 1:
        break

print(change)
