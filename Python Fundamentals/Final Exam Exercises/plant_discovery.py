plants_count = int(input())

my_plants = {}

for _ in range(plants_count):

    plant, rarity = input().split("<->")

    if plant in my_plants.keys():
        my_plants[plant]["Rarity"] = rarity

    my_plants[plant] = {"Rarity": int(rarity), "Rating": []}

command = input().split()

while not command[0] == "Exhibition":

    if command[0] == "Rate:" and command[1] in my_plants.keys():
        plant_name, rating = command[1], int(command[3])
        my_plants[plant_name]["Rating"].append(rating)

    elif command[0] == "Update:" and command[1] in my_plants.keys():
        plant_name, new_rarity = command[1], int(command[3])
        my_plants[plant_name]["Rarity"] = new_rarity

    elif command[0] == "Reset:" and command[1] in my_plants.keys():
        plant_name = command[1]
        my_plants[plant_name]["Rating"].clear()

    else:
        print("error")

    command = input().split()

for plant in my_plants:

    if my_plants[plant]["Rating"] == []:
        my_plants[plant]["Rating"].append(0)

    my_plants[plant]['Rating'] = sum(my_plants[plant]["Rating"]) / len(my_plants[plant]["Rating"])

my_plants = sorted(my_plants.items(), key=lambda x: (-x[1]["Rarity"], -x[1]["Rating"]))

print("Plants for the exhibition:")
for tup in my_plants:
    plant_name, rarity_n_rating = tup[0], tup[1]
    print(f"- {plant_name}; Rarity: {rarity_n_rating['Rarity']}; Rating: {rarity_n_rating['Rating']:.2f}")