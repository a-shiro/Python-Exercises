exp_needed = float(input())
battles = int(input())

total_exp = 0
battle_count = 0

for battle in range(1, battles + 1):
    exp_per_battle = float(input())
    battle_count += 1

    if battle % 3 == 0:
        total_exp += exp_per_battle + (exp_per_battle * 0.15)

    elif battle % 5 == 0:
        total_exp += exp_per_battle - (exp_per_battle * 0.10)

    elif battle % 15 == 0:
        total_exp += exp_per_battle + (exp_per_battle * 0.05)

    else:
        total_exp += exp_per_battle

    if total_exp >= exp_needed:
        break

if total_exp >= exp_needed:
    print(f"Player successfully collected his needed experience for {battle_count} battles.")
else:
    print(f"Player was not able to collect the needed experience, {exp_needed - total_exp:.2f} more needed.")

# 500
# 5
# 50
# 100
# 200
# 100
# 30


# 400
# 5
# 50
# 100
# 200
# 100
# 20