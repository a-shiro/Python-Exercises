from collections import deque


def get_sorted_bomb_types(bomb_types):
    bombs = ['Datura Bombs', 'Cherry Bombs', 'Smoke Decoy Bombs']
    sorted_bomb_types = {}
    index = 0
    for v in bomb_types.values():
        sorted_bomb_types[bombs[index]] = v
        index += 1
    return sorted_bomb_types


def print_outcome(bomb_types, bombs_crafted):
    if bombs_crafted >= 8:
        print(f'Bene! You have successfully filled the bomb pouch!')
    else:
        print(f"You don't have enough materials to fill the bomb pouch.")

    if not bomb_effects:
        print('Bomb Effects: empty')
    else:
        print(f'Bomb Effects: {", ".join(map(str, bomb_effects))}')

    if not bomb_casings:
        print('Bomb Casings: empty')
    else:
        print(f'Bomb Casings: {", ".join(map(str, bomb_casings))}')

    sorted_bomb_types = get_sorted_bomb_types(bomb_types)

    for k, v in sorted(sorted_bomb_types.items()):
        print(f'{k}: {v}')


def get_bombs_crafted(bomb_types):
    bombs_crafted = [v for v in bomb_types.values()]
    return sum(bombs_crafted)


def three_of_each(bomb_types):
    for v in bomb_types.values():
        if v < 3:
            return False
    return True


def stop_crafting(bomb_effects, bomb_casings, bomb_types):
    if not bomb_effects or not bomb_casings:
        return True
    if three_of_each(bomb_types):
        return True
    if bomb_casings[-1] < 0:
        bomb_casings[-1] = 0
        return True
    return False


def craft_bombs(bomb_effects, bomb_casings):
    bomb_types = {
        '40': 0,
        '60': 0,
        '120': 0
    }

    while True:
        effect, casing = bomb_effects[0], bomb_casings[-1]
        result = effect + casing

        if str(result) in bomb_types.keys():
            bomb_effects.popleft(), bomb_casings.pop()
            bomb_types[str(result)] += 1
        else:
            bomb_casings[-1] -= 5

        if stop_crafting(bomb_effects, bomb_casings, bomb_types):
            return bomb_types


bomb_effects = deque([int(x) for x in input().split(', ')])
bomb_casings = [int(x) for x in input().split(', ')]

bomb_types = craft_bombs(bomb_effects, bomb_casings)
bombs_crafted = get_bombs_crafted(bomb_types)
print_outcome(bomb_types, bombs_crafted)


