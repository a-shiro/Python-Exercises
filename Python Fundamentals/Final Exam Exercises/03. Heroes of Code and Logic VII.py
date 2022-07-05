heroes_count = int(input())

my_party = {}

for _ in range(heroes_count):

    name, HP, MP = input().split()
    my_party[name] = {"HP": [int(HP)], "MP": [int(MP)]}

command = input().split(" - ")

while not command[0] == "End":

    if command[0] == "CastSpell":

        hero_name, mana_needed, spell_name = command[1], int(command[2]), command[3]

        if my_party[hero_name]["MP"][0] >= mana_needed:
            my_party[hero_name]['MP'][0] = my_party[hero_name]["MP"][0] - mana_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {my_party[hero_name]['MP'][0]} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif command[0] == "TakeDamage":

        hero_name, dmg, attacker = command[1], int(command[2]), command[3]

        my_party[hero_name]['HP'][0] = my_party[hero_name]["HP"][0] - dmg

        if not my_party[hero_name]['HP'][0] <= 0:
            print(f"{hero_name} was hit for {dmg} HP by {attacker} and now has {my_party[hero_name]['HP'][0]} HP left!")
        else:
            print(f"{hero_name} has been killed by {attacker}!")
            my_party.pop(hero_name)

    elif command[0] == "Recharge":

        hero_name, amount = command[1], int(command[2])

        if my_party[hero_name]["MP"][0] + amount > 200:
            recharged = 200 - my_party[hero_name]["MP"][0]
            my_party[hero_name]["MP"][0] = 200
        else:
            recharged = amount
            my_party[hero_name]["MP"][0] += amount

        print(f"{hero_name} recharged for {recharged} MP!")

    elif command[0] == "Heal":

        hero_name, amount = command[1], int(command[2])

        if my_party[hero_name]["HP"][0] + amount > 100:
            healed = 100 - my_party[hero_name]["HP"][0]
            my_party[hero_name]["HP"][0] = 100
        else:
            healed = amount
            my_party[hero_name]["HP"][0] += amount

        print(f"{hero_name} healed for {healed} HP!")

    command = input().split(" - ")

my_party = sorted(my_party.items(), key=lambda x: (-x[1]["HP"][0], x[0]))

for tup in my_party:

    name, hp_and_mp = tup[0], tup[1]

    print(name)
    print(f' HP: {hp_and_mp["HP"][0]}')
    print(f' MP: {hp_and_mp["MP"][0]}')