import math
cat_breed = input()
cat_gender = input()

if cat_breed != "British Shorthair" and cat_breed != "Siamese" and cat_breed != "Persian" \
    and cat_breed != "Ragdoll" and cat_breed != "American Shorthair" and cat_breed != "Siberian":
    print(f"{cat_breed} is invalid cat!")

elif cat_breed == "British Shorthair":
    if cat_gender == "m":
        human_months = 13 * 12
        cat_months = human_months / 6
        print(f"{math.floor(cat_months)} cat months")
    elif cat_gender == "f":
        human_months = 14 * 12
        cat_months = human_months / 6
        print(f"{math.floor(cat_months)} cat months")

elif cat_breed == "Siamese":
    if cat_gender == "m":
        human_months = 15 * 12
        cat_months = human_months / 6
        print(f"{math.floor(cat_months)} cat months")
    elif cat_gender == "f":
        human_months = 16 * 12
        cat_months = human_months / 6
        print(f"{math.floor(cat_months)} cat months")

elif cat_breed == "Persian":
    if cat_gender == "m":
        human_months = 14 * 12
        cat_months = human_months / 6
        print(f"{math.floor(cat_months)} cat months")
    elif cat_gender == "f":
        human_months = 15 * 12
        cat_months = human_months / 6
        print(f"{math.floor(cat_months)} cat months")

elif cat_breed == "Ragdoll":
    if cat_gender == "m":
        human_months = 16 * 12
        cat_months = human_months / 6
        print(f"{math.floor(cat_months)} cat months")
    elif cat_gender == "f":
        human_months = 17 * 12
        cat_months = human_months / 6
        print(f"{math.floor(cat_months)} cat months")

elif cat_breed == "American Shorthair":
    if cat_gender == "m":
        human_months = 12 * 12
        cat_months = human_months / 6
        print(f"{math.floor(cat_months)} cat months")
    elif cat_gender == "f":
        human_months = 13 * 12
        cat_months = human_months / 6
        print(f"{math.floor(cat_months)} cat months")

elif cat_breed == "Siberian":
    if cat_gender == "m":
        human_months = 11 * 12
        cat_months = human_months / 6
        print(f"{math.floor(cat_months)} cat months")
    elif cat_gender == "f":
        human_months = 12 * 12
        cat_months = human_months / 6
        print(f"{math.floor(cat_months)} cat months")
