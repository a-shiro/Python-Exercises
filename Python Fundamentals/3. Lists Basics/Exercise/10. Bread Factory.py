initial_energy = 100
initial_coins = 100

current_event = input().split("|")

bankrupt = False

for i in current_event:
    type_and_number = i.split("-")

    event_name = type_and_number[0]
    event_number = int(type_and_number[1])

    if event_name == "rest":
        gained_energy = event_number
        if initial_energy + event_number >= 100:
            gained_energy = 100 - initial_energy

        initial_energy += gained_energy

        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {initial_energy}.")

    elif event_name == "order":
        if initial_energy - 30 >= 0:
            initial_coins += event_number
            initial_energy -= 30

            print(f"You earned {event_number} coins.")
        else:
            initial_energy += 50
            print(f"You had to rest!")

    else:
        if initial_coins - event_number > 0:
            initial_coins -= event_number
            print(f"You bought {event_name}.")

        else:
            print(f"Closed! Cannot afford {event_name}.")
            bankrupt = True
            break

if not bankrupt:
    print("Day completed!")
    print(f"Coins: {initial_coins}")
    print(f"Energy: {initial_energy}")

