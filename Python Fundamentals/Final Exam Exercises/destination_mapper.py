import re

places = input()
pattern = r"(=|\/)(?P<location>[A-Z][A-Za-z]{2,})(\1)"
travel_points = 0
loc_list = []

valid_locations = re.finditer(pattern, places)

for loc in valid_locations:

    travel_points += len(loc.group("location"))
    loc_list.append(loc.group("location"))

print(f"Destinations: {', '.join(loc_list)}")
print(f"Travel Points: {travel_points}")