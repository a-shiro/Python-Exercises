def find_loser(player_pool, p_1, p_2):

    p_1_total_skill, p_2_total_skill = 0, 0
    match = False

    if p_1 in player_pool and p_2 in player_pool.keys():

        p_1_roles = [position for position in player_pool[p_1]]
        p_2_roles = [position for position in player_pool[p_2]]

        if len(p_1_roles) <= len(p_2_roles):
            for r in p_1_roles:
                if r in p_2_roles:
                    match = True
                    break
        else:
            for r in p_2_roles:
                if r in p_1_roles:
                    match = True
                    break
        if match:
            for r, s in player_pool[p_1].items():
                p_1_total_skill += s
            for r, s in player_pool[p_2].items():
                p_2_total_skill += s

            if p_1_total_skill > p_2_total_skill:
                return p_2
            elif p_2_total_skill > p_1_total_skill:
                return p_1


def find_total_skill(player_pool):

    total_skill = {}

    for k, v in player_pool.items():
        total_skill[k] = 0
        for p, s in v.items():
            total_skill[k] += s

    return total_skill


player_pool = {}
player_info = input().split(" -> ")

while not player_info == "Season end":

    if len(player_info) == 3:
        player, role, skill = player_info[0], player_info[1], int(player_info[2])

        if player not in player_pool:
            player_pool[player] = {role: skill}

        elif role not in player_pool[player]:
            player_pool[player].update({role: skill})

        elif player_pool[player][role] < skill:
            player_pool[player][role] = skill

    elif len(player_info) == 2:
        p_1, p_2 = player_info[0], player_info[1]

        loser = find_loser(player_pool, p_1, p_2)
        if loser is not None:
            del player_pool[loser]

    player_info = input()

    if " -> " in player_info:
        player_info = player_info.split(" -> ")

    elif " vs " in player_info:
        player_info = player_info.split(" vs ")

player_skill = find_total_skill(player_pool)

for k, v in sorted(player_skill.items(), key=lambda x: (-x[1], x[0])):
    print(f"{k}: {v} skill")
    for r, s in sorted(player_pool[k].items(), key=lambda x: (-x[1], x[0])):
        print(f"- {r} <::> {s}")
