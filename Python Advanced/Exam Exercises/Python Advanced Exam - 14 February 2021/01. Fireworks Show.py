from collections import deque


def firework_craft_conditions(eff, expl):
    result = eff + expl

    if result % 3 == 0 and result % 5 != 0:
        fireworks['Palm'] += 1
        effects.popleft()
        explosions.pop()

    elif result % 5 == 0 and result % 3 != 0:
        fireworks['Willow'] += 1
        effects.popleft()
        explosions.pop()
    elif result % 3 == 0 and result % 5 == 0:
        fireworks['Crossette'] += 1
        effects.popleft()
        explosions.pop()
    else:
        effects[0] -= 1
        effects.append(effects.popleft())


def incorrect_value(eff, expl):
    if eff <= 0 or expl <= 0:
        if eff <= 0:
            effects.popleft()
        if expl <= 0:
            explosions.pop()
        return True
    return False


def enough_fireworks(fireworks):
    for v in fireworks.values():
        if v < 3:
            return False
    return True


def create_fireworks(effects, explosions):
    while True:
        if not effects or not explosions:
            return False

        eff, expl = effects[0], explosions[-1]

        if incorrect_value(eff, expl):
            continue

        firework_craft_conditions(eff, expl)

        if enough_fireworks(fireworks):
            return True


effects = deque(map(int, input().split(', ')))
explosions = list(map(int, input().split(', ')))

fireworks = {
    'Palm': 0,
    'Willow': 0,
    'Crossette': 0
}

can_create_a_show = create_fireworks(effects, explosions)

if can_create_a_show:
    print('Congrats! You made the perfect firework show!')
else:
    print("Sorry. You can't make the perfect firework show.")

if effects:
    print(f"Firework Effects left: {', '.join(map(str, effects))}")
if explosions:
    print(f"Explosive Power left: {', '.join(map(str, explosions))}")

for k, v in fireworks.items():
    print(f'{k} Fireworks: {v}')