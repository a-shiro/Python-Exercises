from collections import deque


def try_again(can_craft_a_present, craft_corresponding_gift, value):
    if can_craft_a_present:
        craft_corresponding_gift(value)
        materials.pop()
        magic_levels.popleft()
    else:
        materials.pop()
        magic_levels.popleft()


def succeeded(presents):
    if presents['Gemstone'] > 0 and presents['Porcelain Sculpture'] > 0:
        return True
    elif presents['Gold'] > 0 and presents['Diamond Jewellery'] > 0:
        return True
    return False


def can_craft_a_present(value):
    return 100 <= value <= 499


def craft_corresponding_gift(value):
    if 100 <= value <= 199:
        presents['Gemstone'] += 1

    elif 200 <= value <= 299:
        presents['Porcelain Sculpture'] += 1

    elif 300 <= value <= 399:
        presents['Gold'] += 1

    elif 400 <= value <= 499:
        presents['Diamond Jewellery'] += 1


def start_crafting(materials, magic_levels):
    while True:
        material, level = materials[-1], magic_levels[0]

        value = material + level

        if can_craft_a_present(value):
            craft_corresponding_gift(value)
            materials.pop()
            magic_levels.popleft()

        elif value < 100:
            if value % 2 == 0:
                value = material * 2 + level * 3
            else:
                value = material * 2 + level * 2

            try_again(can_craft_a_present(value), craft_corresponding_gift, value)

        elif value > 499:
            value /= 2

            try_again(can_craft_a_present(value), craft_corresponding_gift, value)

        if not materials or not magic_levels:
            return


presents = {
    'Gemstone': 0,
    'Porcelain Sculpture': 0,
    'Gold': 0,
    'Diamond Jewellery': 0
}

# read materials and magil lvls
materials = [int(m) for m in input().split(' ')]
magic_levels = deque([int(m) for m in input().split(' ')])

start_crafting(materials, magic_levels)

if succeeded(presents):
    print('The wedding presents are made!')
else:
    print('Aladdin does not have enough wedding presents.')

if materials:
    print(f'Materials left: {", ".join(map(str, materials))}')
if magic_levels:
    print(f'Magic left: {", ".join(map(str, magic_levels))}')

for k, v in sorted(presents.items()):
    if v > 0:
        print(f'{k}: {v}')
