from collections import deque

materials_box = [int(x) for x in input().split(' ')]
magic_box = deque(int(y) for y in input().split(' '))

magic_presents_lvls = [150, 250, 300, 400]
presents = {
    'Doll': 0,
    'Wooden train': 0,
    'Teddy bear': 0,
    'Bicycle': 0
}

while len(materials_box) > 0 and len(magic_box) > 0:

    matched_material = materials_box[-1]
    matched_magic_lvl = magic_box[0]

    current_lvl = matched_material * matched_magic_lvl

    if current_lvl in magic_presents_lvls:
        if current_lvl == 150:
            presents['Doll'] += 1
        elif current_lvl == 250:
            presents['Wooden train'] += 1
        elif current_lvl == 300:
            presents['Teddy bear'] += 1
        elif current_lvl == 400:
            presents['Bicycle'] += 1

        materials_box.pop()
        magic_box.popleft()
    else:
        if current_lvl == 0:
            if matched_material == 0 and matched_magic_lvl == 0:
                magic_box.popleft()
                materials_box.pop()
            elif matched_magic_lvl == 0:
                magic_box.popleft()
            elif matched_material == 0:
                materials_box.pop()
        elif current_lvl < 0:
            add = matched_material + matched_magic_lvl
            materials_box.pop()
            magic_box.popleft()
            materials_box.append(add)
        elif current_lvl > 0:
            materials_box[-1] += 15
            magic_box.popleft()

if presents['Doll'] > 0 and presents['Wooden train'] > 0 or presents['Teddy bear'] > 0 and presents['Bicycle'] > 0:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if len(materials_box) > 0:
    print(f"Materials left: {', '.join(str(i) for i in reversed(materials_box))}")
if len(magic_box) > 0:
    print(f"Magic left: {', '.join(str(i) for i in magic_box)}")

for k, v in sorted(presents.items()):
    if v > 0:
        print(f"{k}: {v}")
