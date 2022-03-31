health = 100
coins = 0
room_number = 0
died = False

dungeon = input().split("|")

for room in dungeon:
    room_number += 1
    command_name, amount = room.split()
    amount = int(amount)

    if command_name == "potion":
        if health + amount > 100:
            amount = 100 - health
        health += amount
        print(f"You healed for {amount} hp.")
        print(f"Current health: {health} hp.")

    elif command_name == "chest":
        coins += amount
        print(f"You found {amount} bitcoins.")

    else:
        health -= amount
        if not health <= 0:
            print(f"You slayed {command_name}.")
        else:
            print(f"You died! Killed by {command_name}.")
            print(f"Best room: {room_number}")
            died = True
            break

if not died:
    print("You've made it!")
    print(f"Bitcoins: {coins}")
    print(f"Health: {health}")

