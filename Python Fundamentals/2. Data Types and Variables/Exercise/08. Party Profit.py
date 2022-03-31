party_size = int(input())
days = int(input())

companion_count = party_size
coins = 0

for day in range(1, days + 1):
    if day % 10 == 0:
        companion_count -= 2
    if day % 15 == 0:
        companion_count += 5

    coins += 50
    coins -= companion_count * 2

    if day % 3 == 0:
        coins -= companion_count * 3
    if day % 5 == 0:
        coins += companion_count * 20
        if day % 15 == 0:
            coins -= companion_count * 2

print(f"{companion_count} companions received {int(coins / companion_count)} coins each.")
