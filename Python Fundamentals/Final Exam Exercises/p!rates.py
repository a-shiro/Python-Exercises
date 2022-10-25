locations = input().split("||")

locations_dict = {}

while not locations[0] == "Sail":

    location, population, gold = locations[0], int(locations[1]), int(locations[2])

    if location not in locations_dict.keys():
        locations_dict[location] = {"Population": population, "Gold": gold}
    else:
        locations_dict[location]["Population"] += population
        locations_dict[location]["Gold"] += gold

    locations = input().split("||")

command = input().split("=>")

while not command[0] == "End":

    if command[0] == "Plunder":

        town_name, people, gold = command[1], int(command[2]), int(command[3])

        locations_dict[town_name]["Population"] -= people
        locations_dict[town_name]["Gold"] -= gold

        print(f"{town_name} plundered! {gold} gold stolen, {people} citizens killed.")

        if locations_dict[town_name]["Population"] <= 0 or locations_dict[town_name]["Gold"] <= 0:
            print(f"{town_name} has been wiped off the map!")
            locations_dict.pop(town_name)

    elif command[0] == "Prosper":

        town_name, gold = command[1], int(command[2])

        if gold > 0:
            locations_dict[town_name]["Gold"] += gold
            print(f"{gold} gold added to the city treasury. {town_name} now has {locations_dict[town_name]['Gold']} gold.")
        else:
            print("Gold added cannot be a negative number!")

    command = input().split("=>")

if not locations_dict == {}:
    print(f"Ahoy, Captain! There are {len(locations_dict.keys())} wealthy settlements to go to:")
    locations_dict = sorted(locations_dict.items(), key=lambda x: (-x[1]["Gold"], x[0]))
    for tup in locations_dict:
        town_name, population_n_gold = tup[0], tup[1]
        print(f'{town_name} -> Population: {population_n_gold["Population"]} citizens, Gold: {population_n_gold["Gold"]} kg')
else:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")