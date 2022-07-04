number_people = int(input())
back = 0
chest = 0
legs = 0
abs = 0
protein_shake = 0
protein_bar = 0

for i in range(number_people):
    type = input()

    if type == "Back":
        back += 1

    elif type == "Chest":
        chest += 1

    elif type ==  "Legs":
        legs += 1

    elif type == "Abs":
        abs += 1

    elif type == "Protein shake":
        protein_shake += 1

    elif type == "Protein bar":
        protein_bar += 1

workout = back + chest + legs + abs
protein = protein_bar + protein_shake



print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abs} - abs")
print(f"{protein_shake} - protein shake")
print(f"{protein_bar} - protein bar")
print(f"{workout / number_people * 100:.2f}% - work out")
print(f"{protein / number_people * 100:.2f}% - protein")

