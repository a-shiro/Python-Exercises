actor_name = input()
actor_points = float(input())
judges_count = int(input())

nomination_points = 1250.5
nominated = False

for i in range(judges_count):
    judge_name = input()
    points_given = float(input())

    actor_points += ((len(judge_name) * points_given) / 2)

    if actor_points > nomination_points:
        nominated = True
        break

if nominated:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {actor_points:.1f}!")

else:
    points_needed = nomination_points - actor_points

    print(f"Sorry, {actor_name} you need {points_needed:.1f} more!")